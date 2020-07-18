"""
Author: Nina del Rosario
Date: 7/18/2020
Script for regridding SMAP L3 data
"""
from datetime import datetime
import numpy as np
import os
import warnings
import xarray as xr
import xtools
import sm_config as config
import matplotlib.pyplot as plt

product = "SMAP L3"
sm_field = config.dict_product_fields[product]['sm_field']
native_res = "36 km"
output_dir = r"C:\git\soil-moisture-sweden\test_output_data\smap L3 xarray export"
in_dir = r"..\input_data\SPL3SMP_smap-L3_36km_clipped_geographic_nc"

clean_weights = False
test_plots = True
method = 'nearest_s2d'
export_ds = True
regrid = False

# all files in directory must be product nc files
file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]
# test short list
ds = xtools.get_mf_dataset(file_list, product)

if export_ds:
    ds.to_netcdf(os.path.join(output_dir, "smap-L3-36km-subset-nofilter.nc"))
    print("smap-L3-36km-subset-nofilter.nc complete")
    print(ds)

if regrid:
    print("regridding")
    dr = ds[sm_field]
    dr_regrid = xtools.regrid(ds, sm_field, method=method)
    print(dr_regrid)
    dr_regrid.to_netcdf(os.path.join(output_dir, "smap_L3_0-25-regrid.nc"))
    print("smap_L3_0-25-regrid.nc complete")