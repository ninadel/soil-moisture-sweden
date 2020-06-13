"""
Author: Nina del Rosario
Date: 6/2/2020
Class to read ASCAT H08 (1 km sm-obs-2) product
"""

from ascat.h_saf import H08img
from datetime import datetime
import os
import numpy
import pandas

# get timestamps
data_path = r'../test_input_data'
output_path = r'../test_output_data'
# print(os.listdir(data_path))

timeframe_start = datetime(2018, 6, 1)
timeframe_end = datetime(2018, 6, 30, 23, 59)
# lat_lon_bbox: [lat_min, lat_max, lon_min, lon_max]
nordic_boundary = [54.53, 71.46, 4.25, 31.73]
icos_boundary = [56.097581, 68.356003, 13.101768, 19.774413]

extent_sweden = {
    'min_lat': 55.375,
    'max_lat': 68.875,
    'min_lon': 11.375,
    'max_lon': 24.125
}

h08_reader = H08img(data_path, day_search_str = 'h08_%Y%m%d__%H%M%S*.buf')

image = h08_reader.read(datetime(2018,6,1,6,15))


