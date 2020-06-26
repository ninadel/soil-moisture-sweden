"""
Author: Nina del Rosario
Date: 5/25/2020
Functions for analyzing soil moisture datasets
"""
import sm_config as config

from datetime import datetime
import h5py
import icos
import ismn
import json
import netCDF4
import numpy
import os
import pandas
import re
import warnings

from ascat import H115Ts
from esa_cci_sm.interface import CCITs
from gldas.interface import GLDASTs
from icos import ICOSTimeSeries
from ismn.interface import ISMN_Interface
from smap_io import SMAPTs
from smos.smos_ic.interface import SMOSTs
from pytesmo.validation_framework.adapters import SelfMaskingAdapter
from pytesmo import metrics
from pytesmo.time_series.anomaly import calc_anomaly
from sentinel import SentinelImg
from smos_extension import SMOSBECImg

def write_log(filename, string, print_string=True, write_output=True):
    if write_output:
        with open(filename, "a") as logfile:
            logfile.write(string + "\n")
    if print_string:
        print(string)


def create_output_dir(output_folder):
    data_output_folder = os.path.join(output_folder, "data_output")
    os.mkdir(data_output_folder)
    log_file = os.path.join(output_folder, "analysis_log.txt")
    metrics_file = os.path.join(output_folder, "analysis_metrics.csv")
    return log_file, metrics_file, data_output_folder


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
    ismn_stations = []
    interface = ISMN_Interface(input_dir)
    for station_object in interface.stations_that_measure("soil moisture"):
        for ISMN_time_series in station_object.data_for_variable("soil moisture", min_depth=0, max_depth=0.1):
            # appends only the first TS of the station in the case where there are multiple sensors per station
            if ISMN_time_series.station not in ismn_stations:
                ismn_readers.append(ISMN_time_series)
                ismn_stations.append(ISMN_time_series.station)
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
    elif product == "CCI Active":
        ts_dir = product_metadata["ts_dir"]
        reader = CCITs(ts_path=ts_dir)
    elif product == "CCI Passive":
        ts_dir = product_metadata["ts_dir"]
        reader = CCITs(ts_path=ts_dir)
    elif product == "CCI Combined":
        ts_dir = product_metadata["ts_dir"]
        reader = CCITs(ts_path=ts_dir)
    elif product == "GLDAS":
        ts_dir = product_metadata["ts_dir"]
        reader = GLDASTs(ts_path=ts_dir)
    elif product == "SMAP L3":
        ts_dir = product_metadata["ts_dir"]
        reader = SMAPTs(ts_path=ts_dir)
    elif product == "SMAP L4":
        ts_dir = product_metadata["ts_dir"]
        reader = SMAPTs(ts_path=ts_dir)
    elif product == "SMOS-IC":
        ts_dir = product_metadata["ts_dir"]
        reader = SMOSTs(ts_path=ts_dir)
    else:
        reader = None
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
    return sm_data


def get_product_data(lon, lat, product, reader, anomaly=False, station=None):
    sm = None
    if reader is not None:
        ts = reader.read(lon, lat)
        if product == "ASCAT 12.5 TS":
            data = ts.data
            data = data.loc[data["ssf"] == 1]
            sm = data[config.dict_product_fields[product]["sm_field"]]
            sm = sm[(sm >= 0) & (sm < 100)]
        elif product == "CCI Active":
            data = ts
            # For now, no filters for CCI
            sm = data[config.dict_product_fields[product]["sm_field"]]
            sm = sm[(sm >= 0) & (sm < 100)]
        elif product == "CCI Passive":
            data = ts
            # For now, no filters for CCI
            sm = data[config.dict_product_fields[product]["sm_field"]]
            sm = sm[(sm >= 0) & (sm < 1)]
        elif product == "CCI Combined":
            data = ts
            # For now, no filters for CCI
            sm = data[config.dict_product_fields[product]["sm_field"]]
            sm = sm[(sm >= 0) & (sm < 1)]
        elif product == "GLDAS":
            data = ts
            # No filters needed for GLDAS
            sm = data[config.dict_product_fields[product]["sm_field"]]
            sm = sm[(sm >= 0) & (sm < 100)]
        elif product == "SMAP L3":
            data = ts
            # For now, no filters for SMAP L3
            sm = data[config.dict_product_fields[product]["sm_field"]]
            sm = sm[(sm >= 0) & (sm < 1)]
        elif product == "SMAP L4":
            data = ts
            # No filters needed for SMAP L4
            sm = data[config.dict_product_fields[product]["sm_field"]]
            sm = sm[(sm >= 0) & (sm < 1)]
        # if product == "SMOS-BEC":
        #     pass
        elif product == "SMOS-IC":
            # Force Timestamp: 6AM CET, 5AM UTC
            # data = ts.shift(5, freq='H')
            data = ts
            # Quality_Flag field is already filtered to 0, 1 by reader
            # For now, no filters for SMOS-IC
            # See "Quality_Flag" field
            sm = data[config.dict_product_fields[product]["sm_field"]]
            sm = sm[(sm >= 0) & (sm < 1)]
    else:
        sm = get_csv_series(product, station)
    if anomaly:
        sm = calc_anomaly(sm)
    return sm


