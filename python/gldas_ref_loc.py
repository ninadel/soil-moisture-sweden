"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/31/2020
Class to handle reference GLDAS data
"""

class GLDASRefLoc(object):
    """
    class that contains a GLDAS time series
    Attributes
    ----------
    lon : float
    lat : float
    dom_veg_class : string
    data: pandas DataFrame
    """
    def __init__(self, lon, lat, dom_veg_class, data):
        self.network = 'GLDAS'
        self.station = "g_{}_{}_{}".format(str(lat).replace(".", "-"), str(lon).replace(".", "-"),
                                           dom_veg_class.replace(" ", "-"))
        self.longitude = lon
        self.latitude = lat
        self.dom_veg_class = dom_veg_class
        self.data = data
