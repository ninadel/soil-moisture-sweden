"""
Author: Nina del Rosario
Date: 6/2/2020
Script for reading SMAP L3 files
"""
from sentinel import SentinelImg
from datetime import datetime
import json
import os

data_path = r'..\sm_sample_files\cgls-biopar-ssm-01km_nordic'
os.listdir(data_path)

with open("dict_icos.json", "r") as f:
    dict_icos = json.load(f)

# trying to read a single image
# "C:\git\soil-moisture-sweden\sm_sample_files\cgls-biopar-ssm-01km_nordic\c_gls_SSM1km_201806010000_CEURO_S1CSAR_V1.1.1_sub.nc"
file_path = r"..\sm_sample_files\cgls-biopar-ssm-01km_nordic\c_gls_SSM1km_201806010000_CEURO_S1CSAR_V1.1.1_sub.nc"

# works when I put an overpass in
# def __init__(self, filename, mode='r', parameter='ssm', flatten=False,
#              grid=None):

image_reader = SentinelImg(file_path)
image = image_reader.read_img()
# help(image)
# print(image.lat.shape)
# print(image.lon.shape)
# print(image.data['ssm'].shape)
# for key,value in image.metadata.items():
#     print(key, value)


locations = {}
for key, value in dict_icos.items():
    locations[key] = {}
    locations[key]['lat'] = value['latitude']
    locations[key]['lon'] = value['longitude']

# print(locations)

values = image_reader.get_values(locations)

print(values)

# trying to read multiple images
#     def __init__(self, data_path, parameter='ssm', subpath_templ=[], flatten=False):
# imagegroup_reader = SentinelDs(data_path)
# imagegroup_reader.read_bulk = True

# NOTE: have to suppress subpath_templ to read files that are all in one directory
# imagegroup_reader.subpath_templ = []

# timestamps = smap_reader.tstamps_for_daterange(datetime(2018, 6, 1), datetime(2018, 6, 30))
# print(timestamps)
# sentinel_image = imagegroup_reader.read(datetime(2018, 6, 3))
# print(image.data)

# for key, values in sentinel_image.data.items():
#     print(key)
#     print(values)

