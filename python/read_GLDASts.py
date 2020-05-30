import os
import numpy
import json
from gldas.interface import GLDASTs
from datetime import datetime

# dictionary for dataset parameters, for each reader in this dictionary, make sure the class is imported
datasets_dict = {'GLDAS' :
    {
        'ts_dir': r'..\test_output_data\test_gldas_reshuffle',
        'grid_dir': r'..\test_output_data\test_gldas_reshuffle',
        'grid_file': 'grid.nc',
        'static_layers_dir': None,
        'reader_name': 'GLDAS_ts',
        'reader_class': 'GLDASTs(ts_dir)'
    }
}

# load station_dict from external file
with open('networks_dict.json', 'r') as f:
    networks_dict = json.load(f)

print(networks_dict)

test_station = networks_dict['FMI']['SAA111']
print(test_station)
print(test_station['lon'], test_station['lat'])

for dataset, dataset_dict in datasets_dict.items():
    dataset_name = dataset
    print(dataset)
    # is this optional?
    static_layers_dir = dataset_dict['static_layers_dir']
    # update to 2.2?
    grid_dir = dataset_dict['grid_dir']
    # update to 2.2?
    grid_file = dataset_dict['grid_file']

    ts_dir = dataset_dict['ts_dir']

    ts_reader = eval(dataset_dict['reader_class'])

    ts = ts_reader.read(test_station['lon'], test_station['lat'])

    # print(ts.data.columns)
    # print(ts.data['soil_moisture'])
    print(ts)
    print(ts.columns)