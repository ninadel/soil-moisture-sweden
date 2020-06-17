"""
Author: Nina del Rosario
Date: 5/25/2020
Functions for analyzing soil moisture datasets
"""
from datetime import datetime
import ismn
import json
import numpy
import os
import pandas

from ascat import H115Ts
from esa_cci_sm.interface import CCITs
from gldas.interface import GLDASTs
import icos
from icos import ICOSTimeSeries
from ismn.interface import ISMN_Interface
import netCDF4
from smap_io import SMAPTs
from smos.smos_ic.interface import SMOSTs
from pytesmo.validation_framework.adapters import SelfMaskingAdapter
from pytesmo import metrics
from pytesmo.time_series.anomaly import calc_anomaly
import sm_config as config


def write_log(filename, string, print_string=True, write_output=True):
    if write_output:
        with open(filename, "a") as logfile:
            logfile.write(string + "\n")
    if print_string:
        print(string)


def create_output_dir(output_folder):
    analysis_results_folder = os.path.join(output_folder, "{}_analysis".format(datetime.now().
                                                                               strftime("%Y%m%d_%H%M%S")))
    os.makedirs(analysis_results_folder)
    data_output_folder = os.path.join(analysis_results_folder, "data_output")
    os.mkdir(data_output_folder)
    log_file = os.path.join(analysis_results_folder, "analysis_log.txt")
    metrics_file = os.path.join(analysis_results_folder, "analysis_metrics.csv")
    return log_file, metrics_file, data_output_folder
    # MOVE to config later


def get_icos_files(input_dir):
    data_dict = {}
    for filename in os.listdir(input_dir):
        filename_parts = filename.split(".")
        station = filename_parts[0]
        data_dict[station] = os.path.join(input_dir, filename)
    return data_dict


def get_icos_readers(input_dir):
    with open("dict_icos.json", "r") as f:
        dict_icos = json.load(f)
    readers = []
    for filename in os.listdir(input_dir):
        filename_parts = filename.split(".")
        station = filename_parts[0]
        metadata = dict_icos[station]
        data = pandas.read_csv(os.path.join(input_dir, filename), index_col=0)
        reader = ICOSTimeSeries(metadata, data)
        readers.append(reader)
    return readers


def get_ismn_readers(input_dir):
    ismn_readers = []
    interface = ISMN_Interface(input_dir)
    for station_object in interface.stations_that_measure("soil moisture"):
        for ISMN_time_series in station_object.data_for_variable("soil moisture", min_depth=0, max_depth=0.1):
            ismn_readers.append(ISMN_time_series)
    return ismn_readers


def get_product_list(products):
    product_list = []
    if type(products) == dict:
        for product, analyze in products.items():
            if analyze:
                product_list.append(product)
    elif type(products) == list:
        product_list = products
    elif type(products) == str:
        product_list = [products]
    return product_list


def get_product_reader(product, product_metadata):
    if product == "ASCAT 12.5 TS":
        ts_dir = product_metadata["ts_dir"]
        grid_dir = product_metadata["grid_dir"]
        grid_file = product_metadata["grid_file"]
        static_layers_dir = product_metadata["static_layers_dir"]
        reader = H115Ts(cdr_path=ts_dir, grid_path=grid_dir, grid_filename=grid_file,
                        static_layer_path=static_layers_dir)
    if product == "CCI Active":
        ts_dir = product_metadata["ts_dir"]
        reader = CCITs(ts_path=ts_dir)
    if product == "CCI Passive":
        ts_dir = product_metadata["ts_dir"]
        reader = CCITs(ts_path=ts_dir)
    if product == "CCI Combined":
        ts_dir = product_metadata["ts_dir"]
        reader = CCITs(ts_path=ts_dir)
    if product == "GLDAS":
        ts_dir = product_metadata["ts_dir"]
        reader = GLDASTs(ts_path=ts_dir)
    if product == "Sentinel":
        reader = None
    if product == "SMAP L3":
        ts_dir = product_metadata["ts_dir"]
        reader = SMAPTs(ts_path=ts_dir)
    if product == "SMAP L4":
        ts_dir = product_metadata["ts_dir"]
        reader = SMAPTs(ts_path=ts_dir)
    if product == "SMOS-BEC":
        reader = None
    if product == "SMOS-IC":
        ts_dir = product_metadata["ts_dir"]
        reader = SMOSTs(ts_path=ts_dir)
    return reader


