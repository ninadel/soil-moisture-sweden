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
output_root = r"../analysis_output/{} grid evaluation {}".format(reference_dataset_name,
                                                                 datetime.now().strftime("%Y%m%d%H%M%S"))

grid_evaluation_dict = {
    'locations': config.dict_swe_gldas_points,
    'reference': (reference_dataset_name, reference_dataset),
    'evaluation': (None, None),
    'start_date': None,
    'end_date': None,
    'match_window': 1/24., #1 hour
    'anomaly': None,
    'evaluate_timeframes': True,
    'export_ts': False,
    'output_root': output_root,
    'verbose': False
}

evaluation_datasets = ['ASCAT 12.5 TS']
# evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC', 'SMOS-IC',
#                        'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']

def evaluate_dataset(evaluation_dataset_name):
    def statement_str(statement):
        evaluation_str = "{} {} (anomaly: {})".format(evaluation_dataset_name, reference_dataset_name,
                                                      evaluation_dict['anomaly'])
        statement_str = "{}: {}".format(statement, evaluation_str)
        return statement_str
    evaluation_metrics = []
    for anomaly_bool in anomaly_evaluation:
        evaluation_dict = grid_evaluation_dict.copy()
        evaluation_dataset_file = config.dict_quarterdeg_files[evaluation_dataset_name]
        evaluation_dataset = xr.open_dataset(evaluation_dataset_file)
        evaluation_dict['evaluation'] = (evaluation_dataset_name, evaluation_dataset)
        evaluation_dict['anomaly'] = anomaly_bool
        print(statement_str("trying"))
        try:
            absolute_metrics = evaluation.evaluate_grid_xr(evaluation_dict)
            for timeframe, metrics_df in absolute_metrics.items():
                evaluation_metrics.append(metrics_df)
            print(statement_str("done"))
        except:
            warning_message = statement_str("evaluation failed")
            warnings.warn(warning_message)
    try:
        metrics_merge = pd.concat(evaluation_metrics, ignore_index=True)
        metrics_merge.to_csv(os.path.join(evaluation_dict['output_root'],
                                          "{} metrics.csv".format(evaluation_dataset_name)), index=False)
    except:
        warning_message = statement_str("metrics output failed")
        warnings.warn(warning_message)

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(evaluate_dataset, evaluation_datasets)