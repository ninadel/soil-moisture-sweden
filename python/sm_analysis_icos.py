"""
Author: Nina del Rosario
Date: 5/31/2020
Script for analyzing SM datasets
"""
from ascat import H115Ts
from icos import ICOSTimeSeries
import json
from pandas import DataFrame, read_csv
import numpy
from pytesmo import temporal_matching, scaling, df_metrics, metrics
import sm_tools
import sm_datasets

# Use dictionary to set analyses to perform, input data locations, and parameters
icos_analyses_dict = {
    "ASCAT 12.5 TS" : {
        "analyze": True,
        "ts_data_dir": r"",
        "grid_dir": r"",
        "grid_file": "",
        "static_layers_dir": None,  # optional
        "parameters": None  # optional
    },
    "GLDAS": {
    },
    "SMAP L4": {
    }
}

# open external dictionaries
# dictionary which defines timeframes to analyze
with open('timeframes_dict.json', 'r') as f:
    timeframes_dict = json.load(f)

with open('icos_dict.json', 'r') as f:
    icos_dict = json.load(f)

# directory that has ICOS in situ data, used to get stations
icos_input_dir = r"..\icos_data"
icos_files = sm_tools.get_icos_stations(icos_input_dir)

metrics_df = DataFrame(columns=['network', 'station', 'temp_scope', 'data_scope', 'product', 'n', 'bias', 'rmsd', 'ubrmsd', 'pearsonr', 'pearson r p-value'])

for product, product_inputs in icos_analyses_dict.items():
    matched_df = DataFrame(columns=['datetime_utc', product, 'icos_ssm', 'icos_ssm_qc'])
    for station, file in icos_files.items():
        file_data = read_csv(file, index_col=0)
        # get insitu data, dropna, filter to qc values of 0 and 3
        station_metadata = icos_dict[station]
        station_ts = ICOSTimeSeries(station_metadata, file_data)
        print(station_ts.ssm_data.shape)
        ssm_filtered_ts = sm_tools.filter_icos_data(station_ts.ssm_data, qc_values=[0, 3], dropna=True)
        # get product data for station lat/lon
        print(ssm_filtered_ts.shape)
        product_data = sm_tools.get_product_data(station_ts.longitude, station_ts.latitude, product_inputs)
        # match data (product is ref ts and in situ is second ts)
        break


# {"ASCAT 12.5 TS" :
#       {
#           "ts_dir": "C:\\git\\soil-moisture-sweden\\sm_sample_files\\ascat-h115-ts-2019",
#           "grid_dir": "C:\\git\\soil-moisture-sweden\\ascat_ts_aux\\warp5_grid",
#           "grid_file": "TUW_WARP5_grid_info_2_3.nc",
#           "static_layers_dir": "C:\\git\\soil-moisture-sweden\\sm_sample_files\\h-saf_static_layers\\static_layer",
#           "reader_name": "ascat_12-5_ts",
#           "reader_class": "H115Ts",
#           "reader_params": "(ts_dir, grid_dir, grid_filename=grid_file, static_layer_path=static_layers_dir)",
#           "data_str": ".data"
#       }
#   }



# create metrics dataframe
# create log txt file
# for eval_name, eval_dataset in datasets dict
    # for ref_name, ref_dataset in datasets dict
        # print to log
        # create comparison matched dataframe: network, station, dataset 1 name, dataset 2 name, datetime, dataset 1 values, dataset 2 values
        # for network name, network dict in station dict
            # print to log
            # create network matched dataframe: network, station, dataset 1 name, dataset 2 name, datetime, dataset 1 values, dataset 2 values
            # for station_name, station_dict in network_dict
                # print to log
                # lon = station lon
                # lat = station lat
                # get reference ts
                # get evaluation ts
                    # NOTE: evaluation ts call is different between ASCAT TS (.data) and reshuffle TS
                # get matched dataset for station
                # print to log: matched record count
                # get metrics for station comparison
                # print to log: station metrics
                # add to metrics dataframe
                # create station matched dataframe: network, station, dataset 1 name, dataset 2 name, datetime, dataset 1 values, dataset 2 values
                # append station matched dataframe to network matched dataframe
                # print to log
            # get metrics for network comparison
            # print to log: network metrics
            # add to metrics dataframe
            # append network matched dataframe to comparison matched dataframe
            # print to log
        # get metrics for comparison (overall)
        # get timestamp
        # write comparison dataframe to csv
        # print to log
        # for timeframe, values in timeframe_dict
            # print to log
            # get filtered dataframe from comparison matched dataframe
            # print to log: filtered record count
            # get metrics for timeframe comparison
            # print to log: timeframe metrics
            # add to metrics dataframe
            # print to log

# print metrics

# get timestamp
# write metrics to csv

# calc anomalies
# https://github.com/TUW-GEO/pytesmo/blob/master/pytesmo/time_series/anomaly.py

# triple collocation
# https://github.com/TUW-GEO/pytesmo/blob/master/docs/Triple%20collocation.rst

### CODE
# snr, err, beta = metrics.tcol_snr(x, y, z)
# print "Error of x approach 1: {:.4f}, approach 2: {:.4f}, true: {:.4f}".format(e_x, err[0], sig_err_x)
# print "Error of y approach 1: {:.4f}, approach 2: {:.4f}, true: {:.4f}".format(e_y, err[1], sig_err_y)
# print "Error of z approach 1: {:.4f}, approach 2: {:.4f}, true: {:.4f}".format(e_z, err[2], sig_err_z)

### OUTPUT
# Error of x approach 1: 0.0200, approach 2: 0.0199, true: 0.0200
# Error of y approach 1: 0.0697, approach 2: 0.0700, true: 0.0700
# Error of z approach 1: 0.0399, approach 2: 0.0400, true: 0.0400

### CODE
# print "scaling parameter for y estimated: {:.2f}, true:{:.2f}".format(1/beta[1], beta_y)
# print "scaling parameter for z estimated: {:.2f}, true:{:.2f}".format(1/beta[2], beta_z)

### OUTPUT
## scaling parameter for y estimated: 0.90, true:0.90
## scaling parameter for z estimated: 1.60, true:1.60

### CODE
# y_beta_scaled = y * beta[1]
# z_beta_scaled = z * beta[2]
# plt.plot(coord, x, alpha=0.3, label='x')
# plt.plot(coord, y_beta_scaled, alpha=0.3, label='y beta scaled')
# plt.plot(coord, z_beta_scaled, alpha=0.3, label='z beta scaled')
# plt.plot(coord, signal, 'k', label='$\Theta$')
# plt.legend()
# plt.show()

