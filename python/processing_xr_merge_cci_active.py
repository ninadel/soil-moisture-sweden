"""
Author: Nina del Rosario
Date: 7/29/2020
Script for merging CCI data using xarray
"""
import os
import xarray as xr
import xtools as xt
import sm_tools as tools

product = "CCI Active"
output_dir = r"../test_output_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
in_dir = r"D:\sm_backup\native\cci-0.25deg_active_global"

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]

# open files and subset
ds = xt.get_mf_dataset(file_list, 'CCI Active')
print(ds)

# export subset to nc
ds.to_netcdf(os.path.join(output_dir, "cci-active-subset-nofilter.nc"))
print("cci-active-subset-nofilter.nc")

