# Author: Nina del Rosario
# Class for extending TUW-GEO smap_io package (https://github.com/TUW-GEO/smap_io) to include SMAP L4
# Adapted from SMAPL3 reader: https://github.com/TUW-GEO/smap_io/blob/master/smap_io/interface.py

# Dependencies
import numpy as np

from pygeobase.io_base import ImageBase, MultiTemporalImageBase
from pygeobase.object_base import Image

from netCDF4 import Dataset
from datetime import timedelta


# Removed overpass
class SPL4SMP_nc_Img(ImageBase):
    """
    Class for reading one image of SMAP Level 4 version 5 Passive Soil Moisture in nc format
    Parameters
    ----------
    filename: string
        filename of the SMAP nc file
    mode: string, optional
        mode of opening the file, only 'r' is implemented at the moment
    parameter : string or list, optional
        one or list of parameters found at http://nsidc.org/data/smap_io/SPL4smp/data-fields
        Default : 'soil_moisture'
    flatten: boolean, optional
        If true the read data will be returned as 1D arrays.
    """

    # TO DO: remove overpass parameters
    def __init__(self, filename, mode='r', parameter='sm_surface_analysis', flatten=False):
        super(SPL4SMP_nc_Img, self).__init__(filename, mode=mode)

        if type(parameter) != list:
            parameter = [parameter]
        self.parameters = parameter
        self.flatten = flatten


    def read(self, timestamp=None):
        return_data = {}
        return_meta = {}

        try:
            ds = Dataset(self.filename)['Analysis_Data']
        except IOError as e:
            print(e)
            print(" ".join([self.filename, "Analysis Data can not be opened"]))
            raise e

        try:
            super_ds = Dataset(self.filename)
        except IOError as e:
            print(e)
            print(" ".join([self.filename, "Analysis Data can not be opened"]))
            raise e

        latitude = super_ds['cell_lat']
        longitude = super_ds['cell_lon']

        parameters = list(self.parameters)

        for parameter in parameters:
            metadata = {}
            param = ds[parameter]
            data = param[:]

            # fill metadata dictionary
            for attr in param.ncattrs():
                metadata[attr] = param.getncattr(attr)

            # mask according to valid_min, valid_max and _FillValue
            try:
                fill_value = metadata['_FillValue']
                valid_min = metadata['valid_min']
                valid_max = metadata['valid_max']
                data = np.where(np.logical_or(data < valid_min, data > valid_max),
                                fill_value, data)
            except KeyError as k:
                print(k)
                print("masking field not present")
                raise k

            return_data[parameter] = data
            return_meta[parameter] = metadata

        if self.flatten:
            longitude = longitude.flatten()
            latitude = latitude.flatten()
            for param in return_data.keys():
                return_data[param] = return_data[param].flatten()

        super_ds.close()
        return Image(longitude, latitude, return_data, return_meta, timestamp)

    def write(self, data):
        raise NotImplementedError()

    def flush(self):
        pass

    def close(self):
        pass

# TO DO: remove overpass parameters
class SPL4SMP_nc_Ds(MultiTemporalImageBase):
    """
    Class for reading a collection of SMAP Level 4 Passive Soil Moisture images in nc format.
    Parameters
    ----------
    data_path: string
        root path of the SMAP data files
    parameter : string or list, optional
        one or list of parameters found at http://nsidc.org/data/smap_io/SPL4smp/data-fields
        Default : 'soil_moisture'
    subpath_templ : list, optional
        If the data is store in subpaths based on the date of the dataset then this list
        can be used to specify the paths. Every list element specifies one path level.
    flatten: boolean, optional
        If true the read data will be returned as 1D arrays.
    """

    # TO DO: remove overpass parameters
    # crid removed
    # set subpath_templ to empty
    def __init__(self, data_path, parameter='sm_surface_analysis',
                 subpath_templ=[], flatten=False):

        ioclass_kws = {'parameter': parameter,
                       'flatten': flatten}

        # example: SMAP_L4_SM_aup_20180628T120000_Vv4030_001_HEGOUT.nc
        filename_templ = "SMAP_L4_SM_aup_{datetime}_*.nc"

        super(SPL4SMP_nc_Ds, self).__init__(data_path, SPL4SMP_nc_Img,
                                         fname_templ=filename_templ,
                                         datetime_format="%Y%m%dT%H%M%S",
                                         subpath_templ=subpath_templ,
                                         exact_templ=False,
                                         ioclass_kws=ioclass_kws)
        
    def tstamps_for_daterange(self, start_date, end_date):
        """
        return timestamps for daterange,
        Parameters
        ----------
        start_date: datetime
            start of date range
        end_date: datetime
            end of date range
        Returns
        -------
        timestamps : list
            list of datetime objects of each available image between
            start_date and end_date
        """
        img_offsets = np.array([timedelta(hours=0), timedelta(hours=3),
                                timedelta(hours=6), timedelta(hours=9),
                                timedelta(hours=12), timedelta(hours=15),
                                timedelta(hours=18), timedelta(hours=21)])

        timestamps = []
        diff = end_date - start_date
        for i in range(diff.days + 1):
            daily_dates = start_date + timedelta(days=i) + img_offsets
            timestamps.extend(daily_dates.tolist())

        return timestamps