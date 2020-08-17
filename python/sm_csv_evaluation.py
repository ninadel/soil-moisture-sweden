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
from multiprocessing import Pool
from pytesmo.temporal_matching import matching
from pytesmo.time_series.anomaly import calc_anomaly


def get_output_root(dataset):
    output_root = r"../analysis_output/station evaluation/{} {}".format(dataset,
                                                                        datetime.now().strftime("%Y%m%d%H%M%S"))
    return output_root


def evaluate_csv_station(evaluation_dict, station):
    metrics = {}
    dataset = evaluation_dict['evaluation_dataset']
    start_date = evaluation_dict['start_date']
    end_date = evaluation_dict['end_date']
    match_window = evaluation_dict['match_window']
    anomaly = evaluation_dict['anomaly']
    evaluate_timefilters = evaluation_dict['evaluate_timefilters']
    evaluate_years = evaluate_timefilters[0]
    evaluate_seasons = evaluate_timefilters[1]
    evaluate_months = evaluate_timefilters[2]
    dataset_folder = config.dict_product_inputs[dataset]['csv_stations']
    sm_field = config.dict_product_fields[dataset]['sm_field']
    network = station.network
    station_name = station.station
    eval_file = os.path.join(dataset_folder, "{}_{}.csv".format(network, station_name.replace(".", "-")))
    ref_data = tools.get_ref_data(station, anomaly=anomaly)
    ref_data = ref_data.tz_localize(None)
    ref_data.rename('ref_sm', inplace=True)
    eval_data = tools.csv_to_pdseries(eval_file)
    eval_data = eval_data[start_date:end_date]
    eval_data = tools.get_filtered_data(dataset, eval_data)
    eval_data = eval_data[sm_field]
    eval_data.dropna()
    if anomaly:
        eval_data = calc_anomaly(eval_data)
    eval_data.rename('eval_sm', inplace=True)
    matched_data = matching(ref_data, eval_data, window=match_window)
    timefilter_data_dict, timefilter_counts = tools.split_by_timeframe(matched_data, years=evaluate_years,
                                                                     seasons=evaluate_seasons, months=evaluate_months)
    for timefilter, timefilter_data in timefilter_data_dict.items():
        metrics[timefilter] = tools.get_metrics(data=timefilter_data, anomaly=anomaly, return_dict=True)
    return metrics, matched_data


def evaluate_csv_network(evaluation_dict, network_matched_data):
    metrics = {}
    anomaly = evaluation_dict['anomaly']
    evaluate_timefilters = evaluation_dict['evaluate_timefilters']
    evaluate_years = evaluate_timefilters[0]
    evaluate_seasons = evaluate_timefilters[1]
    evaluate_months = evaluate_timefilters[2]
    timefilter_data_dict, timefilter_counts = tools.split_by_timeframe(network_matched_data, years=evaluate_years,
                                                                     seasons=evaluate_seasons, months=evaluate_months)
    for timefilter, timefilter_data in timefilter_data_dict.items():
        metrics[timefilter] = tools.get_metrics(data=timefilter_data, anomaly=anomaly, return_dict=True)
    return metrics


