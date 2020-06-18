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
from gldas.grid import GLDAS025Cellgrid
from repurpose.img2ts import Img2Ts

run_reshuffle = True
test_reshuffle = True

input_root = r'C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\SMOS\smos-bec-reprocessed-01km-euro\ASC'
ff = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\SMOS\smos-ic-l3-25km_global\ASC\2015\SM_RE06_MIR_CDF3SA_20150101T000000_20150101T235959_105_001_8.DBL.nc"
outputpath = r'C:\Nina_PCTower_Share\PCTower_SM\smos-ic-l3-25km_global_reshuffle_gldasgrid\ASC'
startdate = datetime(2015, 1, 1, 0, 0, 0)
enddate = datetime(2018, 12, 31, 23, 59, 59)
parameters = ['Soil_Moisture', 'Soil_Moisture_StdError', 'Quality_Flag', 'UTC_Seconds']

# initialize SMOS IC reader
input_dataset = SMOSDs(input_root, parameters=parameters)

# reshuffle
if run_reshuffle:
    # reshuffle(input_root, outputpath, startdate, enddate, parameters=parameters, img_kwargs={'grid': GLDAS025Cellgrid()})
    fp, ff = os.path.split(ff)
    grid=GLDAS025Cellgrid()
    input_dataset = SMOSImg(filename=os.path.join(fp, ff), parameters=parameters, read_flags=None)
    data = input_dataset.read()
    ts_attributes = data.metadata
    input_dataset = SMOSDs(input_root, parameters, flatten=True)
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    global_attr = {'product': 'SMOS_IC'}
    reshuffler = Img2Ts(input_dataset=input_dataset, outputpath=outputpath, startdate=startdate, enddate=enddate,
                        input_grid=grid, cellsize_lat=5.0, cellsize_lon=5.0, global_attr=global_attr, zlib=True,
                        unlim_chunksize=1000, ts_attributes=ts_attributes)

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
