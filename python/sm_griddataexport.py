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
from pytesmo import temporal_matching
from pytesmo.time_series.anomaly import calc_anomaly
from multiprocessing import Pool

ref_dataset_name = 'ERA5 0-1'
ref_file = config.dict_quarterdeg_files[ref_dataset_name]
ref_dataset = xr.open_dataset(ref_file)
start_date = datetime(2015,4,1)
end_date = datetime(2018,23,59,59)
output_root = r"../test_output_data/grid_evaluation_data"
locations = config.dict_swe_gldas_points

grid_dataexport_dict = {
    'locations': config.dict_swe_gldas_points,
    'reference': (ref_dataset_name, ref_dataset),
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

def grid_export_data(eval_dataset_name):
    ref_ts_folder = os.path.join(output_root, eval_dataset_name, "{}_ts".format(ref_dataset_name))
    eval_ts_folder = os.path.join(output_root, eval_dataset_name, "{}_ts".format(eval_dataset_name))
    matched_folder = os.path.join(output_root, eval_dataset_name, "{}_{}-matched".format(ref_dataset_name,
                                                                                       eval_dataset_name))
    os.makedirs(ref_ts_folder)
    os.mkdir(eval_ts_folder)
    os.mkdir(matched_folder)
    eval_dataset = xr.open_dataset(config.dict_quarterdeg_files[eval_dataset_name])
    ref_sm_field = config.dict_product_fields[ref_dataset_name]['sm_field']
    eval_sm_field = config.dict_product_fields[eval_dataset_name]['sm_field']
    ref_sm_data = ref_dataset[ref_sm_field]
    eval_sm_data = eval_dataset[eval_sm_field]
    for loc, loc_data in locations.items():
        lon = loc_data['longitude']
        lat = loc_data['latitude']
        ref_ts = ref_sm_data.sel(time=slice(start_date, end_date), lat=lat, lon=lon).to_pandas()
        eval_ts = eval_sm_data.sel(time=slice(start_date, end_date), lat=lat, lon=lon).to_pandas()
        ref_ts.rename('ref_sm', inplace=True)
        eval_ts.rename('eval_ts', inplace=True)
        ref_abs_ts = ref_ts.to_frame()
        ref_anom_ts = calc_anomaly(ref_ts).to_frame()
        eval_abs_ts = eval_ts.to_frame()
        eval_anom_ts = calc_anomaly(eval_ts).to_frame()
        matched_abs_data = temporal_matching.matching(ref_abs_ts, eval_abs_ts, window=1/24.)
        matched_anom_data = temporal_matching.matching(ref_anom_ts, eval_anom_ts, window=1/24.)
        ref_abs_ts.to_csv(ref_ts_folder,"{}_{}_abs_ts.csv".format(ref_dataset_name,loc))
        ref_anom_ts.to_csv(ref_ts_folder,"{}_{}_anom_ts.csv".format(ref_dataset_name,loc))
        eval_abs_ts.to_csv(eval_ts_folder,"{}_{}_abs_ts.csv".format(eval_dataset_name,loc))
        eval_anom_ts.to_csv(eval_ts_folder,"{}_{}_anom_ts.csv".format(eval_dataset_name,loc))
        matched_abs_data.to_csv(matched_folder,"{}_{}_{}_abs_matched.csv".format(ref_dataset_name,eval_dataset_name,
                                                                                   loc))
        matched_anom_data.to_csv(matched_folder,"{}_{}_{}_anom_matched.csv".format(ref_dataset_name,eval_dataset_name,
                                                                                   loc))
        break
    break

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(grid_export_data, evaluation_datasets)