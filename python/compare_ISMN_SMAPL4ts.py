"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/26/2020
Script for analyzing SM datasets
"""

import ismn.interface as ismn
from smap_io import SMAPTs
import pytesmo.temporal_matching as temp_match
import pytesmo.scaling as scaling
import pytesmo.df_metrics as df_metrics
import pytesmo.metrics as metrics

import os
import matplotlib.pyplot as plt

# ref_data_folder = r"C:\git\soil-moisture-sweden\testdata\ismn\multinetwork\header_values"
ref_data_folder = r"C:\git\soil-moisture-sweden\in_situ_data\HOBE_Data_2015-2018"

eval_data_folder = r"C:\git\soil-moisture-sweden\test_output_data\test_smapL4_reshuffle"

eval_grid_folder = r"C:\git\soil-moisture-sweden\test_output_data\test_smapL4_reshuffle"
eval_grid_file = 'grid.nc'
eval_static_layers_folder = None

# init the eval data reader with the paths
eval_data_reader = SMAPTs(eval_data_folder)

# # init the eval data reader with the paths
# eval_data_reader = ascat.H113Ts(eval_data_folder, eval_grid_folder,
#                                      grid_filename='TUW_WARP5_grid_info_2_3.nc',
#                                      static_layer_path=eval_static_layers_folder)
eval_data_reader.read_bulk = True

# Initialize ISMN reader
ISMN_reader = ismn.ISMN_Interface(ref_data_folder)


i = 0

label_eval = 'sm_surface_analysis'
label_ref = 'insitu_sm'

# this loops through all stations that measure soil moisture
for station in ISMN_reader.stations_that_measure('soil moisture'):
    # this loops through all time series of this station that measure soil moisture
    # between 0 and 0.1 meters
    for ISMN_time_series in station.data_for_variable('soil moisture', min_depth=0, max_depth=0.1):
        if ISMN_time_series.station != "1.02":
            # eval_time_series = eval_data_reader.read(ISMN_time_series.longitude,
            #                                           ISMN_time_series.latitude,
            #                                           mask_ssf=True,
            #                                           mask_frozen_prob=80,
            #                                           mask_snow_prob=80)

            print('processing', ISMN_time_series.station)
            eval_time_series = eval_data_reader.read(ISMN_time_series.longitude,
                                                      ISMN_time_series.latitude)

            # focus only on the relevant variable
            # print(type(eval_time_series))
            # print(eval_time_series[label_eval])
            eval_time_series[label_eval] = eval_time_series[label_eval]

            # drop nan values before doing any matching
            eval_time_series = eval_time_series.dropna()

            ISMN_time_series.data = ISMN_time_series.data.dropna()

            # rename the soil moisture column in ISMN_time_series.data to insitu_sm
            # to clearly differentiate the time series when they are plotted together
            ISMN_time_series.data.rename(columns={'soil moisture':label_ref}, inplace=True)

            # get ISMN data that was observerd within +- 1 hour(1/24. day) of the ASCAT observation
            # do not include those indexes where no observation was found
            matched_data = temp_match.matching(eval_time_series, ISMN_time_series.data,
                                                    window=1 / 24.)
            # matched ISMN data is now a dataframe with the same datetime index
            # as eval_time_series and the nearest insitu observation

            # continue only with relevant columns
            matched_data = matched_data[[label_eval, label_ref]]

            # the plot shows that ISMN and ASCAT are observed in different units
            matched_data.plot(figsize=(15, 5), secondary_y=[label_eval],
                              title='temporally merged data')
            plt.show()

            # this takes the matched_data DataFrame and scales all columns to the
            # column with the given reference_index, in this case in situ
            scaled_data = scaling.scale(matched_data, method='lin_cdf_match',
                                             reference_index=1)

            # now the scaled ascat data and insitu_sm are in the same space
            scaled_data.plot(figsize=(15, 5), title='scaled data')
            plt.show()

            plt.scatter(scaled_data[label_eval].values, scaled_data[label_ref].values)
            plt.xlabel(label_eval)
            plt.ylabel(label_ref)
            plt.show()

            # calculate correlation coefficients, RMSD, bias, Nash Sutcliffe
            x, y = scaled_data[label_eval].values, scaled_data[label_ref].values

            print("ISMN time series:", ISMN_time_series)
            print("compared to")
            print(eval_time_series)
            print("Results:")

            # df_metrics takes a DataFrame as input and automatically
            # calculates the metric on all combinations of columns
            # returns a named tuple for easy printing
            print(df_metrics.pearsonr(scaled_data))
            print("Spearman's (rho,p_value)", metrics.spearmanr(x, y))
            print("Kendalls's (tau,p_value)", metrics.kendalltau(x, y))
            print(df_metrics.kendalltau(scaled_data))
            print(df_metrics.rmsd(scaled_data))
            print("Bias", metrics.bias(x, y))
            print("Nash Sutcliffe", metrics.nash_sutcliffe(x, y))
        
        
    i += 1

    # only show the first 2 stations, otherwise this program would run a long time
    # and produce a lot of plots
    if i >= 2:
        break


