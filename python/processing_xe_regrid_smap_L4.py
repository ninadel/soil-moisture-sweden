"""
Author: Nina del Rosario
Date: 7/29/2020
Script for regridding SMAP L3 data
UPDATE_DESCRIPTION

"""
import os
import xarray as xr
import xtools as xt
import sm_config as config

product = "SMAP L4"
sm_field = config.dict_product_fields[product]['sm_field']
output_dir = r"/Users/nina/Documents/GitHub/soil-moisture-sweden/test_output_data"
f = r"/Users/nina/Documents/GitHub/soil-moisture-sweden/test_output_data/smap_L4_rebuild/smap-L4-09km-subset-nofilter.nc"

ds = xr.open_dataset(f)
# filter out invalid data
# ds = ds.where((ds['retrieval_qual_flag'] == 0) | (ds['retrieval_qual_flag'] == 1) | (ds['retrieval_qual_flag'] == 8))
ds = ds.where((ds[sm_field] >= 0) & (ds[sm_field] < 1))

dr_out = xt.regrid_multidate(ds, sm_field)
dr_out.to_netcdf(os.path.join(output_dir, "smap-L4_0-25-regrid.nc"))