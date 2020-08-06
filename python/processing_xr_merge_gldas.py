"""
Author: Nina del Rosario
Date: 7/29/2020
Script for merging GLDAS data using xarray
"""
import os
import xarray as xr
import xtools as xt
import sm_tools as tools
import sm_config as config

product = "GLDAS"
output_dir = r"../test_output_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
in_dir = r"D:\sm_backup\native\GLDAS_global"

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]

concat_arrays = []
for f in file_list:
    ds = xr.open_dataset(f)
    ds = ds['SoilMoi0_10cm_inst'].sel(
        lat=slice(config.study_area['min_lat'], config.study_area['max_lat']),
        lon=slice(config.study_area['min_lon'], config.study_area['max_lon']))
    concat_arrays.append(ds)

ds_concat = xr.concat(concat_arrays, dim="time")
ds_concat.to_netcdf(os.path.join(output_dir, "gldas-subset-nofilter.nc"))