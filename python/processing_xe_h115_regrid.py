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
import xtools as xt
import xesmf as xe
import sm_config as config
import matplotlib.pyplot as plt

product = "ASCAT 12.5 TS"
sm_field = config.dict_product_fields[product]['sm_field']

output_dir = r"../test_output_data/ascat-h115_regrid"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

f = r"/Users/nina/Documents/GitHub/soil-moisture-sweden/test_output_data/ascat-h115_rebuild-subset-nofilter.nc"
ds = xr.open_dataset(f)

dr_out = xt.regrid_multidate(ds, sm_field)
dr_out.to_netcdf(os.path.join(output_dir, "ascat-h115_0-25-regrid.nc"))

