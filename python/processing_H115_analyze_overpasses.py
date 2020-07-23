"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 7/23/2020

Purpose: Figure out how to split dates with multiple overpasses
Input => Date CSVs where each row is a coordinate
Output => CSV of dataframe => [instrument, date, overpasses (#), min time (list), max time (list), overlap (boolean)]
"""

import os
from datetime import datetime, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_date_str(date):
    date_str = date.strftime("%m/%d/%Y")
    return date_str

def get_dummy_time(date, min=True):
    if min:
        dummy_date = datetime(date.year, date.month, date.day, 23, 59)
    else:
        dummy_date = datetime(date.year, date.month, date.day, 0, 1)
    return dummy_date

output_dir = r"../test_output_dir"
metadata_file = os.path.join(output_dir, "h115_overpass_analysis.csv")
startdate = datetime(2015, 1, 1)
enddate = datetime(2018, 12, 31)
sep = ","

# Create empty dict for storing date dataframe
# 	Key for each instrument => DF
date_dict = {3: None, 4: None}

metadata_dict = {3: {}, 4: {}}

for key in metadata_dict.keys():
    for date in daterange(startdate, enddate):
        metadata_dict[key][get_date_str(date)] = {"overpass_count": 0, "min_time": None, "max_time": None}

"""
For each instrument in date dataframe dict
    # Check for multiple overpasses, update metadata dict
    Create list of coordinate tuples
    Get list len of coordinate tuples
    Create set of list
    Get set len of coordinate tuples
    If set len < list len
        Multiple overpasses => True
        Min time => (datetime(year, month, day, 23, 59),datetime(year, month, day, 23, 59))
        Max time => (datetime(year, month, day, 00, 01),datetime(year, month, day, 00, 01))
    Else
        Multiple overpasses => False
        Min time => (datetime(year, month, day, 23, 59))
        Max time => (datetime(year, month, day, 00, 01))
    For each coordinate
        If multiple overpasses is True
            Sort times
            Check first time against first min time
            Check first time against first max time
            Check second time against second min time
            Check second time against second max time
        Else
            Check time against min time
            Check time against max time
    Update metadata dict
    
Expot metadata dict to csv
"""