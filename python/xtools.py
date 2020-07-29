from datetime import datetime
import numpy as np
import xarray as xr
import warnings
import os
import pandas as pd
import sm_config as config
import sm_tools as tools

try:
    import xesmf as xe
except:
    warnings.warn("could not import xesmf. not windows compatible.")


def preprocess_ascat_h101(in_ds, regrid=False):
    out_ds = in_ds[['proc_flag', 'soil_moisture']]
    # print(out_ds)
    # print(out_ds.coords)
    # print(out_ds['soil_moisture'])
    # out_ds = out_ds.sel(
    #     lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
    #     lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
    if regrid:
        # code for regrid
        pass
    return out_ds


def preprocess_sentinel(in_ds, regrid=False):
    # # get filename
    # source = in_ds['Soil_Moisture'].encoding['source']
    # # get timestamp from filename
    # datestamp = tools.get_filename_timestamp(source, r"_[0-9]{8}T")
    # select variables to keep
    out_ds = in_ds[['Soil_Moisture', 'Quality_Flag']]
    out_ds = in_ds.sel(
        # Sentinel has descending latitude order
        lat=slice(config.dict_extent_sweden['max_lat'], config.dict_extent_sweden['min_lat']),
        lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
    if regrid:
        # code for regrid
        pass
    return out_ds


def preprocess_smos_ic(in_ds, regrid=False):
    # get filename
    source = in_ds['Soil_Moisture'].encoding['source']
    # get timestamp from filename
    datestamp = tools.get_filename_timestamp(source, r"_[0-9]{8}T")
    # datestamp_int = tools.get_filename_timestamp(source, r"_[0-9]{8}T", return_int=True)
    # since timestamp is midnight, add local overpass time in utc
    local_time_utc = 5
    datestamp = datestamp.replace(hour=local_time_utc)
    # timestamp_int = datestamp_int + (local_time_utc * 60 * 60)
    # timestamp = datetime.utcfromtimestamp()
    # select variables to keep
    out_ds = in_ds[['Soil_Moisture', 'Quality_Flag']]
    # subset to sweden
    out_ds = out_ds.sel(
        lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
        lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
    if regrid:
        # code for regrid
        pass
    # add time dimension
    out_ds['time'] = datestamp
    out_ds = out_ds.expand_dims('time').set_coords('time')
    return out_ds


def get_mf_dataset(file_list, product):
    if product == "ASCAT 12.5 Swath":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_ascat_h101, combine='by_coords', decode_times=False)
        return ds
    if product == "Sentinel-1":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_sentinel, combine='by_coords')
        return ds
    if product == "SMOS-IC":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_smos_ic, combine='by_coords')
        return ds


def regrid(ds_in, var, method='nearest_s2d', reuse=False, cleanup=False, mask=True):
    if 'latitude' in ds_in.coords:
        ds_in = ds_in.rename({'latitude': 'lat', 'longitude': 'lon'})
    if 'time' in ds_in.coords:
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon),
                            'time': (['time'], ds_in['time'].values)})
    else:
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon)})
    reg = xe.Regridder(ds_in, ds_out, method=method, reuse_weights=reuse)
    dr_in = ds_in[var]
    dr_out = reg(dr_in)
    if mask:
        # code for masking
        # do separate regrid with bilinear
        # use bilinear to mask results from nearest_s2d
        pass
    if cleanup:
        reg.clean_weight_file()  # clean-up
    return dr_out


def write_ts_quarter_deg(dr, output_dir, overwrite=False, dropna=False):
    location_len = len(config.dict_swe_gldas_points.keys())
    location_count = 0
    for location, metadata in config.dict_swe_gldas_points.items():
        outfile = os.path.join(output_dir, "{}.csv".format(location))
        if not overwrite and os.path.exists(outfile):
            with open(os.path.join(output_dir, "logfile.txt"), "a") as file:
                message = "{} {} exists, skipped".format(datetime.now(), location)
                file.write(message + "\n")
                warnings.warn(message)
            break
        location_count += 1
        print("location {} of {}".format(location_count, location_len))
        # use lat index instead?
        ts = dr.sel(lat=metadata['latitude'], lon=metadata['longitude'])
        # ts_df = ts.to_pandas()
        ts_df = ts.to_pandas()
        if dropna:
            ts_df = ts_df.dropna()
        ts_df.rename("sm", inplace=True)
        # ts_df.dropna(inplace=True)
        if ts_df is not None:
            ts_df.to_csv(outfile)
            with open(os.path.join(output_dir, "logfile.txt"), "a") as file:
                file.write("{} {} ok".format(datetime.now(), location) + "\n")
        else:
            with open(outfile, "w") as file:
                file.write("time, sm" + "\n")
            with open(os.path.join(output_dir, "logfile.txt"), "a") as file:
                file.write("{} {} empty".format(datetime.now(), location) + "\n")


def get_coord_array_index(dict, coord):
    lat = coord[0]
    lon = coord[1]
    lat_array = dict["lat"]
    row = tools.find_nearest(lat_array, lat)[0]
    lon_array = dict[str(row)]
    col = tools.find_nearest(lon_array, lon)[0]
    return row, col


def populate_arrays(coord_dict, shape, data_file, output_vars):
    array_rows = shape[0]
    array_cols = shape[1]
    array_dict = {}
    empty = np.empty((array_rows, array_cols))
    empty[:] = np.NAN
    data = pd.read_csv(data_file)
    for var in output_vars:
        array_dict[var] = np.copy(empty)
    for index, data_row in data.iterrows():
        coord = (data_row['lat'], data_row['lon'])
        row_idx, col_idx = get_coord_array_index(coord_dict, coord)
        for var in output_vars:
            array_dict[var][row_idx,col_idx] = data_row[var]
    return array_dict