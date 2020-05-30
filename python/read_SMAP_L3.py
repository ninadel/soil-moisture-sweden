from smap_io import SPL3SMP_Ds, SPL3SMP_Img
from datetime import datetime
import os

data_path = r'..\sm_sample_files\SPL3SMP-smap-l3-36km\20180601_20180630'
os.listdir(data_path)

# trying to read a single image
file_path = r'..\sm_sample_files\SPL3SMP-smap-l3-36km\20180601_20180630\SMAP_L3_SM_P_20180606_R16510_001.h5'
# image_reader = SPL3SMP_Img(file_path, overpass=None, var_overpass_str=False)

# works when I put an overpass in
image_reader = SPL3SMP_Img(file_path, overpass='AM', parameter=['soil_moisture', 'soil_moisture_error', 'surface_flag'])
# print(image_reader.keys())

# trying to read multiple images
# smap_reader = SPL3SMP_Ds(data_path, overpass = 'AM')
imagegroup_reader = SPL3SMP_Ds(data_path, overpass='AM', parameter=['soil_moisture', 'soil_moisture_error', 'surface_flag'])
imagegroup_reader.read_bulk = True

# NOTE: have to suppress subpath_templ to read files that are all in one directory
imagegroup_reader.subpath_templ = []

# timestamps = smap_reader.tstamps_for_daterange(datetime(2018, 6, 1), datetime(2018, 6, 30))
# print(timestamps)
smap_image = imagegroup_reader.read(datetime(2018,6,3))
# print(image.data)

for key, values in smap_image.data.items():
    print(key)
    print(values)



