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

output_root = "../test_output/_data"

evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'ERA5 0-1', 'ERA5 0-25', 'Sentinel-1',
                       'SMOS-BEC', 'SMOS-IC', 'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']

icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
evaluation_stations = icos_readers + ismn_readers

def export_station_data(dataset):
    station_data_dir = os.path.join(output_root, "station_data")
    dataset_data_dir = os.path.join(output_root, dataset)
    for station in evaluation_stations:
        station_name = station.station
        network_name = station.network
        station_data_file = os.path.join(station_data_dir, '{}_{}.csv'.format(network_name, station_name))
        if not os.path.exists(station_data_file):
            pass


# icos_readers = tools.get_icos_readers(config.icos_input_dir)
# ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
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

# if __name__ == '__main__':
#     with Pool(5) as p:
#         p.map(export_station_data, evaluation_datasets)