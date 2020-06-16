"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/16/2020
Classes to handle netCDF TS data and files
"""
import json
import netCDF4
import sm_tools as tools

class NCTimeSeries(object):
    def __init__(self, input_dir, product):
        self.input_dir = input_dir
        self.product = product
    pass


class NCFile(object):
    def __init__(self, input_file, product):
        self.input_file = input_file
        self.product = product
        with open("dict_product_fields.json", "r") as f:
            dict_product_fields = json.load(f)
        self.lat_field = dict_product_fields[product]['lat_field']
        self.lon_field = dict_product_fields[product]['lon_field']
        self.time_field = dict_product_fields[product]['time_field']
        self.sm_field = dict_product_fields['sm_field']
        self.dataset = netCDF4.Dataset(self.inpput_file, 'r')

    def get_summary(self, show_field_data=True, other_fields=None, output_file=None):
        if output_file is not None:
            write_output = True
        tools.write_log(output_file, "Attributes in dataset:")
        tools.write_log(output_file, self.dataset.ncattrs())
        tools.write_log(output_file, "\nDimensions in dataset:")
        for dimension in self.dataset.dimensions.items():
            tools.write_log(output_file, dimension)
        tools.write_log(output_file, "\nVariables in dataset:")
        for variable in self.dataset.variables.items():
            tools.write_log(output_file, variable)
        tools.write_log(output_file, "\nLongitude field:")
        tools.write_log(output_file, "shape:", self.dataset[self.lon_field][:].shape)
        if show_field_data:
            tools.write_log(output_file, self.dataset[self.lon_field][:])
        tools.write_log(output_file, "\nLatitude field:")
        tools.write_log(output_file, "shape:", self.dataset[self.lat_field][:].shape)
        if show_field_data:
            tools.write_log(output_file, self.dataset[self.lat_field][:])
        tools.write_log(output_file, "\nSM field:")
        tools.write_log(output_file, self.dataset[self.sm_field][:].shape)
        if show_field_data:
            tools.write_log(output_file, self.dataset[self.sm_field][:])
        tools.write_log(output_file, "\nTime field:")
        tools.write_log(output_file, "shape:", self.dataset[self.time_field][:].shape)
        if show_field_data:
            tools.write_log(output_file, self.dataset[self.time_field][:])

