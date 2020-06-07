"""
Author: Nina del Rosario
Date: 5/25/2020
Script for analyzing SM datasets
For icos analysis see sm_analysis_icos.py
"""
from datetime import datetime
import numpy
import os
import pandas

from ascat import H115Ts
import ismn.interface as ismn
from pytesmo import temporal_matching, scaling, df_metrics, metrics
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
                analyses_dict = {"ASCAT 12.5 TS": True}
                see dataset_dict in sm_config.py for dataset names and to set dataset parameters
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
    metrics_df = pandas.DataFrame()
    product_list = tools.get_product_list(products)
    for product in product_list:
        product_str = product.replace(' ', '-')
        product_reader = tools.get_product_reader(product, config.datasets_dict[product])
        product_sm_col = config.datasets_dict[product]['sm_field']
        for ref_loc in references:
            tools.write_log(config.logfile, "analyzing {} x {}".format(product, ref_loc.station))
            ref_data = tools.get_ref_data(ref_loc)[0]
            print(ref_data.size)
            ref_sm_col = tools.get_ref_data(ref_loc)[1]
            product_data = tools.get_product_data(lon=ref_loc.longitude, lat=ref_loc.latitude, product=product,
                                                  reader=product_reader, filter_prod=filter_prod)
            print(product_data.size)
            product_data = product_data.loc[startdate:enddate]
            matched_data = temporal_matching.matching(product_data, ref_data, window=1/24.)
            print('matched_data.size', matched_data.size)
            print(matched_data)
            # insert scaling conditional here
            metric_values = tools.get_metrics(matched_data, product_sm_col, ref_sm_col, anomaly)
            n = matched_data.shape[0]
            station_metrics_df = pandas.DataFrame([[ref_loc.network, ref_loc.station, filter_ref, product_str,
                                                    filter_prod, timeframe, anomaly, n] + metric_values],
                                                  columns=metrics_df_columns)
            tools.write_log(config.logfile, str(station_metrics_df))
            metrics_df = pandas.concat([metrics_df, station_metrics_df])
    metrics_df.to_csv(os.path.join(output_folder))
    return metrics_df


    # ICOS: see existing dictionary
    # ISMN: one network at a time
    # GLDAS: one big network, prefix existing networks e.g. ICOS_Degero


# Dictionary to set analyses to perform
analyses_dict = {
    "ASCAT 12.5 TS": True,
    "GLDAS": False,
    "SMAP L3": False,
    "SMAP L4": False
}

analysis_output_folder = config.analysis_output_dir
icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
reference_list = icos_readers + ismn_readers

# help(ismn_readers[0])
# def evaluate(references, products, startdate, enddate, output_folder, filter_ref=False, filter_prod=True,
#              export_ts=True, timeframe=None, anomaly=False):

evaluation_results = evaluate(reference_list, analyses_dict, startdate=datetime(2015, 4, 1),
                              enddate=datetime(2018, 12, 31, 23, 59), output_folder=analysis_output_folder)

# evaluation_results.to_csv('metrics_{}'.format(config.timestamp))
print(evaluation_results)
