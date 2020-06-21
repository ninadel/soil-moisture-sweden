"""
Author: Nina del Rosario
Date: 5/25/2020
Script for evaluating SM datasets
"""
from datetime import datetime
import os
import pandas

from pytesmo import temporal_matching
import sm_tools as tools
import sm_config as config

# function which compares reference data to evaluation data
# reference can be either ISMN, ICOS, or GLDAS
# def evaluate(products, references, startdate, enddate):
def evaluate(references, products, output_folder, startdate=datetime(2015, 4, 1),
             enddate=datetime(2018, 12, 31, 23, 59), filter_ref=False, filter_prod=True, export_ts=True,
             evaluate_timeframes=True, anomaly=False, metrics_df=None):
    """""
    Function to compare soil moisture product to reference data
    Reference data supported: ICOS and ISMN (GLDAS forthcoming)

    Parameters
    references: list of ICOS or ISMN time series objects (adding GLDAS soon)
    products:   dictionary of product(s) to analyze, examples:
                evaluation_dict = {"ASCAT 12.5 TS": True}
                see product_parameters_dict in sm_config.py for dataset names and to set dataset parameters
    output_folder: directory where metrics and ts data will be saved
    startdate:  datetime used to filter product data to be analyzed (default 4/1/2015)
    enddate:    datetime used to filter product data to be analyzed (default 12/31/2018 23:59)
    filter_ref: boolean, in the case of ICOS data, if this is True only qc flag = 0 will be included 
    filter_prod: boolean, determines whether product data will be quality filtered, see sm_tools.py > get_product_data 
    export_ts: whether ts data (reference, product, and matched) should be exported as csv files to output_folder
    evaluate_timeframes: boolean, if true config.years_timeframes and config.seasons_timeframes will be evaluated
    metrics_df: df of metrics. if None, new metrics_df will be created. otherwise existing metrics_df will be extended.
    """""
    log_file = os.path.join(output_folder, "analysis_log.txt")
    data_output_folder = os.path.join(output_folder, "data_output")
    if not os.path.exists(data_output_folder):
        os.mkdir(data_output_folder)
    if metrics_df is None:
        metrics_df = pandas.DataFrame(columns=config.metrics_df_columns)
    else:
        metrics_df = metrics_df
    product_list = tools.get_product_list(products)
    if anomaly:
        anomaly_str = "anomaly"
    else:
        anomaly_str = "absolute"
    matched_data_dict = {}
    tools.write_log(
        log_file,
        "*** EVALUATION STARTING: {} - {}, filter_ref: {}, filter_prod: {}, evaluate_timeframes: {}, anomaly: {} ***".format(startdate, enddate, filter_ref, filter_prod, evaluate_timeframes, anomaly))
    for product in product_list:
        tools.write_log(log_file, "*** STARTING {} ANALYSIS ***".format(product))
        timeframe = "all-dates"
        product_str = product.replace(' ', '-')
        product_reader = tools.get_product_reader(product, config.dict_product_inputs[product])
        # product_sm_col = config.dict_product_fields[product]['sm_field']
        matched_data_dict = {}
        for station in references:
            ref_data_str = 'ref_data_{}_{}_{}_{}.csv'.format(station.network, station.station, timeframe, anomaly_str)
            product_data_str = 'product_data_{}_{}_{}_{}_{}.csv'.format(product_str, station.network, station.station,
                                                                        timeframe, anomaly_str)
            matched_data_str = 'station_matched_data_{}_{}_{}_{}_{}.csv'.format(product_str, station.network,
                                                                                station.station, timeframe, anomaly_str)
            if station.network not in matched_data_dict.keys():
                matched_data_dict[station.network] = pandas.DataFrame()
            tools.write_log(log_file, "*** analyzing {} x {} {} ***".format(product, station.network, station.station))
            ref_data = tools.get_ref_data(station, filter_ref, anomaly)[0]
            tools.write_log(log_file, 'ref_data.shape: {}'.format(ref_data.shape))
            # ref_sm_col = tools.get_ref_data(station)[1]
            ref_data.rename('ref_sm', inplace=True)
            product_data = tools.get_product_data(lon=station.longitude, lat=station.latitude, product=product,
                                                  reader=product_reader, filter_prod=filter_prod, anomaly=anomaly,
                                                  station=station)
            product_data.rename('product_sm', inplace=True)
            tools.write_log(log_file, 'product_data.shape: {}'.format(product_data.shape))
            product_data = product_data.loc[startdate:enddate]
            tools.write_log(log_file, 'product_data.shape (with date filter): {}'.format(product_data.shape))
            matched_data = temporal_matching.matching(product_data, ref_data, window=1 / 24.)
            network_matched_data = matched_data_dict[station.network]
            matched_data_dict[station.network] = pandas.concat([network_matched_data, matched_data])
            tools.write_log(log_file, '{} matched data shape: {}'.format(
                station.network, matched_data_dict[station.network].shape))
            tools.write_log(log_file, 'matched_data.shape: {}'.format(matched_data.shape))
            # insert scaling conditional here
            metric_values = tools.get_metrics(matched_data, 'product_sm', 'ref_sm', anomaly)
            n = matched_data.shape[0]
            station_metrics_df = pandas.DataFrame([[station.network, station.station, filter_ref, product_str,
                                                    filter_prod, timeframe, anomaly, n] + metric_values],
                                                  columns=config.metrics_df_columns)
            tools.write_log(log_file, str(station_metrics_df))
            metrics_df = pandas.concat([metrics_df, station_metrics_df])
            tools.write_log(log_file, '{} x {} {} analysis complete'.format(product, station.network, station.station))
            tools.write_log(log_file, '')
            if export_ts:
                ref_data.to_csv(os.path.join(data_output_folder, ref_data_str))
                product_data.to_csv(os.path.join(data_output_folder, product_data_str))
                matched_data.to_csv(os.path.join(data_output_folder, matched_data_str))
        # network level analysis
        tools.write_log(log_file, '*** analyzing networks ***')
        for network, network_matched_data in matched_data_dict.items():
            data_output_str = 'network_{}_{}_{}_matched_data.csv'.format(station.network, timeframe, anomaly_str)
            if export_ts:
                network_matched_data.to_csv(os.path.join(data_output_folder, data_output_str))
            tools.write_log(log_file, '*** analyzing {} ***'.format(network))
            metric_values = tools.get_metrics(network_matched_data, 'product_sm', 'ref_sm', anomaly)
            n = network_matched_data.shape[0]
            network_metrics_df = pandas.DataFrame([[station.network, "All", filter_ref, product_str, filter_prod,
                                                    timeframe, anomaly, n] + metric_values],
                                                  columns=config.metrics_df_columns)
            tools.write_log(log_file, str(network_metrics_df))
            metrics_df = pandas.concat([metrics_df, network_metrics_df])
            if evaluate_timeframes:
                if len(config.year_timeframes) > 0:
                    for year in config.year_timeframes:
                        timeframe = year
                        data_output_str = 'network_{}_{}_{}_matched_data.csv'.format(station.network, timeframe,
                                                                                     anomaly_str)
                        tools.write_log(log_file, '*** analyzing {} {} for {} ***'.format(network, timeframe, product))
                        tf_network_matched_data = tools.filter_df_by_timeframe(network_matched_data, year_filter=year)
                        if export_ts:
                            tf_network_matched_data.to_csv(os.path.join(data_output_folder, data_output_str))
                        tools.write_log(log_file, '{} {} matched data shape: {}'.format(station.network, timeframe,
                                                                                        tf_network_matched_data.shape))
                        metric_values = tools.get_metrics(tf_network_matched_data, 'product_sm', 'ref_sm', anomaly)
                        n = tf_network_matched_data.shape[0]
                        tf_network_metrics_df = pandas.DataFrame(
                            [[station.network, "All", filter_ref, product_str, filter_prod, timeframe, anomaly, n] +
                             metric_values], columns=config.metrics_df_columns)
                        tools.write_log(log_file, str(tf_network_metrics_df))
                        metrics_df = pandas.concat([metrics_df, tf_network_metrics_df])
                if len(config.season_timeframes) > 0:
                    for season in config.season_timeframes:
                        timeframe = season
                        data_output_str = 'network_{}_{}_{}_matched_data.csv'.format(station.network, timeframe,
                                                                                     anomaly_str)
                        tools.write_log(log_file, '*** analyzing {} {} for {} ***'.format(network, timeframe, product))
                        tf_network_matched_data = tools.filter_df_by_timeframe(network_matched_data,
                                                                               season_filter=season)
                        if export_ts:
                            tf_network_matched_data.to_csv(os.path.join(data_output_folder, data_output_str))
                        tools.write_log(log_file, '{} {} matched data shape: {}'.format(station.network, timeframe,
                                                                                        tf_network_matched_data.shape))
                        metric_values = tools.get_metrics(tf_network_matched_data, 'product_sm', 'ref_sm', anomaly)
                        n = tf_network_matched_data.shape[0]
                        tf_network_metrics_df = pandas.DataFrame(
                            [[station.network, "All", filter_ref, product_str, filter_prod, timeframe, anomaly, n] +
                             metric_values], columns=config.metrics_df_columns)
                        tools.write_log(log_file, str(tf_network_metrics_df))
                        metrics_df = pandas.concat([metrics_df, tf_network_metrics_df])
        tools.write_log(log_file, '*** {} ANALYSIS COMPLETE ***'.format(product))
        tools.write_log(log_file, '')
        metrics_df.reset_index(drop=True, inplace=True)
    return metrics_df
