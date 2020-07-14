"""
Author: Nina del Rosario
Date: 6/27/2020
Script for exporting CSV files of TS within a bounding box around Sweden
Processes output of processing_H115_export_points.py
"""
import pandas
import os
from datetime import datetime
import sm_tools as tools

write_data = True
input_dir = r"..\input_data\ascat_h115_points_csv\point_data"
dict_file = r"..\input_data\ascat_h115_points_csv\H115_SWE_locations.csv"
output_dir = r"..\input_data\ascat_h115_points_csv\\date_data_unfiltered"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

startdate = datetime(2015, 1, 1)
enddate = datetime(2019, 1, 1)
sep = ","

# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)

locations = pandas.read_csv(dict_file)
locations.set_index("loc", inplace=True)

loc_dict = {}
for index, row in locations.iterrows():
    loc_dict[str(index)] = {}
    loc_dict[str(index)]["longitude"] = row["lon"]
    loc_dict[str(index)]["latitude"] = row["lat"]

for date in tools.get_date_range(startdate, enddate):
    date_str = date.strftime("%Y-%m-%d")
    filename = "{}.csv".format(date_str)
    file = os.path.join(output_dir, filename)

points = len(os.listdir(input_dir))
point_idx = 0
for point_file in os.listdir(input_dir):
    point_idx += 1
    print("{} of {}".format(point_idx, points))
    location_id = point_file.split(".")[0]
    loc_lon = loc_dict[location_id]["longitude"]
    loc_lat = loc_dict[location_id]["latitude"]
    data = pandas.read_csv(os.path.join(input_dir, point_file))
    data.rename(columns={'Unnamed: 0': 'datestamp'}, inplace=True)
    print(data.head())
    print(data.columns)
    # data.set_index('datestamp', inplace=True)
    # last_date = "2000-01-01"
    data_columns = ["datestamp"] + data.columns
    for index, row in data.iterrows():
        print(index)
        short_date = index[0:10]
        # hour = int(index[11:13])
        # if short_date != last_date and hour < 12:
        #     row = (str(loc_lon), str(loc_lat), str(row['sm']), str(row['ssf']))
        #     row_str = sep.join(row)
        filename = "{}.csv".format(short_date)
        out_file = os.path.join(output_dir, filename)
        if os.path.exists(out_file):
            with open(os.path.join(out_file), "a") as file:
                file.write(sep.join(row) + "\n")
        else:
            with open(os.path.join(output_dir, filename), "a") as file:
                file.write(sep.join(data.columns) + "\n")
                file.write(sep.join(row) + "\n")
            last_date = short_date
    break
