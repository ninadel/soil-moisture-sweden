"""
Author: Nina del Rosario
Date: 6/2/2020
Script for reading SMAP L3 files
"""
from sentinel import SentinelImg, SentinelDs
from datetime import datetime
import os

data_path = r'..\sm_sample_files\cgls-biopar-ssm-01km_nordic'
os.listdir(data_path)

# trying to read a single image
# "C:\git\soil-moisture-sweden\sm_sample_files\cgls-biopar-ssm-01km_nordic\c_gls_SSM1km_201806010000_CEURO_S1CSAR_V1.1.1_sub.nc"
file_path = r"..\sm_sample_files\cgls-biopar-ssm-01km_nordic\c_gls_SSM1km_201806010000_CEURO_S1CSAR_V1.1.1_sub.nc"

# works when I put an overpass in
# def __init__(self, filename, mode='r', parameter='ssm', flatten=False,
#              grid=None):

image_reader = SentinelImg(file_path)
# print(image_reader.keys())

# trying to read multiple images
#     def __init__(self, data_path, parameter='ssm', subpath_templ=[], flatten=False):
imagegroup_reader = SentinelDs(data_path)
imagegroup_reader.read_bulk = True

# NOTE: have to suppress subpath_templ to read files that are all in one directory
imagegroup_reader.subpath_templ = []

# timestamps = smap_reader.tstamps_for_daterange(datetime(2018, 6, 1), datetime(2018, 6, 30))
# print(timestamps)
sentinel_image = imagegroup_reader.read(datetime(2018, 6, 3))
# print(image.data)

for key, values in sentinel_image.data.items():
    print(key)
    print(values)

