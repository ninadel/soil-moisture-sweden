import datetime
import os
import pandas
import re
import sm_config as config
import sm_tools as tools
from netCDF4 import Dataset


write_ts_to_file = True
product = "SMOS-BEC"
input_dir = config.dict_product_inputs[product]['raw_dir']
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
    station_ts[location]["data"] = tools.get_series(input_dir, lon_loc=lon, lat_loc=lat, parameters=[sm_key, qf_key],
                                                    date_search_str=r"[0-9]{8}T[0-9]{4}",
                                                    datetime_format=((0, 4), (4, 6), (6, 8), (9, 11), (11, 13)))
    print(station_ts[location]["data"].head())
    station_ts[location]["data"].to_csv(os.path.join(output_dir, station_ts[location]["filename"]), sep=",")


# test = tools.get_series(input_dir, test_lon, test_lat, [sm_key, qf_key], r"[0-9]{8}T[0-9]{4}",
#                         ((0,4), (4, 6), (6, 8), (9, 11), (11, 13)))

#     data_dict = image.get_values(locations)
#     for key, value in data_dict.items():
#         if key == "metadata":
#             metadata = value
#             sm_fill_value = metadata[sm_key]['_FillValue']
#         else:
#             location = key
#             data = value['data']
#             sm_value = data[sm_key]
#             quality_flag = data['quality_flag']
#             # print("quality_flag:", quality_flag)
#             # only add valid values (invalid values were set to fill value by image reader class)
#             if sm_value != sm_fill_value and quality_flag in [0, 1]:
#                 loc_df = station_ts[location]['data']
#                 # if timestamp defaults to midnight, shift time to UTC of local overpass time
#                 obs_timestamp = timestamp
#                 obs_df = pandas.DataFrame([[obs_timestamp, sm_value]], columns=['timestamp', 'sm'])
#                 station_ts[location]['data'] = pandas.concat([loc_df, obs_df])
#
# for location, metadata in station_ts.items():
#     filename = metadata['filename']
#     df = metadata['data']
#     df.set_index('timestamp', drop=True)
#     tools.write_log(os.path.join(output_dir, "results_log_{}.txt".format(export_timestamp)),
#                     "{}: {} rows".format(filename, df.shape[0]))
#     if write_ts_to_file:
#         df.to_csv(os.path.join(output_dir, filename), index=False)