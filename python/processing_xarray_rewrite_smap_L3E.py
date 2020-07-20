"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding merging SMAP L3E data using xarray
"""
from datetime import datetime
import numpy as np
import os
import warnings
import xarray as xr
import xtools
import sm_config as config
import sm_tools as tools
import matplotlib.pyplot as plt

def remove_lat_dups(lat_array):
    new_lat_list = []
    last_lat = None
    for lt in lat_array:
        lt = round(float(lt), 6)
        if last_lat is None:
            new_lat_list.append(lt)
            last_lat = lt
        else:
            if lt < last_lat:
                new_lat_list.append(lt)
                last_lat = lt
            else:
                new_lat = last_lat - 0.000001
                new_lat_list.append(new_lat)
                last_lat = new_lat
    lat_array = np.array(new_lat_list)
    return lat_array

product = "SMAP L3 Enhanced"
sm_field = config.dict_product_fields[product]['sm_field']
output_dir = r"..\input_data\xr"
in_dir = r"..\input_data\SPL3SMP_E_smap-L3E_09km_clipped_geographic_nc"

export_ds = False

# all files in directory must be product nc files
file_list = [os.path.join(in_dir, file) for file in os.listdir(in_dir)]

# first file for creating lat and lon dimensions
first_file = r"..\input_data\SPL3SMP_E_smap-L3E_09km_clipped_geographic_nc\SMAP_L3_SM_P_E_20150401_R16510_001_HEGOUT.nc"
first_ds = xr.open_dataset(first_file, group='Soil_Moisture_Retrieval_Data_AM')
lon = first_ds['longitude'][0, :].values
lat = first_ds['latitude'][:, 0].values
lat = remove_lat_dups(lat)

for file in file_list:
    new_filename = os.path.split(file)[-1].replace(".nc", "_xr.nc")
    print(new_filename)

# get timestamp from filename
datestamp = tools.get_filename_timestamp(first_file, r"E_[0-9]{8}_R")
# since timestamp is midnight, add local overpass time in utc
local_time_utc = 5
lon = first_ds['longitude'][0, :].values
lat = first_ds['latitude'][:, 0].values
lat = remove_lat_dups(lat)
soil_moisture = first_ds['soil_moisture'].values
soil_moisture_da = xr.DataArray(soil_moisture, coords=[lat, lon], dims=["lat", "lon"], name="soil_moisture")
surface_flag = first_ds['surface_flag'].values
surface_flag_da = xr.DataArray(surface_flag, coords=[lat, lon], dims=["lat", "lon"], name="surface_flag")
retrieval_qual_flag = first_ds['retrieval_qual_flag'].values
retrieval_qual_flag_da = \
    xr.DataArray(retrieval_qual_flag, coords=[lat, lon], dims=["lat", "lon"], name="retrieval_qual_flag")
# rebuild dataset
out_ds = xr.merge([soil_moisture_da, surface_flag_da, retrieval_qual_flag_da])
# add datestamp and add as dim
out_ds["time"] = datestamp
out_ds = out_ds.expand_dims('time').set_coords('time')
print(out_ds)
# open multi file dataset
# ds = xtools.get_mf_dataset(file_list, product)
# print(ds)

# if export_ds:
#     ds.to_netcdf(os.path.join(output_dir, "smap-L3E-09km-subset-nofilter.nc"))
#     print("smap-L3E-09km-subset-nofilter.nc complete")
#     print(ds)