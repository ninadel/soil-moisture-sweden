"""
Author: Nina del Rosario
Date: 6/27/2020
Script for extracting location time series from TUW-GEO H115 reader:
    https://github.com/TUW-GEO/ascat/blob/27f43293fab60ec6a81ba24796decd12c2e8f75b/src/ascat/h_saf.py#L745
Script for exporting CSV files of TS within a bounding box around Sweden
"""
import xarray as xr
import pandas
import os
import sm_config as config
import sm_tools as tools
from datetime import datetime
from multiprocessing import Pool

def main():
    export_dict = True
    cells = list(set(config.swe_shuffle_cells + config.den_shuffle_cells))
    startdate = datetime(2015, 1, 1)
    enddate = datetime(2019, 1, 1)
    product = 'ASCAT 12.5 TS'
    input_dir = r"D:\sm_backup\native\ascat-h115-ts-2019"
    output_dir = r"../test_output_data/H115_points_csv"
    dict_file = os.path.join(output_dir, "H115_locations.csv")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # define bounding box for finding locations
    buffer = 2
    min_lat = config.study_area["min_lat"] - buffer
    max_lat = config.study_area["max_lat"] + buffer
    min_lon = config.study_area["min_lon"] - buffer
    max_lon = config.study_area["max_lon"] + buffer
    locations = pandas.DataFrame(columns=['loc', 'lon', 'lat'])

    # find locations within Sweden cells and
    for cell in cells:
        filename = "H115_"+str(cell)+".nc"
        file = os.path.join(input_dir, filename)
        # open H115 file in xarray
        ds = xr.open_dataset(file)
        loc_len = ds['location_id'].size
        for i in range(loc_len):
            loc = int(ds['location_id'].data[i])
            loc_lat = ds['lat'].data[i]
            loc_lon = ds['lon'].data[i]
            # check whether location is in bounding box
            if (loc_lat > min_lat) and (loc_lat < max_lat) and (loc_lon > min_lon) and (loc_lon < max_lon):
                locations = locations.append({"lon": loc_lon, "lat": loc_lat, "loc": str(loc)}, ignore_index=True)

    locations.set_index("loc", inplace=True)
    print(locations)
    locations.to_csv(dict_file)


if __name__ == '__main__':
    main()
