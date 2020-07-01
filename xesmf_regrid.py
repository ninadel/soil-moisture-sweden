import xarray as xr
import xesmf as xe
import sm_config as config

# info on regridding algorithms: https://xesmf.readthedocs.io/en/latest/notebooks/Compare_algorithms.html
def xesmf_regrid(input_ds, input_array, method):
    if method == 'nearest_s2d' or method == 'bilinear':
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon)})
    elif method == 'conservative':
        ds_out = xr.Dataset({'lat': (['lat'], config.regrid_lat),
                             'lon': (['lon'], config.regrid_lon),
                             'lat_b': (['lat_b'], config.regrid_lat_b),
                             'lon_b': (['lon_b'], config.regrid_lon_b)
                             })
    reg = xe.Regridder(input_ds, ds_out, method)
    output_array = reg(input_array)
    return output_array
