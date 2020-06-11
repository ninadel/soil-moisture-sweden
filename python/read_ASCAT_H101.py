"""
Author: Nina del Rosario
Date: 6/2/2020
Script for exploring reading of ASCAT 12.5 H101 product
"""

from ascat.h_saf import H101img
from datetime import datetime
import os

# get timestamps
data_path = r'/media/ninadel/TOSHIBA EXT/sample_rs_files/ascat-12.5-km-bufr'
# print(os.listdir(data_path))

h101_reader = H101img(data_path)

h101_reader.read(datetime(2018,6,10))
#
# for h101_data, metadata, timestamp, lons, lats, time_var in h101_reader.daily_images():
#
#     # this tells you the exact timestamp of the read image
#     print(timestamp.isoformat())
#     print(type(h101_data))
#
#     # the data is a dictionary, each dictionary key contains the array of one variable
#     print("The following variables are in this image", h101_data.keys())
#     print(h101_data['ssm'].shape)
#     print(lons.shape)
#     print(lats.shape)