"""
Author: Nina del Rosario
Date: 7/29/2020
Script for merging SMOS-IC data using xarray
UPDATE_DESCRIPTION
"""
import os
import xarray as xr
import xtools as xt
import sm_tools as tools

product = "SMOS-IC"
output_dir = r"../test_output_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
in_dir = r"D:\sm_backup\native\smos-ic-l3-25km_global\ASC"

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]

# open files and subset
ds = xt.get_mf_dataset(file_list, 'SMOS-IC')
print(ds)

# export subset to nc
ds.to_netcdf(os.path.join(output_dir, "smos-ic_25km-subset-nofilter.nc"))
print("smos-ic_25km-subset-nofilter.nc")

