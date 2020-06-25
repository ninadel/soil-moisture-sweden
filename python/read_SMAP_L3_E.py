"""
Author: Nina del Rosario
Date: 6/2/2020
Script for reading SMAP L3 files
"""
# from smap_io import SPL3SMP_Ds, SPL3SMP_Img
from smap_extension import SPL3SMP_E_H5_Img, SPL3SMP_E_H5_Ds
from datetime import datetime
import os

# "C:\git\soil-moisture-sweden\sm_sample_files\SPL3SMPE-smap-l3-enhanced-09km\SMAP_L3_SM_P_E_20180101_R16510_001_HEGOUT.h5"
data_path = r'..\sm_sample_files\SPL3SMPE-smap-l3-enhanced-09km'

# trying to read a single image
file_path = r'..\sm_sample_files\SPL3SMPE-smap-l3-enhanced-09km\SMAP_L3_SM_P_E_20180101_R16510_001_HEGOUT.h5'
# image_reader = SPL3SMP_Img(file_path, overpass=None, var_overpass_str=False)

# works when I put an overpass in
image_reader = SPL3SMP_E_H5_Img(file_path, overpass='AM', parameter=['soil_moisture', 'surface_flag'],
                                var_overpass_str=False)
# print(image_reader.keys())

# trying to read multiple images
# smap_reader = SPL3SMP_Ds(data_path, overpass = 'AM')
imagegroup_reader = SPL3SMP_E_H5_Ds(data_path, overpass='AM', parameter=['soil_moisture', 'surface_flag'],
                                    var_overpass_str=False)
imagegroup_reader.read_bulk = True

# NOTE: have to suppress subpath_templ to read files that are all in one directory
imagegroup_reader.subpath_templ = []

smap_image = imagegroup_reader.read(datetime(2018,1,4))
# print(image.data)

for key, values in smap_image.data.items():
    print(key)
    print(values)



