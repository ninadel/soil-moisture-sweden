"""
Author: Nina del Rosario
Class for extending TUW-GEO smos package (https://github.com/TUW-GEO/smos) 
to include SMOS L4 (BEC: http://bec.icm.csic.es/land-datasets/)
"""
import warnings
import datetime
import numpy as np
import re
from pygeobase.io_base import ImageBase, MultiTemporalImageBase
from pygeobase.object_base import Image
from datetime import datetime, timedelta
from netCDF4 import Dataset
from pygeogrids.netcdf import load_grid
# from grid import smoc_bec_grid, EASE01CellGrid


class SMOSBECImg(ImageBase):
    """
    Class for reading one SMOS BEC nc image file.
    Parameters
    ----------
    filename: string
        filename of the SMOS BEC nc image file
    mode: string, optional (default: 'r')
        mode of opening the file, only 'r' is implemented at the moment
    parameters : string or list, optional (default: SM)
        one or list of parameters to read, see SMOS documentation
        for more information (default: 'SM').
    flatten: boolean, optional (default:False)
        if set then the data is read into 1D arrays.
        Needed for some legacy code.
    grid : pygeogrids.BasicGrid, optional (default: None)
        A grid object, on which the image data is organised. If None is passed,
    read_flags : bool or None, optional (default: (0, 1))
        Filter values to read based on the selected Quality Flags.
        Values for locations that are not assigned any of the here passed flags
        are replaces with NaN (by default only the missing-data, i.e. flag=2,
        locations are filtered out). If None is passed, no flags are considered.
    """

    def __init__(self, filename, mode='r', parameters='SM', read_flags=(0,1)):

        super(SMOSBECImg, self).__init__(filename, mode=mode)

        if type(parameters) != list:
            parameters = [parameters]

        self.read_flags = read_flags
        self.parameters = parameters
        # 20180601T030707
        timestamp_str = re.findall(r"[0-9]{8}T[0-9]{4}", self.filename)[-1]
        self.timestamp = datetime(int(timestamp_str[0:4]), int(timestamp_str[4:6]), int(timestamp_str[6:8]),
                                  int(timestamp_str[9:11]), int(timestamp_str[11:13]))

    def read_empty(self):
        raise NotImplementedError()
        # '''
        # Create an empty image for filling missing dates, this is necessary
        # for reshuffling as img2ts cannot handle missing days.
        # Returns
        # -------
        # empty_img : dict
        #     Empty arrays of image size for each object parameter
        # '''
        # self.image_missing = True
        #
        # return_img = {}
        # return_metadata = {}
        #
        # yres, xres = self.grid.shape
        #
        # for param in self.parameters:
        #     data = np.full((yres, xres), np.nan)
        #     return_img[param] = data.flatten()
        #     return_metadata[param] = {'image_missing': 1}
        #
        # return return_img, return_metadata

    def read_img(self):
        '''Read existing file to image'''

        # Read a netcdf image

        ds = Dataset(self.filename)

        latitude = ds['lat'][:]
        longitude = ds['lon'][:]

        parameters = list(self.parameters)

        if self.read_flags is not None:
            parameters += ['quality_flag']

        return_data = {}
        return_meta = {}

        for parameter in parameters:
            metadata = {}
            param = ds[parameter]
            data = param[:]

            # fill metadata dictionary
            for attr in param.ncattrs():
                metadata[attr] = param.getncattr(attr)

            # mask according to valid_min, valid_max and _FillValue
            if parameter == 'SM':
                fill_value = metadata['_FillValue']
                valid_min = 0
                valid_max = 0.6
                data = np.where(np.logical_or(data < valid_min, data > valid_max),
                                fill_value, data)

            # if '_FillValue' in metadata.keys():
            #     np.ma.set_fill_value(data, metadata['_FillValue'])
            #     data = data.filled()

            metadata['image_missing'] = 0

            return_data[parameter] = data
            return_meta[parameter] = metadata

        ds.close()
        timekey = 'time'
        return Image(longitude, latitude, return_data, return_meta, self.timestamp, timekey)


        # # filter with the flags
        # if self.read_flags is not None:
        #     flag_mask = ~np.isin(return_img['quality_flag'], self.read_flags)
        # else:
        #     flag_mask = np.full(return_img[parameters[0]].shape, False)
        #
        # for param, data in return_img.items():
        #     if issubclass(data.dtype.type, np.integer):
        #         data = data.astype(np.float32)
        #     data_masked = np.ma.array(data, mask=flag_mask, fill_value=np.nan)
        #     return_img[param] = data_masked.filled()
        #     return_img[param] = return_img[param].flatten()
        #
        # if self.read_flags is not None and ('quality_flag' not in self.parameters):
        #     return_img.pop('quality_flag')
        #     return_metadata.pop('quality_flag')
        #
        # return return_img, return_metadata

    def read_masked_data(self, **kwargs):
        raise NotImplementedError

    def read(self, timestamp=None):
        '''
        Read a single SMOS BEC image, if it exists, else read an empty image
        Parameters
        --------
        timestamp : datetime, optional (default:None)
            Time stamp for the image to read
        '''
        raise NotImplementedError

        # if self.grid is None:
        #     self.grid = smoc_bec_grid()
        return_img, return_metadata = self.read_img()
        # try:
        #     return_img, return_metadata = self.read_img()
        # except IOError:
        #     warnings.warn('Error loading image for {}, '
        #                   'generating empty image instead'.format(timestamp.date()))
        #     warnings.warn('Error loading image for {}, '
        #                   'generating empty image instead'.format(timestamp.date()))
        #     return_img, return_metadata = self.read_empty()

        # if self.flatten:
        #     return Image(self.grid.activearrlon, self.grid.activearrlat,
        #                  return_img, return_metadata, timestamp)
        #
        # else:
        #     yres, xres = self.grid.shape
        #     for key in return_img:
        #         return_img[key] = np.flipud(return_img[key].reshape(xres, yres))
        #
        #     return Image(self.grid.activearrlon.reshape(xres, yres),
        #                  np.flipud(self.grid.activearrlat.reshape(xres, yres)),
        #                  return_img,
        #                  return_metadata,
        #                  timestamp)

    def get_values(self, locations):
        """
        Parameters
        ----------
        locations: dict
            dictionary of locations; keys are location names/ids, values are a dictionary with 'lon' and 'lat' keys

        Returns
        ----------
        an updated dictionary; each location will have a data value
        a metadata key will added which will store metadata for each parameter
        """
        img = self.read_img()
        lat = img.lat
        lon = img.lon
        data = img.data
        metadata = img.metadata

        result_dict = {}
        result_dict['metadata'] = {}

        for location, coordinate in locations.items():
            loc_lat = coordinate['lat']
            loc_lon = coordinate['lon']
            result_dict[location] = {}
            result_dict[location]['lat'] = loc_lat
            result_dict[location]['lon'] = loc_lon
            lat = np.asarray(lat)
            # find nearest indices
            lat_idx = (np.abs(lat - loc_lat)).argmin()
            lon_idx = (np.abs(lon - loc_lon)).argmin()
            result_dict[location]['data'] = {}
            for parameter, parameter_data in data.items():
                fill_value = metadata[parameter]['_FillValue']
                parameter_value = int(parameter_data[:, lat_idx, lon_idx])
                result_dict[location]['data'][parameter] = parameter_value
                result_dict['metadata'][parameter] = metadata[parameter]
        return result_dict

    def write(self):
        raise NotImplementedError()

    def flush(self):
        pass

    def close(self):
        pass


