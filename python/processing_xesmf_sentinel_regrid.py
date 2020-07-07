"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding SMOS-IC data
"""
from datetime import datetime
import numpy as np
import os
import warnings
import xtools
import sm_config as config
import matplotlib.pyplot as plt

product = "Sentinel-1"
native_res = "1km"
sm_field = config.dict_product_fields[product]['sm_field']
clean_weights = False
test_plots = True

output_dir = r"../test_output_data/sentinel"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

in_dir = r"/Volumes/TOSHIBA EXT/sm_backup/cgls-biopar-ssm-01km_europe"

file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]
print(file_list)

# open files and subset
ds = xtools.get_mf_dataset(file_list, 'Sentinel-1')
print(ds)

# export subset to nc
ds.to_netcdf(os.path.join(output_dir, "sentinel_01km-subset-nofilter.nc"))
print("sentinel_01km-subset-nofilter.nc complete")

# print summaries
print('ds summary')
print(ds.dims)
print(ds.coords)
print(ds.data_vars)

# export nc file
ds.to_netcdf(os.path.join(output_dir, "sentinel_01km_subset_nofilter.nc"))
print("sentinel_01km_subset_nofilter.nc complete")

# filter out invalid values
ds = ds.where((ds['ssm'] >= 0) & (ds['ssm'] < 100))
dr = ds[sm_field]

# export valid values to nc
dr.to_netcdf(os.path.join(output_dir, "sentinel_01km_subset_validvalues.nc"))
print("sentinel_01km_subset_validvalues.nc complete")

# ds = xr.open_dataset(r"../test_output_data/sentinel/sentinel_01km_subset_validvalues.nc")
# dr = ds[sm_field]

# if test_plots:
#     plot_test = dr.sel(time="2018-06-01")
#     plot_test.plot()
#     plt.title('{} {} subset, valid values'.format(product, native_res))
#     plt.savefig(os.path.join(output_dir, "test_ssm_subset_validvalues.png"), dpi=150)
#     plt.show()
#     plt.clf()

# interpolate nan?
dr_regrid = xtools.regrid(ds, sm_field, method='nearest_s2d')
# if test_plots:
#     plot_test = dr_regrid.sel(time="2018-06-01")
#     plot_test.plot()
#     plt.title('{} 0.25 regrid'.format(product))
#     plt.savefig(os.path.join(output_dir, "test_ssm_regrid.png"), dpi=150)
#     plt.show()
#     plt.clf()

# export regrid to nc
dr_regrid.to_netcdf(os.path.join(output_dir, "sentinel_0-25-regrid.nc"))
print("sentinel_0-25-regrid.nc complete")

    # xtools.write_ts_quarter_deg(dr_regrid, output_dir)


