"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding SMAP L3E data
"""
import os
import xarray as xr
import xtools as xt
import sm_config as config

product = "SMAP L3 Enhanced"
sm_field = config.dict_product_fields[product]['sm_field']
native_res = "9 km"
output_dir = r"/Users/nina/Documents/GitHub/soil-moisture-sweden/test_output_data"
f = r"/Volumes/TOSHIBA EXT/sm_backup/xr/smap-L3E-09km-subset-nofilter.nc"

ds = xr.open_dataset(f)
# filter out invalid data
ds = ds.where((ds['retrieval_qual_flag'] == 0) | (ds['retrieval_qual_flag'] == 1) | (ds['retrieval_qual_flag'] == 8))
ds = ds.where((ds[sm_field] >= 0) & (ds[sm_field] < 1))

dr_out = xt.regrid_multidate(ds, sm_field)
dr_out.to_netcdf(os.path.join(output_dir, "smap-L3E_0-25-regrid.nc"))