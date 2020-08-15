"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding SMOS-IC data
"""
from datetime import datetime
import numpy as np
import os
import warnings
import xtools
import sm_config as config
import matplotlib.pyplot as plt

product = "Sentinel-1"
sm_field = config.dict_product_fields[product]['sm_field']

output_dir = r"../test_output_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

in_dir = r"D:\sm_backup\native\cgls-biopar-ssm-01km_europe"

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]

# open files and subset
ds = xtools.get_mf_dataset(file_list, 'Sentinel-1')
print(ds)

# export subset to nc
ds.to_netcdf(os.path.join(output_dir, "sentinel_01km-subset-nofilter.nc"))
print("sentinel_01km-subset-nofilter.nc")