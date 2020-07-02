"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding SMOS-IC data
"""
import numpy as np
import os
import xarray as xr
import xtools

# method options: 'nearest_s2d', 'bilinear', and 'conservative' (conservative not currently working)
method = 'nearest_s2d'
# method = 'bilinear'
# method = 'conservative'

try:
    f = r"/Volumes/TOSHIBA EXT/sm_backup/smos-ic-l3-25km_global/ASC/SM_RE06_MIR_CDF3SA_20150101T000000_20150101T235959_105_001_8.DBL.nc"
    in_dir = r"/Volumes/TOSHIBA EXT/sm_backup/smos-ic-l3-25km_global/ASC"
    in_glob = in_dir + "/*.nc"
    test_ds = xr.open_dataset(f)
except:
    f = r"D:\sm_backup\smos-ic-l3-25km_global\ASC\SM_RE06_MIR_CDF3SA_20150101T000000_20150101T235959_105_001_8.DBL.nc"
    in_dir = r"D:\sm_backup\smos-ic-l3-25km_global\ASC"
    in_glob = in_dir + "/*.nc"
    test_ds = xr.open_dataset(f)

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]
# crop for testing
file_list = file_list[0:5]
ds = xtools.get_mf_dataset(file_list, 'SMOS-IC')

# filter out invalid data
ds = ds.where((ds['Quality_Flag'] == 0) & (ds['Soil_Moisture'] >= 0) & (ds['Soil_Moisture'] < 1))

# print summaries
# print('ds_in summary')
# print(ds_in.dims)
# print(ds_in.coords)
# print(ds_in.data_vars)

# # create shell for output grid
# if method == 'nearest_s2d' or method == 'bilinear':
#     ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
#                          'lon': (['lon'], config.regrid_lon)})
# elif method == 'conservative':
#     ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
#                          'lon': (['lon'], config.regrid_lon),
#                          'lat_b': (['lat_b'], config.regrid_lat_b),
#                          'lon_b': (['lon_b'], config.regrid_lon_b)
#                          })

# create regridder object
# reg = xe.Regridder(ds_in, ds_out, method)

# regrid soil moisture
# dr_out = reg(dr_in)
#
# print('dr_out')
# print(dr_out.values)