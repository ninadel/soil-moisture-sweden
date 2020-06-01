"""
Author: Nina del Rosario
Date: 5/25/2020
Functions for analyzing soil moisture datasets
"""
from datetime import datetime
import os
import pandas
from ascat import H115Ts
from pytesmo.validation_framework.adapters import SelfMaskingAdapter

def get_timestamp():
    # Converting datetime object to string
    timestamp = datetime.now()
    timestamp_str = timestamp.strftime("%Y%m%d_%H%M")
    return timestamp_str


def get_icos_stations(dir):
    data_dict = {}
    for filename in os.listdir(dir):
        filename_parts = filename.split(".")
        station = filename_parts[0]
        data_dict[station] = os.path.join(dir, filename)
    return data_dict


# takes a 2 column ICOS time series and filters based on column 2
def filter_icos_data(data, qc_values, dropna=True):
    qc_column = data.columns[1]
    if type(qc_values) != list:
        qc_values = [qc_values]
    data = data.loc[data[qc_column].isin(qc_values)]
    if dropna:
        data = data.dropna()
    return data


def get_product_reader(product, product_inputs, filter_data=True):
    if product == "ASCAT 12.5 TS":
        ts_data_dir = product_inputs["ts_data_dir"]
        grid_dir = product_inputs["ts_data_dir"]
        grid_file = product_inputs["grid_file"]
        static_layers_dir = product_inputs["static_layers_dir"]
        reader = H115Ts(cdr_path=ts_data_dir, grid_path=grid_dir, grid_filename=grid_file,
                    static_layer_path=static_layers_dir)
        if filter_data:
            print(product, "filter: ")
            # filter data
            # ssf flag_values = 0, 1, 2, 3, 4
            # ssf flag_meanings = "unknown unfrozen frozen_temporary melting_water_on_the_surface permanent_ice";
            print(product, "(filtered)", data.shape)
        return reader
    if product == "GLDAS":
        pass
    if product == "SMAP L4":
        pass
    pass


# get data for all network/stations in a dictionary
def get_metrics(data, metrics=('bias', 'rmsd', 'ubrmsd', 'pearsonr', 'pearsonr_p')):
    """""
    data: temporally matched dataset
    metrics: list of metrics to calculate on matched dataset
        default: 'pearsonr', 'bias', 'rmsd', 'ubrmsd'
    """""
    if type(metrics) != list:
        metrics = [metrics]
    # bias, rmsd, ubrmsd, pearsonr, pearsonr p-value
    metric_values = [None, None, None, None, None]
    if data.shape[0] > 4:
        for metric in metrics:
            pass
    return metric_values