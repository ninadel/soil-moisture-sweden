"""
Author: Nina del Rosario
Date: 7/18/2020
Script for regridding H115 repocessed
UPDATE_DESCRIPTION

"""
from datetime import datetime
import numpy as np
import os
import warnings
import xarray as xr
import xtools
import xesmf as xe
import sm_config as config
import matplotlib.pyplot as plt


product = "ASCAT 12.5 TS"
output_dir = r"../input_data/xr"
in_dir = r"../input_data/H115_rebuild"
# r'/media/ninadel/TOSHIBA EXT/sample_rs_files/ascat-12.5-km-bufr'
f = r"../input_data/H115_rebuild/test_h115_reprocessed.nc"
regrid = True

ds = xr.open_dataset(f)
print(ds)

print(os.listdir(in_dir))

if regrid:
    print("regridding")
    # dr = ds[sm_field]
    ds_in = ds
    ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                         'lon': (['lon'], config.regrid_lon)})
    reg = xe.Regridder(ds_in, ds_out, method="nearest_s2d")
    dr_in = ds_in['sm']
    dr_out = reg(dr_in)
    dr_out.to_netcdf(os.path.join(output_dir, "test_h115_regrid.nc"))
    # print("smap_L3_0-25-regrid.nc complete")

    #     ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
    #                          'lon': (['lon'], config.regrid_lon)})
    # reg = xe.Regridder(ds_in, ds_out, method=method, reuse_weights=reuse)
    # dr_in = ds_in[var]
