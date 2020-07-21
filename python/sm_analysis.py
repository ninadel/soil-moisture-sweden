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

# Dictionary which turns on/off product analyses
evaluation_dict = {
    "ASCAT 12.5 TS": True,
    "CCI Active": True,
    "CCI Passive": True,
    "CCI Combined": True,
    "ERA5 0-1": True,
    "ERA5 0-25": True,
    "GLDAS": True,
    "Sentinel-1": True,
    "SMAP L3": True,
    "SMAP L3 Enhanced": True,
    "SMAP L4": True,
    "SMOS-IC": True,
    "SMOS-BEC": True
}

icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
# use this as a parameter below if you want to analyze both ICOS and ISMN
reference_list = icos_readers + ismn_readers

analysis_output_root = r"../analysis_output"
analysis_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
analysis_results_folder = os.path.join(analysis_output_root, "{}_evaluation".format(analysis_timestamp))
os.mkdir(analysis_results_folder)
metrics_filename = "evaluation_metrics_{}.csv".format(analysis_timestamp)
startdate = datetime(2015,4,1)
enddate = datetime(2018, 12, 31, 23, 59)

results = evaluation.evaluate(icos_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=False)
results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
results = evaluation.evaluate(icos_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=True,
                              metrics_df=results)
results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
results = evaluation.evaluate(ismn_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=False,
                              metrics_df=results)
results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
results = evaluation.evaluate(ismn_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=True,
                              metrics_df=results)
results.to_csv(os.path.join(analysis_results_folder, metrics_filename))


# icos_results = evaluation.evaluate_network_product(icos_readers, 'ASCAT 12.5 TS', startdate=datetime, enddate=enddate)