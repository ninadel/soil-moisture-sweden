from ascat.h_saf import H08img
from datetime import datetime
import os
import numpy

# get timestamps
data_path = r'/media/ninadel/TOSHIBA EXT/sample_rs_files/hsaf-smobs2-01km'
# print(os.listdir(data_path))

timeframe_start = datetime(2018, 6, 1)
timeframe_end = datetime(2018, 6, 30, 23, 59)
# lat_lon_bbox: [lat_min, lat_max, lon_min, lon_max]
nordic_boundary = [54.53, 71.46, 4.25, 31.73]
icos_boundary = [56.097581, 68.356003, 13.101768, 19.774413]
test_station_lon = 19.556539
test_station_lat = 64.182029
buffer = 0.00416667

def in_boundary(boundary_box, image, buffer):
    box_lat_min = boundary_box[0]
    box_lat_max = boundary_box[1]
    box_lon_min = boundary_box[2]
    box_lon_max = boundary_box[3]
    image_lons = numpy.array(image.lon[0,:])
    image_lats = numpy.array(image.lat[:,0])
    return (((box_lon_min > image_lons.min() and box_lon_min < image_lons.max()) or (box_lon_max > image_lons.min() and box_lon_max < image_lons.max())) and ((box_lat_min > image_lats.min() and box_lat_min < image_lats.max()) or (box_lat_max > image_lats.min() and box_lat_max < image_lats.max())))

# trying to read multiple images
h08_reader = H08img(data_path, month_path_str = '', )
timestamps = h08_reader.tstamps_for_daterange(datetime(2018, 6, 1, 9, 30), datetime(2018, 6, 1, 11, 30))
print(timestamps)
print(len(timestamps))

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

# h08_img = h08_reader.read(datetime(2018, 6, 2, 18, 54))
# h08_lons = numpy.array(h08_img.lon[0,:])
# h08_lats = numpy.array(h08_img.lat[:,0]).T
# print(h08_lons.shape)
# print(h08_lats.shape)
# print('lon_min ', h08_lons.min())
# print('lon_max ',h08_lons.max())