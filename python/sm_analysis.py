"""
Author: Nina del Rosario
Date: 5/25/2020
Script for analyzing SM datasets
"""
from datetime import datetime
import sm_tools as tools
import sm_config as config
import sm_evaluation as evaluation

# Dictionary which turns on/off product analyses
evaluation_dict = {
    "ASCAT 12.5 TS": False,
    "ASCAT SM-OBS-2": False,    # not supported yet
    "CCI Active": False,     # not supported yet
    "CCI Passive": False,    # not supported yet
    "CCI Combined": False,
    "GLDAS": True,
    "Sentinel-1": False,     # not supported yet
    "SMAP L3": False,
    "SMAP L4": False,
    "SMOS-IC": False,
    "SMOS-BEC": False    # not supported yet
}

insitu_evaluation = True
anomaly_evaluation = False

icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
# use this as a parameter below if you want to analyze both ICOS and ISMN
reference_list = icos_readers + ismn_readers

analysis_output_folder = r"../analysis_output"

if insitu_evaluation:
    # for first argument, use icos_readers, ismn_readers, or reference_list
    insitu_evaluation_results = evaluation.evaluate(icos_readers, evaluation_dict, startdate=datetime(2015, 4, 1),
                                                    enddate=datetime(2018, 12, 31, 23, 59),
                                                    output_folder=analysis_output_folder, anomaly=anomaly_evaluation)
    print(insitu_evaluation_results)