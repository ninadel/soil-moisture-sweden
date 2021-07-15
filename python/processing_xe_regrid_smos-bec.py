"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding SMOS-IC data
UPDATE_DESCRIPTION

"""
import os
import xarray as xr
import xtools as xt
import sm_config as config
import sm_dictionaries as dicts

product = "SMOS-BEC"
sm_field = dicts.dict_product_fields[product]['sm_field']
output_dir = r"../test_output_data"
f = r"/Users/nina/Documents/GitHub/soil-moisture-sweden/test_output_data/smos-bec_01km-subset-nofilter.nc"

ds = xr.open_dataset(f)
# # filter out invalid data
# ds = ds.where((ds['Quality_Flag'] != 2) & (ds[sm_field] >= 0) & (ds[sm_field] < 1))
# quality flag 2 is already filtered out by filtering out values not in the 0-1 interval
ds = ds.where((ds[sm_field] >= 0) & (ds[sm_field] < 1))

dr_out = xt.regrid_multidate(ds, sm_field)
dr_out.to_netcdf(os.path.join(output_dir, "smos-bec_0-25-regrid.nc"))
