"""
Author: Nina del Rosario
Date: 6/28/2020
Script for interpolating H115 data to 0.25 and exporting TS
"""
import matplotlib.pyplot as plt
import numpy
import pandas
import os
from scipy.interpolate import griddata
import sm_config as config

input_dir = r"..\input_data\ascat_h115_points_csv\date_data"
output_dir = r"..\test_output_data\h115_interp_ts"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

#
def get_interp_values(zi, loc_dict):
    result_dict = loc_dict.copy()
    for loc, metadata in result_dict.items():
        lat_idx = metadata["lat_idx"]
        lon_idx = metadata["lon_idx"]
        metadata["value"] = zi[lat_idx, lon_idx]
    return result_dict

# function which opens date csv of available point data, extracts lon, lat, and sm, then generates interpolation data
def get_interp_arrays(date_csv, interp_lat, interp_lon):
    data = pandas.read_csv(date_csv)
    x = data['lon'].to_numpy()
    y = data['lat'].to_numpy()
    z = data['sm'].to_numpy()
    xi, yi = numpy.meshgrid(interp_lon, interp_lat)
    zi = griddata((x, y), z, (xi, yi), method='nearest')
    return xi, yi, zi

def get_idx_dict(loc_dict, lat_array, lon_array):
    idx_dict = loc_dict.copy()
    for key, value in idx_dict.items():
        lat = value["latitude"]
        lat_idx = (numpy.abs(lat_array - lat)).argmin()
        value["lat_idx"] = lat_idx
        value["near_lat"] = lat_array[lat_idx]
        lon = value["longitude"]
        lon_idx = (numpy.abs(lon_array - lon)).argmin()
        value["lon_idx"] = lon_idx
        value["near_lon"] = lon_array[lon_idx]
        # value["lon_idx"] = numpy.asscalar(numpy.where(lon_array == lon)[0])
    return idx_dict

# Create a file and write header for each interpolation TS at 0.25 deg
for loc, metadata in config.dict_swe_gldas_points.items():
    filename = "{}.csv".format(loc)
    file = os.path.join(output_dir, filename)
    if not os.path.exists(file):
        with open(file, "a") as file:
            file.write("date,sm" + "\n")

file_list = [os.path.join(input_dir, date_file) for date_file in os.listdir(input_dir)]
# dictionary of locations to match interpolation data to
interp_point_dict = get_idx_dict(config.dict_swe_gldas_points, config.interp_lat, config.interp_lon)

# test file
file = file_list[0]
xi, yi, zi = get_interp_arrays(file, interp_lat=config.interp_lat, interp_lon=config.interp_lon)
plt.pcolormesh(xi,yi,zi)
plt.savefig(os.path.join(output_dir, "test_ascat_scipyinterpgriddata.png"), dpi=150)
plt.show()