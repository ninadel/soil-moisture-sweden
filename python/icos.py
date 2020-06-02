"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/31/2020
Class to handle ICOS TS data
"""

from ismn.readers import ISMNTimeSeries

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
        for key in metadata:
            setattr(self, key, metadata[key])

        self.network = "ICOS"
        self.sensor = "Insert Sensor Here"
        self.depth_from = ["0.05"]
        self.depth_to = ["0.05"]
        self.data = data

    def get_ssm_data(self, qc_values, dropna=True):
        data = self.data
        if type(qc_values) != list:
            qc_values = [qc_values]
        data = data.loc[data['qc_ssm'].isin(qc_values)]
        if dropna:
            data.dropna()
        return data

# class ISMNTimeSeries(object):
#     """
#     class that contains a time series of ISMN data read from one text file
#     Attributes
#     ----------
#     network : string
#         network the time series belongs to
#     station : string
#         station name the time series belongs to
#     latitude : float
#         latitude of station
#     longitude : float
#         longitude of station
#     elevation : float
#         elevation of station
#     variable : list
#         variable measured
#     depth_from : list
#         shallower depth of layer the variable was measured at
#     depth_to : list
#         deeper depth of layer the variable was measured at
#     sensor : string
#         sensor name
#     data : pandas.DataFrame
#         data of the time series
#     """
#
#     def __init__(self, data):
#
#         for key in data:
#             setattr(self, key, data[key])
#
#     def __repr__(self):
#
#         return '%s %s %.2f m - %.2f m %s measured with %s ' % (
#             self.network,
#             self.station,
#             self.depth_from[0],
#             self.depth_to[0],
#             self.variable[0],
#             self.sensor)
#
#     def plot(self, *args, **kwargs):
#         """
#         wrapper for pandas.DataFrame.plot which adds title to plot
#         and drops NaN values for plotting
#         Returns
#         -------
#         ax : axes
#             matplotlib axes of the plot
#         Raises
#         ------
#         ISMNTSError
#             if data attribute is not a pandas.DataFrame
#         """
#         if type(self.data) is pd.DataFrame:
#             tempdata = self.data.dropna()
#             tempdata = tempdata[tempdata.columns[0]]
#             ax = tempdata.plot(*args, figsize=(15, 5), **kwargs)
#             ax.set_title(self.__repr__())
#             return ax
#         else:
#             raise ISMNTSError("data attribute is not a pandas.DataFrame")