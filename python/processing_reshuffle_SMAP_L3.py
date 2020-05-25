import os
import smap_L3_reshuffle
# from smap_io import reshuffle
import os
from datetime import datetime
from smap_io.interface import SPL3SMP_Ds, SMAPTs

reshuffle = True
test_reshuffle = False

input_root = r'C:\git\soil-moisture-sweden\sm_sample_files\SPL3SMP-smap-l3-36km\20180601_20180630'
outputpath = r'C:\git\soil-moisture-sweden\test_output_data\test_smapL3_reshuffle'
startdate = datetime(2018, 6, 1, 0, 0, 0)
enddate = datetime(2018, 6, 30, 23, 59, 59)
parameters = ['soil_moisture', 'soil_moisture_error', 'retrieval_qual_flag', 'surface_flag', 'EASE_column_index', 'EASE_row_index', 'longitude', 'latitude']

# initialize SMAP L3 reader
input_dataset = SPL3SMP_Ds(input_root, parameter=parameters,
                               overpass='AM', subpath_templ = [],
                               crid=None, flatten=True)

# reshuffle
if reshuffle:
    smap_L3_reshuffle.reshuffle(input_dataset, outputpath, startdate, enddate, parameters, overpass='AM')

# test reshuffle
# output note: why is timestamp set to midnight?
if test_reshuffle:
    ds = SMAPTs(outputpath, parameters=['soil_moisture','soil_moisture_error', 'retrieval_qual_flag', 'surface_flag'],
                ioclass_kws={'read_bulk': True})
    # read_ts takes either lon, lat coordinates or a grid point indices.
    # and returns a pandas.DataFrame
    ts = ds.read(19.556539, 64.182029) # (lon, lat)
    print(ts.head())
