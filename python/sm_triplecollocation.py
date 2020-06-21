from pytesmo.metrics import tcol_snr
from pytesmo import temporal_matching

from datetime import datetime
import os
import sm_config as config
import sm_tools as tools

analysis_output_root = r"../analysis_output"
analysis_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
analysis_results_folder = os.path.join(analysis_output_root, "{}_tc".format(analysis_timestamp))
os.mkdir(analysis_results_folder)
metrics_filename = "metrics_{}.csv".format(analysis_timestamp)
log_filename = "tc_log_{}.csv".format(analysis_timestamp)
log_file = os.path.join(analysis_results_folder, log_filename)

# CCI-SMAP L4-GLDAS
tc_analysis_triplets = {
    ('GLDAS', 'CCI Active', 'CCI Passive'): True,
    ('GLDAS', 'CCI Active', 'SMOS-IC'): False,
    ('GLDAS', 'ASCAT 12.5 TS', 'SMOS-IC'): False
}

def tc_analysis(triplets, locations, anomaly=False):
    reader_dict = {}
    triplets = tools.get_triplet_list(triplets)
    print(triplets)
    # get data for each product for each location
    for triplet in triplets:
        for product in triplet:
            if product not in reader_dict.keys():
                reader_dict[product] = tools.get_product_reader(product, config.dict_product_inputs[product])
    location_counter = 0
    locations_len = len(list(config.dict_swe_gldas_points.keys()))
    for location, metadata in config.dict_swe_gldas_points.items():
        location_counter += 1
        tools.write_log(log_file, "analyzing {} of {} locations".format(location_counter, locations_len))
        ts_dict = {}
        for product, reader in reader_dict.items():
            lat = metadata["latitude"]
            lon = metadata["longitude"]
            ts_dict[product] = tools.get_product_data(lon=lon, lat=lat, product=product, reader=reader, anomaly=anomaly)
        for triplet in triplets:
            product1 = triplet[0]
            product2 = triplet[1]
            product3 = triplet[2]
            product1_data = ts_dict[product1]
            product2_data = ts_dict[product2]
            product3_data = ts_dict[product3]
            product1_data.rename('sm_1', inplace=True)
            product2_data.rename('sm_2', inplace=True)
            product3_data.rename('sm_3', inplace=True)
            tools.write_log(log_file, "{} {} data.shape: {}".format(location, product1, product1_data.shape))
            tools.write_log(log_file, "{} {} data.shape: {}".format(location, product2, product2_data.shape))
            tools.write_log(log_file, "{} {} data.shape: {}".format(location, product3, product3_data.shape))
            # print(product1_data.head())
            # print(product2_data.head())
            # print(product3_data.head())
            if product1_data.size > 0 and product2_data.size > 0 and product3_data.size > 0:
                matched_data = temporal_matching.matching(product2_data, product3_data, product1_data, window=.5)
                tools.write_log(log_file,
                    "{} [{}, {}, {}] matched_data.shape: {}".format(
                        location, product1, product2, product3, matched_data.shape))
            else:
                tools.write_log(log_file, "{} [{}, {}, {}] insufficient data to match".format(
                        location, product1, product2, product3))
    # for location, metadata in config.dict_swe_gldas_points.items():
    # pass


tc_results = tc_analysis(tc_analysis_triplets, config.dict_swe_gldas_points, anomaly=False)
