"""
Author: Nina del Rosario
Date: 7/23/2020
Script for reading date csv data and splitting it into AM overpasses
"""
import datetime
import os
import pandas as pd
import math
import statistics


# function to convert time in datestamp to a decimal number
def get_time_value(row):
    time_value = row['datestamp'].hour + row['datestamp'].minute / 60
    return time_value


# function which takes current overpass dictionary and returns matching overpass, or None if time is not near any overpass
def get_overpass(dict, time_value):
    nearest_overpass = None
    min_time_diff = 9999
    match_threshold = 1
    for overpass, metadata in dict.items():
        overpass_average = statistics.mean(metadata['time_values'])
        time_diff = abs(overpass_average - time_value)
        if time_diff < min_time_diff:
            min_time_diff = time_diff
            if time_diff < match_threshold:
                nearest_overpass = overpass
    return nearest_overpass


def get_overpass_groups(data):
    # dict to store overpass data
    overpass_dict = {}
    # dict to store locations and their data rows
    location_data_dict = {}
    # variable for keeping track of max number of rows for a location (indicating min number of overpasses)
    location_rows_max = 0
    # variable for keeping track of how many overpasses are in dictionary
    overpass_count = 0
    # get unique list of location ids
    locations = data['location_id'].unique()
    # build a dictionary of rows for each location in date file
    for location in locations:
        location_data = data[data['location_id'] == location]
        location_row_count = location_data.shape[0]
        if location_row_count > location_rows_max:
            location_rows_max = location_row_count
        if location_row_count not in location_data_dict.keys():
            location_data_dict[location_row_count] = {}
        location_data_dict[location_row_count][location] = location_data
    counter = location_rows_max
    while counter > 0:
        # if overpass_dict is empty, create entries for minimum number of known overpass
        overpass_dict_empty = len(overpass_dict.keys()) == 0
        if overpass_dict_empty:
            for i in range(1, counter + 1):
                overpass_dict[i] = {}
                overpass_dict[i]['data'] = None
                overpass_dict[i]['time_values'] = []
                overpass_count += 1
        # get location data matching the number of overpasses
        ungrouped_data = location_data_dict[counter]
        # iterate through each row to find matching overpass
        for location_idx, location_data in ungrouped_data.items():
            row_idx = 1
            # create dictionary to keep track of what overpasses have been used for this location
            used_overpass = {}
            for count in overpass_dict.keys():
                used_overpass[count] = False
            for iter_idx, row in location_data.iterrows():
                # variable to keep track of overpasses
                time_value = get_time_value(row)
                # row is series - convert to dataframe for concatenation
                row = row.to_frame().transpose()
                # if no existing overpasses, populate overpass_dict with starting data
                if overpass_dict[row_idx]['data'] is None:
                    overpass_dict[row_idx]['data'] = row
                    overpass_dict[row_idx]['time_values'].append(time_value)
                # if overpasses exist, try to match row to overpass
                else:
                    matching_overpass = get_overpass(overpass_dict, time_value)
                    # if a matching overpass is found and hasn't been used yet
                    if matching_overpass is not None and not used_overpass[matching_overpass]:
                        overpass_dict[matching_overpass]['data'] = \
                            pd.concat([overpass_dict[matching_overpass]['data'], row])
                        overpass_dict[matching_overpass]['time_values'].append(time_value)
                        used_overpass[matching_overpass] = True
                    # if a matching overpass is not found, create new overpass
                    else:
                        overpass_count += 1
                        overpass_dict[overpass_count] = {}
                        overpass_dict[overpass_count]['data'] = row
                        overpass_dict[overpass_count]['time_values'] = [time_value]
                row_idx += 1
        counter -= 1
    return overpass_dict


def get_mean_datestamp(time_values, base_date):
    mean_time_value = statistics.mean(time_values)
    mean_time_hour = math.floor(mean_time_value)
    mean_time_minutes = math.floor((mean_time_value - mean_time_hour) * 60)
    mean_time = short_date + datetime.timedelta(hours=mean_time_hour)
    mean_time = mean_time + datetime.timedelta(minutes=mean_time_minutes)
    return mean_time


input_dir = r"D:\sm_backup\csv\ascat_h115_points_csv\date_data"
output_dir = r"..\test_output_data\h115_overpass_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# # dict to store overpass data
# overpass_dict = {}
# # dict to store locations in date file with morning data and matching morning data
# location_data_dict = {}

# # start by assuming a date has a single AM overpasses
# max_rows = 1
# # variable for keeping track of how many overpasses are in dictionary
# overpass_count = 0

# for each date file
for input_filename in os.listdir(input_dir):
    print(input_filename)
    short_date_str = input_filename.split(".")[0]
    short_date = datetime.datetime.strptime(short_date_str, "%Y-%m-%d")
    cutoff_date = short_date + datetime.timedelta(hours=12)
    # open CSV
    input_file = os.path.join(input_dir, input_filename)
    data = pd.read_csv(input_file)
    data['datestamp'] = pd.to_datetime(data.datestamp)
    satellites = data['sat_id'].unique()
    for satellite in satellites:
        # filter data by satellite
        satellite_data = data[data['sat_id'] == satellite]
        # filter to AM data only
        morning_data = satellite_data[satellite_data['datestamp'] < cutoff_date]
        overpass_dict = get_overpass_groups(morning_data)
        for overpass, overpass_data in overpass_dict.items():
            overpass_rows = overpass_data['data'].shape[0]
            mean_time = get_mean_datestamp(overpass_data['time_values'], short_date)
            output_filename = "sat{}_{}_{:02d}-{:02d}.csv".format(satellite, short_date_str, mean_time.hour, mean_time.minute)
            print(output_filename)
            print("{} rows".format(overpass_rows))
            output_file = os.path.join(output_dir, output_filename)
            overpass_data['data'].to_csv(output_file)