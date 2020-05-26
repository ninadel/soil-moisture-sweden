import os
import numpy
import json
from gldas.interface import GLDASTs
from datetime import datetime

# load station_dict from external file
with open('station_dict.json', 'r') as f:
    station_dict = json.load(f)

print(station_dict)

test_station = station_dict['FMI']['SAA111']
print(test_station)
print(test_station['lon'], test_station['lat'])

# is this optional?
static_layer_path = None
grid_dir = r'C:\git\soil-moisture-sweden\gldas_ts_aux'
grid_file = 'grid.nc'

ts_dir = r'C:\git\soil-moisture-sweden\test_output_data\test_gldas_reshuffle'
ts_reader = ds = GLDASTs(ts_dir)

ts = ts_reader.read(test_station['lon'], test_station['lat'])

print('hello')
print(ts)

