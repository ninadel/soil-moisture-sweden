"""
Author: Nina del Rosario
Date: 6/27/2020
Script for extracting location time series from TUW-GEO H115 reader:
    https://github.com/TUW-GEO/ascat/blob/27f43293fab60ec6a81ba24796decd12c2e8f75b/src/ascat/h_saf.py#L745
Script for exporting CSV files of TS within a bounding box around Sweden
"""
import xarray as xr
import numpy as np
import sm_config as config
import sm_tools as tools
import os
import json


def main():
    export_nc = True
    export_dict_file = True
    buffer = 2
    output_dir = "../test_output_data/warp_coordinates_swe"
    # coordinate limits different from dictionary - need a wider longitude range to create a rectangular grid from a curvilinear grid
    min_lon = 2
    max_lon = 94
    ref_lon = 4
    lon_window_width = 120
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    f = r"C:\git\soil-moisture-sweden\ascat_ts_aux\warp5_grid\TUW_WARP5_grid_info_2_3.nc"
    warp = xr.open_dataset(f)

    #     if config.dict_extent_sweden["min_lat"] - buffer < lat < config.dict_extent_sweden["max_lat"] + buffer and \
    #             10 < lon < 60:
    lat_array = warp.lat.values
    lon_array = warp.lon.values
    gpi_array = warp['gpi'].values
    lat_filtered_array = lat_array[np.where((lat_array > config.study_area['min_lat'] - buffer) &
                                   (lat_array < config.study_area["max_lat"] + buffer) &
                                   (lon_array > min_lon) & (lon_array < max_lon))]
    lon_filtered_array = lon_array[np.where((lat_array > config.study_area["min_lat"] - buffer) &
                                   (lat_array < config.study_area["max_lat"] + buffer) &
                                   (lon_array > min_lon) & (lon_array < max_lon))]
    gpi_filtered_array = gpi_array[np.where((lat_array > config.study_area["min_lat"] - buffer) &
                                   (lat_array < config.study_area["max_lat"] + buffer) &
                                   (lon_array > min_lon) & (lon_array < max_lon))]

    lat_dict = {}
    for lat in np.unique(lat_filtered_array):
        matching_lon = lon_filtered_array[np.where(lat_filtered_array == lat)]
        nearest_idx, nearest_lon = tools.find_nearest(matching_lon, ref_lon)
        lat_dict[lat] = matching_lon[nearest_idx:nearest_idx+lon_window_width]
        # print((lat, (matching_lon[nearest_idx-1], matching_lon[nearest_idx], matching_lon[nearest_idx+lon_window_width])))
        ref_lon = nearest_lon

    lat_keys = list(lat_dict.keys())
    lat_keys.sort(reverse=True)

    empty = np.empty((len(lat_keys), lon_window_width))
    empty[:] = np.nan
    lat_grid = empty.copy()
    lon_grid = empty.copy()
    for ilt, lt in enumerate(lat_keys):
        lat_grid[ilt,:] = lt
        # lon_grid[0:lon_window_width+1,i] = lat_dict[lt]
        # lon_grid[0:lon_window_width + 1, i] = i
        lns = lat_dict[lt]
        for iln, ln in enumerate(lns):
            lon_grid[ilt, iln] = lns[iln]


    ds_template = xr.Dataset(
        {
            "sm": (
                ("row", "col"),
                np.empty((167, 120)),
            ),
            "sm_noise": (
                ("row", "col"),
                np.empty((167, 120)),
            ),
            "conf_flag": (
                ("row", "col"),
                np.empty((167, 120)),
            ),
            "corr_flag": (
                ("row", "col"),
                np.empty((167, 120)),
            ),
            "proc_flag": (
                ("row", "col"),
                np.empty((167, 120)),
            ),
            "ssf": (
                ("row", "col"),
                np.empty((167, 120)),
            ),
        },
        # coords={"lat": lat_grid, "lon": lon_grid, "row": rowNums, "col": colNums}
        coords={
            "lat": (("row", "col"), lat_grid),
            "lon": (("row", "col"), lon_grid)
        }
    )

    ds_template["time"] = 0
    ds_template = ds_template.expand_dims("time").set_coords("time")

    if export_nc:
        ds_template.to_netcdf(os.path.join(output_dir, "ascat_h115_swe_template.nc"))

    # build dictionary file for coordinates, to be used to populate template
    lat_list = lat_grid[:,0].tolist()
    # lat_round = [round(lat, 6) for lat in lat_list]
    coord_dict = {"lat": lat_list}

    for i in range(0,len(lat_list)):
        lon_list = lon_grid[i,:].tolist()
        # lon_round = [round(lon, 6) for lon in lon_list]
        coord_dict[i] = lon_list

    if export_dict_file:
        dict_file = os.path.join(output_dir, "dict_h115_swe_coords.json")
        with open(dict_file, 'w') as f:
            json.dump(coord_dict, f)


if __name__ == '__main__':
    main()
