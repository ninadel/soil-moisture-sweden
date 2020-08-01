"""
Author: Nina del Rosario
Date: 6/27/2020
Script for regridding ERA5 file
"""

import xarray as xr
import sm_config as config
import xtools as xt
import os

product = "ERA5 0-1"
sm_field = config.dict_product_fields[product]['sm_field']
f = r"/Volumes/TOSHIBA EXT/sm_backup/native/ERA5-Land/hourly/0-1_ERA5-Land_hourly.nc"
ds = xr.open_dataset(f)
output_dir = r"../test_output_data"

dr_out = xt.regrid_multidate(ds, sm_field)
dr_out.to_netcdf(os.path.join(output_dir, "era-0-1_0-25-regrid.nc"))
