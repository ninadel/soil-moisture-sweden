"""
Author: Nina del Rosario
Date: 7/23/2020
Writing dictionary of HOBE station locations
"""
import json
import sm_config as config
import sm_tools as tools

HOBE_dict = {}

ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
print(ismn_readers)
print(len(ismn_readers))
# "SE-Htm": {
#     "station": "Hyltemossa",
#     "latitude": 56.097581,
#     "longitude": 13.419064,
#     "elevation": 115
# },

for station in ismn_readers:
    key = "HOBE {}".format(station.station)
    HOBE_dict[key] = {}
    HOBE_dict[key]['station'] = station.station
    HOBE_dict[key]['network'] = "HOBE"
    HOBE_dict[key]['latitude'] = station.latitude
    HOBE_dict[key]['longitude'] = station.longitude
    HOBE_dict[key]['elevation'] = station.elevation

print(HOBE_dict)

with open('dict_hobe.json', 'w') as f:
    json.dump(HOBE_dict, f)

# for station in ismn_readers:
#     print(tools.get_station_ts_filename(station))