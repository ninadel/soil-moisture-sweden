"""
Author: Nina del Rosario
Date: 6/27/2020
Script for exporting CSV files of TS within a bounding box around Sweden
"""

# import netCDF4
import datetime
import warnings
import xarray as xr
try:
    import xesmf as xe
except:
    warnings.warn("could not import xesmf. not windows compatible.")
# import matplotlib
import numpy
import os
import sm_config as config
# import sm_tools as tools

f = r"../input_data/ERA5-Land/0-1_ERA5-Land_hourly.nc"
ds = xr.open_dataset(f)
output_dir = r"../era5_ts"

ds = ds.rename({'latitude': 'lat', 'longitude': 'lon'})
dr = ds['swvl1']

ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                     'lon': (['lon'], config.regrid_lon),
                     'time': (['time'], ds['time'].values)
                    })

reg = xe.Regridder(ds, ds_out, 'nearest_s2d')
dr_out = reg(dr)

# EXPORT dr to .nc