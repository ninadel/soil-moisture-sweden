"""
Author: Nina del Rosario
Date: 1/24/2021
Status: this file may be obsolete? might have been replaced by sm_gridevaluation.py
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

evaluation_dataset_name = 'ERA5 0-1'

matched_data = {
    'SMAP L4': None,
    'ASCAT 12.5 TS': None,
    'SMAP L3 Enhanced': None,
    'GLDAS': None,
    'Sentinel-1': None,
    'SMOS-BEC': None,
    'SMOS-IC': None,
    'SMAP L3': None,
    'CCI Combined': None,
    'CCI Passive': None,
    'CCI Active': None
}



start_date = None
end_date = None

timefilters = (
    (None, None, 2015),
    (None, None, 2016),
    (None, None, 2017),
    (None, None, 2018),
    (None, "spring", 2015),
    (None, "summer", 2015),
    (None, "fall", 2015),
    (None, "winter", 2016),
    (None, "spring", 2016),
    (None, "summer", 2016),
    (None, "fall", 2016),
    (None, "winter", 2017),
    (None, "spring", 2017),
    (None, "summer", 2017),
    (None, "fall", 2017),
    (None, "winter", 2018),
    (None, "spring", 2018),
    (None, "summer", 2018),
    (None, "fall", 2018),
    (1,None,None),
    (2,None,None),
    (3,None,None),
    (4,None,None),
    (5,None,None),
    (6,None,None),
    (7,None,None),
    (8,None,None),
    (9,None,None),
    (10,None,None),
    (11,None,None),
    (12,None,None),
    (1,None,2016),
    (1,None,2017),
    (1,None,2018),
    (2,None,2016),
    (2,None,2017),
    (2,None,2018),
    (3,None,2016),
    (3,None,2017),
    (3,None,2018),
    (4,None,2015),
    (4,None,2016),
    (4,None,2017),
    (4,None,2018),
    (5,None,2015),
    (5,None,2016),
    (5,None,2017),
    (5,None,2018),
    (6,None,2015),
    (6,None,2016),
    (6,None,2017),
    (6,None,2018),
    (7,None,2015),
    (7,None,2016),
    (7,None,2017),
    (7,None,2018),
    (8,None,2015),
    (8,None,2016),
    (8,None,2017),
    (8,None,2018),
    (9,None,2015),
    (9,None,2016),
    (9,None,2017),
    (9,None,2018),
    (10,None,2015),
    (10,None,2016),
    (10,None,2017),
    (10,None,2018),
    (11,None,2015),
    (11,None,2016),
    (11,None,2017),
    (11,None,2018),
    (12,None,2015),
    (12,None,2016),
    (12,None,2017),
    (12,None,2018)
)

for timefilter in timefilters:
    print(timefilter)

    # timefilters:
# 2015
# 2016
# 2017
# 2018
# 2015 spring
# 2015 summer
# 2015 fall
# 2016 winter
# 2016 spring
# 2016 summer
# 2016 fall
# 2017 winter
# 2018

grid_evaluation_dict = {
    'locations': config.dict_swe_gldas_points,
    'reference': (reference_dataset_name, reference_dataset),
    'evaluation': (None, None),
    'start_date': None,
    'end_date': None,
    'match_window': 1/24., #1 hour
    'anomaly': None,
    'evaluate_timeframes': True,
    'export_ts': True,
    'output_root': output_root,
    'verbose': False
}

evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC', 'SMOS-IC',
                       'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']

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