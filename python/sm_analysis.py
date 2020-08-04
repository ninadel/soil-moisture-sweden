"""
Author: Nina del Rosario
Date: 5/25/2020
Script for analyzing SM datasets
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

evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC', 'SMOS-IC',
                       'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']

def evaluate_dataset(evaluation_dataset_name):
    def statement_str(statement):
        evaluation_str = "{} {} (anomaly: {})".format(evaluation_dataset_name, reference_dataset_name,
                                                      evaluation_dict['anomaly'])
        statement_str = "{}: {}".format(statement, evaluation_str)
        return statement_str
    anomaly_evaluation = [False, True]
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
                                          "{} metrics.csv".format(evaluation_dataset_name)))
    except:
        warning_message = statement_str("metrics output failed")
        warnings.warn(warning_message)

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(evaluate_dataset, evaluation_datasets)


# for dataset_name, dataset_file in config.dict_quarterdeg_files.items():
#     evaluation_dataset_name = dataset_name
#     if evaluation_dataset_name != reference_dataset_name:
#         evaluation_dict = grid_evaluation_dict.copy()
#         evaluation_dict['reference'] = (reference_dataset_name, reference_dataset)
#         evaluation_dataset = xr.open_dataset(dataset_file)
#         evaluation_dict['evaluation'] = (evaluation_dataset_name, evaluation_dataset)
#         evaluation_dict['anomaly'] = False
#         evaluation_str = "{} (anomaly: {})".format(evaluation_dataset_name, evaluation_dict['anomaly'])
#         print("trying {}".format(evaluation_str))
#         try:
#             evaluation.evaluate_grid_xr(evaluation_dict)
#         except:
#             warnings.warn("could not process evaluation for {}".format(evaluation_str))
#         evaluation_dict['anomaly'] = True
#         evaluation_str = "{} (anomaly: {})".format(evaluation_dataset_name, evaluation_dict['anomaly'])
#         print("trying {}".format(evaluation_str))
#         try:
#             evaluation.evaluate_grid_xr(evaluation_dict)
#         except:
#             warnings.warn("could not process evaluation for {}".format(evaluation_str))

# # Dictionary which turns on/off product analyses
# evaluation_dict = {
#     "ASCAT 12.5 TS": True,
#     "CCI Active": True,
#     "CCI Passive": True,
#     "CCI Combined": True,
#     "ERA5 0-1": True,
#     "ERA5 0-25": True,
#     "GLDAS": True,
#     "Sentinel-1": True,
#     "SMAP L3": True,
#     "SMAP L3 Enhanced": True,
#     "SMAP L4": True,
#     "SMOS-IC": True,
#     "SMOS-BEC": True
# }

# # icos_readers = tools.get_icos_readers(config.icos_input_dir)
# # ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
# # use this as a parameter below if you want to analyze both ICOS and ISMN
# reference_list = icos_readers + ismn_readers
#
# analysis_output_root = r"../analysis_output"
# analysis_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# analysis_results_folder = os.path.join(analysis_output_root, "{}_evaluation".format(analysis_timestamp))
# os.mkdir(analysis_results_folder)
# metrics_filename = "evaluation_metrics_{}.csv".format(analysis_timestamp)
# startdate = datetime(2015,4,1)
# enddate = datetime(2018, 12, 31, 23, 59)
#
# results = evaluation.evaluate_shuffle(icos_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=False)
# results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
# results = evaluation.evaluate_shuffle(icos_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=True,
#                               metrics_df=results)
# results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
# results = evaluation.evaluate_shuffle(ismn_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=False,
#                               metrics_df=results)
# results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
# results = evaluation.evaluate_shuffle(ismn_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=True,
#                               metrics_df=results)
# results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
#
#
# icos_results = evaluation.evaluate_network_product(icos_readers, 'ASCAT 12.5 TS', startdate=datetime, enddate=enddate)