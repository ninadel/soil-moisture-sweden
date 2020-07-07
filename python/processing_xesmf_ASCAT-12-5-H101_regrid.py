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

product = "ASCAT 12.5 Swath"
sm_field = config.dict_product_fields[product]['sm_field']
native_res = "12.5 km"
output_dir = r"../test_output_data/ascat-12-5-h101"
in_dir = r"/Users/nina/Documents/GitHub/soil-moisture-sweden/test_input_data/OneDrive_3_7-6-2020"
clean_weights = False
test_plots = True
method = 'nearest_s2d'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# all files in directory must be product nc files
file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]
ds = xtools.get_mf_dataset(file_list, product)

print(ds)

# export
# ds.to_netcdf(os.path.join(output_dir, "smos-ic_25km-subset-nofilter.nc"))
# print("smos-ic_25km-subset-nofilter.nc complete")
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
#
# dr = ds['Soil_Moisture']
#
# if test_plots:
#     plot_test = dr.sel(time="2018-06-01")
#     plot_test.plot()
#     plt.title('{} {} subset, valid values'.format(product, native_res))
#     plt.savefig(os.path.join(output_dir, "test_soilmoisture_subset_validvalues.png"), dpi=150)
#     plt.show()
#     plt.clf()
#
# print("regridding")
# dr_regrid = xtools.regrid(ds, sm_field, method=method)
# if test_plots:
#     plot_test = dr_regrid.sel(time="2018-06-01")
#     plot_test.plot()
#     plt.title('{} 0.25 regrid, {}'.format(product, method))
#     plt.savefig(os.path.join(output_dir, "test_ssm_regrid.png"), dpi=150)
#     plt.show()
#     plt.clf()
#
# print(dr_regrid)
# dr_regrid.to_netcdf(os.path.join(output_dir, "smos-ic_0-25-regrid.nc"))
# print("smos-ic_0-25-regrid.nc complete")

# xtools.write_ts_quarter_deg(dr_regrid, output_dir)