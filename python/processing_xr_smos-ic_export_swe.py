import os
import xarray as xr
import xtools
import sm_config as config

product = 'SMOS-IC'
output_dir = r"..\test_output_data\SMOS-IC_regrid_ts"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
f = r"..\input_data\xr\regrid\smos-ic_0-25-regrid.nc"
sm_field = config.dict_product_fields[product]['sm_field']

ds = xr.open_dataset(f)
print(ds)
dr = ds[sm_field]
print(dr)

# def write_ts_quarter_deg(dr, output_dir, overwrite=False):
xtools.write_ts_quarter_deg(dr, output_dir)
