"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding SMOS-IC data
"""
from datetime import datetime
import numpy as np
import os
import warnings
import xarray as xr
import xtools
import sm_config as config
import matplotlib.pyplot as plt

product = "SMAP L3 Enhanced"
sm_field = config.dict_product_fields[product]['sm_field']
native_res = "9 km"
output_dir = r"../test_output_data/smap_L3E_ts"
in_dir = r"D:\sm_backup\SPL3SMP_E_smap-L3E_09km_clipped_geographic_nc"

clean_weights = False
test_plots = True
method = 'nearest_s2d'

f = r"D:\sm_backup\SPL3SMP_E_smap-L3E_09km_clipped_geographic_nc\SMAP_L3_SM_P_E_20150404_R16510_001_HEGOUT.nc"
ds = xr.open_dataset(f, group="Soil_Moisture_Retrieval_Data_AM")
dr = ds[sm_field]
# print(dr)
print(ds['latitude'])
print(ds['longitude'])
# print(ds['latitude'][:,0])
# print(ds['longitude'][0,:])
# print(ds.encoding['source'])
# dr.assign_coords(lat=ds['latitude'])
# dr.assign_coords(lon=ds['longitude'])
# print(dr)
# out_ds = out_ds.sel(
#         lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
#         lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))

# dr_value = dr.sel(lat=71.477135, lon=4.341286)

# subset = ds.sel(
#     lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
#     lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))

# print summaries
# print('ds summary')
# print(ds.dims)
# print(ds.coords)
# print(ds.data_vars)
#
# print(dr)

# all files in directory must be product nc files
file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]
# test short list
# file_list = file_list[0:5]
ds = xtools.get_mf_dataset(file_list, product)
ds.to_netcdf(os.path.join(output_dir, "smap-L3E-09km-subset-nofilter.nc"))
print("smap-L3E-09km-subset-nofilter.nc complete")
print(ds)
#
# # filter out invalid data
# ds = ds.where((ds['Quality_Flag'] == 0) & (ds[sm_field] >= 0) & (ds[sm_field] < 1))
#
# ds.to_netcdf(os.path.join(output_dir, "smos-ic_25km-subset-qualityfilter.nc"))
# print("smos-ic_25km-subset-qualityfilter.nc complete")
#
# # print summaries
# print('ds summary')
# print(ds.dims)
# print(ds.coords)
# print(ds.data_vars)

dr = ds[sm_field]

# if test_plots:
#     plot_test = dr.sel(time="2018-06-01")
#     plot_test.plot()
#     plt.title('{} {} subset, valid values'.format(product, native_res))
#     plt.savefig(os.path.join(output_dir, "test_soilmoisture_subset_validvalues.png"), dpi=150)
#     plt.show()
#     plt.clf()
#
print("regridding")
dr_regrid = xtools.regrid(ds, sm_field, method=method)
# if test_plots:
#     plot_test = dr_regrid.sel(time="2018-06-01")
#     plot_test.plot()
#     plt.title('{} 0.25 regrid, {}'.format(product, method))
#     plt.savefig(os.path.join(output_dir, "test_ssm_regrid.png"), dpi=150)
#     plt.show()
#     plt.clf()
#
print(dr_regrid)
dr_regrid.to_netcdf(os.path.join(output_dir, "smap_L3E_0-25-regrid.nc"))
print("smap_L3E_0-25-regrid.nc complete")
#
# # xtools.write_ts_quarter_deg(dr_regrid, output_dir)