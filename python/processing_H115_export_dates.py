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

date_dict = {}
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
    date_df_columns = ['location_id', 'lon', 'lat']
    for column in data.columns:
        date_df_columns.append(column)
    for index, row in data.iterrows():
        short_date = row['datestamp'][0:10]
        if short_date not in date_dict.keys():
            date_dict[short_date] = pandas.DataFrame(columns=date_df_columns)
        row_dict = {'location_id': location_id, 'lon': loc_lon, 'lat': loc_lat}
        for column in data.columns:
            row_dict[column] = row[column]
        date_dict[short_date] = date_dict[short_date].append(row_dict, ignore_index=True)

for short_date in date_dict.keys():
    date_file = os.path.join(output_dir, "{}.csv".format(short_date))
    date_dict[short_date].to_csv(date_file, index=False)

