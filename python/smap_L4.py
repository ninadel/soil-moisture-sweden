# Author: Nina del Rosario
# Class for extending TUW-GEO smap_io package (https://github.com/TUW-GEO/smap_io) to include SMAP L4
# Adapted from SMAPL3 reader: https://github.com/TUW-GEO/smap_io/blob/master/smap_io/interface.py

# Dependencies
import os
from pygeobase.io_base import ImageBase, MultiTemporalImageBase
from pygeobase.object_base import Image
from pynetcf.time_series import GriddedNcOrthoMultiTs
import pygeogrids.netcdf as ncdf
import h5py
import numpy as np
from parse import *
from datetime import timedelta
import warnings


# TO DO: remove overpass parameters
# Classes for H5 format
class SPL4SMP_h5_Img(ImageBase):
    """
    Class for reading one image of SMAP Level 4 version 5 Passive Soil Moisture in h5 format
    Parameters
    ----------
    filename: string
        filename of the SMAP h5 file
    mode: string, optional
        mode of opening the file, only 'r' is implemented at the moment
    parameter : string or list, optional
        one or list of parameters found at http://nsidc.org/data/smap_io/SPL4smp/data-fields
        Default : 'soil_moisture'
    overpass : str, optional (default: 'AM')
        Select 'AM' for the descending overpass or 'PM' for the ascending one.
        If there is only one overpass in the file (old SMAP versions) pass None.
        Passing PM will result in reading variables called *name*_pm
        Passing AM will result in reading variables called *name*
    var_overpass_str : bool, optional (default: True)
        Append overpass indicator to the loaded variables. E.g. Soil Moisture
        will be called soil_moisture_pm and soil_moisture_am, and soil_moisture
        in all cases if this is set to False.
    flatten: boolean, optional
        If true the read data will be returned as 1D arrays.
    """

    # old version
    # def __init__(self, filename, mode='r', parameter='soil_moisture',
    #              overpass='AM', var_overpass_str=True, flatten=False):

    # TO DO: remove overpass parameters
    def __init__(self, filename, mode='r', parameter='soil_moisture',
                 flatten=False):
        super(SPL4SMP_h5_Img, self).__init__(filename, mode=mode)

        if type(parameter) != list:
            parameter = [parameter]
        self.overpass = overpass
        self.overpass_templ = 'Soil_Moisture_Retrieval_Data{orbit}'
        self.var_overpass_str = var_overpass_str
        self.parameters = parameter
        self.flatten = flatten

    def assert_overpass(self, ds):
        if self.overpass is None: # find overpasses in file
            overpasses = []
            for k in list(ds.keys()):
                p = parse(self.overpass_templ, k)
                if p is not None and ('orbit' in p.named.keys()):
                    overpasses.append(p['orbit'][1:]) # omit leading _

            if len(overpasses) > 1:
                raise IOError('Multiple overpasses ({}) found in file, please specify which'
                              'overpass to load.'.format(self.overpass))
        else:
            assert self.overpass.upper() in ['AM', 'PM']

    def read(self, timestamp=None):

        return_data = {}
        return_meta = {}

        try:
            ds = h5py.File(self.filename, mode='r')
        except IOError as e:
            print(e)
            print(" ".join([self.filename, "can not be opened"]))
            raise e

        self.assert_overpass(ds)

        overpass = self.overpass

        overpass_str = '_' + overpass.upper() if overpass else ''
        sm_field = self.overpass_templ.format(orbit=overpass_str)

        if sm_field not in ds.keys():
            raise NameError(sm_field, 'Field does not exists. Try deactivating overpass option.')

        if overpass:
            overpass_str = '_' + overpass.lower() if overpass.upper() == 'PM' else ''
        else:
            overpass_str = ''

        latitude = ds[sm_field]['latitude%s' % overpass_str][:]
        longitude = ds[sm_field]['longitude%s' % overpass_str][:]

        for parameter in self.parameters:
            metadata = {}
            param = ds[sm_field][parameter + overpass_str]
            data = param[:]
            # mask according to valid_min, valid_max and _FillValue
            try:
                fill_value = param.attrs['_FillValue']
                valid_min = param.attrs['valid_min']
                valid_max = param.attrs['valid_max']
                data = np.where(np.logical_or(data < valid_min, data > valid_max),
                                fill_value, data)
            except KeyError:
                pass

            # fill metadata dictionary with metadata from image
            for key in param.attrs:
                metadata[key] = param.attrs[key]

            if self.var_overpass_str:
                if overpass is None:
                    warnings.warn('Renaming variable only possible if overpass in given.'
                                  ' Use names as in file.')
                    ret_param_name = parameter
                else:
                    ret_param_name = parameter + '_' + overpass.lower()
            else:
                ret_param_name = parameter

            return_data[ret_param_name] = data
            return_meta[ret_param_name] = metadata

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

