"""
Author: Nina del Rosario
Date: 8/4/2020
Script for evaluating SM for each GLDAS cell in Sweden using ERA5 as a reference
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

reference_dataset_name = 'ERA5 0-1'
reference_file = config.dict_quarterdeg_files[reference_dataset_name]
reference_dataset = xr.open_dataset(reference_file)
anomaly_evaluation = [False, True]
output_root = r"../test_output_data/grid_evaluation_data".format(reference_dataset_name,
                                                                 datetime.now().strftime("%Y%m%d%H%M%S"))

grid_dataexport_dict = {
    'locations': config.dict_swe_gldas_points,
    'reference': (reference_dataset_name, reference_dataset),
    'evaluation': (None, None),
    'start_date': None,
    'end_date': None,
    'match_window': 1/24., #1 hour
    'anomaly': None,
    'output_root': output_root,
    'verbose': False
}

evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC', 'SMOS-IC',
                       'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']

def grid_export_data(evaluation_dataset_name):
    pass

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(grid_export_data, evaluation_datasets)