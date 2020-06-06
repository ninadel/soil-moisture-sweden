"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/31/2020
Script to reshuffle SMOS IO data based on repurpose package
"""
import os
from smos.smos_ic import reshuffle
# from smap_io import reshuffle
import os
from datetime import datetime
from smos.smos_ic.interface import SMOSDs, SMOSTs
from smos.smos_ic.reshuffle import reshuffle

run_reshuffle = True
test_reshuffle = True

input_root = r'C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\smos-ic-l3-25km_global\ASC'
outputpath = r'C:\Nina_PCTower_Share\PCTower_SM\smos-ic-l3-25km_global_reshuffle\ASC'
startdate = datetime(2015, 1, 1, 0, 0, 0)
enddate = datetime(2018, 12, 31, 23, 59, 59)
parameters = ['Soil_Moisture', 'Soil_Moisture_StdError', 'Quality_Flag', 'UTC_Seconds']

# initialize SMOS IC reader
input_dataset = SMOSDs(input_root, parameters=parameters)

# reshuffle
if run_reshuffle:
    reshuffle(input_root, outputpath, startdate, enddate, parameters=parameters)
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
