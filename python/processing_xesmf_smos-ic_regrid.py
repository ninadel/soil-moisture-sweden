"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding SMOS-IC data
"""
from datetime import datetime
import numpy as np
import os
import warnings
import xarray as xr
import xtools
import sm_config as config

output_dir = r"../test_output_data/smos_ic_regrid_ts"
# method options: 'nearest_s2d', 'bilinear', and 'conservative' (conservative not currently working)
method = 'nearest_s2d'
# method = 'bilinear'
# method = 'conservative'

in_dir = r"/Volumes/TOSHIBA EXT/sm_backup/smos-ic-l3-25km_global/ASC"
in_glob = in_dir + "/*.nc"

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]
# crop for testing
file_list = file_list
ds = xtools.get_mf_dataset(file_list, 'SMOS-IC')

# filter out invalid data
ds = ds.where((ds['Quality_Flag'] == 0) & (ds['Soil_Moisture'] >= 0) & (ds['Soil_Moisture'] < 1))

# print summaries
print('ds summary')
print(ds.dims)
print(ds.coords)
print(ds.data_vars)

dr = ds['Soil_Moisture']

dr_regrid = xtools.regrid(ds, 'Soil_Moisture')
print(dr_regrid)

xtools.write_ts_quarter_deg(dr_regrid, output_dir)