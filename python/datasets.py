# dataset class
class Dataset(object):
    """
    Parameters
        data: pandas dataframe
        network: in-situ network name
        station: in-situ station name
    """

    def __init__(self, data, network=None, station=None):
        self.data = data
        self.network = network
        self.station = station


class TSDataset(Dataset):
    """""
    class for handling time series for a single station
    """""

    def __init__(self, data, network, station):
        super().__init__(data, network, station)

    def get_timeframe_data(self, year_filter=None, month_filter=None):
        """
        year_filter = list of years
        month_filter = list of months
        """

        if type(year_filter) is list:
            # filter based on year
            pass
        else:
            if type(year_filter) is str:
                year_filter = int(year_filter)
            # filter based on year

        if type(month_filter) is list:
            # filter based on month
            pass
        else:
            if type(month_filter) is str:
                month_filter = int(month_filter)
            # filter based on month

    def get_date_range(self):
        # from timestamps get start date
        # return [start date, end date]
        pass


class MatchedDataset(TSDataset):
    """""
    class for handling temporally matched data
    """""

    def __init__(self, data, network, station, eval_dataset=None, ref_dataset=None):
        super().__init__(data, network, station)
        self.eval_dataset = eval_dataset
        self.ref_dataset = ref_dataset

    def get_network_data(self, networks):
        """
        network_filter = list of networks
        station_filter = list of stations
        year_filter = list of years
        month_filter = list of months
        """

        if type(networks) is list:
            # filter based on list
            pass
        if type(networks) is str:
            # filter based on str
            pass

    def get_station_data(self, stations):
        """
        stations: list of stations or name of station
        """
        if type(stations) is list:
            # filter based on list
            pass
        if type(stations) is str:
            # filter based on string
            pass

    def get_metrics(self, data):
        # get two data columns and calculate metrics
        # return list of metrics
        pass
