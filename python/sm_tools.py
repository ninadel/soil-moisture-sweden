"""
Author: Nina del Rosario
Date: 5/25/2020
Functions for analyzing soil moisture datasets
"""
import ismn
import pandas
import pytesmo
import datetime


def get_timestamp():
    # Converting datetime object to string
    timestamp = datetime.now()
    timestampStr = timestamp.strftime("%y%m%d_%H%M")
    return timestampStr


# based on a directory of in situ text files, create a dictionary of stations
def get_station_dict(input_dir):
    # return dictionary
    # see "C:\git\nordic-insitu-sm-data\ismn-network-processing.ipynb" for reference
    pass


def concat_data(data1, data2):
    pass

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


