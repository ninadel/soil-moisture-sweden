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