"""
Author: Nina del Rosario
Date: 6/27/2020
Script for converting location TS to date TS
Processes output of processing_H115_export_points.py
Each output file is a date, any location with any data matching date is added to CSV,
locations may have multiple observations for a date
UPDATE_DESCRIPTION
Why was this necessary?
"""
import pandas
import os
from datetime import datetime


def main():
    write_data = True
    input_dir = r"..\test_output_data\H115_points_csv\point_data"
    dict_file = r"C:\git\soil-moisture-sweden\test_output_data\H115_points_csv\H115_locations.csv"
    output_dir = r"..\test_output_data\H115_dates_csv"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    startdate = datetime(2015, 1, 1)
    enddate = datetime(2019, 1, 1)
    sep = ","

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
        date_column = ['location_id', 'lon', 'lat']
        for column in data.columns:
            date_column.append(column)
        date_column_str = sep.join(date_column)
        for index, row in data.iterrows():
            short_date = row['datestamp'][0:10]
            date_file = os.path.join(output_dir, "{}.csv".format(short_date))
            new_row = [str(location_id), str(loc_lon), str(loc_lat)]
            for column in data.columns:
                new_row.append(str(row[column]))
            new_row_str = sep.join(new_row)
            if not os.path.exists(date_file):
                with open(date_file, "w") as file:
                    file.write(date_column_str + "\n")
                    file.write(new_row_str + "\n")
            else:
                with open(date_file, "a") as file:
                    file.write(new_row_str + "\n")


if __name__ == '__main__':
    main()
