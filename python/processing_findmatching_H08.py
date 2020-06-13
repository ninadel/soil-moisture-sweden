"""
Author: Nina del Rosario
Date: 6/2/2020
Class to read ASCAT H08 (1 km sm-obs-2) product
"""

from ascat.h_saf import H08img
from datetime import datetime
import os
import numpy
import pandas

# get timestamps
data_path = r'../test_input_data'
# print(os.listdir(data_path))

output_path = r'../test_output_data'
matching_files = os.path.join(output_path, "matching_files.txt")
all_files = os.path.join(output_path, "all_files.txt")

timeframe_start = datetime(2018, 6, 1)
timeframe_end = datetime(2018, 6, 30, 23, 59)
# lat_lon_bbox: [lat_min, lat_max, lon_min, lon_max]
nordic_boundary = [54.53, 71.46, 4.25, 31.73]
icos_boundary = [56.097581, 68.356003, 13.101768, 19.774413]

dict_extent_sweden = {
    'min_lat': 55.375,
    'max_lat': 68.875,
    'min_lon': 11.375,
    'max_lon': 24.125
}

h08_reader = H08img(data_path, day_search_str = 'h08_%Y%m%d__%H%M%S*.buf')

h08_img_dict = {}

# for file in os.listdir(os.path.join(data_path, 'h08_201806_buf')):
#     year = int(file[4:8])
#     month = int(file[8:10])
#     day = int(file[10:12])
#     hour = int(file[13:15])
#     minute = int(file[15:17])
#     h08_img_dict[file] = {}
#     date_list.append(datetime(year,month,day,hour,minute))
match_count = 0

for file in os.listdir(os.path.join(data_path, 'h08_201806_buf')):
    year = int(file[4:8])
    month = int(file[8:10])
    day = int(file[10:12])
    hour = int(file[13:15])
    minute = int(file[15:17])
    dt = datetime(year, month, day, hour, minute)
    print(dt)
    try:
        image = h08_reader.read(dt)
        image_lons = numpy.array(image.lon[0,:])
        image_lats = numpy.array(image.lat[:,0])
        with open(all_files, "a") as logfile:
            logfile.write("{} {} {} {} {} {} \n".format(file, dt, image_lons.min(), image_lons.max(), image_lats.min(),
                                                        image_lats.max()))
        if (dict_extent_sweden['min_lat'] < image_lats.max() and dict_extent_sweden['min_lat'] > image_lats.min() or \
            dict_extent_sweden['max_lat'] > image_lats.min() and dict_extent_sweden['max_lat'] < image_lats.max()) and \
                (dict_extent_sweden['min_lon'] < image_lons.max() and dict_extent_sweden['min_lon'] > image_lons.min() or \
                 dict_extent_sweden['max_lon'] > image_lons.min() and dict_extent_sweden['max_lon'] < image_lons.max()):
            match_count += 1
            print(match_count)
            with open(matching_files, "a") as logfile:
                logfile.write("{} {} {} {} {} {} \n".format(file, dt, image_lons.min(), image_lons.max(),
                                                            image_lats.min(), image_lats.max()))
    except:
        print("skipping image")

print(match_count)

# for date in date_list:
#     image = h08_reader.read(date)
#     image_lons = numpy.array(image.lon[0,:])
#     image_lats = numpy.array(image.lat[:,0])
#     h08_img_dict[date]
#     print('lon_min', image_lons.min(), 'lon_max', image_lons.max(), 'lat_min', image_lats.min(), 'lat_max',
#           image_lats.max())
#


# trying to read multiple images
# h08_reader.month_path_str = ''

timestamps = []
#
# for h08_data, metadata, timestamp, lons, lats, time_var in h08_reader.daily_images(datetime(2018, 6, 1)):
# #
# #     # this tells you the exact timestamp of the read image
#     print(timestamp.isoformat())
#     timestamps.append(timestamp.isoformat)
    # print(type(h08_data))

    # the data is a dictionary, each dictionary key contains the array of one variable
    # print("The following variables are in this image", h08_data.keys())
    # print(h08_data['ssm'].shape)
    # print(lons.shape)
    # print(lats.shape)

# print(timestamps)

# h08_img = h08_reader.read(datetime(2018,6, 1, 6, 15))

# help(h08_img)

# number_list = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(less_than_zero)
#
# # Output: [-5, -4, -3, -2, -1]
# timestamp_in_timeframe = list(filter(lambda x: (x.hour > 10 and x.hour < 11) or (x.hour > 22 and x.hour < 23), timestamps))
# print(timestamp_in_timeframe)
# in_boundary_count = 0
# timestamp_count = 0
# for timestamp in timestamps:
#     print('timestamp ', timestamp)
#     timestamp_count += 1
#     print('timestamp_count ', timestamp_count)
#     h08_img = h08_reader.read(timestamp)
#     if in_boundary(icos_boundary, h08_img, buffer):
#         in_boundary_count += 1
#         print('in_boundary_count ', in_boundary_count)

# h08_img = h08_reader.read(datetime(2018, 6, 10, 6, 33))
# h08_lons = numpy.array(h08_img.lon[0,:])
# h08_lats = numpy.array(h08_img.lat[:,0])
# print(h08_lons.shape)
# print(h08_lats.shape)
# print('lon_min ', h08_lons.min())
# print('lon_max ',h08_lons.max())