"""
Author: Nina del Rosario
Date: 5/25/2020
Script for evaluating SM datasets
"""
from datetime import datetime
import os
import pandas
import pytz
import warnings

from pytesmo import metrics, temporal_matching
from pytesmo.scaling import scale
import sm_tools as tools
import sm_config as config


def evaluate_station_product(station, product, product_reader=None, startdate=datetime(2015, 4, 1),
                             enddate=datetime(2018, 12, 31, 23, 59), anomaly=False, year_filter=None,
                             season_filter=None, match_window=1/24., scale_method=None, logfile=None):
    """
    Description: Matches and evaluates data for a single location

    Parameters
    ----------
    station : ISMN_time_series object
    product : string, must match a product in dict_product_fields.json dictionary
    product_reader_dict : dict, dictionary of product readers. If None, new product reader will be initiated.
        (default: None)
    startdate: datetime object (default: None)
    enddate: datetime object (default: None)
    anomaly: boolean (default: None)
    year_filter: string (default: None)
    season_filter: string (default: None)
    match_window: number which indicates window used by pytesmo.temporal_matching (default: 1/24.)
    scale_method: scaling method used by pytesmo.scaling (default: None)

    Returns
    ----------
    dictionary with station timeseries, product timeseries, matched timeseries, and metrics
    """
    evaluation_dict = {}
    station_name = station.station
    print(station_name)
    evaluation_dict['station'] = station_name
    evaluation_dict['product'] = product
    evaluation_dict['startdate'] = startdate
    evaluation_dict['enddate'] = enddate
    evaluation_dict['anomaly'] = anomaly
    evaluation_dict['year_filter'] = year_filter
    evaluation_dict['season_filter'] = season_filter
    # get station data
    station_data = tools.get_ref_data(station, anomaly=anomaly)
    print('station_data.shape', station_data.shape)
    station_data.rename('ref_sm', inplace=True)
    # get product data
    if product_reader is None:
        product_metadata = config.dict_product_inputs[product]
        product_reader = tools.get_product_reader(product, product_metadata)

    try:
        product_data = tools.get_product_data(lon=station.longitude, lat=station.latitude, product=product,
                                              reader=product_reader, anomaly=anomaly, station=station)
        product_data.rename(product, inplace=True)
        print('product_data.shape', product_data.shape)
    except:
        print("can't get product data")
        return None
    # filter product data by date/timeframe
    if startdate is not None and enddate is not None:
        product_data = product_data[(product_data.index >= startdate) & (product_data.index <= enddate)]
    elif startdate is not None:
        product_data = product_data[product_data.index >= startdate]
    elif enddate is not None:
        product_data = product_data[product_data.index <= enddate]
    if year_filter is not None:
        product_data = tools.get_timeframe_data(product_data, year_filter=year_filter)
    if season_filter is not None:
        product_data = tools.get_timeframe_data(product_data, season_filter=season_filter)

    try:
        matched_data = temporal_matching.matching(product_data, station_data, window=match_window)
    except:
        matched_data = None

    if matched_data is not None and scale_method is not None:
        try:
            matched_data = scale(matched_data, method=scale_method, reference_index=1)
            evaluation_dict['evaluation_data'] = matched_data
            evaluation_dict['scaled'] = True
        except:
            evaluation_dict['evaluation_data'] = None
            evaluation_dict['scaled'] = True
    else:
        evaluation_dict['evaluation_data'] = matched_data
        evaluation_dict['scaled'] = False

    evaluation_dict['n'] = evaluation_dict['evaluation_data'].shape[0]

    if evaluation_dict['evaluation_data'] is not None:
        try:
            evaluation_dict['metrics'] = get_evaluation_metrics(evaluation_dict['evaluation_data'], anomaly)
        except:
            evaluation_dict['metrics']

    return evaluation_dict


