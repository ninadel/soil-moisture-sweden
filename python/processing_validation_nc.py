"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/31/2020
Script for exploring SMOS BEC file format
"""
import datetime as dt  # Python standard library datetime  module
import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from datetime import datetime
import time
import os
import pandas
import sm_tools as tools
import sm_config as config

product = "SMOS-BEC"
input_dir = config.dict_product_inputs[product]['raw_dir']
output_dir = config.dict_product_inputs[product]['ts_dir']
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
file_list = os.listdir(input_dir)
file_list.sort()
export_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
sm_key = config.dict_product_fields[product]['sm_field']
qf_key = 'quality_flag'
time_key = 'time'
product_lon = config.dict_product_fields[product]['lon_field']
product_lat = config.dict_product_fields[product]['lat_field']


# Degero: lon 19.556539 lat 64.182029
station_lon = 19.556539
station_lat = 64.182029



series = tools.get_nc_series(input_dir, station_lon, station_lat, [sm_key, qf_key], r"[0-9]{8}T[0-9]{4}",
                        ((0,4), (4, 6), (6, 8), (9, 11), (11, 13)))
print(series)
print(series.shape)

