"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/9/2020
Script for extracting GLDAS dominant vegetation type: https://ldas.gsfc.nasa.gov/gldas/vegetation-class-mask
"""
import json
import netCDF4
import pandas
import sm_tools as tools

def main():
    with open("dict_gldas_veg.json", "r") as f:
        dict_gldas_veg = json.load(f)

    veg_grid = r"..\gldas_ts_aux\GLDASp4_domveg_025d.nc4"
    veg_grid_nc = netCDF4.Dataset(veg_grid, 'r')

    lon_array = veg_grid_nc['lon'][:]
    lat_array = veg_grid_nc['lat'][:]

    sweden_points_file = r"..\pointlists\pointlist_Sweden_quarter.csv"
    sweden_points = pandas.read_csv(sweden_points_file)

    sweden_GLDAS_points = {}
    sweden_GLDAS_domveg_types = []

    for index, row in sweden_points.iterrows():
        nearest_lon_idx = tools.find_nearest(lon_array, row['lon'])[0]
        nearest_lat_idx = tools.find_nearest(lat_array, row['lat'])[0]
        value = veg_grid_nc['GLDAS_domveg'][0, nearest_lat_idx, nearest_lon_idx]
        veg_class = dict_gldas_veg[str(int(value))]
        if veg_class != "Ocean":
            # sweden_GLDAS_domveg_points[value_str] = {}
            sweden_GLDAS_points[row['point']] = {}
            sweden_GLDAS_points[row['point']]['lat'] = row['lat']
            sweden_GLDAS_points[row['point']]['lon'] = row['lon']
            sweden_GLDAS_points[row['point']]['veg_class_name'] = veg_class

    with open('dict_swe_points.json', 'w') as f:
        json.dump(sweden_GLDAS_points, f)


if __name__ == '__main__':
    main()
