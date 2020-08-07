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

def evaluate_stations(dataset):
    # for station in stations
        # import reference csv
        # import dataset csv
        # match dataset
        # for each timeframe
            # calculate metrics
    pass