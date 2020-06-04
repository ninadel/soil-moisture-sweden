"""
Author: Nina del Rosario
Date: 6/2/2020
File to explore reading of ASCAT 12.5 TS (H115 2019)
"""

import os
import pandas
import numpy
import json
from ascat.h_saf import H115Ts
from datetime import datetime
import sm_config as config

# H25 Metop ASCAT DR2015 SSM 12.5 km sampling
# H108 Metop ASCAT DR2015 EXT SSM 12.5 km sampling
# H109 Metop ASCAT DR2016 SSM 12.5 km sampling
# H111 Metop ASCAT DR2017 SSM time series 12.5 km sampling
# H112 Metop ASCAT DR2017 EXT SSM time series 12.5 km sampling
# H113 Metop ASCAT DT2018 SSM time series 12.5 Km sampling
# H114 Metop ASCAT DR2018 EXT time series 12.5 Km
# H115 Metop ASCAT DT2019 SSM time series 12.5 Km sampling
# H116 Metop ASCAT DR2019 EXT time series 12.5 Km

# The soil moisture product represents the water content in the upper soil layer (< 2 cm) in relative units between
# totally dry conditions (0%) and total water capacity (100%). The time series are available on a discrete global grid
# (DGG) with a spatial resolution of 25 km (grid spacing 12.5 km). The temporal sampling rate is irregular (every 1-2
# days) and depends on the latitude. Each surface soil moisture estimate has an associated noise value, indicating the
# uncertainty. The soil moisture product has not been pre-filtered, meaning that a masking of invalid measurements
# (e.g. frozen ground, snow cover) by the user is highly recommended before further processing.



for dataset, dataset_dict in config.datasets_dict.items():
    dataset_name = dataset
    print(dataset)
    # is this optional?
    static_layers_dir = dataset_dict['static_layers_dir']
    # update to 2.2?
    grid_dir = dataset_dict['grid_dir']
    # update to 2.2?
    grid_file = dataset_dict['grid_file']

    ts_dir = dataset_dict['ts_dir']


    ts_reader = H115Ts
    ts_reader = eval(dataset_dict['reader_class'])

    # Degero: 19.556539 64.182029
    ts = ts_reader.read(19.556539, 64.182029)

    print(ts)
    print(ts.data.columns)
    print('ts.data', ts.data.shape)
    print(ts.data['ssf'])
    ts.data.to_csv('..\\product_sample_data\\H115_sample.csv')
    # print(ts.data['sm'])
    # help(ts)

