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
from gldas.interface import GLDAS_Noah_v21_025Ds
from repurpose.img2ts import Img2Ts
from pygeogrids.grids import BasicGrid
run_reshuffle = True
test_reshuffle = True

input_root = r"D:\sm_backup\smos-ic-l3-25km_global\ASC"
gldas_reader = GLDAS_Noah_v21_025Ds(data_path=r"C:\git\soil-moisture-sweden\test_output_data\gldas_subset")
gldas_reader.subpath_templ = []
gldas_data = gldas_reader.read(datetime(2018,6,1))
grid = BasicGrid(gldas_data.lon, gldas_data.lat)
# grid = r"C:\git\soil-moisture-sweden\input_data\GLDAS_global_reshuffle\grid.nc"

ff = r"D:\sm_backup\smos-ic-l3-25km_global\ASC\2015\SM_RE06_MIR_CDF3SA_20150101T000000_20150101T235959_105_001_8.DBL.nc"
outputpath = r"D:\sm_backup\smos-ic-l3-25km_global_reshuffle_GLDASgrid"
startdate = datetime(2015, 1, 1, 0, 0, 0)
enddate = datetime(2018, 12, 31, 23, 59, 59)
parameters = ['Soil_Moisture', 'Soil_Moisture_StdError', 'Quality_Flag', 'UTC_Seconds']

# initialize SMOS IC reader
input_dataset = SMOSDs(input_root, parameters=parameters)

# reshuffle
if run_reshuffle:
    # reshuffle(input_root, outputpath, startdate, enddate, parameters=parameters, img_kwargs={'grid': GLDAS025Cellgrid()})
    fp, ff = os.path.split(ff)
    input_dataset = SMOSImg(filename=os.path.join(fp, ff), parameters=parameters)
    data = input_dataset.read()
    ts_attributes = data.metadata
    input_dataset = SMOSDs(input_root, parameters)
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    global_attr = {'product': 'SMOS_IC'}
    reshuffler = Img2Ts(input_dataset=input_dataset, outputpath=outputpath, startdate=startdate, enddate=enddate,
                        target_grid=grid, cellsize_lat=5.0, cellsize_lon=5.0, global_attr=global_attr, zlib=True,
                        unlim_chunksize=1000, ts_attributes=ts_attributes)
    reshuffler.calc()

# test reshuffle
# output note: why is timestamp set to midnight?
if test_reshuffle:
    pass
    # ds = SMOSTs(outputpath, parameters=parameters,
    #             ioclass_kws={'read_bulk': True})
    # # read_ts takes either lon, lat coordinates or a grid point indices.
    # # and returns a pandas.DataFrame
    # # Degero: 19.556539 64.182029
    # ts = ds.read(19.556539, 64.182029)
    # print(ts)
