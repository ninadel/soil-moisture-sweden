"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/15/2020
Script that takes a reshuffle TS and writes them to text files for a set of defined locations
"""

import json
import sm_tools as tools
import os

# dictionary which stores static fields (e.g. lat, lon, sm field)
with open("dict_product_fields.json", "r") as f:
    dict_product_fields = json.load(f)

# dictionary which stores GLDAS points for Sweden
with open("dict_swe_gldas_points.json", "r") as f:
    dict_swe_gldas_points = json.load(f)

output_dir = r"..\SWE_ts_csv\CCI-Active_0-25"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# for gpi, coordinate in dict_swe_gldas_points.items():
#     print(gpi, coordinate)

tools.write_grid_shuffle_ts('CCI Active', output_dir, dict_swe_gldas_points, filter_prod=False, anomaly=False)
tools.write_grid_shuffle_ts('CCI Active', output_dir, dict_swe_gldas_points, filter_prod=True, anomaly=True)