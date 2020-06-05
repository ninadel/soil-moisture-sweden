"""
Author: Nina del Rosario
Date: 5/25/2020
Functions for analyzing soil moisture datasets
"""
from datetime import datetime
import json
import os
import pandas

from ascat import H115Ts
from gldas.interface import GLDASTs
from icos import ICOSTimeSeries
from ismn.interface import ISMN_Interface
from smap_io import SMAPTs
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


def get_icos_files(input_dir):
    data_dict = {}
    for filename in os.listdir(input_dir):
        filename_parts = filename.split(".")
        station = filename_parts[0]
        data_dict[station] = os.path.join(input_dir, filename)
    return data_dict


def get_icos_readers(input_dir):
    with open('icos_dict.json', 'r') as f:
        icos_dict = json.load(f)
    readers = []
    for filename in os.listdir(input_dir):
        filename_parts = filename.split(".")
        station = filename_parts[0]
        metadata = icos_dict[station]
        data = pandas.read_csv(os.path.join(input_dir, filename))
        reader = ICOSTimeSeries(metadata, data)
        readers.append(reader)
    return readers


def get_ismn_readers(input_dir):
    ismn_readers = []
    interface = ISMN_Interface(input_dir)
    for network in interface.list_networks():
        for stationname in interface.list_stations(network=network):
            station = interface.get_station(stationname, network=network)
            if 'soil moisture' in station.variables:
                ismn_readers.append(station)
    return ismn_readers


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
    if product == "SMAP L3":
        ts_dir = product_metadata["ts_dir"]
        reader = SMAPTs(ts_path=ts_dir)
    if product == "SMAP L4":
        ts_dir = product_metadata["ts_dir"]
        reader = SMAPTs(ts_path=ts_dir)
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
    if product == 'SMAP L3':
        data = ts
        if filter_product:
            print("For now, no filters for SMAP L3")
    if product == 'SMAP L4':
        data = ts
        if filter_product:
            print("For now, no filters for SMAP L4")
    if variable == 'sm':
        data = data[product_metadata['sm_field']]
    return data


def get_product_list(products):
    product_list = []
    if str(type(products)) == "<class 'dict'>":
        for product, value in products.items():
            if value["analyze"]:
                product_list.append(product)
    elif str(type(products)) == "<class 'list'>":
        product_list = products
    elif str(type(products)) == "<class 'str'>":
        product_list = [products]
    return product_list


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
