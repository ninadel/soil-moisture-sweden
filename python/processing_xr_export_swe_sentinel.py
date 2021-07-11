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

product = 'Sentinel-1'
output_dir = r"..\test_output_data\sentinel-1_regrid_ts"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
f = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\satellite\0-25_regrid\Sentinel\sentinel_0-25-regrid-mask.nc"
sm_field = dicts.dict_product_fields[product]['sm_field']

ds = xr.open_dataset(f)
print(ds)
dr = ds[sm_field]
print(dr)

# def write_ts_quarter_deg(dr, output_dir, overwrite=False):
xtools.write_ts_quarter_deg(dr, output_dir)
