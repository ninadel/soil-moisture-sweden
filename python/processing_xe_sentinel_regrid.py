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
import xtools as xt
import xesmf as xe
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

f = r"/Volumes/TOSHIBA EXT/sm_backup/xr/sentinel_01km-subset-nofilter.nc"
# in_dir = r"/Volumes/TOSHIBA EXT/sm_backup/native/cgls-biopar-ssm-01km_europe"

# file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]
# print(file_list)
# file = file_list[0]
#
ds = xr.open_dataset(f)
print(ds)
print(ds['ssm'].shape)
print(ds['ssm'][0,:,:])
# print(ds[0,:,:])

# print(ds['ssm'][0,:,:].shape)
# print(ds['time'].shape)
# print(len(ds['time']))
# print(ds['time'][0].values)
# print(ds)
#
ds_in = ds['ssm'][0, :, :]
print(ds_in)
print(ds_in.shape)
ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                     'lon': (['lon'], config.regrid_lon)})
nearest_reg = xe.Regridder(ds_in, ds_out, method="nearest_s2d", reuse_weights=True)
bilinear_reg = xe.Regridder(ds_in, ds_out, method="bilinear", reuse_weights=True)

concat_arrays = []

for index, time in enumerate(ds['time'].values):
    print(time)
    dr_in = ds['ssm'][index,:,:]
    # dr_in.plot()
    # plt.show()
    # plt.clf()
    nearest_dr_out = nearest_reg(dr_in)
    # nearest_dr_out.plot()
    # plt.show()
    # plt.clf()
    output_shape = nearest_dr_out.shape
    dr_regrid = nearest_dr_out.copy()
    bilinear_dr_out = bilinear_reg(dr_in)
    # print(bilinear_dr_out)
    for i in range(0,output_shape[0]):
        if bilinear_dr_out.values[i,:].mean() == 0:
            dr_regrid.values[i,:] = np.nan
    for i in range(0,output_shape[1]):
        if bilinear_dr_out.values[:,i].mean() == 0:
            dr_regrid.values[:,i] = np.nan
    # dr_regrid.plot()
    # plt.show()
    # plt.clf()
    # print(dr_regrid)
    concat_arrays.append(dr_regrid)

ds_concat = xr.concat(concat_arrays)
ds_concat.to_netcdf(os.path.join(output_dir, "sentinel_0-25-regrid-mask.nc"))


# def regrid(ds_in, var, method='nearest_s2d', reuse=False, cleanup=False, mask=True):
#     if 'latitude' in ds_in.coords:
#         ds_in = ds_in.rename({'latitude': 'lat', 'longitude': 'lon'})
#     if 'time' in ds_in.coords:
#         ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
#                              'lon': (['lon'], config.regrid_lon),
#                             'time': (['time'], ds_in['time'].values)})
#     else:
#         ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
#                              'lon': (['lon'], config.regrid_lon)})
#     reg = xe.Regridder(ds_in, ds_out, method=method, reuse_weights=reuse)
#     dr_in = ds_in[var]
#     dr_out = reg(dr_in)
#     if mask:
#         # code for masking
#         # do separate regrid with bilinear
#         # use bilinear to mask results from nearest_s2d
#         pass
#     if cleanup:
#         reg.clean_weight_file()  # clean-up
#     return dr_out

# for time in ds['time']
    # extract 2D sm array
    # extract time
    # get nearests2d regrid
    # get bilinear regrid
    # extend with time

# for time in range(0,len()):
#     print(time.value)
#     break

# dr = ds['ssm']
# dr_regrid = xt.regrid(ds, sm_field, method="nearest_s2d", reuse=True)
# print("nearest_s2d")
# print(dr_regrid)
# dr_regrid_bl = xt.regrid(ds, sm_field, method="bilinear", reuse=True)
# print("bilinear")
# print(dr_regrid_bl)
# dr_regrid[np.isnan(dr_regrid_bl)] = np.nan
# print("mask")
# print(dr_regrid)

# # interpolate nan?
# dr_regrid = xtools.regrid(ds, sm_field, method='nearest_s2d')
#
# # export regrid to nc
# dr_regrid.to_netcdf(os.path.join(output_dir, "sentinel_0-25-regrid.nc"))
# print("sentinel_0-25-regrid.nc complete")

