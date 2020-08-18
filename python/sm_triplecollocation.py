from pytesmo import temporal_matching
from pytesmo.metrics import tcol_snr
import multiprocessing as mp
from datetime import datetime
from itertools import permutations
import os
import pandas
import sm_config as config
import sm_tools as tools
import math


def get_triplets(model, active, passive):
    triplets = []
    for m in model:
        for a in active:
            for p in passive:
                triplets.append((m,a,p))
    return triplets


def get_tc_dicts(triplets, loc_dict, output_root):
    tc_dicts = []
    mf = os.path.join(output_root, "tc_metrics.csv")
    lf = os.path.join(output_root, "tc_log.txt")
    for triplet in triplets:
        for anomaly_value in [False, True]:
            if anomaly_value:
                anomaly_str = "anomaly"
            else:
                anomaly_str = "absolute"
            tc_dict = {
                'triplet': triplet,
                'loc_dict': loc_dict,
                'output_root': output_root,
                'match_window': 1 / 24.,  # 1 hour
                'anomaly': anomaly_value,
                'verbose': True,
                'anomaly_str': anomaly_str,
                'evaluation_str': "{}_{}".format(triplet, anomaly_str),
                'metrics_file': mf,
                'logfile': lf
            }
            tc_dicts.append(tc_dict)
    return tc_dicts


def tc_analysis(tc_dict):
    def convert_snr_r(snr):
        # 1/squareroot(1 + (1/SNR))
        r = 1./math.sqrt(1. + (1./snr))
        return r

    def get_tc_df():
        metrics_df = pandas.DataFrame(columns=['location', 'lat', 'lon', 'location_veg_class', 'product', 'triplet',
                                               'n', 'snr', 'r', 'err_std', 'beta'])
        return metrics_df

    def get_metrics_row(calculate=True):
        metrics_row = {
            'location': loc, 'lat': lat, 'lon': lon, 'location_veg_class': loc_vc, 'product': product,
            'triplet': triplet, 'n': n, 'snr': None, 'r': None, 'err_std': None, 'beta': None
        }
        if calculate:
            metrics_row['snr'] = snr[idx]
            metrics_row['r'] = convert_snr_r(snr[idx])
            metrics_row['err_std'] = err_std[idx]
            metrics_row['beta'] = beta[idx]
        return metrics_row
    triplet = tc_dict['triplet']
    loc_dict = tc_dict['loc_dict']
    metrics_file = tc_dict['metrics_file']
    logfile = tc_dict['logfile']
    loc_counter = 0
    loc_len = len(list(loc_dict.keys()))
    for loc, loc_data in loc_dict.items():
        loc_counter += 1
        loc_vc = loc_data["veg_class_name"]
        lat = loc_data["latitude"]
        lon = loc_data["longitude"]
        ts_dict = {}
        tools.write_log(logfile, "analyzing {}: {} of {} locations".format(loc, loc_counter, loc_len))
        for dataset in triplet:
            csv_quarter_dir = os.path.join(config.dict_product_inputs[dataset]['csv_quarters'])
            loc_filename = os.path.join(csv_quarter_dir, "{}_{}.csv".format(dataset, loc))
            loc_data = tools.csv_to_pdseries(loc_filename)
            loc_data = loc_data.squeeze()
            loc_data.rename(dataset, inplace=True)
            loc_data.dropna()
            ts_dict[dataset] = loc_data
            tools.write_log(logfile, "{} {} data.shape: {}".format(loc, dataset, ts_dict[dataset].shape))
            perm = permutations(triplet)
            matched_data = pandas.DataFrame()
        if ts_dict[triplet[0]].size > 0 and ts_dict[triplet[1]].size > 0 and ts_dict[triplet[2]].size > 0:
            for p in perm:
                permutation_matched_data = temporal_matching.matching(ts_dict[p[0]], ts_dict[p[1]], ts_dict[p[2]],
                                                                      window=.5)
                if permutation_matched_data.shape[0] > matched_data.shape[0]:
                    matched_data = permutation_matched_data
                    product_order = p
            tools.write_log(logfile, "{} {} matched_data.shape: {}".format(loc, product_order, matched_data.shape))
        else:
            tools.write_log(logfile, "{} {} insufficient data to match".format(loc, triplet))
        n = matched_data.shape[0]
        try:
            snr, err_std, beta = tcol_snr(matched_data[triplet[0]].to_numpy(), matched_data[triplet[1]].to_numpy(),
                                          matched_data[triplet[2]].to_numpy())
            tools.write_log(logfile, '{} {} snr: {}'.format(loc, triplet, snr))
            tools.write_log(logfile, '{} {} err_std: {}'.format(loc, triplet, err_std))
            tools.write_log(logfile, '{} {} beta: {}'.format(loc, triplet, beta))
            for idx, product in enumerate(triplet):
                metrics_df = get_tc_df()
                metrics_row = get_metrics_row()
                metrics_df = metrics_df.append(metrics_row, ignore_index=True)
                if not os.path.exists(metrics_file):
                    metrics_df.to_csv(metrics_file, index=False)
                else:
                    metrics_df.to_csv(metrics_file, mode='a', header=False, index=False)
        except:
            for idx, product in enumerate(triplet):
                metrics_df = get_tc_df()
                metrics_row = get_metrics_row(calculate=False)
                metrics_df = metrics_df.append(metrics_row, ignore_index=True)
                if not os.path.exists(metrics_file):
                    metrics_df.to_csv(metrics_file, index=False)
                else:
                    metrics_df.to_csv(metrics_file, mode='a', header=False, index=False)
            tools.write_log(logfile, "{} {} could not run tcol analysis".format(loc, triplet))


if __name__ == '__main__':
    tc_output_root = r"../analysis_output/tc_analysis_{}".format(datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.makedirs(tc_output_root)
    # model = ["ERA5 0-1", "GLDAS"]
    # active = ["ASCAT 12.5 TS", "Sentinel-1", "CCI Active"]
    # passive = ["SMAP L3 Enhanced", "SMOS-IC"]
    model = ["ERA5 0-1"]
    active = ["ASCAT 12.5 TS"]
    passive = ["SMAP L3 Enhanced", "SMOS-IC"]
    triplets = get_triplets(model, active, passive)
    dicts = get_tc_dicts(triplets, config.dict_swe_gldas_points, tc_output_root)
    with mp.get_context("spawn").Pool(1) as p:
        p.map(tc_analysis, dicts)
