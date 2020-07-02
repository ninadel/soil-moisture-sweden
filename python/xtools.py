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
    if product == "SMOS-IC":
        prep_func = preprocess_smos_ic
    ds = xr.open_mfdataset(file_list, preprocess=prep_func, combine='by_coords')
    return ds

def regrid(ds_in, var, method='nearest_s2d'):
    if 'latitude' in ds_in.coords:
        ds_in = ds_in.rename({'latitude': 'lat', 'longitude': 'lon'})
    if 'time' in ds_in.coords:
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon),
                            'time': (['time'], ds_in['time'].values)})
    else:
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon)})
    reg = xe.Regridder(ds_in, ds_out, method)
    dr_in = ds_in[var]
    dr_out = reg(dr_in)
    return dr_out

def write_ts_quarter_deg(dr, output_dir, var='Soil_Moisture'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for location, metadata in config.dict_swe_gldas_points.items():
        print(location)
        ts = dr.sel(lat=metadata['latitude'], lon=metadata['longitude'])
        ts_df = ts.to_pandas()
        print(type(ts_df))
        ts_df.rename("sm", inplace=True)
        ts_df.dropna(inplace=True)
        outfile = os.path.join(output_dir, "{}.csv".format(location))
        if ts_df is not None:
            ts_df.to_csv(outfile)
            with open(os.path.join(output_dir, "logfile.txt"), "a") as file:
                file.write("{} {} ok".format(datetime.now(), location) + "\n")
        else:
            with open(outfile, "w") as file:
                file.write(", sm" + "\n")
            with open(os.path.join(output_dir, "logfile.txt"), "a") as file:
                file.write("{} {} empty".format(datetime.now(), location) + "\n")