def evaluation_csv(evaluation_dict):
    def get_station_metrics_df():
        metrics_df = pd.DataFrame(columns=['network', 'station', 'station_code', 'lon', 'lat', 'cover', 'eval_dataset',
                                           'timefilter', 'anomaly', 'pearson_r', 'pearson_r_p-value', 'bias', 'rmsd',
                                           'ubrmsd', 'n', 'pearson_sig'])
        return metrics_df
    def get_station_metrics_row():
        metrics_row = {'network': network, 'station': station_name, 'station_code': station_code, 'lon': lon,
                       'lat': lat, 'cover': station_cover, 'eval_dataset': dataset, 'timefilter': timefilter,
                       'anomaly': anomaly_str}
        metrics_row.update(timefilter_metrics)
        return metrics_row
    def get_network_metrics_df():
        metrics_df = pd.DataFrame(columns=['network', 'eval_dataset', 'timefilter', 'anomaly', 'pearson_r',
                                           'pearson_r_p-value', 'bias', 'rmsd', 'ubrmsd', 'n', 'pearson_sig'])
        return metrics_df
    def get_network_metrics_row():
        metrics_row = {'network': network, 'eval_dataset': dataset, 'timefilter': timefilter, 'anomaly': anomaly_str}
        metrics_row.update(timefilter_metrics)
        return metrics_row
    def log_results():
        tools.write_log(logfile, timefilter_evaluation_str, print_string=verbose)
        n = timefilter_metrics['n']
        sig = timefilter_metrics['pearson_sig']
        pearson_r = timefilter_metrics['pearson_r']
        tools.write_log(logfile, "{}, rows: {}".format(timefilter_evaluation_str, n), print_string=verbose)
        tools.write_log(logfile, "{}, pearson_r: {}".format(timefilter_evaluation_str, pearson_r),
                        print_string=verbose)
        tools.write_log(logfile, "{}, significant: {}".format(timefilter_evaluation_str, sig),
                        print_string=verbose)
    stations = evaluation_dict['stations']
    dataset = evaluation_dict['evaluation_dataset']
    anomaly = evaluation_dict['anomaly']
    output_root = evaluation_dict['output_root']
    export_matched = evaluation_dict['export_matched']
    verbose = evaluation_dict['verbose']
    if anomaly:
        anomaly_str = "anomaly"
    else:
        anomaly_str = "absolute"
    if export_matched:
        matched_data_folder = os.path.join(output_root, "matched_data")
        if not os.path.exists(matched_data_folder):
            os.makedirs(matched_data_folder)
    evaluation_str = "{}_{}".format(dataset, anomaly_str)
    station_evaluation_metrics_file = os.path.join(output_root, "{} station metrics.csv".format(evaluation_str))
    network_evaluation_metrics_file = os.path.join(output_root, "{} network metrics.csv".format(evaluation_str))
    logfile = os.path.join(output_root, "{} log.txt".format(evaluation_str))
    tools.write_log(logfile, evaluation_str, print_string=verbose)
    matched_data_dict = {}
    for station in stations:
        network = station.network
        station_name = station.station
        station_cover = tools.get_station_cover(station)
        station_code = tools.get_station_code(station)
        station_evaluation_str = "{}_{}".format(evaluation_str, station_code)
        tools.write_log(logfile, station_evaluation_str, print_string=verbose)
        lon = station.longitude
        lat = station.latitude
        try:
            station_metrics_dict, matched_data = evaluate_csv_station(evaluation_dict, station)
            if export_matched:
                matched_data_file = os.path.join(matched_data_folder, "{}_matched.csv".format(station_evaluation_str))
                matched_data.to_csv(matched_data_file)
            if network not in matched_data_dict.keys():
                matched_data_dict[network] = {}
            matched_data_dict[network][station_code] = matched_data
            for timefilter, timefilter_metrics in station_metrics_dict.items():
                timefilter_evaluation_str = "{}_{}".format(station_evaluation_str, timefilter)
                log_results()
                station_metrics_df = get_station_metrics_df()
                station_metrics_row = get_station_metrics_row()
                station_metrics_df = station_metrics_df.append(station_metrics_row, ignore_index=True)
                if not os.path.exists(station_evaluation_metrics_file):
                    station_metrics_df.to_csv(station_evaluation_metrics_file, index=False)
                else:
                    station_metrics_df.to_csv(station_evaluation_metrics_file, mode='a', header=False, index=False)
        except:
            tools.write_log(logfile, "{}: failed".format(station_evaluation_str), print_string=verbose)
    for network_key, network_stations_dict in matched_data_dict.items():
        network_matched_data = None
        for station_code, station_matched_data in network_stations_dict.items():
            if network_matched_data is None:
                network_matched_data = station_matched_data
            else:
                network_matched_data = pd.concat([network_matched_data, station_matched_data])
        network_evaluation_str = "{}_{}".format(evaluation_str, network_key)
        network_metrics_dict = evaluate_csv_network(evaluation_dict, network_matched_data)
        for timefilter, timefilter_metrics in network_metrics_dict.items():
            timefilter_evaluation_str = "{}_{}".format(network_evaluation_str, timefilter)
            log_results()
            network_metrics_df = get_network_metrics_df()
            network_metrics_row = get_network_metrics_row()
            network_metrics_df = network_metrics_df.append(network_metrics_row, ignore_index=True)
            if not os.path.exists(network_evaluation_metrics_file):
                network_metrics_df.to_csv(network_evaluation_metrics_file, index=False)
            else:
                network_metrics_df.to_csv(network_evaluation_metrics_file, mode='a', header=False, index=False)


def main(dataset):
    output_root = get_output_root(dataset)
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
        'evaluate_timefilters': ((2015, 2018), True, True),
        'output_root': output_root,
        'export_matched': True,
        'verbose': True
    }
    for anomaly_value in [False, True]:
        evaluation_dict = station_evaluation_dict.copy()
        evaluation_dict['anomaly'] = anomaly_value
        evaluation_csv(evaluation_dict)



if __name__ == '__main__':
    evaluation_datasets = ['ERA5 0-1', 'ERA5 0-25', 'SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'Sentinel-1',
                           'SMOS-BEC', 'SMOS-IC', 'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active', 'GLDAS']
    with Pool(5) as p:
        p.map(main, evaluation_datasets)



