"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/6/2020
Script to reshuffle CCI data based on repurpose package
"""
import os
import os
from datetime import datetime
from esa_cci_sm.interface import CCI_SM_025Img, CCI_SM_025Ds, CCITs
from esa_cci_sm.reshuffle import reshuffle

run_reshuffle = True
test_reshuffle = True

input_root = r'C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\CCI\cci-0.25deg_global'
outputpath = r'C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\CCI\cci-0.25deg_global_reshuffle'
startdate = datetime(2015, 1, 1, 0, 0, 0)
enddate = datetime(2018, 12, 31, 23, 59, 59)
parameters = ['sm', 'sm_uncertainty']

# initialize CCI reader
# input_dataset = CCI_SM_025Ds(input_root, parameter=parameters)

# reshuffle
if run_reshuffle:
    reshuffle(input_root, outputpath, startdate, enddate, parameters=parameters)
# test reshuffle

# output note: why is timestamp set to midnight?
if test_reshuffle:
    ts = CCITs(outputpath, parameters=parameters,
                ioclass_kws={'read_bulk': True})
    # read_ts takes either lon, lat coordinates or a grid point indices.
    # and returns a pandas.DataFrame
    # Degero: 19.556539 64.182029
    ts = ts.read(19.556539, 64.182029)
    print(ts)
