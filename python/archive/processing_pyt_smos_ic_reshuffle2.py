"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/31/2020
Script to reshuffle SMOS IO data based on repurpose package
"""
import os
from smos.smos_ic import reshuffle
import os
from datetime import datetime
from smos.smos_ic.interface import SMOSImg, SMOSDs, SMOSTs
from smos.smos_ic.reshuffle import reshuffle
from pygeogrids.grids import BasicGrid
import netCDF4
import numpy as np
from repurpose.img2ts import Img2Ts

run_reshuffle = True
test_reshuffle = False

input_root = r'C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\SMOS\smos-ic-l3-25km_nordic_0-25-remap\ASC'
ff = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\SMOS\smos-ic-l3-25km_nordic_0-25-remap\ASC\SM_RE06_MIR_CDF3SA_20150101T000000_20150101T235959_105_001_8.DBL_sub_remap.nc"
outputpath = r'C:\Nina_PCTower_Share\PCTower_SM\smos-ic-l3-25km_nordic_reshuffle_gldasgrid\ASC'
startdate = datetime(2015, 1, 1, 0, 0, 0)
enddate = datetime(2018, 12, 31, 23, 59, 59)
parameters = ['Soil_Moisture', 'Quality_Flag']
ff_data = netCDF4.Dataset(ff)
# lats = ff_data.variables['lat'][:]
# lons = ff_data.variables['lon'][:]
# lats, lons = np.meshgrid(lats, lons)
# lats = lats.flatten()
# lons = lons.flatten()

ts_attributes = {}
for parameter in parameters:
    data = ff_data.variables[parameter][:]
    # read long name, FillValue and unit
    for attr in ff_data.variables[parameter].ncattrs():
        ts_attributes[attr] = ff_data.variables[parameter].getncattr(attr)

# print(ts_attributes)

# grid = GLDAS025Cellgrid()



# initialize SMOS IC reader
input_dataset = SMOSDs(input_root, parameters=parameters)

# reshuffle
if run_reshuffle:
    # reshuffle(input_root, outputpath, startdate, enddate, parameters=parameters, img_kwargs={'grid': GLDAS025Cellgrid()})
    fp, ff = os.path.split(ff)
    # grid=GLDAS025Cellgrid()
    input_dataset = SMOSDs(input_root, parameters, flatten=True)
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    global_attr = {'product': 'SMOS_IC'}
    reshuffler = Img2Ts(input_dataset=input_dataset, outputpath=outputpath, startdate=startdate, enddate=enddate,
                        input_grid=grid, cellsize_lat=5.0, cellsize_lon=5.0, global_attr=global_attr, zlib=True,
                        unlim_chunksize=1000, ts_attributes=ts_attributes)
    # reshuffler = Img2Ts(input_dataset=input_dataset, outputpath=outputpath, startdate=startdate, enddate=enddate,
    #                     target_grid=grid, cellsize_lat=5.0, cellsize_lon=5.0, global_attr=global_attr, zlib=True,
    #                     unlim_chunksize=1000, ts_attributes=ts_attributes)
    reshuffler.calc()

# test reshuffle
# output note: why is timestamp set to midnight?
if test_reshuffle:
    ds = SMOSTs(outputpath, parameters=parameters,
                ioclass_kws={'read_bulk': True})
    # read_ts takes either lon, lat coordinates or a grid point indices.
    # and returns a pandas.DataFrame
    # Degero: 19.556539 64.182029
    ts = ds.read(19.556539, 64.182029)
    print(ts)
