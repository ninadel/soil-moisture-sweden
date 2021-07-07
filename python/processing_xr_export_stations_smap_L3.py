"""
Author: Nina del Rosario
Date: 7/18/2020
Script for exporting station ts with xarray

UPDATE_DESCRIPTION

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

product = "SMAP L3"
output_dir = os.path.join(output_root, product)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

f = r"..\input_data\xr\smap-L3-36km-subset-nofilter.nc"
ds = xr.open_dataset(f)

print(ds)

for station in station_list:
    station_name = station.station
    print(station_name)
    ts = ds.sel(lat=station.latitude, lon=station.longitude, method='nearest')
    # print(ts.values)
    ts_filename = tools.get_station_ts_filename(station)
    ts_file = os.path.join(output_dir, ts_filename)
    ts_pandas = ts.to_dataframe()
    ts_pandas.to_csv(ts_file)