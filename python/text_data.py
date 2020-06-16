"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/16/2020
Classes to handle csv TS data
"""
import pandas


class TextDataTs(object):
    def __init__(self, filename):
        file_parts = filename.split(_)
        # product_gpi_lat_lon_res.csv
        self.product = file_parts[0]
        self.gpi = file_parts[1]
        self.lat = file_parts[2]
        self.lon = file_parts[3]
        self.resolution = file_parts[4]
        self.data = pandas.read_csv(filename, sep=",")
    def filter_data(self, filter_dict):
        pass

