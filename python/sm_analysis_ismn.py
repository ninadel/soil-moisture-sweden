"""
Author: Nina del Rosario
Date: 6/3/2020
Script for comparing SM datasets to ISMN in-situ data
"""
from ascat import H115Ts
from datetime import datetime
import numpy
import os
import pandas
import ismn.interface as ismn
from pytesmo import temporal_matching, scaling, df_metrics, metrics
import sm_config as config
import sm_tools as tools

# Dictionary to set analyses to perform
# Use datasets_dict.json to change default parameters
ismn_analyses_dict = {
    "ASCAT 12.5 TS": {
        "analyze": True,
    },
    "GLDAS": {
        "analyze": True
    },
    "SMAP L4": {
        "analyze": False
    }
}

filter_product = True
ismn_data_scope = None

metrics_df_columns = ['timestamp', 'network', 'station', 'temp_scope', 'ismn_data_scope', 'product',
                      'product_data_scope', 'n', 'bias', 'rmsd', 'ubrmsd', 'pearsonr', 'pearsonr_p']
metrics_df = pandas.DataFrame(columns=metrics_df_columns)
os.mkdir(config.ismn_analysis_output_dir)

# config
analysis_startdate = datetime(2015, 4, 1)
analysis_enddate = datetime(2018, 12, 31, 23, 59)
analysis_queue = {}
for product, product_inputs in ismn_analyses_dict.items():
    if product_inputs['analyze']:
        analysis_queue[product] = product_inputs

for product, product_inputs in analysis_queue.items():
    temp_scope = analysis_startdate.strftime("%Y%m%d")+"_"+analysis_enddate.strftime("%Y%m%d")
    product_str = product.replace(' ', '-')
    product_metadata = config.datasets_dict[product]
    print("analyzing {}; temp_scope {}".format(product, temp_scope))
    # initialize product reader
    network_matched_df = pandas.DataFrame()
    if filter_product:
        product_data_scope = 'Filtered'
    else:
        product_data_scope = 'Unfiltered'
    product_reader = tools.get_product_reader(product, product_metadata)
    # filter product data by date
    # initiate ismn reader
    ISMN_reader = ismn.ISMN_Interface(config.ismn_input_dir)
    for station_object in ISMN_reader.stations_that_measure('soil moisture'):
        for ISMN_time_series in station_object.data_for_variable('soil moisture', min_depth=0, max_depth=0.1):
            network = ISMN_time_series.network
            station = ISMN_time_series.station
            print("analyzing {} * {} for {}".format(product, station, temp_scope))
            station_ts = ISMN_time_series.data.dropna()
            station_ts.rename(columns={'soil moisture':'ismn_ssm'}, inplace=True)
            station_ssm_data = station_ts[['ismn_ssm']]
            print(station, 'station_ts.shape', station_ts.shape)
            # get product data for station
            product_data = tools.get_product_data(lon=ISMN_time_series.longitude, lat=ISMN_time_series.latitude,
                                                  product=product, product_metadata=product_metadata,
                                                  product_reader=product_reader, filter_product=filter_product)
            filename = '{}_data_{}_{}.csv'.format(product_str, station, config.timestamp)
            product_data.to_csv(os.path.join(config.ismn_analysis_output_dir, filename), sep=",")
            print('product_data.shape', product_data.shape)
            product_data = product_data.loc[analysis_startdate:analysis_enddate]
            #data = data.loc[data['qc_ssm'].isin(qc_values)]
            print('product_data.shape after date filter', product_data.shape)
            # print('product_data.columns', product_data.columns)
            matched_data = temporal_matching.matching(product_data, station_ssm_data, window=1/24.)
            print('matched_data.shape', matched_data.shape)
            filename = 'matched_data_{}_{}_{}.csv'.format(station, product_str, config.timestamp)
            matched_data.to_csv(os.path.join(config.ismn_analysis_output_dir, filename), sep=",")
            # for now, not sure if only % products are scaled
            matched_rows = matched_data.shape[0]
            if matched_rows > 10:
                # scaling causing errors, hold off for now
                 # start future function
                metrics = tools.get_metrics(matched_data, product_metadata['sm_field'], 'ismn_ssm')
                bias = metrics[0]
                rmsd = metrics[1]
                ubrmsd = metrics[2]
                pearsonr = metrics[3]
                pearsonr_p = metrics[4]
                print("---")
                print("{} ssm * {} ssm metrics:".format(station, product))
                print("bias: {}, rmsd: {}, ubrmsd: {}, pearsonr: {}, pearsonr_p: {}, n: {}".format(bias, rmsd, ubrmsd, pearsonr, pearsonr_p, matched_rows))
                station_metrics_df = pandas.DataFrame([[config.timestamp, network, station, temp_scope, ismn_data_scope,
                                                        product_str, product_data_scope, matched_rows, bias, rmsd, ubrmsd,
                                                        pearsonr, pearsonr_p]], columns=metrics_df_columns)
                metrics_df = pandas.concat([metrics_df, station_metrics_df])
                # end future function
            else:
                print('{} matched rows. metrics not computed for station.'.format(matched_rows))
            filename = 'matched_data_{}_{}_{}_{}_{}_{}.csv'.format(network, station, ismn_data_scope, product_str,
                                                                   product_data_scope, config.timestamp)
            network_matched_df = pandas.concat([network_matched_df, matched_data])
    # network level analysis
    # start future function
    metrics = tools.get_metrics(network_matched_df, product_metadata['sm_field'], 'ismn_ssm')
    bias = metrics[0]
    rmsd = metrics[1]
    ubrmsd = metrics[2]
    pearsonr = metrics[3]
    pearsonr_p = metrics[4]
    matched_rows = network_matched_df.shape[0]
    print("---")
    print("{} ssm * {} ssm metrics:".format(network, product))
    print("bias: {}, rmsd: {}, ubrmsd: {}, pearsonr: {}, pearsonr_p: {}, n: {}".format(bias, rmsd, ubrmsd, pearsonr,
                                                                                       pearsonr_p, matched_rows))
    print("---")
    network_metrics_df = pandas.DataFrame([[config.timestamp, 'ISMN', 'All', temp_scope, ismn_data_scope,
                                            product_str, product_data_scope, matched_rows, bias, rmsd, ubrmsd,
                                            pearsonr, pearsonr_p]], columns=metrics_df_columns)
    metrics_df = pandas.concat([metrics_df, network_metrics_df])
    filename = 'matched-data_ISMN _all_{}_{}_{}_{}.csv'.format(ismn_data_scope, product_str, product_data_scope,
                                                            config.timestamp)
    network_matched_df.to_csv(os.path.join(config.ismn_analysis_output_dir, filename), sep=",")
    # # end future function
    # for timeframe in config.timeframes_dict.items():
    #     break
    #     # filter network matched data by timeframe
    #     # get product data for station lat/lon
    #     # match data (product is ref ts and in situ is second ts)
    #     # timeframe_metrics_df = pandas.DataFrame([[timestamp, 'ICOS', None, temp_scope, ismn_data_scope, product,
    #     #                                           product_data_scope, matched_rows, bias, rmsd, ubrmsd, pearsonr,
    #     #                                           pearsonr_p]], columns=metrics_df_columns)
    #     # metrics_df = pandas.concat([metrics_df, timeframe_metrics_df])
    #     pass

filename = 'metrics_ISMN_Products_{}_{}.csv'.format(product_data_scope, config.timestamp)
metrics_df.to_csv(os.path.join(config.ismn_analysis_output_dir, filename))

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

