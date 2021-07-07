"""
Author: Nina del Rosario
Date: 5/25/2020
Script for evaluating SM datasets
UPDATE_DESCRIPTION
"""
from datetime import datetime
import os
import pandas as pd
import warnings

from pytesmo import metrics, temporal_matching
from pytesmo.scaling import scale
from pytesmo.time_series.anomaly import calc_anomaly
import sm_tools as tools
import sm_config as config


# function to evaluate time series for two datasets for one location
# input: dictionary datasets, ref = tuple of name, data, eval = tuple of name, data
# output: dictionary of location metrics, dictionary of metrics, matched data
# evaluate location
def evaluate_gridcell_xr(evaluation_dict, lon, lat):
    # reference: tuple of reference dataset name and reference dataset
    # reference name is a string, reference_dataset is an xarray dataset
    ref_dataset_name, ref_dataset = evaluation_dict['reference']
    # evaluation: a tuple of evaluation dataset name and evaluation dataset
    # evaluation_name is a string, evaluation_dataset is an xarray dataset
    eval_dataset_name, eval_dataset = evaluation_dict['evaluation']
    # start_date is a datetime.datetime object
    start_date = evaluation_dict['start_date']
    # end_date is a datetime.datetime object
    end_date = evaluation_dict['end_date']
    # anomaly: boolean which determines if absolute or anomaly values are calculated
    anomaly = evaluation_dict['anomaly']
    # match window: number value for temporal matching (1 hour = 1/24.)
    match_window = evaluation_dict['match_window']
    # evaluate_timeframes: a boolean - if True, matched data will be split into timeframes and a separate metrics table and inventory table
    # will be returned
    evaluate_timeframes = evaluation_dict['evaluate_timeframes']
    data = {}
    metrics = {}
    ref_sm_field = config.dict_product_fields[ref_dataset_name]['sm_field']
    eval_sm_field = config.dict_product_fields[eval_dataset_name]['sm_field']
    ref_ts = ref_dataset[ref_sm_field]
    eval_ts = eval_dataset[eval_sm_field]
    ref_ts = ref_ts.sel(time=slice(start_date, end_date), lat=lat, lon=lon).to_pandas()
    eval_ts = eval_ts.sel(time=slice(start_date, end_date), lat=lat, lon=lon).to_pandas()
    ref_ts.rename('ref_sm', inplace=True)
    ref_ts = ref_ts.to_frame()
    eval_ts.rename('eval_ts', inplace=True)
    eval_ts = eval_ts.to_frame()
    matched_data = temporal_matching.matching(ref_ts, eval_ts, window=match_window)
    data['matched_data'] = matched_data
    data['ref_ts'] = ref_ts
    data['eval_ts'] = eval_ts
    metrics['all'] = tools.get_metrics(data=matched_data, anomaly=anomaly, return_dict=True)
    if evaluate_timeframes:
        timeframe_data_dict, timeframe_counts = tools.split_by_timeframe(matched_data)
        for timeframe, timeframe_data in timeframe_data_dict.items():
            metrics[timeframe] = tools.get_metrics(data=timeframe_data, anomaly=anomaly, return_dict=True)
    return metrics, data


# function to cycle through each in-situ station in a network, evaluate network-level timeframes
# input: folder for in-situ station data
# output: dictionary of
# evaluate station network
def evaluate_insitu_network_xr(evaluation_dict):
    # evaluation: a tuple of evaluation dataset name and evaluation dataset
    # evaluation_name is a string, evaluation_dataset is an xarray dataset
    evaluation_name, evaluation_dataset = evaluation_dict['evaluation']
    # network: a tuple of the network name and the folder where network in-situ data is located
    network_name, network_data = evaluation_dict['network']
    # start_date is a datetime.datetime object
    start_date = evaluation_dict['start_date']
    # end_date is a datetime.datetime object
    end_date = evaluation_dict['end_date']
    # match window: number value for temporal matching (1 hour = 1/24.)
    match_window = evaluation_dict['match_window']
    # evaluate_timeframes: a boolean - if True, matched data will be split into timeframes and a separate metrics table and inventory table
    # will be returned
    evaluate_timeframes = evaluation_dict['evaluate_timeframes']
    # export_ts: a boolean - if True, time series data (reference, evaluation, matched) will be exported as csv to output_folder,
    # but metrics and inventory will be exported
    export_ts = evaluation_dict['export_ts']
    # output_root: a folder location to output metrics table, inventory table, and datasets (if export_datasets = True)
    # if None, output will be returned by function but not saved to file
    output_root = evaluation_dict['output_root']
    # cycle through each location
        # metrics, matched_data = evaluate_location_xr(dataset_dict)
        # get metrics and add to df
        # get inventory and add to df
        # for each timeframe
            # add matched data to
    # build dataframe of all matched data
    pass


