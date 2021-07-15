"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 7/15/20211

This class inherits from pytesmo's ISMNTimeSeries class:
https://pytesmo.readthedocs.io/en/v0.6.10/_modules/pytesmo/io/ismn/interface.html,
which allows pytesmo to interface with ICOS time series data in the same way as ISMN data
"""

from ismn.readers import ISMNTimeSeries
import pandas

class ICOSTimeSeries(ISMNTimeSeries):
    """
    class that contains a time series of ISMN data read from one text file
    Attributes
    ----------
    network : string
        network the time series belongs to
    station : string
        station name the time series belongs to
    latitude : float
        latitude of station
    longitude : float
        longitude of station
    elevation : float
        elevation of station
    variable : list
        variable measured
    depth_from : list
        shallower depth of layer the variable was measured at
    depth_to : list
        deeper depth of layer the variable was measured at
    sensor : string
        sensor name
    data : pandas.DataFrame
        data of the time series
    """
    def __init__(self, metadata, data):
        self.station = metadata["station"]
        self.network = "ICOS"
        self.sensor = "Delta-T Theta Probe ML2x"
        self.depth_from = ["0.05"]
        self.depth_to = ["0.05"]
        self.longitude = metadata["longitude"]
        self.latitude = metadata["latitude"]
        self.elevation = metadata["elevation"]
        self.data = data
        self.data.index = pandas.to_datetime(self.data.index)