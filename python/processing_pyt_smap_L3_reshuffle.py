"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/31/2020
Script to reshuffle SMAP L3 data based on repurpose package
"""
import os
import pyt_reshuffle_smap_L3
# from smap_io.reshuffle import reshuffle
import os
from datetime import datetime
from smap_io.interface import SPL3SMP_Ds, SMAPTs

run_reshuffle = True
test_reshuffle = True

# input_root = r'C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\SMAP\SPL3SMP-smap-l3-36km_clipped_h5'
# outputpath = r'C:\Nina_PCTower_Share\PCTower_SM\SPL3SMP-smap-l3-36km_nordic_reshuffle'
input_root = r'C:\Nina_PCTower_Share\PCTower_SM\SPL3SMP_smap-L3-36km_global_h5 - Copy'
outputpath = r'C:\Nina_PCTower_Share\PCTower_SM\SPL3SMP-smap-l3-36km_global_reshuffle'
startdate = datetime(2015, 4, 1, 0, 0, 0)
enddate = datetime(2018, 12, 31, 23, 59, 59)
parameters = ['soil_moisture', 'surface_flag']

# initialize SMAP L3 reader
input_dataset = SPL3SMP_Ds(input_root, parameter=parameters, overpass='AM', subpath_templ=[], crid=None, flatten=True)
input_dataset.subpath_templ = []

# reshuffle
if run_reshuffle:
    reshuffle_smap_L3.reshuffle(input_dataset, outputpath, startdate, enddate, parameters, overpass='AM')

# test reshuffle
# output note: why is timestamp set to midnight?
if test_reshuffle:
    ds = SMAPTs(outputpath, parameters=parameters,
                ioclass_kws={'read_bulk': True})
    # read_ts takes either lon, lat coordinates or a grid point indices.
    # and returns a pandas.DataFrame
    # Degero: 19.556539 64.182029
    ts = ds.read(19.556539, 64.182029)
    print(ts)