# function for evaluating a set of grid cells in a region
def evaluate_grid_xr(evaluation_dict):
    def get_new_grid_metrics_df():
        metrics_df = pd.DataFrame(columns=['ref_dataset', 'eval_dataset', 'timefilter', 'anomaly', 'loc',
                                               'lon', 'lat', 'veg_class', 'pearson_r', 'pearson_r_p-value', 'bias',
                                               'rmsd', 'ubrmsd', 'n', 'pearson_sig'])
        return metrics_df
    def get_grid_metrics_row():
        metrics_row = {'ref_dataset': ref_dataset_name, 'eval_dataset': eval_dataset_name, 'timefilter': timeframe,
                       'anomaly': anomaly, 'loc': loc, 'lon': lon, 'lat': lat, 'veg_class': veg_class}
        return metrics_row
    # locations: a dictionary where each key is a location name,
    # the value is another dictionary with "longitude" and "latitude" keys that have numeric coordinate values
    locations = evaluation_dict['locations']
    # reference: tuple of reference dataset name and reference dataset
    # reference name is a string, reference_dataset is an xarray dataset
    ref_dataset_name, ref_dataset = evaluation_dict['reference']
    # evaluation: a tuple of evaluation dataset name and evaluation dataset
    # evaluation_name is a string, evaluation_dataset is an xarray dataset
    eval_dataset_name, eval_dataset = evaluation_dict['evaluation']
    # anomaly: boolean which determines if absolute or anomaly values are calculated
    anomaly = evaluation_dict['anomaly']
    # export_ts: a boolean - if True, time series data (reference, evaluation, matched) will be exported as csv to output_folder,
    # but metrics and inventory will be exported
    export_ts = evaluation_dict['export_ts']
    # output_root: a folder location to output metrics table, inventory table, and datasets (if export_datasets = True)
    # a subfolder for each evaluation dataset will be created
    output_root = evaluation_dict['output_root']
    # verbose: boolean which determines if log messages are printed (if false, warnings will still be printed)
    verbose = evaluation_dict['verbose']
    metrics_dict = {}
    if anomaly:
        anomaly_str = "anomaly"
    else:
        anomaly_str = "absolute"
    evaluation_str = "{} {} {}".format(eval_dataset_name, ref_dataset_name, anomaly_str)
    output_folder = os.path.join(output_root, evaluation_str)
    os.makedirs(output_folder)
    if export_ts:
        ts_folder = os.path.join(output_folder, "ts_folder")
        os.mkdir(ts_folder)
    logfile = os.path.join(output_folder, "{} log.txt".format(evaluation_str))
    tools.write_log(logfile, evaluation_str, print_string=verbose)
    for loc, loc_data in locations.items():
        loc_evaluation_str = "{} {}".format(evaluation_str, loc)
        try:
            lon = loc_data['longitude']
            lat = loc_data['latitude']
            veg_class = loc_data['veg_class_name']
            loc_metrics_dict, loc_data_dict = evaluate_gridcell_xr(evaluation_dict=evaluation_dict, lon=lon, lat=lat)
            for timefilter, timefilter_metrics in loc_metrics_dict.items():
                timefilter_evaluation_str = "{} {}".format(loc_evaluation_str, timefilter)
                n = timefilter_metrics['n']
                sig = timefilter_metrics['pearson_sig']
                pearson_r = timefilter_metrics['pearson_r']
                tools.write_log(logfile, "{}, rows: {}".format(timefilter_evaluation_str, n), print_string=verbose)
                tools.write_log(logfile, "{}, pearson_r: {}".format(timefilter_evaluation_str, pearson_r),
                                print_string=verbose)
                tools.write_log(logfile, "{}, significant: {}".format(timefilter_evaluation_str, sig),
                                print_string=verbose)
                loc_metrics_row = get_grid_metrics_row()
                loc_metrics_row.update(timefilter_metrics)
                if timefilter not in metrics_dict.keys():
                    metrics_dict[timefilter] = get_new_grid_metrics_df()
                metrics_dict[timefilter] = metrics_dict[timefilter].append(loc_metrics_row, ignore_index=True)
            if export_ts:
                loc_ref_data = loc_data_dict['ref_ts']
                loc_ref_data.to_csv(os.path.join(os.path.join(ts_folder, "{} {} ts.csv".format(ref_dataset_name, loc))))
                loc_eval_data = loc_data_dict['eval_ts']
                loc_eval_data.to_csv(os.path.join(os.path.join(ts_folder, "{} {} ts.csv".format(eval_dataset_name, loc))))
                loc_matched_data = loc_data_dict['matched_data']
                loc_matched_data.to_csv(os.path.join(os.path.join(ts_folder, "{} matched.csv".format(loc_evaluation_str))))
        except:
            message = "WARNING! could not process {}".format(loc_evaluation_str)
            warnings.warn(message)
            tools.write_log(logfile, message, print_string=verbose)
    for timeframe, metrics_df in metrics_dict.items():
        metrics_df.to_csv(os.path.join(output_folder, "{} {} metrics.csv".format(evaluation_str, timeframe)),
                          index=False)
    return metrics_dict

