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
import matplotlib.pyplot as plt

product = "SMAP L3 Enhanced"
sm_field = config.dict_product_fields[product]['sm_field']
native_res = "9 km"
output_dir = r"../test_output_data/smap_L3E_ts"
in_dir = r"C:\git\soil-moisture-sweden\sm_sample_files\SPL3SMPE-smap-l3-enhanced-09km_nc"

clean_weights = False
test_plots = True
method = 'nearest_s2d'
export_ds = True
regrid = False

f = r"C:\git\soil-moisture-sweden\sm_sample_files\SPL3SMPE-smap-l3-enhanced-09km_nc\SMAP_L3_SM_P_E_20180601_R16510_001_HEGOUT.nc"
ds = xr.open_dataset(f, group="Soil_Moisture_Retrieval_Data_AM")
dr = ds[sm_field]
# print(dr)
print(ds['latitude'])
print(ds['longitude'])

# all files in directory must be product nc files
file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]
# test short list
ds = xtools.get_mf_dataset(file_list, product)

if export_ds:
    ds.to_netcdf(os.path.join(output_dir, "smap-L3E-09km-subset-nofilter.nc"))
    print("smap-L3E-09km-subset-nofilter.nc complete")
    print(ds)
    dr = ds[sm_field]

if regrid:
    print("regridding")
    dr_regrid = xtools.regrid(ds, sm_field, method=method)
    print(dr_regrid)
    dr_regrid.to_netcdf(os.path.join(output_dir, "smap_L3E_0-25-regrid.nc"))
    print("smap_L3E_0-25-regrid.nc complete")