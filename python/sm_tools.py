"""
Author: Nina del Rosario
Date: 5/25/2020
Functions for analyzing soil moisture datasets
"""
from datetime import datetime
import os
import pandas
from ascat import H115Ts
from gldas.interface import GLDASTs
from pytesmo.validation_framework.adapters import SelfMaskingAdapter
from pytesmo import metrics


def get_timestamp():
    # Converting datetime object to string
    timestamp = datetime.now()
    timestamp_str = timestamp.strftime("%Y%m%d_%H%M%S")
    return timestamp_str


def write_log(filename, string, print_string=True):
    with open(filename, 'a') as logfile:
        logfile.write(string + '\n')
    if print_string:
        print(string)


def get_icos_stations(input_dir):
    data_dict = {}
    for filename in os.listdir(input_dir):
        filename_parts = filename.split(".")
        station = filename_parts[0]
        data_dict[station] = os.path.join(input_dir, filename)
    return data_dict


def get_product_reader(product, product_metadata):
    if product == "ASCAT 12.5 TS":
        ts_dir = product_metadata["ts_dir"]
        grid_dir = product_metadata["grid_dir"]
        grid_file = product_metadata["grid_file"]
        static_layers_dir = product_metadata["static_layers_dir"]
        reader = H115Ts(cdr_path=ts_dir, grid_path=grid_dir, grid_filename=grid_file,
                        static_layer_path=static_layers_dir)
    if product == "GLDAS":
        ts_dir = product_metadata["ts_dir"]
        reader = GLDASTs(ts_path=ts_dir)
    if product == "SMAP L4":
        pass
    return reader


def get_product_data(lon, lat, product, product_metadata, product_reader, filter_product=True, variable='sm'):
    ts = product_reader.read(lon, lat)
    if product == 'ASCAT 12.5 TS':
        data = ts.data
        if filter_product:
            data = data.loc[data['ssf'] == 1]
    if product == 'GLDAS':
        data = ts
        if filter_product:
            print("No filters for GLDAS")
    if variable == 'sm':
        data = data[product_metadata['sm_field']]
    return data


# get data for all network/stations in a dictionary
def get_metrics(data, xcol, ycol):
    """""
    data: temporally matched dataset
    metrics: list of metrics to calculate on matched dataset
        default: 'pearsonr', 'bias', 'rmsd', 'ubrmsd'
    """""
    x, y = data[xcol].values, data[ycol].values
    bias = metrics.bias(x, y)
    rmsd = metrics.rmsd(x, y)
    ubrmsd = metrics.ubrmsd(x, y)
    pearsonr = metrics.pearsonr(x, y)[0]
    pearsonr_p = metrics.pearsonr(x, y)[1]
    return [bias, rmsd, ubrmsd, pearsonr, pearsonr_p]


def convert_tab_comma(filename):
    file_df = pandas.read_csv(filename, sep="\t")
    output_file = filename[:-4]+'_commareformat'+filename[-4:]
    file_df.to_csv(output_file, sep=",")
