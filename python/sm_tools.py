"""
Author: Nina del Rosario
Date: 5/25/2020
Functions for analyzing soil moisture datasets
"""
import datetime
import ismn
import os
import pandas
import pytesmo

def get_timestamp():
    # Converting datetime object to string
    timestamp = datetime.now()
    timestampStr = timestamp.strftime("%y%m%d_%H%M")
    return timestampStr


def add_icos_data(input_dir, stations, icos_dict, data_only=True):
    temp_dict = {}
    if type(stations) != list:
        stations = [stations]
    for station in stations:
        filename = station + '.csv'
        data = pandas.read_csv(os.path.join(input_dir, filename), sep=',', index_col=0)
        icos_dict[station]['data'] = data
    # generate dict where data key is present
    if data_only:
        for station, metadata_dict in icos_dict.items():
            if 'data' in metadata_dict.keys():
                temp_dict[station] = metadata_dict
        icos_dict = temp_dict
    return icos_dict

# get location data (lon, lat, ts)
def get_location_data(lon, lat, ts):
    # get data
    # return dataframe
    pass


# get data for all network/stations in a dictionary
def compare_ts(eval_ts_data, ref_ts_data, eval_ts_name=None, ref_ts_name=None, timeframe=None, network=None, station=None, lon=None, lat=None):
    """""
    eval_ts: dataset of product to be evaluated
    ref_ts: reference dataset
    timeframe: timeframe dictionary, default is None
    """""
    print('analyzing', )
    # initiate matched dataset object
    matched_data = []
    # get metrics on matched datset object
    metrics = matched_data.get_metrics()
    return metrics


