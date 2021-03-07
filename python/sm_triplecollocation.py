"""
Author: Nina del Rosario
Date: 2/10/2021
Script for evaluating SM products using triple collocation analysis
Includes adaptation of pytesmo tc_snr function: https://github.com/TUW-GEO/pytesmo/blob/master/src/pytesmo/metrics.py
Status: In progress
"""

from pytesmo import temporal_matching
# should we use this function or keep writing our own?
from pytesmo.metrics import tcol_snr as pytesmo_tcol_snr
from pytesmo.time_series.anomaly import calc_anomaly
import multiprocessing as mp
from datetime import datetime
from itertools import permutations
import os
import pandas
import sm_config as config
import sm_tools as tools
import numpy as np
import math

# function which generates permutations of modeled, active, and passive products
# based on the assumption that triplets analyzed in TC should be distinct (e.g. do not include 2 passive products in a
# triplet
def get_triplets(mod, act, pas):
    """
    Generates permutations of modeled, active, and passive products
    Based on the assumption that triplets analyzed in TC should be distinct (e.g. do not include 2 passive products in
    a triplet
    :param mod: list of model products
    :param act: list of active products
    :param pas: list of passive products
    :return: a list of triplets generated by permutations
    """

    trips = []
    for p in pas:
        for m in mod:
            for a in act:
                trips.append((p, m, a))
    return trips


# function which generates a dictionary which is used by the triple collocation analysis function
def get_tc_dicts(trips, loc_dict, root, calculate=True, export_matched=False, tcol_func="local",
                 export_calcs=False, match_window=0.5, anomaly_values=[True], verbose=False):
    """
    :param trips: list of three products to be evaluated
    :param loc_dict: a dictionary of locations to be evaluated, syntax:
        {
            "912322": {     // location name
            "latitude": 68.375,
            "longitude": 20.625,
            "veg_class_name": "Open Shrublands "
            }
                }
    :param root: directory where logs, datasets, and metrics will be saved to
    :param calculate: calculate tcol metrics (if false, generates matched data only without metrics)
    :param export_matched: whether matched datasets are exported to root as csv files
    :param tcol_func: formula used to calculate triple col metrics (e.g. pytesmo or sm_tools.py function)
    :param match_window: precision in temporal matching (e.g. 0.5 = 12 hours)
    :param anomaly_values: whether datasets being fed into tcol analysis are absolute or anomaly
    :param verbose: whether detailed output messages are printed
    :return: a list of dictionaries, where each dictionary describes a tcol analysis of a single point for 3 datasets
    """

    tcds = []

    for trip in trips:
        for anomaly_value in anomaly_values:
            for loc in loc_dict.keys():

                loc_data = config.dict_swe_gldas_points[loc]
                loc_vc = loc_data["veg_class_name"]

                # filter out irrelevant vegetation classes
                # need to fix: this is igno
                # if loc_vc not in config.ignore_veg_classes:
                #     break

                if anomaly_value:
                    anomaly_str = "anomaly"
                else:
                    anomaly_str = "absolute"

                evaluation_str = "{}_{}_{}_{}_{}".format(trip[0], trip[1], trip[2], anomaly_str, loc)

                logf = os.path.join(root, "tc_log_{}.txt".format(evaluation_str))

                if export_matched:
                    matf = os.path.join(root, 'matched_data', 'matched_{}.csv'.format(evaluation_str))
                else:
                    matf = None

                if tcol_func == "pytesmo":
                    pass
                else:
                    pass


                if calculate:
                    metf = os.path.join(root, "tc_metrics_{}.csv".format(evaluation_str))
                else:
                    metf = None

                tcd = {
                    'triplet': trip,
                    'loc': loc,
                    'output_root': root,
                    'match_window': match_window,
                    'anomaly': anomaly_value,
                    'verbose': verbose,
                    'anomaly_str': anomaly_str,
                    'evaluation_str': evaluation_str,
                    'calculate': calculate,
                    'export_calculations': export_calcs,
                    'metrics_file': metf,
                    'logfile': logf,
                    'tcol_function': tcol_func,
                    'export_matched': export_matched,
                    'matched_file': matf
                }

                tcds.append(tcd)

    return tcds


