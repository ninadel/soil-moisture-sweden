import xarray as xr
import numpy as np
import sm_config as config
import sm_tools as tools
import os

buffer = 2
output_dir = "../test_output_data/warp_coordinates_swe"
min_lon = 2
max_lon = 90
ref_lon = 6
lon_window_width = 100
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

f = r"C:\git\soil-moisture-sweden\ascat_ts_aux\warp5_grid\TUW_WARP5_grid_info_2_3.nc"
warp = xr.open_dataset(f)

#     if config.dict_extent_sweden["min_lat"] - buffer < lat < config.dict_extent_sweden["max_lat"] + buffer and \
#             10 < lon < 60:
lat_array = warp.lat.values
lon_array = warp.lon.values
gpi_array = warp['gpi'].values
lat_filtered_array = lat_array[np.where((lat_array > config.dict_extent_sweden["min_lat"] - buffer) &
                               (lat_array < config.dict_extent_sweden["max_lat"] + buffer) &
                               (lon_array > min_lon) & (lon_array < max_lon))]
lon_filtered_array = lon_array[np.where((lat_array > config.dict_extent_sweden["min_lat"] - buffer) &
                               (lat_array < config.dict_extent_sweden["max_lat"] + buffer) &
                               (lon_array > min_lon) & (lon_array < max_lon))]
gpi_filtered_array = gpi_array[np.where((lat_array > config.dict_extent_sweden["min_lat"] - buffer) &
                               (lat_array < config.dict_extent_sweden["max_lat"] + buffer) &
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
    lat_grid[ilt,:] = round(lt,4)
    # lon_grid[0:lon_window_width+1,i] = lat_dict[lt]
    # lon_grid[0:lon_window_width + 1, i] = i
    lns = lat_dict[lt]
    for iln, ln in enumerate(lns):
        lon_grid[ilt, iln] = round(lns[iln],4)

# lat & lon variables
print(lat_grid)
print(lon_grid)

# row and col dimensions

rowNums = [*range(0,len(lat_keys))]
colNums = [*range(0,lon_window_width)]

print(rowNums)
print(colNums)