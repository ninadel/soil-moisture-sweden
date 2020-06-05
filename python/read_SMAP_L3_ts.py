import os
import numpy
import json
from smap_io import SMAPTs
from datetime import datetime

# dictionary for dataset parameters, for each reader in this dictionary, make sure the class is imported
datasets_dict = {'SMAP L3' :
    {
        'ts_dir': r'C:\Nina_PCTower_Share\PCTower_SM\SPL3SMP-smap-l3-36km_nordic_reshuffle',
        'grid_dir': r'C:\Nina_PCTower_Share\PCTower_SM\SPL3SMP-smap-l3-36km_nordic_reshuffle',
        'grid_file': 'grid.nc',
        'static_layers_dir': None,
        'reader_name': 'SMAP_L3_ts',
        'reader_class': 'SMAPTs(ts_dir)'
    }
}

# load networks_dict from external file
with open('networks_dict.json', 'r') as f:
    networks_dict = json.load(f)

print(networks_dict)

# test_station = networks_dict['FMI']['SAA111']
# print(test_station)
# print(test_station['lon'], test_station['lat'])

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

    # Degero: 19.556539 64.182029
    ts = ts_reader.read(19.556539, 64.182029)

    print(ts)
    print(ts.columns)
    ts.to_csv('..\\product_sample_data\\SPL3SMP-reshuffle.csv')


