"""
Author: Nina del Rosario
Date: 5/25/2020
Functions for analyzing soil moisture datasets
"""
import datetime
import os
import pandas

def get_timestamp():
    # Converting datetime object to string
    timestamp = datetime.now()
    timestampStr = timestamp.strftime("%y%m%d_%H%M")
    return timestampStr


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


def get_product_data(lon, lat, product_inputs):
    # if product has a .data suffix
    # if product doesn't have a .data suffix
    pass


# get data for all network/stations in a dictionary
def get_metrics(data, metrics=('bias', 'rmsd', 'ubrmsd', 'pearsonr')):
    """""
    data: temporally matched dataset
    metrics: list of metrics to calculate on matched dataset
        default: 'pearsonr', 'bias', 'rmsd', 'ubrmsd'
    """""
    print('getting metrics', metrics)
    if type(metrics) != list:
        metrics = [metrics]
    # bias, rmsd, ubrmsd, pearsonr, pearsonr p-value
    metric_values = []
    for metric in metrics:
        pass
    return metric_values