def evaluate_network_product(stations, product, startdate=datetime(2015, 4, 1),
                             enddate=datetime(2018, 12, 31, 23, 59), anomaly=False, year_filter=None,
                             season_filter=None, match_window=1/24., scale_method=None, logfile=None):
    """
    Description: Matches and evaluates data for a single location

    Parameters
    ----------
    station : list of ISMN_time_series objects
    product : string, must match a product in dict_product_fields.json dictionary
    product_reader_dict : dict, dictionary of product readers. If None, new product reader will be initiated.
        (default: None)
    startdate: datetime object (default: None)
    enddate: datetime object (default: None)
    anomaly: boolean (default: None)
    year_filter: string (default: None)
    season_filter: string (default: None)
    match_window: number which indicates window used by pytesmo.temporal_matching (default: 1/24.)
    scale_method: scaling method used by pytesmo.scaling (default: None)

    Returns
    ----------
    dictionary 1:
        dictionary of network-level metrics
    dictionary 2:
        first level of keys are network names
        second level of keys are station names
        values for station keys are a dictionary of station timeseries, product timeseries, matched timeseries,
            and metrics
    """

    station_evaluation_dict = {}
    network_evaluation_dict = {}
    network_evaluation_dict['product'] = product
    network_evaluation_dict['startdate'] = startdate
    network_evaluation_dict['enddate'] = enddate
    network_evaluation_dict['anomaly'] = anomaly
    network_evaluation_dict['year_filter'] = year_filter
    network_evaluation_dict['season_filter'] = season_filter

    product_metadata = config.dict_product_inputs[product]
    product_reader = tools.get_product_reader(product, product_metadata)

    for station in stations:
        station_name = station.station
        network_name = station.network
        if network_name not in station_evaluation_dict.keys():
            station_evaluation_dict[network_name] = {}
        if network_name not in network_evaluation_dict.keys():
            network_evaluation_dict[network_name] = {}
        station_evaluation_dict[network_name][station_name] = evaluate_station_product(
            station=station, product=product, product_reader=product_reader, startdate=startdate,
            enddate=enddate, anomaly=anomaly, year_filter=year_filter, season_filter=season_filter,
            match_window=match_window, scale_method=scale_method)

    for network, stations in station_evaluation_dict.items():
        network_evaluation_dict[network_name]
        for station, station_dict in stations.items():
            if 'scaled' not in network_evaluation_dict[network_name].keys():
                network_evaluation_dict[network_name]['scaled'] = station_dict['scaled']
            if 'evaluation_data' not in network_evaluation_dict[network_name].keys():
                network_evaluation_dict[network_name]['evaluation_data'] = station_dict['evaluation_data']
            else:
                if station_dict['evaluation_data'] is not None:
                    network_evaluation_dict[network_name]['evaluation_data'] = \
                        pandas.concat([network_evaluation_dict[network_name]['evaluation_data'],
                                       station_dict['evaluation_data']])

    for network, network_dict in network_evaluation_dict.items():
        network_dict['n'] = network_dict['evaluation_data'].shape[0]
        network_dict['metrics'] = get_evaluation_metrics(network_dict['evaluation_data'], anomaly)

    return network_evaluation_dict, station_evaluation_dict


def evaluate_timeframe(matched_data, year_filter=None, season_filter=None, anomaly=False):
    timeframe_data = tools.get_timeframe_data(matched_data, year_filter, season_filter)
    timeframe_metrics = get_evaluation_metrics(timeframe_data, anomaly)
    return timeframe_metrics


def get_evaluation_metrics(evaluation_data, anomaly):
    metrics_dict = {}

    columns = evaluation_data.columns
    x = evaluation_data[columns[0]].values
    y = evaluation_data[columns[1]].values

    if anomaly:
        metrics_dict['bias'] = None
        metrics_dict['rmsd'] = None
        metrics_dict['ubrmsd'] = None

    try:
        if anomaly is False:
            metrics_dict['bias'] = metrics.bias(x, y)
            metrics_dict['rmsd'] = metrics.rmsd(x, y)
            metrics_dict['ubrmsd'] = metrics.ubrmsd(x, y)
    except:
        metrics_dict['bias'] = None
        metrics_dict['rmsd'] = None
        metrics_dict['ubrmsd'] = None

    try:
        metrics_dict['pearson_r'] = metrics.pearsonr(x, y)[0]
        metrics_dict['pearson_r_p-value'] = metrics.pearsonr(x, y)[1]
    except:
        metrics_dict['pearson_r'] = None
        metrics_dict['pearson_r_p-value'] = None

    return metrics_dict

