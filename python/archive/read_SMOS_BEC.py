"""
Author: Nina del Rosario
Date: 6/2/2020
Script to explore reading SMAP L4 files
"""
from smos_extension import SMOSBECImg
from datetime import datetime
import os

data_path = r'..\sm_sample_files\smos-bec-01km\ASC'
os.listdir(data_path)

file_path = r'..\sm_sample_files\smos-bec-01km\ASC\BEC_SM____SMOS__EUM_L4__A_20180601T030707_001km_1d_REP_v5.0.nc'

# trying to read a single image
# def __init__(self, filename, mode='r', parameters='SM', flatten=False,
#                  grid=None, read_flags=(0,1)):
image_reader = SMOSBECImg(file_path)
#
# image = image_reader.read()

# trying to read multiple images
# def __init__(self, data_path, parameters='SM', flatten=False,
#                  grid=None, filename_templ=None, read_flags=(0,1)):
imagegroup_reader = SMOSBECDs(data_path)
imagegroup_reader.read_bulk = True

# NOTE: have to suppress subpath_templ to read files that are all in one directory
# imagegroup_reader.subpath_templ = []

# timestamps = smap_reader.tstamps_for_daterange(datetime(2018, 6, 1), datetime(2018, 6, 30))
# print(timestamps)

# print(image.data['SM'].shape)

smos_image = imagegroup_reader.read(datetime(2018, 6, 3))
print(smos_image.data.head())
print(smos_image.data['SM'].shape)