def get_metrics(data, xcol=None, ycol=None, anomaly=False):
    """""
    Calculate metrics for a pair of TS
    data: temporally matched dataset
    metrics: list of metrics to calculate on matched dataset
        default: "pearsonr", "bias", "rmsd", "ubrmsd"
    """""
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
    """""
    Converts tab delimited to comma separated
    filename: tab delimited file
    """""
    file_df = pandas.read_csv(filename, sep="\t")
    output_file = filename[:-4]+"_commareformat"+filename[-4:]
    file_df.to_csv(output_file, sep=",")


# given an NC file and coordinate fields, return lower left coordinate and upper right coordinate
def get_geo_extent(nc_file, lon_field="lon", lat_field="lat"):
    """""
    Finds the minimum and maxiumum lat/lon of a netcdf file
    Returns tuple of lower-left and upper-right coordinates
    nc_file: netcdf filename
    lon_field: name of longitude field (default 'lon')
    lat_field: name of latitude field (default 'lat')
    """""
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
    """""
    For an array and value, finds the nearest member of array
    Returns tuple of array index
    """""
    array = numpy.asarray(array)
    idx = (numpy.abs(array - value)).argmin()
    return idx, array[idx]


def get_nc_series(input_root, location, parameters, date_search_str, datetime_format, time_dim=True, lon_field="lon",
                  lat_field="lat"):
    """""
    Parameters
    input_root: directory of nc files
    location: tuple or dictionary of locations. 
        if tuple of a single location, [format (lat, lon)], a single ts dataframe will be returned. 
        if a dict, a dict of ts dataframes will be returned
            dictionary should be a set of locations. e.g.
                {"City 1": {
                    "longitude": 15,
                    "latitude": 15
                    },
                "City 2": {
                    "longitude": 25,
                    "latitude": 10
                    }
                }
    parameters: parameters to return
    date_search_str: regex expression for finding timestamp e.g. r"[0-9]{8}T[0-9]{4}", must be unique enough to occur 
        only once in filename
    datetime_format: tuple of tuples. for the above date_search_str, the locations of datetime elements in the string
        (year, month, day) or (year, month, day, hour, minute) 
        example: in the above string, datetime_format would be ((0,4), (4, 6), (6, 8), (9, 11), (11, 13))
        the length of the tuple will determine whether hours/minutes will be added to timestamp, otherwise it will
        default to midnight
    time_dim: boolean, whether the data is organized with 3 dimensions (time, lat, lon) (default: True)
    lon_field: the name of the longitude field in the dataset (default: 'lon')
    lat_field: the name of the latitude field in the dataset (default: 'lat')
    """""
    warnings.filterwarnings("ignore")
    # function to get ts row for a single location
    def get_loc_df(ln_array, lt_array, ln, lt):
        nr_lon_idx = find_nearest(ln_array, ln)[0]
        nr_lat_idx = find_nearest(lt_array, lt)[0]
        vs = [timestamp]
        for p in parameters:
            if time_dim:
                v = ds[p][:][:, nr_lat_idx, nr_lon_idx]
            else:
                v = ds[p][nr_lat_idx, nr_lon_idx]
            v = numpy.asscalar(numpy.asarray(v))
            vs.append(v)
        l_df = pandas.DataFrame([vs], columns=columns)
        return l_df
    # turn parameters into a column list
    if type(parameters) != list:
        parameters = [parameters]
    columns = ["timestamp"]
    for parameter in parameters:
        columns.append(parameter)
    # check location type and create output shells
    loc_ts_dict = {}
    if type(location) == dict:
        loc_meta_dict = location
    elif type(location) == tuple:
        loc_meta_dict = {}
        loc_meta_dict["loc"] = {"longitude": location[1], "latitude": location[0]}
    else:
        print("invalid location. should be a tuple or dictionary.")
        return None
    # start processing files
    files = os.listdir(input_root)
    for filename in files:
        file = os.path.join(input_root, filename)
        ds = netCDF4.Dataset(file, mode="r")
        timestamp = get_filename_timestamp(filename=filename, date_search_str=date_search_str,
                                           datetime_format=datetime_format)
        lon_array = ds[lon_field][:]
        lat_array = ds[lat_field][:]
        # for each file, process all locations and store results in dictionary
        for loc, metadata in loc_meta_dict.items():
            loc_ts_dict[loc] = pandas.DataFrame(columns=columns)
            lon_loc = metadata['longitude']
            lat_loc = metadata['latitude']
            if check_extent(lon_loc, lat_loc, file):
                loc_row = get_loc_df(lon_array, lat_array, lon_loc, lat_loc)
                loc_ts_dict[loc] = pandas.concat([loc_ts_dict[loc], loc_row])
    for loc, ts in loc_ts_dict.items():
        ts.set_index("timestamp", inplace=True)
    if len(loc_ts_dict.keys) == 1:
        return ts
    else:
        return loc_ts_dict


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
        lat = coordinate['latitude']
        lat_str = str(lat).replace('.', '-')
        lon = coordinate['longitude']
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


