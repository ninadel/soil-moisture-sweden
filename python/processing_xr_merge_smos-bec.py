"""
Author: Nina del Rosario
Date: 7/29/2020
Script for merging SMOS-BEC data using xarray
"""
import os
import xarray as xr
import xtools as xt
import sm_tools as tools

product = "SMOS-BEC"
output_dir = r"/Users/nina/Documents/GitHub/soil-moisture-sweden/test_output_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
in_dir = r"/Volumes/TOSHIBA EXT/sm_backup/native/smos-bec-reprocessed-01km-euro/ASC"

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]

# open files and subset
ds = xt.get_mf_dataset(file_list, 'SMOS-BEC')
print(ds)

# export subset to nc
ds.to_netcdf(os.path.join(output_dir, "smos-bec_01km-subset-nofilter.nc"))
print("smos-bec_01km-subset-nofilter.nc")

