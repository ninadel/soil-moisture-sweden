"""
Author: Nina del Rosario
Date: 5/25/2020
Script for analyzing SM datasets
"""

import sm_tools
import sm_datasets
import json

# directory that has in situ data, used to get stations
# in_situ_dir = ''

# get stations
# sm_tools.get_station_dict(r'C:\git\nordic-insitu-sm-data')

# load timeframe_dict from external file
with open('timeframes_dict.json', 'r') as t:
    timeframes_dict = json.load(t)

# dictionary levels: function, product, year, reader (extra dict for ascat?)
with open('datasets_dict.json', 'r') as d:
    datasets_dict = json.load(d)

print(datasets_dict)

# initiate readers and add to datasets dict
# initiate reader
# add to dataset_dict
    # "name": reader obj

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

