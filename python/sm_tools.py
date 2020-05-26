import ismn
import pandas
import pytesmo


# based on a directory of in situ text files, create a dictionary of stations
def get_station_dict(input_dir):
    # return dictionary
    # see "C:\git\nordic-insitu-sm-data\ismn-network-processing.ipynb" for reference
    pass

# get location data (lon, lat, ts)
def get_location_data(lon, lat, ts):
    # get data
    # return dataframe
    pass

# get data for all network/stations in a dictionary
def compare_datasets(eval_dataset, ref_dataset, timeframe=None):
    """""
    eval_dataset: dataset of product to be evaluated
    ref_dataset: reference dataset
    timeframe: timeframe dictionary, default is None
    """""
    # initiate matched dataset object
    matched_data = []
    # get metrics on matched datset object
    metrics = matched_data.get_metrics()
    return metrics


