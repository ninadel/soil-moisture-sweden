"""
Author: Nina del Rosario
Date: 6/27/2020
Script for exporting CSV files of TS within a bounding box around Sweden
"""

import netCDF4
import datetime
import xarray as xr
# import xesmf as xe
import matplotlib
import numpy
import os
import sm_config as config
import sm_tools as tools

f = r"..\input_data\ERA5-Land\0-1_ERA5-Land_0600.nc"
ds = xr.open_dataset(f)

print(ds.dims)
print(ds.coords)
print(ds.data_vars)

test_lat = config.dict_icos["SE-Deg"]["latitude"]
test_lon = config.dict_icos["SE-Deg"]["longitude"]

print(ds['latitude'].values)
print(ds['longitude'].values)
print(ds['time'].values)
# {
#     "min_lat": 55.375,
#     "max_lat": 68.875,
#     "min_lon": 11.375,
#     "max_lon": 24.125
# }
# time_series = ds['swvl1'].sel(time=slice('2015-04-01T06:00:00', '2018-12-31T06:00:00'), latitude=test_lat, longitude=test_lon)
for time in ds['time'].values:
        date_image = ds['swvl1'].sel(time=time)
    print(date_image)
    break

# print(round(config.dict_extent_sweden['min_lat'], 1) - 0.03)
# print(round(config.dict_extent_sweden['max_lat'], 1) - 0.03)

ds_out = xr.Dataset({'latitude': (['latitude'], config.regrid_lat),
                     'longitude': (['longitude'], config.regrid_lat),
                    }
                   )
# regridder = xe.Regridder(ds, ds_out, 'bilinear')
