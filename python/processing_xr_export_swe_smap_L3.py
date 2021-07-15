"""
Author: Nina del Rosario
Date: UPDATE_DATE
UPDATE_DESCRIPTION
"""

import os
import xarray as xr
import xtools
import sm_config as config
import sm_dictionaries as dicts

product = "SMAP L3"
output_dir = r"..\test_output_data\smap_L3_regrid_ts"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
f = r"..\input_data\xr\regrid\smap-L3_0-25-regrid.nc"
sm_field = dicts.dict_product_fields[product]['sm_field']

ds = xr.open_dataset(f)
print(ds)
dr = ds[sm_field]
print(dr)

# def write_ts_quarter_deg(dr, output_dir, overwrite=False):
xtools.write_ts_quarter_deg(dr, output_dir)
