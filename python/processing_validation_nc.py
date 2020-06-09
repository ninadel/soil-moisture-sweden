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

# Degero: lon 19.556539 lat 64.182029
station_lon = 19.556539
station_lat = 64.182029


# print(os.listdir(r"..\sm_sample_files\smos-bec-01km\ASC"))
# series = tools.get_series(r"..\sm_sample_files\smos-bec-01km\ASC", station_lon, station_lat, parameters=['SM'])
# print(series)

series = tools.get_series(r"..\sm_sample_files\smos-bec-01km\ASC", station_lon, station_lat, sm_field='SM')
print(series)


# "smos-bec-01km\ASC\BEC_SM____SMOS__EUM_L4__A_20180601T030707_001km_1d_REP_v5.0.nc"
# nc = netCDF4.Dataset(
#     r"..\sm_sample_files\smos-bec-01km\ASC\BEC_SM____SMOS__EUM_L4__A_20180601T030707_001km_1d_REP_v5.0.nc", 'r')
# print(nc.variables.keys())
# print(list(nc.variables.keys()))