def get_ref_data(ts, filter_ref=False, anomaly=False):
    if type(ts) == icos.ICOSTimeSeries:
        ref_data = ts.data
        if filter_ref:
            ref_data = ref_data.loc[ref_data["qc_ssm"] == 0]
        sm_field = "soil moisture"
        sm_data = ref_data[sm_field]
        sm_data.dropna()
        # return sm_data, sm_field
    elif type(ts) == ismn.readers.ISMNTimeSeries:
        ref_data = ts.data
        sm_field = "soil moisture"
        sm_data = ref_data[sm_field]
        sm_data.dropna()
        # return sm_data, sm_field
    sm_data = ref_data[sm_field]
    if anomaly:
        sm_data = calc_anomaly(sm_data)
    return sm_data, sm_field


def get_product_data(lon, lat, product, reader, filter_prod=True, anomaly=False):
    ts = reader.read(lon, lat)
    if product == "ASCAT 12.5 TS":
        data = ts.data
        if filter_prod:
            data = data.loc[data["ssf"] == 1]
        # Timestampp OK
    if product == "CCI Active":
        data = ts
        # For now, no filters for CCI
    if product == "CCI Passive":
        data = ts
        # For now, no filters for CCI
    if product == "CCI Combined":
        data = ts
        # For now, no filters for CCI
    if product == "GLDAS":
        data = ts
        # No filters for GLDAS
        # Timestampp OK
    if product == "SMAP L3":
        data = ts
        # For now, no filters for SMAP L3
        # Force Timestamp: 6AM CET, 5AM UTC
    if product == "SMAP L4":
        data = ts
        # For now, no filters for SMAP L4
        # Timestampp OK
    if product == "SMOS-BEC":
        pass
    if product == "SMOS-IC":
        data = ts
        # For now, no filters for SMOS-IC
        # See "Quality_Flag" field
        # Timestampp OK
    sm = data[config.dict_product_fields[product]["sm_field"]]
    if anomaly:
        sm = calc_anomaly(sm)
    return sm


# get data for all network/stations in a dictionary
def get_metrics(data, xcol, ycol, anomaly=False):
    """""
    data: temporally matched dataset
    metrics: list of metrics to calculate on matched dataset
        default: "pearsonr", "bias", "rmsd", "ubrmsd"
    """""
    if data.shape[0] == 0:
        bias = None
        rmsd = None
        ubrmsd = None
        pearsonr = None
        pearsonr_p = None
    else:
        x, y = data[xcol].values, data[ycol].values
        pearsonr = metrics.pearsonr(x, y)[0]
        pearsonr_p = metrics.pearsonr(x, y)[1]
        if not anomaly:
            bias = metrics.bias(x, y)
            rmsd = metrics.rmsd(x, y)
            ubrmsd = metrics.ubrmsd(x, y)
        else:
            bias = None
            rmsd = None
            ubrmsd = None
    return [bias, rmsd, ubrmsd, pearsonr, pearsonr_p]


def convert_tab_comma(filename):
    file_df = pandas.read_csv(filename, sep="\t")
    output_file = filename[:-4]+"_commareformat"+filename[-4:]
    file_df.to_csv(output_file, sep=",")


# given an NC file and coordinate fields, return lower left coordinate and upper right coordinate
def get_geo_extent(nc_file, lon_field="lon", lat_field="lat"):
    nc = netCDF4.Dataset(nc_file, "r")
    try:
        lon_array = nc[lon_field][:]
        lat_array = nc[lat_field][:]
        ll = (numpy.amin(lat_array), numpy.amin(lon_array))
        ur = (numpy.amax(lat_array), numpy.amax(lon_array))
        return ll, ur
    except:
        print("cant\' read file")


