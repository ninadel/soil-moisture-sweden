"""
Author: Nina del Rosario
Date: 6/2/2020
Script to explore reading CCI files
"""
from esa_cci_sm.interface import CCI_SM_025Img, CCI_SM_025Ds
from datetime import datetime
import os

data_path = r'..\sm_sample_files\cci-0.25deg_global'
os.listdir(data_path)
sm_field = 'sm'

# trying to read a single image
# def __init__(self, filename, mode='r', parameter=None, subgrid=None,
#                  array_1D=False)
file_path = os.path.join(data_path, 'ESACCI-SOILMOISTURE-L3S-SSMV-COMBINED-20180601000000-fv04.7.nc')
image_reader = CCI_SM_025Img(file_path)

# print(image_reader.keys())
image1 = image_reader.read()
print(image1.data[sm_field].shape)

# trying to read multiple images
# def __init__(self, data_path, parameter=None, subgrid=None, array_1D=False):
imagegroup_reader = CCI_SM_025Ds(data_path, parameter=[sm_field])
imagegroup_reader.read_bulk = True

# NOTE: have to suppress subpath_templ to read files that are all in one directory
imagegroup_reader.subpath_templ = []

image2 = imagegroup_reader.read(datetime(2018, 6, 3))
print(image2.data)
print(image2.data[sm_field].shape)