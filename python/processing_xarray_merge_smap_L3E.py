"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding merging SMAP L3E data using xarray
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
output_dir = r"..\input_data\xr"
in_dir = r"..\input_data\SPL3SMP_E_smap-L3E_09km_clipped_geographic_nc"

export_ds = True

# all files in directory must be product nc files
file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]

# open multi file dataset
ds = xtools.get_mf_dataset(file_list, product)

if export_ds:
    ds.to_netcdf(os.path.join(output_dir, "smap-L3E-09km-subset-nofilter.nc"))
    print("smap-L3E-09km-subset-nofilter.nc complete")
    print(ds)
    