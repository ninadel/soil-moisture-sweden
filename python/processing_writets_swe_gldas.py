"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/15/2020
Script that takes a reshuffle TS and writes them to text files for a set of defined locations
UPDATE_DESCRIPTION
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

output_dir = r"..\SWE_ts_csv\GLDAS_0-25"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# for gpi, coordinate in dict_swe_gldas_points.items():
#     print(gpi, coordinate)
# counter = 0
# group = 0
# group_dict = {}
# group_dict['0'] = {}
#
# for location, coordinate in dict_swe_gldas_points.items():
#     group_dict[str(group)][location] = coordinate
#     counter += 1
#     if counter == 20:
#         counter = 0
#         group += 1
#         group_dict[str(group)] = {}

# print(len(group_dict))
#
# for group, loc_dict in group_dict.items():
tools.write_grid_shuffle_ts('GLDAS', output_dir, dict_swe_gldas_points, filter_prod=True, anomaly=False)
tools.write_grid_shuffle_ts('GLDAS', output_dir, dict_swe_gldas_points, filter_prod=True, anomaly=True)

# tools.write_grid_shuffle_ts('GLDAS', output_dir, dict_swe_gldas_points, filter_prod=True, anomaly=False)