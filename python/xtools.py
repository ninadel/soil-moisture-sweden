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


def preprocess_ascat_h101(in_ds):
    out_ds = in_ds[['proc_flag', 'soil_moisture']]
    # print(out_ds)
    # print(out_ds.coords)
    # print(out_ds['soil_moisture'])
    # out_ds = out_ds.sel(
    #     lat=slice(config.study_area['min_lat'], config.study_area['max_lat']),
    #     lon=slice(config.study_area['min_lon'], config.study_area['max_lon']))
    return out_ds


def preprocess_cci(in_ds):
    # subset to sweden
    out_ds = in_ds.sel(
        # CCI has descending latitude order
        lat=slice(config.study_area['max_lat'], config.study_area['min_lat']),
        lon=slice(config.study_area['min_lon'], config.study_area['max_lon']))
    return out_ds


# def preprocess_gldas(in_ds):
#     out_ds = in_ds['SoilMoi0_10cm_inst']
#     # subset to sweden
#     out_ds = out_ds.sel(
#         lat=slice(config.study_area['min_lat'], config.study_area['max_lat']),
#         lon=slice(config.study_area['min_lon'], config.study_area['max_lon']))
#     return out_ds


def preprocess_sentinel(in_ds):
    # # get filename
    # source = in_ds['Soil_Moisture'].encoding['source']
    # # get timestamp from filename
    # datestamp = tools.get_filename_timestamp(source, r"_[0-9]{8}T")
    out_ds = in_ds.sel(
        # Sentinel has descending latitude order
        lat=slice(config.study_area['max_lat'], config.study_area['min_lat']),
        lon=slice(config.study_area['min_lon'], config.study_area['max_lon']))
    return out_ds


def preprocess_smos_bec(in_ds):
    # get filename
    source = in_ds['SM'].encoding['source']
    # get timestamp from filename
    datestamp = tools.get_filename_timestamp(source, r"_[0-9]{8}T")
    # datestamp_int = tools.get_filename_timestamp(source, r"_[0-9]{8}T", return_int=True)
    # since timestamp is midnight, add local overpass time in utc
    local_time_utc = 5
    datestamp = datestamp.replace(hour=local_time_utc)
    # subset to sweden
    out_ds = in_ds.sel(
        lat=slice(config.study_area['min_lat'], config.study_area['max_lat']),
        lon=slice(config.study_area['min_lon'], config.study_area['max_lon']))
    # add time dimension
    out_ds['time'].values[:] = datestamp
    # out_ds = out_ds.expand_dims('time').set_coords('time')
    return out_ds


def preprocess_smos_ic(in_ds):
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
    # subset to sweden
    out_ds = in_ds.sel(
        lat=slice(config.study_area['min_lat'], config.study_area['max_lat']),
        lon=slice(config.study_area['min_lon'], config.study_area['max_lon']))
    # add time dimension
    out_ds['time'] = datestamp
    out_ds = out_ds.expand_dims('time').set_coords('time')
    return out_ds


def get_mf_dataset(file_list, product):
    if product == "ASCAT 12.5 Swath":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_ascat_h101, combine='by_coords', decode_times=False)
        return ds
    # if product == "GLDAS":
    #     ds = xr.open_mfdataset(file_list, preprocess=preprocess_gldas, combine='by_coords')
    #     return ds
    if product == "CCI Active" or product == "CCI Passive" or product == "CCI Combined":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_cci, combine='by_coords')
        return ds
    if product == "Sentinel-1":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_sentinel, combine='by_coords')
        return ds
    if product == "SMOS-IC":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_smos_ic, combine='by_coords')
        return ds
    if product == "SMOS-BEC":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_smos_bec, combine='by_coords')
        return ds


def regrid(ds_in, var, method='nearest_s2d', reuse=False, cleanup=True, mask=True):
    if 'latitude' in ds_in.coords:
        ds_in = ds_in.rename({'latitude': 'lat', 'longitude': 'lon'})
    if 'time' in ds_in.coords and ds_in.time.size > 1:
        dr_out = regrid_multidate(ds_in, var, method=method, reuse=False, cleanup=cleanup, mask=mask)
    else:
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon)})
        reg = xe.Regridder(ds_in, ds_out, method=method, reuse_weights=reuse)
        dr_in = ds_in[var]
        dr_out = reg(dr_in)
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


def mask_edges(array, mask, mask_value=0):
    masked_array = array.copy()
    shape = array.shape
    for i in range(0, shape[0]):
        if mask.values[i, :].mean() == 0:
            masked_array.values[i, :] = np.nan
    for i in range(0, shape[1]):
        if mask.values[:, i].mean() == 0:
            masked_array.values[:, i] = np.nan
    return masked_array


def regrid_multidate(ds_in, var, method='nearest_s2d', reuse=False, cleanup=True, mask=True):
    if 'latitude' in ds_in.coords:
        ds_in = ds_in.rename({'latitude': 'lat', 'longitude': 'lon'})
    if mask:
        # code for masking
        concat_arrays = []
        ds_in_first = ds_in[var][0, :, :]
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon)})
        nearest_reg = xe.Regridder(ds_in_first, ds_out, method="nearest_s2d", reuse_weights=reuse)
        bilinear_reg = xe.Regridder(ds_in_first, ds_out, method="bilinear", reuse_weights=reuse)
        for index in range(0, ds_in.time.values.size):
            dr_in = ds_in[var][index, :, :]
            nearest_dr_out = nearest_reg(dr_in)
            bilinear_dr_out = bilinear_reg(dr_in)
            dr_regrid = mask_edges(nearest_dr_out, bilinear_dr_out)
            concat_arrays.append(dr_regrid)
        if cleanup:
            nearest_reg.clean_weight_file()  # clean-up
            bilinear_reg.clean_weight_file()  # clean-up
        dr_concat = xr.concat(concat_arrays, dim="time")
        return dr_concat
    else:
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon),
                             'time': (['time'], ds_in.time.values)})
        reg = xe.Regridder(ds_in, ds_out, method=method, reuse_weights=reuse)
        dr_in = ds_in[var]
        dr_out = reg(dr_in)
        if cleanup:
            reg.clean_weight_file()  # clean-up
        return dr_out
