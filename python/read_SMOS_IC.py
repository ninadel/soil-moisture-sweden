"""
Author: Nina del Rosario
Date: 6/2/2020
Script to explore reading SMOS IC files
"""
from smos.smos_ic.interface import SMOSImg, SMOSDs
from datetime import datetime
import os

data_path = r'C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\smos-ic-l3-25km_global\ASC'
os.listdir(data_path)

# trying to read a single image
# def __init__(self, filename, mode='r', parameters='Soil_Moisture', flatten=False, grid=None, read_flags=(0,1))
file_path = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\smos-ic-l3-25km_global\ASC\2018\SM_RE06_MIR_CDF3SA_20180601T000000_20180601T235959_105_001_8.DBL.nc"
image_reader = SMOSImg(file_path)

print(image_reader.keys())
image = image_reader.read()

# trying to read multiple images
# def __init__(self, data_path, parameters='Soil_Moisture', flatten=False,
#                  grid=None, filename_templ=None, read_flags=(0,1)):
imagegroup_reader = SMOSDs(data_path, parameters=['Soil_Moisture'])
imagegroup_reader.read_bulk = True

print(image.data['Soil_Moisture'].shape)

smos_image = imagegroup_reader.read(datetime(2018, 6, 3))
print(smos_image.data.head())
print(smos_image.data['Soil_Moisture'].shape)