def tc_analysis(tc_dict, match_permutations=False):
    def get_tc_df():
        # mdf = pandas.DataFrame(columns=['location', 'lat', 'lon', 'location_veg_class', 'product', 'triplet', 'anomaly',
        #                                 'n', 'snr', 'r', 'err_std', 'beta'])
        mdf = pandas.DataFrame(columns=['location', 'lat', 'lon', 'location_veg_class', 'product', 'triplet', 'anomaly',
                                        'n', 'cov_0', 'cov_1', 'cov_2', 'snr', 'err_std', 'beta', 'r'])
        return mdf

    def get_metrics_row(calc=True):
        mr = {
            'location': loc, 'lat': lat, 'lon': lon, 'location_veg_class': loc_vc, 'product': product,
            'triplet': triplet, 'anomaly': anomaly_str, 'n': n, 'cov_0': None, 'cov_1': None, 'cov_2': None,
            'snr': None, 'err_std': None, 'beta': None, 'r': None
        }
        if calc:
            mr['cov_0'] = tcol_cov[idx][0]
            mr['cov_1'] = tcol_cov[idx][1]
            mr['cov_2'] = tcol_cov[idx][2]
            mr['snr'] = snr[idx]
            mr['err_std'] = err_std[idx]
            mr['beta'] = beta[idx]
            mr['r'] = (r[idx])
        return mr

    print(type(tc_dict))
    triplet = tc_dict['triplet']
    loc = tc_dict['loc']
    anomaly = tc_dict['anomaly']
    anomaly_str = tc_dict['anomaly_str']
    metrics_file = tc_dict['metrics_file']
    logfile = tc_dict['logfile']
    loc_data = config.dict_swe_gldas_points[loc]
    loc_vc = loc_data["veg_class_name"]
    lat = loc_data["latitude"]
    lon = loc_data["longitude"]
    calc = tc_dict["calculate"]
    match_window = tc_dict["match_window"]
    tcol_func = tc_dict['tcol_function']
    export_matched = tc_dict['export_matched']
    root = tc_dict['output_root']

    if export_matched:
        matched_subdir = os.path.join(root, "matched_data")
        if not os.path.exists(matched_subdir):
            os.mkdir(matched_subdir)
    ts_dict = {}

    for dataset in triplet:
        csv_quarter_dir = config.dict_product_inputs[dataset]['csv_quarters']
        loc_filename = os.path.join(csv_quarter_dir, "{}_{}.csv".format(dataset, loc))
        loc_data = tools.csv_to_pdseries(loc_filename)
        loc_data = loc_data.squeeze()
        if anomaly:
            loc_data = calc_anomaly(loc_data)
        loc_data.rename(dataset, inplace=True)
        loc_data.dropna()
        ts_dict[dataset] = loc_data
        tools.write_log(logfile, "{} {} data.shape: {}".format(loc, dataset, ts_dict[dataset].shape))

    # check that data is available for all three datasets
    if ts_dict[triplet[0]].size > 0 and ts_dict[triplet[1]].size > 0 and ts_dict[triplet[2]].size > 0:
        matched_data = None
        product_order = None

        if match_permutations:
            # go through each permutation of the three datasets and find the order that yields the most observations based
            # on temporal matching
            perms = permutations(triplet)
            for perm in perms:
                perm_matched_data = temporal_matching.matching(ts_dict[perm[0]], ts_dict[perm[1]], ts_dict[perm[2]],
                                                               window=match_window)
                if matched_data is None:
                    matched_data = perm_matched_data
                    product_order = perm
                elif perm_matched_data.shape[0] > matched_data.shape[0]:
                    matched_data = perm_matched_data
                    product_order = perm
        else:
            matched_data = temporal_matching.matching(ts_dict[triplet[0]], ts_dict[triplet[1]], ts_dict[triplet[2]],
                                                      window=match_window)
            product_order = triplet

        tools.write_log(logfile, "{} {} matched_data.shape: {}".format(loc, product_order, matched_data.shape))

    else:
        tools.write_log(logfile, "{} {} insufficient data to match".format(loc, triplet))

    n = matched_data.shape[0]

    # export matched data as csv
    if export_matched:
        matched_file = tc_dict['matched_file']
        matched_data.to_csv(matched_file)

    # try:
    if calc:
        # calculate tcol metrics using pytesmo function
        if tcol_func == "pytesmo":
            tcol_cov = np.array([None, None, None])
            snr, err_std, beta = pytesmo_tcol_snr(matched_data[triplet[0]].to_numpy(),
                                                  matched_data[triplet[1]].to_numpy(),
                                                  matched_data[triplet[2]].to_numpy())

        # calculate tcol metrics using local sm_tools.py function
        else:
            tcol_cov = tools.calc_tcol_cov(matched_data[triplet[0]].to_numpy(),
                                                  matched_data[triplet[1]].to_numpy(),
                                                  matched_data[triplet[2]].to_numpy())

            snr, err_std, beta = tools.calc_tcol_snr(matched_data[triplet[0]].to_numpy(),
                                                     matched_data[triplet[1]].to_numpy(),
                                                     matched_data[triplet[2]].to_numpy())

        r = tools.calc_tcol_r(snr)
        if tcol_func == "local":
            tools.write_log(logfile, '{} {} cov: {}'.format(loc, triplet, tcol_cov))
        tools.write_log(logfile, '{} {} snr: {}'.format(loc, triplet, snr))
        tools.write_log(logfile, '{} {} err_std: {}'.format(loc, triplet, err_std))
        tools.write_log(logfile, '{} {} beta: {}'.format(loc, triplet, beta))
        tools.write_log(logfile, '{} {} r: {}'.format(loc, triplet, r))

        for idx, product in enumerate(triplet):
            metrics_df = get_tc_df()
            metrics_row = get_metrics_row()
            metrics_df = metrics_df.append(metrics_row, ignore_index=True)
            if not os.path.exists(metrics_file):
                metrics_df.to_csv(metrics_file, index=False)
            else:
                metrics_df.to_csv(metrics_file, mode='a', header=False, index=False)
                
        print(metrics_file)

