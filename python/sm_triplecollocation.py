from pytesmo.metrics import tcol_snr
from pytesmo import temporal_matching
from pytesmo.metrics import tcol_snr

from datetime import datetime
from itertools import permutations
import os
import pandas
import sm_config as config
import sm_tools as tools

analysis_output_root = r"../analysis_output"
analysis_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
analysis_results_folder = os.path.join(analysis_output_root, "{}_tc".format(analysis_timestamp))
os.mkdir(analysis_results_folder)
metrics_filename = "tc_metrics_{}.csv".format(analysis_timestamp)
log_filename = "tc_log_{}.csv".format(analysis_timestamp)
log_file = os.path.join(analysis_results_folder, log_filename)

# CCI-SMAP L4-GLDAS
tc_analysis_triplets = {
    ('GLDAS', 'CCI Active', 'CCI Passive'): True,
    ('GLDAS', 'CCI Active', 'SMOS-IC'): False,
    ('GLDAS', 'ASCAT 12.5 TS', 'SMOS-IC'): False
}

def tc_analysis(triplets, locations, anomaly=False):
    metrics = pandas.DataFrame()
    reader_dict = {}
    triplets = tools.get_triplet_list(triplets)
    # get data for each product for each location
    for triplet in triplets:
        for product in triplet:
            if product not in reader_dict.keys():
                reader_dict[product] = tools.get_product_reader(product, config.dict_product_inputs[product])
    location_counter = 0
    locations_len = len(list(config.dict_swe_gldas_points.keys()))
    for location, metadata in config.dict_swe_gldas_points.items():
        location_metrics = pandas.DataFrame()
        location_vc = config.dict_swe_gldas_points[location]["veg_class_name"]
        location_counter += 1
        tools.write_log(log_file, "analyzing {}: {} of {} locations".format(location, location_counter, locations_len))
        ts_dict = {}
        for triplet in triplets:
            for product in triplet:
                if product not in ts_dict.keys():
                    reader = reader_dict[product]
                    product_data = tools.get_product_data(lon=lon, lat=lat, product=product, reader=reader,
                                                          anomaly=anomaly)
                    product_data = tools.get_timeshifted_data(product, product_data)
                ts_dict[product] = product_data
        for triplet in triplets:
            triplet_metrics = pandas.DataFrame()
            for product in triplet:
                lat = metadata["latitude"]
                lon = metadata["longitude"]
                ts_dict[product].rename(product, inplace=True)
                tools.write_log(log_file, "{} {} data.shape: {}".format(location, product,
                                                                        ts_dict[product].shape))
            perm = permutations(triplet)
            matched_data = pandas.DataFrame()
            if ts_dict[triplet[0]].size > 0 and ts_dict[triplet[1]].size > 0 and ts_dict[triplet[2]].size > 0:
                for p in perm:
                    permutation_matched_data = temporal_matching.matching(ts_dict[p[0]], ts_dict[p[1]], ts_dict[p[2]],
                                                                          window=.5)
                    if permutation_matched_data.shape[0] > matched_data.shape[0]:
                        matched_data = permutation_matched_data
                        product_order = p
                        n = matched_data.shape[0]
                tools.write_log(log_file, "{} {} matched_data.shape: {}".format(location, product_order,
                                                                                matched_data.shape))
            else:
                tools.write_log(log_file, "{} {} insufficient data to match".format(location, triplet))
            for column in matched_data.columns:
                series = matched_data[column].to_numpy()
                ts_dict[column] = series
            try:
                snr, err_std, beta = tcol_snr(ts_dict[triplet[0]], ts_dict[triplet[1]], ts_dict[triplet[2]])
                tools.write_log(log_file, '{} {} snr: {}'.format(location, triplet, snr))
                tools.write_log(log_file, '{} {} err_std: {}'.format(location, triplet, err_std))
                tools.write_log(log_file, '{} {} beta: {}'.format(location, triplet, beta))
                for idx, product in enumerate(triplet):
                    product_metrics = pandas.DataFrame([[location, location_vc, product, triplet, n, snr[idx],
                                                         err_std[idx], beta[idx]]],
                                                       columns=['location', 'location_veg_class', 'product', 'triplet',
                                                                'n', 'snr', 'err_std', 'beta'])
            except:
                for idx, product in enumerate(triplet):
                    product_metrics = pandas.DataFrame([[location, location_vc, product, triplet, n, None, None, None]],
                                                       columns=['location', 'location_veg_class', 'product', 'triplet',
                                                                'n', 'snr', 'err_std', 'beta'])
                tools.write_log(log_file, "{} {} could not run tcol analysis".format(location, triplet))
            triplet_metrics = triplet_metrics.append(product_metrics)
        location_metrics = location_metrics.append(triplet_metrics)
    metrics = metrics.append(location_metrics)
    return metrics


tc_results = tc_analysis(tc_analysis_triplets, config.dict_swe_gldas_points, anomaly=False)
tc_results.to_csv(os.path.join(analysis_results_folder, metrics_filename))