# TO DO: remove overpass parameters
class SPL4SMP_h5_Ds(MultiTemporalImageBase):
    """
    Class for reading a collection of SMAP Level 4 Passive Soil Moisture images in h5 format.
    Parameters
    ----------
    data_path: string
        root path of the SMAP data files
    parameter : string or list, optional
        one or list of parameters found at http://nsidc.org/data/smap_io/SPL4smp/data-fields
        Default : 'soil_moisture'
    overpass : str, optional
        Select 'AM' for the descending overpass or 'PM' for the ascending one.
        Dataset version must support multiple overpasses, else choose None
    var_overpass_str : bool, optional (default: True)
        Append overpass indicator to the loaded variables. E.g. Soil Moisture
        will be called soil_moisture_pm and soil_moisture_am, and soil_moisture
        in all cases if this is set to False.
    subpath_templ : list, optional
        If the data is store in subpaths based on the date of the dataset then this list
        can be used to specify the paths. Every list element specifies one path level.
    crid : int, optional (default: None)
        Only read files with this specific Composite Release ID.
        See also https://nsidc.org/data/smap/data_versions#CRID
    flatten: boolean, optional
        If true the read data will be returned as 1D arrays.
    """

    # TO DO: remove overpass parameters
    def __init__(self, data_path, parameter='soil_moisture', overpass='AM',
                 var_overpass_str=True, subpath_templ=['%Y.%m.%d'], crid=None, flatten=False):

        ioclass_kws = {'parameter': parameter,
                       'overpass': overpass,
                       'var_overpass_str': var_overpass_str,
                       'flatten': flatten}
        if crid is None:
            # new filename template for SMAP L4: SMAP_L4_SM_aup_20150331T030000_Vv4030_001_HEGOUT
            filename_templ = "SMAP_L4_SM_P_{datetime}_*.h5"
        else:
            filename_templ = "SMAP_L4_SM_P_{datetime}_R%i*.h5" % crid

        super(SPL4SMP_Ds, self).__init__(data_path, SPL4SMP_h5_Img,
                                         fname_templ=filename_templ,
                                         datetime_format="%Y%m%d",
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
        timestamps = []
        diff = end_date - start_date
        for i in range(diff.days + 1):
            daily_date = start_date + timedelta(days=i)
            timestamps.append(daily_date)

        return timestamps
        
# TO DO: remove overpass parameters
# Classes for NC format
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
    overpass : str, optional (default: 'AM')
        Select 'AM' for the descending overpass or 'PM' for the ascending one.
        If there is only one overpass in the file (old SMAP versions) pass None.
        Passing PM will result in reading variables called *name*_pm
        Passing AM will result in reading variables called *name*
    var_overpass_str : bool, optional (default: True)
        Append overpass indicator to the loaded variables. E.g. Soil Moisture
        will be called soil_moisture_pm and soil_moisture_am, and soil_moisture
        in all cases if this is set to False.
    flatten: boolean, optional
        If true the read data will be returned as 1D arrays.
    """

    # TO DO: remove overpass parameters
    def __init__(self, filename, mode='r', parameter='soil_moisture',
                 overpass='AM', var_overpass_str=True, flatten=False):
        super(SPL4SMP_nc_Img, self).__init__(filename, mode=mode)

        if type(parameter) != list:
            parameter = [parameter]
        self.overpass = overpass
        self.overpass_templ = 'Soil_Moisture_Retrieval_Data{orbit}'
        self.var_overpass_str = var_overpass_str
        self.parameters = parameter
        self.flatten = flatten

    def assert_overpass(self, ds):
        pass
        
    def read(self, timestamp=None):
        pass
        
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
    overpass : str, optional
        Select 'AM' for the descending overpass or 'PM' for the ascending one.
        Dataset version must support multiple overpasses, else choose None
    var_overpass_str : bool, optional (default: True)
        Append overpass indicator to the loaded variables. E.g. Soil Moisture
        will be called soil_moisture_pm and soil_moisture_am, and soil_moisture
        in all cases if this is set to False.
    subpath_templ : list, optional
        If the data is store in subpaths based on the date of the dataset then this list
        can be used to specify the paths. Every list element specifies one path level.
    crid : int, optional (default: None)
        Only read files with this specific Composite Release ID.
        See also https://nsidc.org/data/smap/data_versions#CRID
    flatten: boolean, optional
        If true the read data will be returned as 1D arrays.
    """

    # TO DO: remove overpass parameters
    def __init__(self, data_path, parameter='soil_moisture', overpass='AM',
                 var_overpass_str=True, subpath_templ=['%Y.%m.%d'], crid=None, flatten=False):
        ioclass_kws = {'parameter': parameter,
                       'overpass': overpass,
                       'var_overpass_str': var_overpass_str,
                       'flatten': flatten}
        if crid is None:
            # new filename template for SMAP L4: SMAP_L4_SM_aup_20150331T030000_Vv4030_001_HEGOUT
            filename_templ = "SMAP_L4_SM_P_{datetime}_*.nc"
        else:
            filename_templ = "SMAP_L4_SM_P_{datetime}_R%i*.nc" % crid

        super(SPL4SMP_Ds, self).__init__(data_path, SPL4SMP_nc_Img,
                                         fname_templ=filename_templ,
                                         datetime_format="%Y%m%d",
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
        timestamps = []
        diff = end_date - start_date
        for i in range(diff.days + 1):
            daily_date = start_date + timedelta(days=i)
            timestamps.append(daily_date)

        return timestamps
        
    


