"""
Author: Nina del Rosario
Date: 8/4/2020
Script for evaluating SM for each GLDAS cell in Sweden using ERA5 as a reference
UPDATE_DESCRIPTION
"""
from datetime import datetime
import os
import sm_config as config
import xarray as xr
from multiprocessing import Pool

start_date = datetime(2015,4,1)
end_date = datetime(2018,12,31,23,59,59)
output_root = r"../test_output_data/grid_sm_data"
locations = config.dict_swe_gldas_points

export_datasets = ['ERA5 0-1', 'SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC',
                   'SMOS-IC', 'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']


def grid_export_data(dataset_name):
    dataset_folder = os.path.join(output_root,dataset_name)
    os.makedirs(dataset_folder)
    dataset = xr.open_dataset(config.dict_quarterdeg_files[dataset_name])
    sm_field = config.dict_product_fields[dataset_name]['sm_field']
    sm_data = dataset[sm_field]
    for loc, loc_data in locations.items():
        print(dataset_name,loc)
        lon = loc_data['longitude']
        lat = loc_data['latitude']
        ts = sm_data.sel(time=slice(start_date, end_date), lat=lat, lon=lon).to_pandas()
        ts.rename('sm', inplace=True)
        ts = ts.to_frame()
        ts.to_csv(os.path.join(dataset_folder, "{}_{}.csv".format(dataset_name,loc)))

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(grid_export_data, export_datasets)