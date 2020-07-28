"""
Author: Nina del Rosario
Date: 7/18/2020
Script for regridding SMAP L3 data
"""
from datetime import datetime
import numpy as np
import os
import warnings
import xarray as xr
import xtools
import sm_config as config
import matplotlib.pyplot as plt


product = "SMAP L3"
output_dir = r"..\input_data\xr"
in_dir = r"..\input_data\SPL3SMP_smap-L3_36km_clipped_NoReproj_nc"

export_ds = False

# first file for creating lat and lon dimensions
first_file = r"..\input_data\SPL3SMP_smap-L3_36km_clipped_NoReproj_nc\SMAP_L3_SM_P_20150401_R16510_001_HEGOUT.nc"
first_ds = xr.open_dataset(first_file, group='Soil_Moisture_Retrieval_Data_AM')
lon = first_ds['longitude'][0, :].values
lat = first_ds['latitude'][:, 0].values
local_time_utc = 5

ds_list = []

for filename in os.listdir(in_dir):
    file = os.path.join(in_dir, filename)
    datestamp = tools.get_filename_timestamp(file, r"P_[0-9]{8}_R")
    datestamp = datestamp.replace(hour=local_time_utc)
    print(file)
    ds = xr.open_dataset(file, group='Soil_Moisture_Retrieval_Data_AM')
    soil_moisture = ds['soil_moisture'].values
    soil_moisture_da = xr.DataArray(soil_moisture, coords=[lat, lon], dims=["lat", "lon"], name="soil_moisture")
    surface_flag = ds['surface_flag'].values
    surface_flag_da = xr.DataArray(surface_flag, coords=[lat, lon], dims=["lat", "lon"], name="surface_flag")
    retrieval_qual_flag = ds['retrieval_qual_flag'].values
    retrieval_qual_flag_da = xr.DataArray(retrieval_qual_flag, coords=[lat, lon], dims=["lat", "lon"],
                                          name="retrieval_qual_flag")
    out_ds = xr.merge([soil_moisture_da, surface_flag_da, retrieval_qual_flag_da])
    out_ds["time"] = datestamp
    out_ds = out_ds.expand_dims('time').set_coords('time')
    ds_list.append(out_ds)

concat_ds = xr.concat(ds_list, dim="time")
print(concat_ds)
print(concat_ds.lat)
print(concat_ds.lon)
print(concat_ds.time)
concat_ds.to_netcdf(os.path.join(output_dir, "smap-L3-36km-subset-filter.nc"))


product = "SMAP L3"
sm_field = config.dict_product_fields[product]['sm_field']
output_dir = r"../test_output_data"
in_dir = r"..\input_data\SPL3SMP_smap-L3_36km_clipped_geographic_nc"

clean_weights = False
regrid = True

f = r"/Volumes/TOSHIBA EXT/sm_backup/xr/smap-L3-36km-subset-nofilter.nc"
ds = xr.open_dataset(f)
print(ds)
dr = ds[sm_field]
plot_test = dr.sel(time="2018-06-01T05:00:00")
plot_test.plot()
plt.show()
plt.clf()
# print(ds)
# print(ds[sm_field].values)

# filter out invalid values
ds = ds.where((ds['retrieval_qual_flag'] == 0) | (ds['retrieval_qual_flag'] == 1) |
              (ds['retrieval_qual_flag'] == 8))
ds = ds.where((ds[sm_field] >= 0) & (ds[sm_field] < 1))
dr = ds[sm_field]
plot_test = dr.sel(time="2018-06-01T05:00:00")
plot_test.plot()
plt.show()
plt.clf()
# print(ds)
# print(ds[sm_field].values)

# if export_ds:
#     ds.to_netcdf(os.path.join(output_dir, "smap-L3-36km-subset-nofilter.nc"))
#     print("smap-L3-36km-subset-nofilter.nc complete")
#     print(ds)

if regrid:
    print("regridding")
    dr = ds[sm_field]
    dr_regrid = xtools.regrid(ds, sm_field, method="nearest_s2d", reuse=False)
    plot_test = dr_regrid.sel(time="2018-06-01T05:00:00")
    plot_test.plot()
    plt.show()
    plt.clf()
    print(dr_regrid)
    dr_regrid_bl = xtools.regrid(ds, sm_field, method="bilinear")
    dr_regrid[np.isnan(dr_regrid_bl)] = np.nan
    plot_test = dr_regrid.sel(time="2018-06-01T05:00:00")
    plot_test.plot()
    plt.show()
    plt.clf()
    print(dr_regrid)
    dr_regrid.to_netcdf(os.path.join(output_dir, "smap_L3_0-25-regrid2.nc"))
    print("smap_L3_0-25-regrid.nc complete")