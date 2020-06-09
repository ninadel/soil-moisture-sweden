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
series = tools.get_series(r"..\sm_sample_files\smos-bec-01km\ASC", 'SM', station_lon, station_lat)
print(series)