# for text-driven datasets, generate filename
def get_station_ts_filename(station_object=None, station_name=None, network_name=None):
    if station_object is not None:
        network = station_object.network
        station = station_object.station
        #     product_str = product.replace(' ', '-')
        filename = "{}_{}.csv".format(network, station.replace(".", "-"))
    elif station_name is not None and network_name is not None:
        filename = "{}_{}.csv".format(network_name, station_name.replace(".", "-"))
    return filename


# for text-driven datasets, retrieve time series
def get_csv_series(product, station):
    ts_dir = config.dict_product_inputs[product]["ts_dir"]
    filename = get_station_ts_filename(station)
    file = os.path.join(ts_dir, filename)
    df = pandas.read_csv(file)
    df = df.set_index(pandas.DatetimeIndex(df['timestamp']))
    if product == "Sentinel-1":
        # product is already filtered by sentinel reader
        sm = df['sm']
        sm = sm[(sm >= 0) & (sm < 100)]
        return sm
    if product == "SMOS-BEC":
        sm_key = config.dict_product_fields[product]['sm_field']
        columns = df.columns
        print(df.shape)
        if 'quality_flag' in columns:
            # filter product based on quality flag
            # 0: Good quality data;
            # 1: L1 brightness temperature corrected by sea-land contamination;
            # 2: L3 soil moisture with no data;
            # 4: L4 soil moisture without physical meaning";
            df = df[(df['quality_flag'] == 0) | (df['quality_flag'] == 1)]
        sm = df[sm_key]
        sm.rename('sm', inplace=True)
        sm = sm[(sm >= 0) & (sm < 1)]
        return sm


def get_img_reader(product, file):
    reader = None
    if product == "Sentinel-1":
        reader = SentinelImg(file)
    # SMOS-BEC reader not currently working
    # if product == "SMOS-BEC":
    #     reader = SMOSBECImg(file, parameters=["SM", "quality_flag"])
    return reader


# filters dataframe by date, assuming index is a datetimeindex
def get_timeframe_data(df, year_filter=None, season_filter=None):
    if year_filter is not None:
        df = df[df.index.year == year_filter]
    if season_filter is not None:
        if season_filter == 'non-winter':
            df = df[(df.index.month != 12) & (df.index.month != 1) & (df.index.month != 2)]
        if season_filter == 'winter':
            df = df[(df.index.month == 12) | (df.index.month == 1) | (df.index.month == 2)]
        if season_filter == 'spring':
            df = df[(df.index.month == 3) | (df.index.month == 4) | (df.index.month == 5)]
        if season_filter == 'summer':
            df = df[(df.index.month == 6) | (df.index.month == 7) | (df.index.month == 8)]
        if season_filter == 'fall':
            df = df[(df.index.month == 9) | (df.index.month == 10) | (df.index.month == 11)]
    return df