# for a value, find the nearest value and its index
def find_nearest(array, value):
    array = numpy.asarray(array)
    idx = (numpy.abs(array - value)).argmin()
    return idx, array[idx]


def get_series(input_root, lon_loc, lat_loc, parameters, lon_field="lon", lat_field="lat", datetime_len=8,
               datetime_startstr="201", cutoff=None):
    if type(parameters) != list:
        parameters = [parameters]
    series = pandas.DataFrame()
    files = os.listdir(input_root)
    count = 0
    for file in files:
        date_str_idx = file.find(datetime_startstr)
        date_str = file[date_str_idx:date_str_idx + 8]
        file_path = os.path.join(input_root, file)
        nc = netCDF4.Dataset(file_path, "r")
        lon_array = nc[lon_field][:]
        lat_array = nc[lat_field][:]
        nearest_lon_idx = find_nearest(lon_array, lon_loc)[0]
        nearest_lat_idx = find_nearest(lat_array, lat_loc)[0]
        values = [date_str]
        columns = ["date_str"]
        for parameter in parameters:
            columns.append(parameter)
            value = nc[parameter][:][0, nearest_lat_idx, nearest_lon_idx]
            values.append(value)
        file_df = pandas.DataFrame([values], columns=columns)
        series = pandas.concat([series, file_df])
        count += 1
        if cutoff is not None:
            if count == cutoff:
                break
    series.set_index("date_str", inplace=True)
    return series


def get_netcdf_summary(file, lon_field=None, lat_field=None, sm_field=None, time_field=None, show_field_data=True):
    dataset = netCDF4.Dataset(file, 'r')
    print("Attributes in dataset:")
    print(dataset.ncattrs())
    print("\nDimensions in dataset:")
    for dimension in dataset.dimensions.items():
        print(dimension)
    print("\nVariables in dataset:")
    for variable in dataset.variables.items():
        print(variable)
    if lon_field is not None:
        print("\nLongitude field:")
        print("shape:", dataset[lon_field][:].shape)
        if show_field_data:
            print(dataset[lon_field][:])
    if lat_field is not None:
        print("\nLatitude field:")
        print("shape:", dataset[lat_field][:].shape)
        if show_field_data:
            print(dataset[lat_field][:])
    if sm_field is not None:
        print("\nSM field:")
        print("shape:", dataset[sm_field][:].shape)
        if show_field_data:
            print(dataset[sm_field][:])
    if time_field is not None:
        print("\nTime field:")
        print("shape:", dataset[time_field][:].shape)
        if show_field_data:
            print(dataset[time_field][:])


# given a product with a suffle reader and a dictionary of locations, write TS to csv files
def write_grid_shuffle_ts(product, output_dir, locations, filter_prod=True, anomaly=False):
    product_str = product.replace(' ', '-')
    reader = get_product_reader(product, config.dict_product_inputs[product])
    if filter_prod:
        filter_str = "filtered"
    else:
        filter_str = "unfiltered"
    if anomaly:
        anomaly_str = "anomaly"
    else:
        anomaly_str = "absolute"
    location_count = len(locations)
    index_count = 0
    for location, coordinate in locations.items():
        lat = coordinate['lat']
        lat_str = str(lat).replace('.', '-')
        lon = coordinate['lon']
        lon_str = str(lon).replace('.', '-')
        output_filename = "{}_{}_{}_{}_{}_{}.csv".format(product_str, location, lat_str, lon_str, filter_str,
                                                         anomaly_str)
        data = get_product_data(lon=lon, lat=lat, product=product, reader=reader, filter_prod=filter_prod,
                                anomaly=anomaly)
        print("data.shape:", data.shape)
        output_file = os.path.join(output_dir, output_filename)
        data.to_csv(output_file, sep=',', encoding='latin-1')
        del data
        index_count += 1
        print("{} of {} locations processed".format(index_count, location_count))
    else:
        index_count += 1
