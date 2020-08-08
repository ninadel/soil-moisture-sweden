"""
Author: Nina del Rosario
Date: 7/19/2020
Script for merging SMAP L3 data using xarray
"""
import os
import xarray as xr
import sm_tools as tools

product = "SMAP L4"
output_dir = r"..\test_output_data\smap_L4_rebuild"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
in_dir = r"D:\sm_backup\native\SPL4SMAU-smap-ma-L4-09km_clipped_nc"

# first file for creating lat and lon dimensions
coord_file = r"D:\sm_backup\native\SPL4SMAU-smap-ma-L4-09km_clipped_nc\SMAP_L4_SM_aup_20150331T030000_Vv4030_001_HEGOUT.nc"
coord_ds = xr.open_dataset(coord_file)
lon = coord_ds['cell_lon'][0, :].values
lat = coord_ds['cell_lat'][:, 0].values

ds_list = []

for filename in os.listdir(in_dir):
    if filename[-3::] == ".nc":
        file = os.path.join(in_dir, filename)
        ds = xr.open_dataset(file)
        datestamp = ds['time'].values
        print(datestamp)
        ds_sm = xr.open_dataset(file, group="Analysis_Data")
        sm_surface_analysis = ds_sm['sm_surface_analysis'].values
        sm_surface_analysis_da = xr.DataArray(sm_surface_analysis, coords=[lat, lon], dims=["lat", "lon"],
                                              name="sm_surface_analysis")
        # sm_surface_analysis_da.to_netcdf(os.path.join(output_dir, "smap-L4-09km_rebuild_{}.nc".format(filename[15:28])))
        sm_surface_analysis_ensstd = ds_sm['sm_surface_analysis_ensstd'].values
        sm_surface_analysis_ensstd_da = xr.DataArray(sm_surface_analysis_ensstd, coords=[lat, lon], dims=["lat", "lon"],
                                                     name="sm_surface_analysis_ensstd")
        out_ds = xr.merge([sm_surface_analysis_da, sm_surface_analysis_ensstd_da])
        out_ds['time'] = datestamp
        out_ds = out_ds.expand_dims('time').set_coords('time')
        out_ds.to_netcdf(os.path.join(output_dir, "smap-L4-09km_rebuild_{}.nc".format(filename[15:28])))
        ds_list.append(out_ds)

concat_ds = xr.concat(ds_list, dim="time")
concat_ds.to_netcdf(os.path.join(output_dir, "smap-L4-09km-subset-nofilter.nc"))
