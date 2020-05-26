import sm_tools
import datasets
import json

# station_dict = get_station_dict(input_dir)
# sm-tools.get_station_dict(r'C:\git\nordic-insitu-sm-data')
with open('timeframe_dict.json', 'r') as f:
    timeframes = json.load(f)

# print(timeframes)

dataset_dict = {}

# start reader for each reference dataset and append dataset to dictionary
# start reader for each evaluation dataset and append dataset to dictionary

# create empty metric dataset for all comparisons
    # headings: dataset 1, dataset 2, network, station, timeframe, metric 1, metric 2, metric 3, metric 4
# for each evaluation dataset
    # for each reference dataset
            # create empty comparison dataset for matched data
            # headings: network, station, timestamp, dataset 1 name, dataset 1 data, dataset 2 name, dataset 2 data
        # for each network in station dict
            # for each station in station_dict
                # get evaluation dataset for station
                # get reference dataset for station
                # temporal match datasets
                # concat station matched datasets to comparison dataset
        # calculate metrics across all data, network = all, station = all, timeframe = all
        # calculate metrics across networks, network = network, station = network, timeframe = all
            # for each network, create a filtered dataframe
            # calculate metrics
        # calculate metrics across all stations, network = network, station = station, timeframe = all
            # for each sstation, create a filtered dataframe
            # calculate metrics
        # calculate metrics for each timeframe across all data, network = all, station = all, timeframe = timeframe
            # for each timeframe, create a filtered dataframe
            # calculate metrics
        # calculate metrics for each timeframe across all Sweden, network = ICOS, station = all, timeframe = timeframe
            # for each timeframe, create a filtered dataframe
            # calculate metrics

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

