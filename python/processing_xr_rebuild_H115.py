import xarray as xr
import xtools as xt
import json
import sm_tools as tools
from datetime import datetime
import numpy as np
import pandas as pd
import os

def build_ds(array_dict, lat_grid, lon_grid, timestamp=None):
    ds = xr.Dataset(
        {
            "sm": (
                ("row", "col"),
                array_dict["sm"],
            ),
            "sm_noise": (
                ("row", "col"),
                array_dict["sm_noise"],
            ),
            "conf_flag": (
                ("row", "col"),
                array_dict["conf_flag"],
            ),
            "corr_flag": (
                ("row", "col"),
                array_dict["corr_flag"],
            ),
            "proc_flag": (
                ("row", "col"),
                array_dict["proc_flag"],
            ),
            "ssf": (
                ("row", "col"),
                array_dict["ssf"],
            ),
        },
        # coords={"lat": lat_grid, "lon": lon_grid, "row": rowNums, "col": colNums}
        coords={
            "lat": (("row", "col"), lat_grid),
            "lon": (("row", "col"), lon_grid)
        }
    )
    if timestamp is not None:
        ds["time"] = timestamp
        ds = ds.expand_dims("time").set_coords("time")
    return ds


# dictionary which defines timeframes to analyze
with open("dict_h115_swe_coords.json", "r") as f:
    dict_h115_swe_coords = json.load(f)

input_dir = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\csv\ascat-h115-ts_points_csv\overpass_data"
output_dir = r"..\test_output_data\h115_reprocessed\timedim"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
template_f = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\satellite\native_resolution\ASCAT-12-5\ascat_h115_swe_template.nc"
ds = xr.open_dataset(template_f)
ds_shape = ds['lat'].shape
lat_array = ds['lat'].values
lon_array = ds['lon'].values
output_vars = ['sm', 'sm_noise', 'conf_flag', 'corr_flag', 'proc_flag', 'ssf']

for filename in os.listdir(input_dir):
    file = os.path.join(input_dir, filename)
    arrays = xt.populate_arrays(dict_h115_swe_coords, ds_shape, file, output_vars)
    sat = filename[3:4]
    year = int(filename[5:9])
    month = int(filename[10:12])
    day = int(filename[13:15])
    hour = int(filename[16:18])
    minute = int(filename[19:21])
    timestamp = datetime(year, month, day, hour, minute)
    print(timestamp)
    ds = build_ds(arrays, lat_array, lon_array, timestamp)
    # ds = build_ds(arrays, lat_array, lon_array)
    output_file = os.path.join(output_dir,
                               "ascat-h115-12-5_reprocessed_sat{}_{}{:02d}{:02d}{:02d}{:02d}.nc".format(
                                   sat,year,month,day,hour,minute))
    ds.to_netcdf(output_file)