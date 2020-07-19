"""
Author: Nina del Rosario
Date: 7/18/2020
Script for exporting station ts with xarray

Need to do:
ERA5, SMPL3E, ASCAT H115
"""
import os
import sm_tools as tools
import sm_config as config
import xarray as xr

output_root = r"..\test_output_data\station_csv"

icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
# use this as a parameter below if you want to analyze both ICOS and ISMN
station_list = icos_readers + ismn_readers

product = "SMAP L3 Enhanced"
output_dir = os.path.join(output_root, product)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

f = r"..\input_data\xr\smap-L3E-09km-subset-nofilter.nc"
ds = xr.open_dataset(f)

print(ds)
print(ds.x)
print(ds)

for station in station_list:
    station_name = station.station
    print(station_name)
    ts = ds['swvl1'].sel(latitude=station.latitude, longitude=station.longitude, method='nearest')
    ts_filename = tools.get_station_ts_filename(station)
    ts_file = os.path.join(output_dir, ts_filename)
    ts_pandas = ts.to_pandas()
    ts_pandas.rename('swvl1', inplace=True)
    ts_pandas.to_csv(ts_file)
    break