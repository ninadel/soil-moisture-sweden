"""
Author: Nina del Rosario
Date: 6/2/2020
Script for exploring reading GLDAS TS (generated via repurpose package)
"""

import os
import numpy
import json
from gldas.interface import GLDASTs
from datetime import datetime
import sm_config as config

# load station_dict from external file
ts_reader = GLDASTs(config.datasets_dict['GLDAS']['ts_dir'])

# Degero: 19.556539 64.182029
ts = ts_reader.read(19.556539, 64.182029)

# print(ts.data.columns)
# print(ts.data['soil_moisture'])
print(ts)
print(ts.columns)