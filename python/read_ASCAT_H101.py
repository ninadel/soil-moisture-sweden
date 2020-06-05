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
print(os.listdir(data_path))