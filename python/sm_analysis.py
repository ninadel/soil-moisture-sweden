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
def evaluate(products, references, output_folder, startdate, enddate, export_ts=True, timeframes=None):
    metrics_df_columns = ['network', 'station', 'temp_scope', 'ismn_data_scope', 'product',
                          'product_data_scope', 'n', 'bias', 'rmsd', 'ubrmsd', 'pearsonr', 'pearsonr_p']
    metrics_df = pandas.DataFrame()
    product_list = tools.get_product_list(products)
    ref_data_scope = None
    product_data_scope = None
    temp_scope = None
    for product in product_list:
        product_str = product.replace(' ', '-')
        for ref_loc in references:
            print(ref_loc.station)
            # future func: get ssm data
            if str(type(ref_loc)) == "<class 'icos.ICOSTimeSeries'>":
                ref_data = ref_loc.data['icos_ssm']
                # add ICOS filtering?
            elif str(type(ref_loc)) == "<class 'ismn.readers.ISMNTimeSeries'>":
                ref_data = ref_loc.data.dropna()
                # ref_data.rename(columns={'soil moisture': 'ref_ssm'}, inplace=True)
            elif str(type(ref_loc)) == "<class 'ismn.interface.ISMN_station'>":
                # add GLDAS coordinate handling
                pass
            product_metadata = config.datasets_dict[product]
            product_reader = tools.get_product_reader(product, product_metadata)
            # insert scaling conditional here
            product_data = tools.get_product_data(lon=ref_loc.longitude, lat=ref_loc.latitude,
                                                  product=product, product_metadata=product_metadata,
                                                  product_reader=product_reader, filter_product=True)
            product_data = product_data.loc[startdate:enddate]
            matched_data = temporal_matching.matching(product_data, ref_data, window=1/24.)
            matched_rows = matched_data.shape[0]
            metrics = tools.get_metrics(matched_data, product_metadata['sm_field'], 'soil moisture')
            n = matched_data.shape[0]
            station_metrics_df = pandas.DataFrame([[ref_loc.network, ref_loc.station, temp_scope, ref_data_scope, product_str,
                                                    product_data_scope, n] + metrics], columns=metrics_df_columns)
            print(station_metrics_df)
            metrics_df = pandas.concat([metrics_df, station_metrics_df])
    return metrics_df


    # ICOS: see existing dictionary
    # ISMN: one network at a time
    # GLDAS: one big network, prefix existing networks e.g. ICOS_Degero


# Dictionary to set analyses to perform
analyses_dict = {
    "ASCAT 12.5 TS": {
        "analyze": True
    },
    "GLDAS": {
        "analyze": False
    },
    "SMAP L3": {
        "analyze": False
    },
    "SMAP L4": {
        "analyze": False
    }
}

timestamp = tools.get_timestamp()
output_folder = "{}_analysis".format(timestamp)
icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
reference_list = ismn_readers + icos_readers

# help(ismn_readers[0])
evaluation_results = evaluate(analyses_dict, ismn_readers, output_folder, startdate=datetime(2015, 4, 1),
                              enddate=datetime(2018, 12, 31, 23, 59))

evaluation_results.to_csv('metrics_{}'.format(timestamp))
print(evaluation_results)
