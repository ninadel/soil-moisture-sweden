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

evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'ERA5 0-1', 'ERA5 0-25', 'Sentinel-1',
                       'SMOS-BEC', 'SMOS-IC', 'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']

def evaluate_csv_station(dataset):
    # for station in stations
        # import reference csv
        # import dataset csv
        # match dataset
        # for each timeframe
            # calculate metrics
    pass

def evaluation_csv_network(dataset):
    def get_new_network_metrics_df():
        metrics_df = pd.DataFrame(columns=['network', 'station', 'lon', 'lat', 'eval_dataset', 'timefilter', 'anomaly',
                                           'pearson_r', 'pearson_r_p-value', 'bias', 'rmsd', 'ubrmsd', 'n',
                                           'pearson_sig'])
        return metrics_df
    def get_network_metrics_row():
        metrics_row = {'network': network, 'station': station, 'lon': lon, 'lat': lat, 'eval_dataset': dataset,
                       'timefilter': timefilter, 'anomaly': anomaly}
        return metrics_row
    dataset_folder = config.dict_product_inputs[dataset]['csv_stations']
    pass