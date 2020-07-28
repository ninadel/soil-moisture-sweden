"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/6/2020
Script to reshuffle CCI data based on repurpose package
"""
import os
# from gldas.grid import GLDAS025Cellgrid
import grid_gldas
from datetime import datetime
from esa_cci_sm.interface import CCI_SM_025Img, CCI_SM_025Ds, CCITs
from esa_cci_sm.reshuffle import reshuffle
from repurpose.img2ts import Img2Ts
from esa_cci_sm.grid import CCICellGrid

run_reshuffle = True
test_reshuffle = False

input_root = r'C:\Nina_PCTower_Share\PCTower_SM\cci-0.25deg_global\2018'
outputpath = r'C:\Nina_PCTower_Share\PCTower_SM\test_output'
startdate = datetime(2015, 1, 1, 0, 0, 0)
enddate = datetime(2018, 12, 31, 23, 59, 59)
parameters = ['sm', 'sm_uncertainty']

input_grid = CCICellGrid()
# SET TARGET GRID TO GLDAS
target_grid = grid_gldas.GLDAS025Cellgrid()

global_attr = {'product' : 'ESA CCI SM'}
ts_attributes = None

# initialize CCI reader
# input_dataset = CCI_SM_025Ds(input_root, parameter=parameters)

input_dataset = CCI_SM_025Ds(input_root, parameters)
input_dataset.subpath_templ = []
test_image = input_dataset.read(datetime(2018,6,1))
# for key, value in test_image.data.items():
#     print(key)

reshuffle = Img2Ts(input_dataset=input_dataset, outputpath=outputpath, startdate=startdate, enddate=enddate,
            input_grid=input_grid, target_grid=target_grid, cellsize_lat=5.0, cellsize_lon=5.0,
            global_attr=global_attr, zlib=True, unlim_chunksize=1000, ts_attributes=ts_attributes)

# reshuffle
if run_reshuffle:
    # reshuffle(input_root, outputpath, startdate, enddate, parameters=parameters)
    print("run reshuffle")
    input_dataset = CCI_SM_025Ds(input_root, parameters)
    reshuffler = Img2Ts(input_dataset, outputpath=outputpath,
                        startdate=startdate, enddate=enddate, input_grid=input_grid,
                        target_grid=target_grid, cellsize_lat=5.0, cellsize_lon=5.0,
                        global_attr=global_attr, zlib=True, unlim_chunksize=1000, ts_attributes=ts_attributes)
# test reshuffle

# output note: why is timestamp set to midnight?
# if test_reshuffle:
#     ts = CCITs(outputpath, parameters=parameters,
#                 ioclass_kws={'read_bulk': True})
#     # read_ts takes either lon, lat coordinates or a grid point indices.
#     # and returns a pandas.DataFrame
#     # Degero: 19.556539 64.182029
#     ts = ts.read(19.556539, 64.182029)
#     print(ts)
