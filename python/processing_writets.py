"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/15/2020
Script that takes a set of NC files and writes TS text files for a set of defined locations
"""

import json

# dictionary which stores static fields (e.g. lat, lon, sm field)
with open("dict_product_fields.json", "r") as f:
    dict_product_fields = json.load(f)


def writets_tofile(input_dir, output_dir, product, resolution, parameters):
     pass
# for each file
    # for each location to find
        # determine filename: Descriptor_Resolution_Lat_Lon_TS.csv
        # if file does not exist for location
            # create a text file for filename
            # write column names: date, variable-1... variable-n
        # get date from filename or file
        # append to data string
        # for each variable
            # find value
            # append to data string
        # write data to filename