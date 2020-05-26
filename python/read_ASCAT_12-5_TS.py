import os
import numpy
import json
from ascat.h_saf import H25Ts, H109Ts, H111Ts, H113Ts
from datetime import datetime

# H25 Metop ASCAT DR2015 SSM 12.5 km sampling
# H108 Metop ASCAT DR2015 EXT SSM 12.5 km sampling
# H109 Metop ASCAT DR2016 SSM 12.5 km sampling
# H111 Metop ASCAT DR2017 SSM time series 12.5 km sampling
# H112 Metop ASCAT DR2017 EXT SSM time series 12.5 km sampling
# H113 Metop ASCAT DT2018 SSM time series 12.5 Km sampling
# H114 Metop ASCAT DR2018 EXT time series 12.5 Km

# The soil moisture product represents the water content in the upper soil layer (< 2 cm) in relative units between
# totally dry conditions (0%) and total water capacity (100%). The time series are available on a discrete global grid
# (DGG) with a spatial resolution of 25 km (grid spacing 12.5 km). The temporal sampling rate is irregular (every 1-2
# days) and depends on the latitude. Each surface soil moisture estimate has an associated noise value, indicating the
# uncertainty. The soil moisture product has not been pre-filtered, meaning that a masking of invalid measurements
# (e.g. frozen ground, snow cover) by the user is highly recommended before further processing.

# load station_dict from external file
with open('station_dict.json', 'r') as f:
    station_dict = json.load(f)

print(station_dict)

test_station = station_dict['FMI']['SAA111']
print(test_station)
print(test_station['lon'], test_station['lat'])

# is this optional?
static_layers_dir = r'C:\git\soil-moisture-sweden\sm_sample_files\h-saf_static_layers\static_layer'
# update to 2.2?
grid_dir = r'C:\git\soil-moisture-sweden\sm_sample_files\TUW_WARP5_grid_info_2_1'
# update to 2.2?
grid_file = 'TUW_WARP5_grid_info_2_1.nc'

ascat_2018ts_dir = r'C:\git\soil-moisture-sweden\sm_sample_files\ascat-h113-ts-2018'
ts_reader = H113Ts(ascat_2018ts_dir,
                             grid_dir,
                             grid_filename=grid_file,
                             static_layer_path=static_layers_dir)


ts = ts_reader.read(test_station['lon'], test_station['lat'])

print(ts)

