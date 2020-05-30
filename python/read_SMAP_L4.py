from smap_extension import SPL4SMP_nc_Ds, SPL4SMP_nc_Img
from datetime import datetime
import os

data_path = r'..\sm_sample_files\SPL4SMAU-smap-ma-l4-09km_clipped_nc'
os.listdir(data_path)

# trying to read a single image
file_path = r"..\sm_sample_files\SPL4SMAU-smap-ma-l4-09km_clipped_nc\SMAP_L4_SM_aup_20180628T120000_Vv4030_001_HEGOUT.nc"
# image_reader = SPL3SMP_Img(file_path, overpass=None, var_overpass_str=False)

# works when I put an overpass in
# image_reader = SPL4SMP_nc_Img(file_path, overpass='AM', parameter=['soil_moisture', 'soil_moisture_error', 'surface_flag'])
image_reader = SPL4SMP_nc_Img(file_path)
# print(image_reader.keys())
image = image_reader.read()
# image.data['soil_moisture'].shape

# trying to read multiple images
# smap_reader = SPL3SMP_Ds(data_path, overpass = 'AM')
imagegroup_reader = SPL4SMP_nc_Ds(data_path, parameter=['sm_surface_analysis', 'sm_surface_analysis_ensstd'])
imagegroup_reader.read_bulk = True

# NOTE: have to suppress subpath_templ to read files that are all in one directory
imagegroup_reader.subpath_templ = []

# timestamps = smap_reader.tstamps_for_daterange(datetime(2018, 6, 1), datetime(2018, 6, 30))
# print(timestamps)

smap_image = imagegroup_reader.read(datetime(2018,6,3))
print(smap_image.data)
# print(smap_image.data)
# print(type(smap_image))
print(smap_image.data['sm_surface_analysis'].shape)
# for key, values in smap_image.data.items():
#     print(key)
#     print(values)