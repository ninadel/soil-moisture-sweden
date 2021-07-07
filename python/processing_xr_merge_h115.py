"""
Author: Nina del Rosario
Date: UPDATE_DATE
UPDATE_DESCRIPTION
"""

import xarray as xr
import xtools as xt
import json
import sm_tools as tools
from datetime import datetime
import numpy as np
import pandas as pd
import os

input_dir = r"..\test_output_data\H115_reprocessed"
output_dir = r"..\test_output_data"

file_list = [os.path.join(input_dir, file) for file in os.listdir(input_dir)]

ds = xr.open_mfdataset(file_list, combine='by_coords')
ds.to_netcdf(os.path.join(output_dir, "ascat-h115_rebuild-subset-nofilter.nc"))

# alternate way
# ds_list = [xr.open_dataset(os.path.join(input_dir, filename)) for filename in os.l istdir(input_dir)]

# concat_ds = xr.concat(ds_list, dim="time")
# concat_ds.to_netcdf(os.path.join(output_dir, "ascat-h115_rebuild-subset-nofilter.nc"))