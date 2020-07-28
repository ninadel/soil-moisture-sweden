"""
Author: Nina del Rosario
Date: 6/27/2020
Script for exporting CSV files of TS within a bounding box around Sweden
"""

# import netCDF4
import datetime
import warnings
import xarray as xr
try:
    import xesmf as xe
except:
    warnings.warn("could not import xesmf. not windows compatible.")
# import matplotlib
import numpy
import os
import sm_config as config
# import sm_tools as tools

f = r"../input_data/ERA5-Land/0-1_ERA5-Land_hourly.nc"
ds = xr.open_dataset(f)
output_dir = r"../era5_ts"

# print(ds.dims)
# print(ds.coords)
# print(ds.data_vars)

test_lat = config.dict_icos["SE-Deg"]["latitude"]
test_lon = config.dict_icos["SE-Deg"]["longitude"]

# print(ds['latitude'].values)
# print(ds['longitude'].values)
# print(ds['time'].values)
# print(type(ds['time'].values))
ds = ds.rename({'latitude': 'lat', 'longitude': 'lon'})
dr = ds['swvl1']

# {
#     "min_lat": 55.375,
#     "max_lat": 68.875,
#     "min_lon": 11.375,
#     "max_lon": 24.125
# }
# time_series = ds['swvl1'].sel(time=slice('2015-04-01T06:00:00', '2018-12-31T06:00:00'), latitude=test_lat, longitude=test_lon)
ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                     'lon': (['lon'], config.regrid_lon),
                     'time': (['time'], ds['time'].values)
                    })

reg = xe.Regridder(ds, ds_out, 'nearest_s2d')
dr_out = reg(dr)
# print(dr_out[:])
print(dr)
print(dr_out)
print(len(config.regrid_lat))
print(len(config.regrid_lon))

for location, metadata in config.dict_swe_gldas_points.items():
    print(location)
    try:
        ts = dr_out.sel(lat=metadata['latitude'], lon=metadata['longitude'])
        ts_df = ts.to_pandas()
        ts_df.rename('sm', inplace=True)
        outfile = os.path.join(output_dir, "{}.csv".format(location))
        ts_df.to_csv(outfile)
        with open(os.path.join(output_dir, "logfile.txt"), "a") as file:
            file.write("{} ok".format(location) + "\n")
    except:
        with open(os.path.join(output_dir, "logfile.txt"), "a") as file:
            file.write("{} failed".format(location) + "\n")

# regridder.clean_weight_file()  # clean-up

