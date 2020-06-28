"""
Author: Nina del Rosario
Date: 6/27/2020
Script for exporting CSV files of TS within a bounding box around Sweden
"""
import xarray as xr
import pandas
import os
import sm_config as config
import sm_tools as tools
from datetime import datetime

input_dir = r"..\sm_sample_files\ascat-h115-ts-2019"
output_dir = r"../test_output_data/H115_points_csv"
point_subdir = "point_data"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

startdate = datetime(2015, 1, 1)
enddate = datetime(2019, 1, 1)

product = 'ASCAT 12.5 TS'
reader = tools.get_product_reader(product, config.dict_product_inputs[product])

# find bounding box
min_lat = 9999
max_lat = -9999
min_lon = 9999
max_lon = -9999

for key, value in config.dict_swe_gldas_points.items():
    if value["latitude"] < min_lat:
        min_lat = value["latitude"]
    if value["latitude"] > max_lat:
        max_lat = value["latitude"]
    if value["longitude"] < min_lon:
        min_lon = value["longitude"]
    if value["longitude"] > max_lon:
        max_lon = value["longitude"]

locations = pandas.DataFrame(columns=['loc', 'lon', 'lat'])

# find locations within Sweden cells and
for cell in config.swe_shuffle_cells:
    filename = "H115_"+str(cell)+".nc"
    file = os.path.join(input_dir, filename)
    ds = xr.open_dataset(file)
    loc_len = ds['location_id'].size
    for i in range(loc_len):
        loc = int(ds['location_id'].data[i])
        loc_lat = ds['lat'].data[i]
        loc_lon = ds['lon'].data[i]
        if (loc_lat > min_lat - 1) and (loc_lat < max_lat + 1) and (loc_lon > min_lon -1) and (loc_lon < max_lon + 1):
            locations = locations.append({"lon": loc_lon, "lat": loc_lat, "loc": str(loc)}, ignore_index=True)

print(locations)
locations.set_index("loc", inplace=True)

for index, row in locations.iterrows():
    ts = reader.read(row['lon'], row['lat'])
    data = ts.data[startdate::]
    data = data[['sm', 'ssf', 'sat_id']]
    filename = "{}.csv".format(index)
    data.to_csv(os.path.join(output_dir, point_subdir, filename))