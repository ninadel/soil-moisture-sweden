"""
Author: Nina del Rosario
Date: 6/27/2020
Script for exporting CSV files of TS within a bounding box around Sweden
Processes output of processing_H115_export_points.py
"""
import pandas
import os
from datetime import datetime, timedelta

write_data = True
input_dir = r"..\test_output_data\H115_points_csv\point_data"
dict_file = r"..\test_output_data\H115_points_csv\H115_SWE_locations.csv"
output_dir = r"..\test_output_data\H115_points_csv\date_data"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

startdate = datetime(2015, 1, 1)
enddate = datetime(2019, 1, 1)
sep = ","

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

locations = pandas.read_csv(dict_file)
locations.set_index("loc", inplace=True)

loc_dict = {}
for index, row in locations.iterrows():
    loc_dict[str(index)] = {}
    loc_dict[str(index)]["longitude"] = row["lon"]
    loc_dict[str(index)]["latitude"] = row["lat"]

for date in daterange(startdate, enddate):
    date_str = date.strftime("%Y-%m-%d")
    filename = "{}.csv".format(date_str)
    file = os.path.join(output_dir, filename)
    if not os.path.exists(file):
        with open(os.path.join(output_dir, filename), "a") as file:
            file.write("lon,lat,sm,ssf" + "\n")

for point_file in os.listdir(input_dir):
    location_id = point_file.split(".")[0]
    loc_lon = loc_dict[location_id]["longitude"]
    loc_lat = loc_dict[location_id]["latitude"]
    data = pandas.read_csv(os.path.join(input_dir, point_file))
    data.set_index('Unnamed: 0', inplace=True)
    last_date = "2000-01-01"
    for index, row in data.iterrows():
        short_date = index[0:10]
        time = index[11:16]
        if short_date != last_date:
            row = (str(loc_lon), str(loc_lat), str(row['sm']), str(row['ssf']))
            row_str = sep.join(row)
            filename = "{}.csv".format(short_date)
            if write_data:
                with open(os.path.join(output_dir, filename), "a") as file:
                    file.write(row_str + "\n")
            last_date = short_date