"""
Author: Nina del Rosario
Date: 8/4/2020
Script for evaluating SM for each in-situ station (HOBE & ICOS)
Status: In progress
"""
from datetime import datetime
import os
import sm_tools as tools
import sm_config as config
import pandas as pd
import warnings
from multiprocessing import Pool
from pytesmo.temporal_matching import matching
from pytesmo.time_series.anomaly import calc_anomaly


def evaluate_csv_station(evaluation_dict, station):
    metrics = {}
    dataset = evaluation_dict['evaluation_dataset']
    start_date = evaluation_dict['start_date']
    end_date = evaluation_dict['end_date']
    match_window = evaluation_dict['match_window']
    anomaly = evaluation_dict['anomaly']
    evaluate_timefilters = evaluation_dict['evaluate_timefilters']
    verbose = evaluation_dict['verbose']
    dataset_folder = config.dict_product_inputs[dataset]['csv_stations']
    sm_field = config.dict_product_fields[dataset]['sm_field']
    network = station.network
    station_name = station.station
    eval_file = os.path.join(dataset_folder, "{}_{}.csv".format(network, station_name.replace(".", "-")))
    ref_data = tools.get_ref_data(station, anomaly=anomaly)
    ref_data = ref_data.tz_localize(None)
    eval_data = tools.csv_to_pdseries(eval_file)
    eval_data = eval_data[start_date:end_date]
    eval_data = tools.get_filtered_data(dataset, eval_data)
    eval_data = eval_data[sm_field]
    if anomaly:
        eval_data = calc_anomaly(eval_data)
    matched_data = matching(ref_data, eval_data, window=match_window)
    if evaluate_timefilters:
        timeframe_data_dict, timeframe_counts = tools.split_by_timeframe(matched_data, years=(2015,2018), months=False)
        for timeframe, timeframe_data in timeframe_data_dict.items():
            metrics[timeframe] = tools.get_metrics(data=timeframe_data, anomaly=anomaly, return_dict=True)
    else:
        metrics['No_Timefilter'] = tools.get_metrics(data=matched_data, anomaly=anomaly, return_dict=True)
    return metrics


def evaluation_csv_network(evaluation_dict):
    def get_station_metrics_df():
        metrics_df = pd.DataFrame(columns=['network', 'station', 'lon', 'lat', 'eval_dataset', 'timefilter', 'anomaly',
                                           'pearson_r', 'pearson_r_p-value', 'bias', 'rmsd', 'ubrmsd', 'n',
                                           'pearson_sig'])
        return metrics_df
    def get_station_metrics_row():
        metrics_row = {'network': network, 'station': station_name, 'lon': lon, 'lat': lat, 'eval_dataset': dataset,
                       'timefilter': timefilter, 'anomaly': anomaly_str}
        metrics_row.update(timefilter_metrics)
        return metrics_row
    metrics_df = None
    stations = evaluation_dict['stations']
    dataset = evaluation_dict['evaluation_dataset']
    anomaly = evaluation_dict['anomaly']
    output_root = evaluation_dict['output_root']
    verbose = evaluation_dict['verbose']
    if anomaly:
        anomaly_str = "anomaly"
    else:
        anomaly_str = "absolute"
    # evaluation_str = "{} {} {}".format(dataset, anomaly_str, datetime.now().strftime("%Y%m%d%H%M%S"))
    evaluation_str = "{} {}".format(dataset, anomaly_str)
    evaluation_metrics_file = os.path.join(output_root, "{} metrics.csv".format(evaluation_str))
    logfile = os.path.join(output_root, "{} log.txt".format(evaluation_str))
    for station in stations:
        network = station.network
        station_name = station.station
        station_evaluation_str = "{} {} {}".format(evaluation_str, network, station_name)
        lon = station.longitude
        lat = station.latitude
        try:
            station_metrics_dict = evaluate_csv_station(evaluation_dict, station)
            for timefilter, timefilter_metrics in station_metrics_dict.items():
                timefilter_evaluation_str = "{} {}".format(station_evaluation_str, timefilter)
                n = timefilter_metrics['n']
                sig = timefilter_metrics['pearson_sig']
                pearson_r = timefilter_metrics['pearson_r']
                tools.write_log(logfile, "{}, rows: {}".format(timefilter_evaluation_str, n), print_string=verbose)
                tools.write_log(logfile, "{}, pearson_r: {}".format(timefilter_evaluation_str, pearson_r),
                                print_string=verbose)
                tools.write_log(logfile, "{}, significant: {}".format(timefilter_evaluation_str, sig),
                                print_string=verbose)
                station_metrics_df = get_station_metrics_df()
                station_metrics_row = get_station_metrics_row()
                station_metrics_df = station_metrics_df.append(station_metrics_row, ignore_index=True)
                if not os.path.exists(evaluation_metrics_file):
                    station_metrics_df.to_csv(evaluation_metrics_file, index=False)
                else:
                    station_metrics_df.to_csv(evaluation_metrics_file, mode='a', header=False, index=False)
        except:
            tools.write_log(logfile, "{}: failed".format(station_evaluation_str), print_string=verbose)
    return metrics_df


def main(dataset):
    output_root = r"../analysis_output/station evaluation/{} {}".format(dataset, datetime.now().strftime("%Y%m%d%H%M%S"))
    if not os.path.exists(output_root):
        os.makedirs(output_root)
    icos_readers = tools.get_icos_readers(config.icos_input_dir)
    ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
    evaluation_stations = icos_readers + ismn_readers
    station_evaluation_dict = {
        'stations': evaluation_stations,
        'evaluation_dataset': dataset,
        'start_date': datetime(2015, 4, 1),
        'end_date': datetime(2018, 12, 31, 23, 59),
        'match_window': 1 / 24.,  # 1 hour
        'anomaly': None,
        'evaluate_timefilters': True,
        'output_root': output_root,
        'verbose': True
    }
    for anomaly_value in [False, True]:
        # try:
        evaluation_dict = station_evaluation_dict.copy()
        evaluation_dict['anomaly'] = anomaly_value
        evaluation_csv_network(evaluation_dict)
        break


if __name__ == '__main__':
    evaluation_datasets = ['ERA5 0-1', 'ERA5 0-25', 'SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'Sentinel-1',
                           'SMOS-BEC', 'SMOS-IC', 'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active', 'GLDAS']
    with Pool(5) as p:
        p.map(main, evaluation_datasets)

