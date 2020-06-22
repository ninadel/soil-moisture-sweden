import datetime
import os
import pandas
import re
import sm_config as config
import sm_tools as tools
from netCDF4 import Dataset


write_ts_to_file = True
product = "SMOS-BEC"
# input_dir = config.dict_product_inputs[product]['raw_dir']
input_dir = r"C:\git\soil-moisture-sweden\sm_sample_files\smos-bec-01km_global\ASC"
output_dir = config.dict_product_inputs[product]['ts_dir']
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
file_list = os.listdir(input_dir)
file_list.sort()
export_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
sm_key = config.dict_product_fields[product]['sm_field']
qf_key = 'quality_flag'
time_key = 'time'
product_lon = config.dict_product_fields[product]['lon_field']
product_lat = config.dict_product_fields[product]['lat_field']

ref_locations = {}
icos_stations = config.dict_icos
hobe_stations = config.dict_hobe
ref_locations.update(config.dict_icos)
ref_locations.update(config.dict_hobe)

# TEST: SM value range
# for filename in os.listdir(input_dir):
#     file = os.path.join(input_dir, filename)
#     counts = tools.get_nc_parameter_count(file, sm_key)
#     print(counts.shape)

# dict to store station ts dataframes
station_ts = {}
# dict used for get_values function
ref_locations_len = len(list(ref_locations.keys()))
location_idx = 0
for location, metadata in ref_locations.items():
    location_idx += 1
    print("*** processing location {} of {} ***".format(location_idx, ref_locations_len))
    network = metadata["network"]
    station = metadata["station"]
    lon = metadata['longitude']
    lat = metadata['latitude']
    station_ts[location] = {}
    station_ts[location]["filename"] = tools.get_station_ts_filename(station_object=None, station_name=station,
                                                                     network_name=network)
    print(station_ts[location]["filename"])
    station_ts[location]["data"] = tools.get_nc_series(input_dir, lon_loc=lon, lat_loc=lat, parameters=[sm_key, qf_key],
                                                       date_search_str=r"[0-9]{8}T[0-9]{4}",
                                                       datetime_format=((0, 4), (4, 6), (6, 8), (9, 11), (11, 13)))
    print(station_ts[location]["data"].head())
    station_ts[location]["data"].to_csv(os.path.join(output_dir, station_ts[location]["filename"]), sep=",")