if __name__ == '__main__':
    output_root = r"../analysis_output/tc_analysis_{}".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    os.makedirs(output_root)
    # model = ["ERA5 0-1", "GLDAS"]
    # active = ["ASCAT 12.5 TS", "Sentinel-1", "CCI Active"]
    # passive = ["SMAP L3 Enhanced", "SMOS-IC"]
    model = ["ERA5 0-1"]
    active = ["ASCAT 12.5 TS"]
    # passive = ["SMAP L4", "SMAP L3"]
    passive = ["SMAP L3 Enhanced", "SMOS-IC"]
    calc_metrics = True
    exp_matched = True
    triplets = get_triplets(model, active, passive)
    # tc_dicts = get_tc_dicts(triplets, config.dict_swe_gldas_points, output_root, calculate=calc_metrics,
    #                         export_matched=exp_matched, anomaly_values=[False, True])
    tc_dicts = get_tc_dicts(triplets, config.dict_swe_gldas_points, output_root, calculate=calc_metrics,
                            export_matched=exp_matched, anomaly_values=[True])
    with mp.get_context("spawn").Pool(1) as p:
    # with mp.get_context("spawn").Pool(5) as p:
    #     p.map(tc_analysis, tc_dicts)
        p.map(tc_analysis, tc_dicts[0:5])
    # tc_analysis(tc_dicts[0])
    if calc_metrics:
        tc_metrics_files = [tc_dict['metrics_file'] for tc_dict in tc_dicts]
        tc_metrics_merged = tools.merge_tables(tc_metrics_files)
        tc_metrics_merged.to_csv(os.path.join(output_root, "tc_metrics.csv"), index=False)
    tc_log_files = [tc_dict['logfile'] for tc_dict in tc_dicts]
    master_logfile = os.path.join(output_root, "master_log.txt")
    with open(master_logfile, 'w') as outfile:
        for lf in tc_log_files:
            with open(lf) as infile:
                outfile.write(infile.read())

    print("merge complete")

