"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding ASCAT 12.5 Swath data
"""

import numpy as np
import os
import xarray as xr
import sm_config as config

# method options: 'nearest_s2d', 'bilinear', and 'conservative' (conservative not currently working)
method = 'nearest_s2d'
# method = 'bilinear'
# method = 'conservative'

def preprocess(ds):
    '''keep only the first timestep for each file'''
    ds = ds.sel(
        lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
        lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
    ds = ds.where(ds['Quality_Flag'] == 0)
    return ds

f = r"/Volumes/TOSHIBA EXT/sm_backup/smos-ic-l3-25km_global/ASC/SM_RE06_MIR_CDF3SA_20150101T000000_20150101T235959_105_001_8.DBL.nc"
in_dir = r"/Volumes/TOSHIBA EXT/sm_backup/smos-ic-l3-25km_global/ASC"
in_glob = in_dir + "/*.nc"
vars = ['lat', 'lon', 'Days', 'Processing_Flags', 'Soil_Moisture']
# ds_in = xr.open_dataset(f, decode_times=False)
# ds = xr.open_mfdataset(in_glob, data_vars=vars)

test_ds = xr.open_dataset(f)
print(test_ds['Soil_Moisture'].count())
print(test_ds['Soil_Moisture'].encoding)


print('subset')
test_ds = test_ds.sel(
    lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
    lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
print(test_ds['Soil_Moisture'].count())
print('pre-mask (Quality_Flag)')
test_ds = test_ds.where((test_ds['Quality_Flag'] == 0) | (test_ds['Quality_Flag'] == 1))
print(test_ds['Soil_Moisture'].count())

# test_ds = test_ds.expand_dims('time')
print(test_ds)
# print(test_ds['time'])
test_ds = test_ds.assign(time=5)
print(test_ds)
print(test_ds['time'])
# help(test_ds['Soil_Moisture'].values.min)
# print(ds)

# print summaries
# print('ds_in summary')
# print(ds_in.dims)
# print(ds_in.coords)
# print(ds_in.data_vars)

# select array for variable to be regridded and mask out invalid values
# print('dr_in')
# dr_in = ds_in['soil_moisture'].where((ds_in['soil_moisture'] >= 0) & (ds_in['soil_moisture']<100))
# print(dr_in.values)

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