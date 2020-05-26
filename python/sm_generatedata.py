"""
Author: Nina del Rosario
Date: 5/25/2020
Script for generating data
"""
import ismn
import pandas
import pytesmo
import smap_io
import datetime
import json
from ascat import H113Ts

dataloc_dict = {
    'ASCAT Ts 2015': None,
    'ASCAT Ts 2016': None,
    'ASCAT Ts 2017': None,
    'ASCAT Ts 2018': None,
    'GLDAS': None,
    'Sentinel-1': None,
    'SMAP L3': None
                }
datareader_dict = {}

datareader_dict['ASCAT Ts 2018'] = 'H113Ts'
print(datareader_dict)

years = ['2015', '2016', '2017', '2018']

dataloc_dict['SMAP L3'] = r"C:\git\soil-moisture-sweden\sm_sample_files\SPL3SMP-smap-l3-36km"

# eval object example
# ts_reader2 = eval('H113Ts(ascat_2018ts_dir, grid_dir, grid_filename=grid_file, static_layer_path=static_layers_dir)')
# print(type(ts_reader2))

# print(dataloc_dict)