# class SMOSBECDs(MultiTemporalImageBase):
#     """
#     Class for reading SMOS BEC images in nc format.
#     Parameters
#     ----------
#     data_path : string
#         Path to the nc files
#     parameter : string or list, optional
#         one or list of parameters to read, see SMOS documentation
#         for more information (default: 'SM').
#     flatten: boolean, optional
#         If set then the data is read into 1D arrays.
#         Needed for some legacy code.
#     grid : pygeogrids.CellGrid
#         Grid that the image data is organised on
#     read_flags : bool, optional (default: (0, 1))
#         Filter values to read based on the selected Quality Flags.
#         Values for locations that are not assigned any of the here passed flags
#         are replaces with NaN (by default only the missing-data, i.e. flag=2,
#         locations are filtered out).
#     """
#
#     def __init__(self, data_path, parameters='SM', flatten=False,
#                  grid=None, filename_templ=None, read_flags=(0,1)):
#
#         ioclass_kws = {'parameters': parameters,
#                        'flatten': flatten,
#                        'grid': grid,
#                        'read_flags': read_flags}
#
#         sub_path = ['%Y']
#
#         if filename_templ is None:
#             # BEC_SM____SMOS__EUM_L4__A_20180601T030707_001km_1d_REP_v5.0.nc
#             # BEC_SM____SMOS__EUM_L4__D_20180601T185755_001km_1d_REP_v5.0.nc
#             # SM_RE06_MIR_CDF3SA_20180601T000000_20180601T235959_105_001_8.DBL
#             filename_templ = "BEC_SM____SMOS__EUM_L4__*_{datetime}T*_001km_1d_REP_v5.0.nc"
#
#         super(SMOSBECDs, self).__init__(data_path, ioclass=SMOSBECImg,
#                                      fname_templ=filename_templ,
#                                      datetime_format="%Y%m%d",
#                                      subpath_templ=sub_path,
#                                      exact_templ=False,
#                                      ioclass_kws=ioclass_kws)
#
#     def _assemble_img(self, timestamp, mask=False, **kwargs):
#         img = None
#         try:
#             filepath = self._build_filename(timestamp)
#         except IOError:
#             filepath = None
#
#         if self._open(filepath):
#             kwargs['timestamp'] = timestamp
#             if mask is False:
#                 img = self.fid.read(**kwargs)
#             else:
#                 img = self.fid.read_masked_data(**kwargs)
#
#         return img
#
#     def read(self, timestamp, **kwargs):
#         return self._assemble_img(timestamp, **kwargs)
#
#     def tstamps_for_daterange(self, start_date, end_date):
#         """
#         return timestamps for daterange,
#         Parameters
#         ----------
#         start_date: datetime.datetime
#             start of date range
#         end_date: datetime.datetime
#             end of date range
#         Returns
#         -------
#         timestamps : list
#             list of datetime objects of each available image between
#             start_date and end_date
#         """
#         img_offsets = np.array([timedelta(hours=0)])
#
#         timestamps = []
#         diff = end_date - start_date
#         for i in range(diff.days + 1):
#             daily_dates = start_date + timedelta(days=i) + img_offsets
#             timestamps.extend(daily_dates.tolist())
#
#         return timestamps