"""
Author: Nina del Rosario
Date: 8/4/2020
Script for evaluating SM for each in-situ station (HOBE & ICOS)
Status: In progress
"""
from datetime import datetime
import os
import sm_tools as tools
import sm_config as config
import sm_evaluation as evaluation
import xarray as xr
import pandas as pd
import warnings
from multiprocessing import Pool

output_root = "../test_output/csv_station_data"

evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'ERA5 0-1', 'ERA5 0-25', 'Sentinel-1',
                       'SMOS-BEC', 'SMOS-IC', 'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']

icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
evaluation_stations = icos_readers + ismn_readers

def export_station_data(dataset):
    dataset_data_dir = os.path.join(output_root, dataset)
    if not os.path.exists(dataset_data_dir):
        os.makedirs(dataset_data_dir)
    xr_file = config.dict_native_files[dataset]
    df = xr.open_dataset(xr_file)
    for station in evaluation_stations:
        network_name = station.network
        station_name = station.station
        station_name.replace(".", "-")
        lat = station.latitude
        lon = station.longitude
    if dataset == "ASCAT 12.5 TS":
        row = tools.find_nearest(config.dict_h115_coords['lat'], lat)[0]
        col = tools.find_nearest(config.dict_h115_coords[str(row)], lon)[0]
        df = df.sel(row=row, col=col).to_pandas()
    else:
        df = df.sel(lat=lat, lon=lon).to_pandas()
    df.to_csv(os.path.join(dataset_data_dir, "{}_{}.csv".format(network_name, station_name)))


if __name__ == '__main__':
    with Pool(5) as p:
        p.map(export_station_data, evaluation_datasets)