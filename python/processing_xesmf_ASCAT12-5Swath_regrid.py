"""
Author: Nina del Rosario
Date: 6/30/2020
Script for regridding ASCAT 12.5 Swath data
"""

import xarray as xr
import xesmf as xe
import sm_config as config

# method options: 'nearest_s2d', 'bilinear', and 'conservative' (conservative not currently working)
method = 'nearest_s2d'
# method = 'bilinear'
# method = 'conservative'

f = r"../input_data/ASCATSwath/W_XX-EUMETSAT-Darmstadt,SURFACE+SATELLITE,METOPA+ASCAT_C_EUMP_20180101071800_58129_eps_o_125_ssm_l2.nc"
ds_in = xr.open_dataset(f, decode_times=False)

# print summaries
print('ds_in summary')
print(ds_in.dims)
print(ds_in.coords)
print(ds_in.data_vars)

# select array for variable to be regridded and mask out invalid values
print('dr_in')
dr_in = ds_in['soil_moisture'].where((ds_in['soil_moisture'] >= 0) & (ds_in['soil_moisture']<100))
print(dr_in.values)

# create shell for output grid
if method == 'nearest_s2d' or method == 'bilinear':
    ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                         'lon': (['lon'], config.regrid_lon)})
elif method == 'conservative':
    ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                         'lon': (['lon'], config.regrid_lon),
                         'lat_b': (['lat_b'], config.regrid_lat_b),
                         'lon_b': (['lon_b'], config.regrid_lon_b)
                         })

# create regridder object
reg = xe.Regridder(ds_in, ds_out, method)

# regrid soil moisture
dr_out = reg(dr_in)

print('dr_out')
print(dr_out.values)