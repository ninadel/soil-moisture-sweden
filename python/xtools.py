from datetime import datetime
import xarray as xr
import warnings
import os
import pandas
import sm_config as config
import sm_tools as tools

try:
    import xesmf as xe
except:
    warnings.warn("could not import xesmf. not windows compatible.")


def preprocess_sentinel(in_ds):
    out_ds = in_ds.sel(
        # Sentinel has descending latitude order
        lat=slice(config.dict_extent_sweden['max_lat'], config.dict_extent_sweden['min_lat']),
        lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
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
    # select variables to keep
    out_ds = in_ds[['Soil_Moisture', 'Quality_Flag']]
    # subset to sweden
    out_ds = out_ds.sel(
        lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
        lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
    # add time dimension
    out_ds['time'] = datestamp
    out_ds = out_ds.expand_dims('time').set_coords('time')
    return out_ds


def get_mf_dataset(file_list, product):
    if product == "Sentinel-1":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_sentinel, combine='by_coords')
        return ds
    if product == "SMOS-IC":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_smos_ic, combine='by_coords')
        return ds


def regrid(ds_in, var, method='nearest_s2d', reuse=False, cleanup=False):
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
    print(dr_in)
    dr_out = reg(dr_in)
    if cleanup:
        reg.clean_weight_file()  # clean-up
    return dr_out


def write_ts_quarter_deg(dr, output_dir, overwrite=False):
    location_len = len(config.dict_swe_gldas_points.keys())
    location_count = 0
    for location, metadata in config.dict_swe_gldas_points.items():
        outfile = os.path.join(output_dir, "{}.csv".format(location))
        if not overwrite and os.path.exists(outfile):
            with open(os.path.join(output_dir, "logfile.txt"), "a") as file:
                file.write("{} {} exists, skipped".format(datetime.now(), location) + "\n")
            break
        location_count += 1
        print("location {} of {}".format(location_count, location_len))
        # use lat index instead?
        ts = dr.sel(lat=metadata['latitude'], lon=metadata['longitude'])
        # ts_df = ts.to_pandas()
        ts_df = ts.to_pandas().dropna()
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
