"""
Author: Nina del Rosario, nina.del@gmail.com
6/18/2020
Class for analysing Sentinel-1 SSM data (https://land.copernicus.eu/global/products/ssm)
"""
import numpy as np
import os
from pygeobase.io_base import ImageBase, MultiTemporalImageBase
from pygeobase.object_base import Image
from pynetcf.time_series import GriddedNcOrthoMultiTs
from pygeogrids.netcdf import load_grid
from netCDF4 import Dataset
from dateutil.relativedelta import relativedelta


class SentinelImg(ImageBase):
    """
    Class for reading one SMOS BEC nc image file.
    Parameters
    ----------
    filename: string
        filename of the Sentinel nc image file
    mode: string, optional (default: 'r')
        mode of opening the file, only 'r' is implemented at the moment
    parameters : string or list, optional (default: ssm)
        one or list of parameters to read
        for more information (default: 'ssm').
    flatten: boolean, optional (default:False)
        if set then the data is read into 1D arrays.
        Needed for some legacy code.
    grid : pygeogrids.BasicGrid, optional (default: None)
        A grid object, on which the image data is organised. If None is passed,
    """
    def __init__(self, filename, mode='r', parameter='ssm', flatten=False,
                 grid=None):
        super(SentinelImg, self).__init__(filename, mode=mode)

        if type(parameter) != list:
            parameter = [parameter]
        self.parameters = parameter
        self.flatten = flatten


    def read(self, timestamp=None):
        return_data = {}
        return_meta = {}

        try:
            ds = Dataset(self.filename)
        except IOError as e:
            print(e)
            print(" ".join([self.filename, "Dataset can not be opened"]))
            raise e

        latitude = ds['lat'][:]
        longitude = ds['lon'][:]

        parameters = list(self.parameters)

        for parameter in parameters:
            metadata = {}
            param = ds[parameter]
            data = param[:]

            # fill metadata dictionary
            for attr in param.ncattrs():
                metadata[attr] = param.getncattr(attr)

            # mask according to valid_min, valid_max and _FillValue
            if parameter == 'ssm':
                fill_value = metadata['_FillValue']
                valid_min = 0
                valid_max = 100
                data = np.where(np.logical_or(data < valid_min, data > valid_max),
                                fill_value, data)

            return_data[parameter] = data
            return_meta[parameter] = metadata

        if self.flatten:
            longitude = longitude.flatten()
            latitude = latitude.flatten()
            for param in return_data.keys():
                return_data[param] = return_data[param].flatten()

        ds.close()
        return Image(longitude, latitude, return_data, return_meta, timestamp)

    def write(self, data):
        raise NotImplementedError()

    def flush(self):
        pass

    def close(self):
        pass

class SentinelDs(MultiTemporalImageBase):
    """
    Class for reading a collection of Sentinel-1 images in nc format.
    Parameters
    ----------
    data_path: string
        root path of the Sentinel-1 data files
    parameter : string or list, optional
        Default : 'ssm'
    subpath_templ : list, optional
        If the data is store in subpaths based on the date of the dataset then this list
        can be used to specify the paths. Every list element specifies one path level.
    flatten: boolean, optional
        If true the read data will be returned as 1D arrays.
    """
    def __init__(self, data_path, parameter='ssm', subpath_templ=[], flatten=False):
        ioclass_kws = {'parameter': parameter,
                       'flatten': flatten}
        # c_gls_SSM1km_201501010000_CEURO_S1CSAR_V1.1.1_sub.nc
        # filename_templ = "c_gls_SSM1km_{datetime}_*.nc"
        # datetime_format = "%Y%m%d%H%M%S" ?
        filename_templ = "c_gls_SSM1km_{datetime}0000*.nc"
        super(SentinelDs, self).__init__(data_path, SentinelImg, fname_templ=filename_templ, datetime_format="%Y%m%d",
                                         subpath_templ=subpath_templ, exact_templ=False, ioclass_kws=ioclass_kws)

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

        nxt = lambda date: date + relativedelta(days=1)

        timestamps = [start_date]
        while nxt(timestamps[-1]) <= end_date:
            timestamps.append(nxt(timestamps[-1]))

        return timestamps


class SentinelTs(GriddedNcOrthoMultiTs):
    def __init__(self, ts_path, grid_path=None, **kwargs):
        '''
        Class for reading Sentinel-1 SM time series after reshuffling.
        Parameters
        ----------
        ts_path : str
            Directory where the netcdf time series files are stored
        grid_path : str, optional (default: None)
            Path to grid file, that is used to organize the location of time
            series to read. If None is passed, grid.nc is searched for in the
            ts_path.
        Optional keyword arguments that are passed to the Gridded Base:
        ------------------------------------------------------------------------
            parameters : list, optional (default: None)
                Specific variable names to read, if None are selected, all are read.
            offsets : dict, optional (default:None)
                Offsets (values) that are added to the parameters (keys)
            scale_factors : dict, optional (default:None)
                Offset (value) that the parameters (key) is multiplied with
            ioclass_kws: dict
                Optional keyword arguments to pass to OrthoMultiTs class:
                ----------------------------------------------------------------
                    read_bulk : boolean, optional (default:False)
                        if set to True the data of all locations is read into memory,
                        and subsequent calls to read_ts read from the cache and not from disk
                        this makes reading complete files faster#
                    read_dates : boolean, optional (default:False)
                        if false dates will not be read automatically but only on specific
                        request useable for bulk reading because currently the netCDF
                        num2date routine is very slow for big datasets
        '''
        if grid_path is None:
            grid_path = os.path.join(ts_path, "grid.nc")

        grid = load_grid(grid_path)
        super(SentinelTs, self).__init__(ts_path, grid, **kwargs)