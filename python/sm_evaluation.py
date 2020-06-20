"""
Author: Nina del Rosario
Date: 5/25/2020
Script for evaluating SM datasets
"""
import os
import pandas

from pytesmo import temporal_matching
import sm_tools as tools
import sm_config as config


# function which compares reference data to evaluation data
# reference can be either ISMN, ICOS, or GLDAS
# def evaluate(products, references, startdate, enddate):
def evaluate(references, products, startdate, enddate, output_folder, filter_ref=False, filter_prod=True,
             export_ts=True, timeframe=None, anomaly=False):
    """""
    Function to compare soil moisture product to reference data
    Reference data supported: ICOS and ISMN (GLDAS forthcoming)

    Parameters
    references: list of ICOS or ISMN time series objects (adding GLDAS soon)
    products:   dictionary of product(s) to analyze, examples:
                evaluation_dict = {"ASCAT 12.5 TS": True}
                see product_parameters_dict in sm_config.py for dataset names and to set dataset parameters
    startdate:  datetime used to filter product data to be analyzed
    enddate:    datetime used to filter product data to be analyzed
    output_folder: directory where metrics and ts data will be saved
    filter_ref: boolean, in the case of ICOS data, if this is True only qc flag = 0 will be included 
    filter_prod: boolean, determines whether product data will be quality filtered, see sm_tools.py > get_product_data 
    export_ts: whether ts data (reference, product, and matched) should be exported as csv files to output_folder
    timeframe: dictionary of timeframe(s) to analyze. if none, metrics will be calculated for entire startdate-enddate. 
                if timeframe dictionary is provided, network-level metrics will be calculated for entire startdate-
                enddate and each timeframe
    """""
    log_file, metrics_file, data_output_folder = tools.create_output_dir(output_folder)
    metrics_df = pandas.DataFrame(columns=config.metrics_df_columns)
    product_list = tools.get_product_list(products)
    for product in product_list:
        product_str = product.replace(' ', '-')
        product_reader = tools.get_product_reader(product, config.dict_product_inputs[product])
        product_sm_col = config.dict_product_fields[product]['sm_field']
        for station in references:
            tools.write_log(log_file, "*** analyzing {} x {} {} ***".format(product, station.network, station.station))
            ref_data = tools.get_ref_data(station, filter_ref, anomaly)[0]
            ref_data.to_csv(os.path.join(data_output_folder, 'ref_data_{}_{}.csv'.format(station.network,
                                                                                         station.station)))
            tools.write_log(log_file, 'ref_data.shape: {}'.format(ref_data.shape))
            ref_sm_col = tools.get_ref_data(station)[1]
            ref_data.rename('ref_sm', inplace=True)
            product_data = tools.get_product_data(lon=station.longitude, lat=station.latitude, product=product,
                                                  reader=product_reader, filter_prod=filter_prod, anomaly=anomaly,
                                                  station=station)
            product_data.to_csv(os.path.join(data_output_folder, '{}_data_{}_{}.csv'.format(product_str,
                                                                                            station.network,
                                                                                            station.station)))
            product_data.rename('product_sm', inplace=True)
            tools.write_log(log_file, 'product_data.shape: {}'.format(product_data.shape))
            product_data = product_data.loc[startdate:enddate]
            tools.write_log(log_file, 'product_data.shape (with date filter): {}'.format(product_data.shape))
            matched_data = temporal_matching.matching(product_data, ref_data, window=1 / 24.)
            matched_data.to_csv(os.path.join(data_output_folder, 'matched_data_{}_{}_{}.csv'.format(product_str,
                                                                                                    station.network,
                                                                                                    station.station)))
            tools.write_log(log_file, 'matched_data.shape: {}'.format(matched_data.shape))
            # insert scaling conditional here
            metric_values = tools.get_metrics(matched_data, 'product_sm', 'ref_sm', anomaly)
            n = matched_data.shape[0]
            station_metrics_df = pandas.DataFrame([[station.network, station.station, filter_ref, product_str,
                                                    filter_prod, timeframe, anomaly, n] + metric_values],
                                                  columns=config.metrics_df_columns)
            tools.write_log(log_file, str(station_metrics_df))
            metrics_df = pandas.concat([metrics_df, station_metrics_df])
            metrics_df.reset_index(drop=True, inplace=True)
            tools.write_log(log_file, '{} x {} {} analysis complete'.format(product, station.network, station.station))
            tools.write_log(log_file, '')
    metrics_df.to_csv(metrics_file, sep=',')
    return metrics_df
