import ismn
import pandas

# based on a directory of in situ text files, create a dictionary of stations
def get_station_dict(input_dir):
    # return dictionary
    # see "C:\git\nordic-insitu-sm-data\ismn-network-processing.ipynb" for reference
    pass

# get data for all network/stations in a dictionary
def get_global_data(dict, ts):
    # start global dataframe
    # get networks from dict
    # for each network
        # get network data
        # add network column
        # concat to global dataframe
    # get network data
    # add network column
    # concat network dataframes
    pass

# get network data (network, ts)
def get_network_data(network, ts):
    # start network dataframe
    # get stations from dict
    # for each station
        # get station data
        # add station column
        # concat to network dataframe
    pass

# get station data (station, ts)
def get_station_data(station, ts):
    # get lon and lat from dictionary
	# get location data (lon = station['lon'], lat = station['lat', ts)
	pass

# get location data (lon, lat, ts)
def get_location_data(lon, lat, ts):
    # get data
    # return dataframe
    pass