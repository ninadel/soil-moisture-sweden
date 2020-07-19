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


def preprocess_ascat_h101(in_ds):
    out_ds = in_ds[['proc_flag', 'soil_moisture']]
    print(out_ds)
    print(out_ds.coords)
    print(out_ds['soil_moisture'])
    # out_ds = out_ds.sel(
    #     lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
    #     lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
    return out_ds


def preprocess_sentinel(in_ds):
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
    return out_ds


def preprocess_smap_L3(in_ds):
    # get filename
    source = in_ds.encoding['source']
    # get timestamp from filename
    datestamp = tools.get_filename_timestamp(source, r"P_[0-9]{8}_R")
    # since timestamp is midnight, add local overpass time in utc
    local_time_utc = 5
    datestamp = datestamp.replace(hour=local_time_utc)
    # open dataset as subgroup
    tmp_ds =  xr.open_dataset(source, group='Soil_Moisture_Retrieval_Data_AM')
    # retrieve variables for rebuilding dataset
    lon = tmp_ds['longitude'].values
    lat = tmp_ds['latitude'].values
    soil_moisture = tmp_ds['soil_moisture'].values
    surface_flag = tmp_ds['surface_flag'].values
    retrieval_qual_flag = tmp_ds['retrieval_qual_flag'].values
    # rebuild dataset
    out_ds = xr.Dataset(
        {
            "soil_moisture": (["x", "y"], soil_moisture),
            "surface_flag": (["x", "y"], surface_flag),
            "retrieval_qual_flag": (["x", "y"], retrieval_qual_flag),
        },
        coords={
            "lon": (["x", "y"], lon),
            "lat": (["x", "y"], lat),
        },
    )
    # add datestamp and add as dim
    out_ds["time"] = datestamp
    out_ds = out_ds.expand_dims('time').set_coords('time')
    return out_ds


def preprocess_smap_L3E(in_ds):
    # get filename
    source = in_ds.encoding['source']
    # get timestamp from filename
    datestamp = tools.get_filename_timestamp(source, r"E_[0-9]{8}_R")
    # since timestamp is midnight, add local overpass time in utc
    local_time_utc = 5
    datestamp = datestamp.replace(hour=local_time_utc)
    # open dataset as subgroup
    tmp_ds =  xr.open_dataset(source, group='Soil_Moisture_Retrieval_Data_AM')
    # retrieve variables for rebuilding dataset
    lon = tmp_ds['longitude'].values
    lat = tmp_ds['latitude'].values
    soil_moisture = tmp_ds['soil_moisture'].values
    surface_flag = tmp_ds['surface_flag'].values
    retrieval_qual_flag = tmp_ds['retrieval_qual_flag'].values
    # rebuild dataset
    out_ds = xr.Dataset(
        {
            "soil_moisture": (["x", "y"], soil_moisture),
            "surface_flag": (["x", "y"], surface_flag),
            "retrieval_qual_flag": (["x", "y"], retrieval_qual_flag),
        },
        coords={
            "lon": (["x", "y"], lon),
            "lat": (["x", "y"], lat),
        },
    )
    # add datestamp and add as dim
    out_ds["time"] = datestamp
    out_ds = out_ds.expand_dims('time').set_coords('time')
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
    if product == "ASCAT 12.5 Swath":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_ascat_h101, combine='by_coords', decode_times=False)
        return ds
    if product == "Sentinel-1":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_sentinel, combine='by_coords')
        return ds
    if product == "SMAP L3":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_smap_L3, combine='by_coords')
        return ds
    if product == "SMAP L3 Enhanced":
        ds = xr.open_mfdataset(file_list, preprocess=preprocess_smap_L3E, combine='by_coords')
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


def get_xr_series(xr_dataset, coordinate_dim=False):
    pass