def evaluate(references, products, output_folder, startdate=datetime(2015, 4, 1), enddate=datetime(2018, 12, 31, 23, 59),
             export_ts=True, evaluate_timeframes=True, anomaly=False, metrics_df=None):
    """""
    Function to compare soil moisture product to reference data
    Reference data supported: ICOS and ISMN (GLDAS forthcoming)

    Parameters
    ----------
    references: list of ICOS or ISMN time series objects (adding GLDAS soon)
    products:   dictionary of product(s) to analyze, examples:
                evaluation_dict = {"ASCAT 12.5 TS": True}
                see product_parameters_dict in sm_config.py for dataset names and to set dataset parameters
    output_folder: directory where metrics and ts data will be saved
    startdate:  datetime used to filter product data to be analyzed (default 4/1/2015)
    enddate:    datetime used to filter product data to be analyzed (default 12/31/2018 23:59)
    export_ts: whether ts data (reference, product, and matched) should be exported as csv files to output_folder
    evaluate_timeframes: boolean, if true config.years_timeframes and config.seasons_timeframes will be evaluated
    metrics_df: df of metrics. if None, new metrics_df will be created. otherwise existing metrics_df will be extended.
    """""
    log_file = os.path.join(output_folder, "analysis_log.txt")
    data_output_folder = os.path.join(output_folder, "data_output")

    # in case analysis fails, get an empty metrics row to indicate that something failed
    def get_empty_metrics_df():
        empty_df = pandas.DataFrame([[network_name, station_name, product_str, timeframe, anomaly, n, None, None,
                                      None, None, None]], columns=config.metrics_df_columns)
        return empty_df

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
        "*** EVALUATION STARTING: {} - {}, evaluate_timeframes: {}, anomaly: {} ***".format(
            startdate, enddate, evaluate_timeframes, anomaly))
    for product in product_list:
        tools.write_log(log_file, "*** STARTING {} ({}) ANALYSIS ***".format(product, anomaly_str))
        timeframe = "all-dates"
        product_str = product.replace(' ', '-')
        product_reader = tools.get_product_reader(product, config.dict_product_inputs[product])
        # product_sm_col = config.dict_product_fields[product]['sm_field']
        matched_data_dict = {}
        for station in references:
            station_name = station.station
            network_name = station.network
            ref_data_str = 'ref_data_{}_{}_{}_{}.csv'.format(network_name, station_name, timeframe, anomaly_str)
            product_data_str = 'product_data_{}_{}_{}_{}_{}.csv'.format(product_str, network_name, station_name,
                                                                        timeframe, anomaly_str)
            matched_data_str = 'station_matched_data_{}_{}_{}_{}_{}.csv'.format(product_str, network_name,
                                                                                station_name, timeframe, anomaly_str)
            # scaled_data_str = 'station_scaled_data_{}_{}_{}_{}_{}.csv'.format(product_str, network_name,
            #                                                                   station_name, timeframe, anomaly_str)
            if network_name not in matched_data_dict.keys():
                matched_data_dict[network_name] = pandas.DataFrame()
            tools.write_log(log_file, "*** analyzing {} x {} {} ({}) ***".format(product, network_name,
                                                                                 station_name, anomaly_str))
            ref_data = tools.get_ref_data(station, anomaly=anomaly)
            tools.write_log(log_file, 'ref_data.shape: {}'.format(ref_data.shape))
            if export_ts:
                ref_data.to_csv(os.path.join(data_output_folder, ref_data_str))
            # ref_sm_col = tools.get_ref_data(station)[1]
            ref_data.rename('ref_sm', inplace=True)
            product_data = tools.get_product_data(lon=station.longitude, lat=station.latitude, product=product,
                                                  reader=product_reader, anomaly=anomaly, station=station)
            print("product_data")
            print(product_data)
            print(type(product_data))
            product_data.rename('product_sm', inplace=True)
            tools.write_log(log_file, 'product_data.shape: {}'.format(product_data.shape))
            product_data = product_data.loc[startdate:enddate]
            tools.write_log(log_file, 'product_data.shape (with date filter): {}'.format(product_data.shape))
            product_data = tools.get_timeshifted_data(product, product_data)
            if export_ts:
                product_data.to_csv(os.path.join(data_output_folder, product_data_str))
            matched_data = pandas.DataFrame()
            if product_data.shape[0] > 0:
                matched_data = temporal_matching.matching(product_data, ref_data, window=1 / 24.)
                n = matched_data.shape[0]
                if export_ts:
                    matched_data.to_csv(os.path.join(data_output_folder, matched_data_str))
                # if config.dict_product_fields[product]['scale'] != "":
                #     matched_data = scale(matched_data, method='lin_cdf_match', reference_index=1)
                #     try:
                #         matched_data = scale(matched_data, method='lin_cdf_match', reference_index=1)
                #         if export_ts:
                #             matched_data.to_csv(os.path.join(data_output_folder, scaled_data_str))
                #     except:
                #         empty_metrics_df = get_empty_metrics_df()
                #         metrics_df = pandas.concat([metrics_df, empty_metrics_df])
                #         message = "Could not scale data. Skipping to next station."
                #         warnings.warn(message)
                #         tools.write_log(log_file, message)
                #         break
                network_matched_data = matched_data_dict[network_name]
                matched_data_dict[network_name] = pandas.concat([network_matched_data, matched_data])
                tools.write_log(log_file, '{} matched data shape: {}'.format(
                    network_name, matched_data_dict[network_name].shape))
                tools.write_log(log_file, 'matched_data.shape: {}'.format(matched_data.shape))
            # insert scaling conditional here
            else:
                tools.write_log(log_file, 'insufficient data for matching: {}'.format(product))
            try:
                metric_values = tools.get_metrics(matched_data, 'product_sm', 'ref_sm', anomaly)
                station_metrics_df = pandas.DataFrame([[network_name, station_name, product_str, timeframe,
                                                        anomaly, n] + metric_values], columns=config.metrics_df_columns)
                tools.write_log(log_file, str(station_metrics_df))
                metrics_df = pandas.concat([metrics_df, station_metrics_df])
                tools.write_log(log_file, '{} x {} {} ({}) analysis complete'.format(product, network_name,
                                                                                     station_name, anomaly_str))
                tools.write_log(log_file, '')
            except:
                empty_metrics_df = get_empty_metrics_df()
                metrics_df = pandas.concat([metrics_df, empty_metrics_df])
                message = "Could not calculate metrics. Skipping to next station."
                warnings.warn(message)
                tools.write_log(log_file, message)
                # write break here?
        # network level analysis
        tools.write_log(log_file, '*** analyzing networks ({}) ***'.format(anomaly_str))
        for network, network_matched_data in matched_data_dict.items():
            station_name = "All"
            # network_matched_data.dropna
            data_output_str = 'network_{}_{}_{}_{}_matched_data.csv'.format(
                product, network_name, timeframe, anomaly_str)
            if export_ts:
                network_matched_data.to_csv(os.path.join(data_output_folder, data_output_str))
            tools.write_log(log_file, '*** analyzing {} ({}) ***'.format(network, anomaly_str))
            try:
                metric_values = tools.get_metrics(network_matched_data, 'product_sm', 'ref_sm', anomaly)
                n = network_matched_data.shape[0]
                network_metrics_df = pandas.DataFrame(
                    [[network_name, station_name, product_str, timeframe, anomaly, n] + metric_values],
                    columns=config.metrics_df_columns)
                tools.write_log(log_file, str(network_metrics_df))
                metrics_df = pandas.concat([metrics_df, network_metrics_df])
            except:
                empty_metrics_df = get_empty_metrics_df()
                metrics_df = pandas.concat([metrics_df, empty_metrics_df])
                message = "Could not calculate network metrics."
                warnings.warn(message)
                tools.write_log(log_file, message)
                # write break here?
            if evaluate_timeframes:
                if len(config.year_timeframes) > 0:
                    for year in config.year_timeframes:
                        timeframe = year
                        data_output_str = 'network_{}_{}_{}_matched_data.csv'.format(network_name, timeframe,
                                                                                     anomaly_str)
                        tools.write_log(log_file, '*** analyzing {} {} for {} ({}) ***'.format(network, timeframe,
                                                                                               product, anomaly_str))
                        tf_network_matched_data = tools.get_timeframe_data(network_matched_data, year_filter=year)
                        if export_ts:
                            tf_network_matched_data.to_csv(os.path.join(data_output_folder, data_output_str))
                        tools.write_log(log_file, '{} {} matched data shape: {}'.format(network_name, timeframe,
                                                                                        tf_network_matched_data.shape))
                        try:
                            metric_values = tools.get_metrics(tf_network_matched_data, 'product_sm', 'ref_sm', anomaly)
                            n = tf_network_matched_data.shape[0]
                            tf_network_metrics_df = pandas.DataFrame(
                                [[network_name, "All", product_str, timeframe, anomaly, n] + metric_values],
                                columns=config.metrics_df_columns)
                            tools.write_log(log_file, str(tf_network_metrics_df))
                            metrics_df = pandas.concat([metrics_df, tf_network_metrics_df])
                        except:
                            empty_metrics_df = get_empty_metrics_df()
                            metrics_df = pandas.concat([metrics_df, empty_metrics_df])
                            message = "Could not calculate timeframe metrics."
                            warnings.warn(message)
                            tools.write_log(log_file, message)
                            # write break here?
                if len(config.season_timeframes) > 0:
                    for season in config.season_timeframes:
                        timeframe = season
                        data_output_str = 'network_{}_{}_{}_matched_data.csv'.format(network_name, timeframe,
                                                                                     anomaly_str)
                        tools.write_log(log_file, '*** analyzing {} {} for {} ***'.format(network, timeframe, product))
                        tf_network_matched_data = tools.get_timeframe_data(network_matched_data,
                                                                               season_filter=season)
                        if export_ts:
                            tf_network_matched_data.to_csv(os.path.join(data_output_folder, data_output_str))
                        tools.write_log(log_file, '{} {} matched data shape: {}'.format(network_name, timeframe,
                                                                                        tf_network_matched_data.shape))
                        try:
                            metric_values = tools.get_metrics(tf_network_matched_data, 'product_sm', 'ref_sm', anomaly)
                            n = tf_network_matched_data.shape[0]
                            tf_network_metrics_df = pandas.DataFrame(
                                [[network_name, "All", product_str, timeframe, anomaly, n] + metric_values],
                                columns=config.metrics_df_columns)
                            tools.write_log(log_file, str(tf_network_metrics_df))
                            metrics_df = pandas.concat([metrics_df, tf_network_metrics_df])
                        except:
                            empty_metrics_df = get_empty_metrics_df()
                            metrics_df = pandas.concat([metrics_df, empty_metrics_df])
                            message = "Could not calculate timeframe metrics."
                            warnings.warn(message)
                            tools.write_log(log_file, message)
                            # write break here?
        tools.write_log(log_file, '*** {} ({}) ANALYSIS COMPLETE ***'.format(product, anomaly_str))
        tools.write_log(log_file, '')
        metrics_df.reset_index(drop=True, inplace=True)
    return metrics_df
