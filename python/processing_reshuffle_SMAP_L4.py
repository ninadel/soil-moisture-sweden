"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/31/2020
Script to reshuffle SMAP L4 data based on repurpose package
"""
import os
import reshuffle_smap_L4
# from smap_io import reshuffle
import os
from datetime import datetime
from smap_extension import SPL4SMP_nc_Ds
from smap_io import SMAPTs

reshuffle = True
test_reshuffle = False

input_root = r"C:\git\soil-moisture-sweden\test_input_data"
outputpath = r"C:\Nina_PCTower_Share\PCTower_SM\SMAPL4_nordic_reshuffle"
startdate = datetime(2015, 4, 1, 0, 0, 0)
enddate = datetime(2018, 12, 31, 23, 59, 59)

parameters = ['sm_surface_analysis', 'sm_surface_analysis_ensstd']

# initialize SMAP L4 reader
input_dataset = SPL4SMP_nc_Ds(input_root, parameter=parameters, subpath_templ=[], flatten=True)

# reshuffle
if reshuffle:
    reshuffle_smap_L4.reshuffle(input_dataset, outputpath, startdate, enddate, parameters)

# test reshuffle
# output note: why is timestamp set to midnight?
if test_reshuffle:
    ds = SMAPTs(outputpath, parameters=parameters, ioclass_kws={'read_bulk': True})
    # read_ts takes either lon, lat coordinates or a grid point indices.
    # and returns a pandas.DataFrame
    ts = ds.read(19.556539, 64.182029) # (lon, lat)
    print(ts)
