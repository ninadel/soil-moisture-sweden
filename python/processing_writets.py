"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/15/2020
Script that takes a set of NC files and writes TS text files for a set of defined locations
"""

import json
# import sm_tools as tools

# dictionary which stores static fields (e.g. lat, lon, sm field)
with open("dict_product_fields.json", "r") as f:
    dict_product_fields = json.load(f)

# dictionary which stores GLDAS points for Sweden
with open("dict_swe_gldas_points.json", "r") as f:
    dict_swe_gldas_points = json.load(f)

output_dir = r"..\SWE_ts_csv\GLDAS_0-25"

# for gpi, coordinate in dict_swe_gldas_points.items():
#     print(gpi, coordinate)

write_grid_shuffle_ts('GLDAS', output_dir, dict_swe_gldas_points, filter_prod=True, anomaly=False)