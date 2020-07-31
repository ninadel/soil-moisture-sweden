import xarray as xr
import xtools as xt
import json
import sm_tools as tools
from datetime import datetime
import numpy as np
import pandas as pd
import os

in_dir = r"/Volumes/TOSHIBA EXT/sm_backup/xr/ascat_h115_reprocessed_AM_xr/timedim"
output_dir = r"/Users/nina/Documents/GitHub/soil-moisture-sweden/test_output_data"

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]

ds = xr.open_mfdataset(file_list, combine='by_coords')
print(ds)
ds.to_netcdf(os.path.join(output_dir, "ascat-h115_rebuild-subset-nofilter.nc"))

# concat_arrays = []
# for f in file_list:
#     ds = xr.open_dataset(f)
#     ds = ds['SoilMoi0_10cm_inst'].sel(
#         lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
#         lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
#     concat_arrays.append(ds)
#
# ds_concat = xr.concat(concat_arrays, dim="time")
# ds_concat.to_netcdf(os.path.join(output_dir, "gldas-subset-nofilter.nc"))