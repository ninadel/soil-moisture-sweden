import xarray as xr
import warnings
import sm_config as config
import sm_tools as tools

try:
    import xesmf
except:
    warnings.warn("could not import xesmf. not windows compatible.")


def preprocess_smos_ic(in_ds):
    # get filename
    source = in_ds['Soil_Moisture'].encoding['source']
    # get timestamp from filename
    datestamp_int = tools.get_filename_timestamp(source, r"_[0-9]{8}T", return_int=True)
    # since timestamp is midnight, add local overpass time in utc
    local_time_utc = 5
    timestamp_int = datestamp_int + (local_time_utc * 60 * 60)
    # select variables to keep
    out_ds = in_ds[['Soil_Moisture', 'Quality_Flag']]
    # subset to sweden
    out_ds = out_ds.sel(
        lat=slice(config.dict_extent_sweden['min_lat'], config.dict_extent_sweden['max_lat']),
        lon=slice(config.dict_extent_sweden['min_lon'], config.dict_extent_sweden['max_lon']))
    # mask out invalid data
    # "0: data OK, 1: data not recommended, 2: missing data"
    # Valid soil moisture range: 0 - 1
    # out_ds = out_ds.where((out_ds['Quality_Flag'] == 0) &
    #                                       (out_ds['Soil_Moisture'] >= 0) &
    #                                       (out_ds['Soil_Moisture'] < 1))
    # add time dimension
    out_ds['time'] = timestamp_int
    out_ds = out_ds.expand_dims('time').set_coords('time')
    return out_ds

def get_mf_dataset(file_list, product):
    if product == "SMOS-IC":
        prep_func = preprocess_smos_ic
    ds = xr.open_mfdataset(file_list, preprocess=prep_func, combine='by_coords')
    return ds
