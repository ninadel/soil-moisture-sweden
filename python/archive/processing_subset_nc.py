import json
import netCDF4
import numpy
import os
import datetime
from pytesmo.timedate import julian

with open("dict_extent_sweden.json", "r") as f:
    dict_extent_sweden = json.load(f)

with open("dict_extent_nordic.json", "r") as f:
    dict_extent_nordic = json.load(f)

# dictionary which stores static fields (e.g. lat, lon, sm field)
with open("dict_product_fields.json", "r") as f:
    dict_product_fields = json.load(f)

input_dir = r"..\sm_sample_files\cgls-biopar-ssm-01km"
output_dir = r"..\test_output_data\gldas_subset"
product_name = "GLDAS"

product_metadata = dict_product_fields[product_name]
lat_field = product_metadata['lat_field']
lon_field = product_metadata['lon_field']
time_field = product_metadata['time_field']
# metadata fields that don't need to be subset
meta_variables = ['time', 'time_bnds']
# fields that need to be subset based on lat/lon dimensions
subset_variables = [product_metadata['sm_field']]

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

extent_buffer = 2.5
subset_min_lat = dict_extent_nordic['min_lat'] - extent_buffer
subset_max_lat = dict_extent_nordic['max_lat'] + extent_buffer
subset_min_lon = dict_extent_nordic['min_lon'] - extent_buffer
subset_max_lon = dict_extent_nordic['max_lon'] + extent_buffer

for file in os.listdir(input_dir):
    file_extension_index = file.rfind(".")
    dst_filename = file[:file_extension_index] + "_sub" + file[file_extension_index:]
    with netCDF4.Dataset(os.path.join(input_dir, file)) as src, netCDF4.Dataset(os.path.join(output_dir, dst_filename),
                                                                                "w") as dst:
        dst.setncatts(src.__dict__)
        # copy time dimensions and data
        for name, dimension in src.dimensions.items():
            if name == lat_field:
                lats = src[lat_field][:]
                # latitude lower and upper index based on defined bounds
                latli = numpy.argmin(numpy.abs(lats - subset_min_lat))
                latui = numpy.argmin(numpy.abs(lats - subset_max_lat))
                lat_subset = src[lat_field][latli:latui]
                dst.createDimension(lat_field, lat_subset.size)
            elif name == lon_field:
                lons = src[lon_field][:]
                # longitude lower and upper index based on defined bounds
                lonli = numpy.argmin(numpy.abs(lons - subset_min_lon))
                lonui = numpy.argmin(numpy.abs(lons - subset_max_lon))
                # subset lat and lon subsets
                lon_subset = src[lon_field][lonli:lonui]
                # based on subset sizes, create lat and lon dimensions
                dst.createDimension(lon_field, lon_subset.size)
            else:
                dst.createDimension(name, (len(dimension) if not dimension.isunlimited() else None))
        # create lat variable
        dst.createVariable(lat_field, src[lat_field].datatype, lat_field)
        dst[lat_field].setncatts(src[lat_field].__dict__)
        dst[lat_field][:] = lat_subset
        # create lon variable
        dst.createVariable(lon_field, src[lon_field].datatype, lon_field)
        dst[lon_field].setncatts(src[lon_field].__dict__)
        dst[lon_field][:] = lon_subset
        for variable in meta_variables:
            dst.createVariable(variable, src[variable].datatype, src[variable].dimensions)
            dst[variable][:] = src[variable][:]
            # copy variable attributes all at once via dictionary
            dst[variable].setncatts(src[variable].__dict__)
        for variable in subset_variables:
            print(variable)
            src_var_attributes = src[variable].__dict__
            dst_var_attributes = {}
            for key, value in src_var_attributes.items():
                if key == "_FillValue":
                    continue
                else:
                    dst_var_attributes[key] = value
            dst.createVariable(variable, src[variable].datatype, (time_field, lat_field, lon_field),
                               fill_value=src_var_attributes['_FillValue'])
            dst[variable][:] = src[variable][:, latli:latui, lonli:lonui]
            dst[variable].setncatts(dst_var_attributes)
    break

# import netCDF4 as nc
# toexclude = ['ExcludeVar1', 'ExcludeVar2']
#
# with netCDF4.Dataset("in.nc") as src, netCDF4.Dataset("out.nc", "w") as dst:
#     # copy global attributes all at once via dictionary
#     dst.setncatts(src.__dict__)
#     # copy dimensions
#     for name, dimension in src.dimensions.items():
#         dst.createDimension(
#             name, (len(dimension) if not dimension.isunlimited() else None))
#     # copy all file data except for the excluded
#     for name, variable in src.variables.items():
#         if name not in toexclude:
#             x = dst.createVariable(name, variable.datatype, variable.dimensions)
#             dst[name][:] = src[name][:]
#             # copy variable attributes all at once via dictionary
#             dst[name].setncatts(src[name].__dict__)
