"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/11/2020
Script for exploring TUW_WARP5_grid
"""
import datetime as dt  # Python standard library datetime  module
import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from datetime import datetime
import time
import os
import pandas

file_loc = r"..\sm_sample_files\smos-bec-01km\ASC\BEC_SM____SMOS__EUM_L4__A_20180622T033954_001km_1d_REP_v5.0.nc"
nc_fid = netCDF4.Dataset(file_loc, 'r')
# help(nc_fid)
print(nc_fid.ncattrs())

for key, value in nc_fid.dimensions.items():
    print(key)


lat = nc_fid['lat'][:]
lon = nc_fid['lon'][:]
print('lat.shape', lat.shape)
print('lon.shape', lon.shape)

# print(nc_fid['lat'].shape)
#
# print(nc_fid['lat'])
# print(lon)
# print(lon)
# print(type(lon))

# param = nc_fid['SM']
# data = param[:]
# print(data.shape)
# print(type(data))
# # help(data)
# print(data[0,50,50])
#
print(nc_fid['lat'].shape)
print(nc_fid['lat'])
lat = nc_fid['lat'][:]
# print('lat.shape', lat.shape)
# print(lat)
# print(type(lat))
#
#
# # Degero: lon 19.556539 lat 64.182029
# station_lon = 19.556539
# station_lat = 64.182029
#
# # data_array_lon = np.ma.asarray(lon)
# # data_array_lat = np.ma.asarray(lat)
# # print(find_nearest(data_array_lon, station_lon)[0], find_nearest(data_array_lat, station_lat)[0])
# # print(find_nearest(data_array_lon, station_lon)[1], find_nearest(data_array_lat, station_lat)[1])
# # print(np.amin(data_array_lat))
# # print(np.amax(data_array_lat))
#
# print(get_geo_extent(r"..\sm_sample_files\smos-bec-01km\ASC\BEC_SM____SMOS__EUM_L4__A_20180622T033954_001km_1d_REP_v5.0.nc", 'lon', 'lat'))