def get_triplet_list(triplets):
    triplet_list = []
    for triplet, analyze in triplets.items():
        if analyze:
            triplet_list.append(triplet)
    return triplet_list


def get_timeshifted_data(product, product_data):
    hours = product_data.index.hour
    if not hours.any():
        value, interval = config.dict_timeshifts[product]
        product_data = product_data.shift(value, freq=interval)
        return product_data
    else:
        return product_data


def get_nc_parameter_count(file, parameter):
    ds = netCDF4.Dataset(file, mode="r")
    param_values = numpy.asarray(ds[parameter][:]).ravel()
    (unique, counts) = numpy.unique(param_values, return_counts=True)
    frequencies = numpy.asarray((unique, counts)).T
    return frequencies

# function to find timestamps from a filename, given a searchsting and format
def get_filename_timestamp(filename, date_search_str, datetime_format):
    """""
    Parameters
    filename: filename string
    date_search_str: regex expression for finding timestamp e.g. r"[0-9]{8}T[0-9]{4}", must be unique enough to occur 
        only once in filename
    datetime_format: tuple of tuples. for the above date_search_str, the locations of datetime elements in the string
        (year, month, day) or (year, month, day, hour, minute) 
        example: in the above string, datetime_format would be ((0,4), (4, 6), (6, 8), (9, 11), (11, 13))
        the length of the tuple will determine whether hours/minutes will be added to timestamp, otherwise it will
        default to midnight
    """""
    timestamp_str = re.findall(date_search_str, filename)[-1]
    # when datetime_format is year, month, day
    if len(datetime_format) == 3:
        timestamp = datetime(int(timestamp_str[datetime_format[0][0]:datetime_format[0][1]]),
                             int(timestamp_str[datetime_format[1][0]:datetime_format[1][1]]),
                             int(timestamp_str[datetime_format[2][0]:datetime_format[2][1]]))
    # when datetime_format is year, month, day, hour, minute
    if len(datetime_format) == 5:
        timestamp = datetime(int(timestamp_str[datetime_format[0][0]:datetime_format[0][1]]),
                             int(timestamp_str[datetime_format[1][0]:datetime_format[1][1]]),
                             int(timestamp_str[datetime_format[2][0]:datetime_format[2][1]]),
                             int(timestamp_str[datetime_format[3][0]:datetime_format[3][1]]),
                             int(timestamp_str[datetime_format[4][0]:datetime_format[4][1]]))
    return timestamp


def check_extent(lon_loc, lat_loc, file, lon_field, lat_field):
    ll, ur = get_geo_extent(file, lon_field, lat_field)
    print(any([lat_loc < ll[0], lat_loc > ur[0], lon_loc < ll[1], lon_loc > ur[1]]))
    return not any([lat_loc < ll[0], lat_loc > ur[0], lon_loc < ll[1], lon_loc > ur[1]])


def get_nc_values(file, location, parameters, time_dim=True, lon_field="lon", lat_field="lat"):
    loc_values_dict = {}
    if type(location) == dict:
        loc_meta_dict = location
    else:
        loc_meta_dict = {}
        loc_meta_dict["loc"] = {
            "longitude": location[1],
            "latitude": location[0]
        }
    if type(parameters) != list:
        parameters = [parameters]
    ds = netCDF4.Dataset(file, mode="r")
    lon_array = ds[lon_field][:]
    lat_array = ds[lat_field][:]
    for loc, metadata in loc_meta_dict.items():
        nr_lon_idx = find_nearest(lon_array, ln)[0]
        nr_lat_idx = find_nearest(lat_array, lt)[0]
        for p in parameters:
            if time_dim:
                v = ds[p][:][:, nr_lat_idx, nr_lon_idx]
            else:
                v = ds[p][nr_lat_idx, nr_lon_idx]
            v = numpy.asscalar(numpy.asarray(v))
            loc_values_dict[loc][p] = v
    return loc_values_dict
