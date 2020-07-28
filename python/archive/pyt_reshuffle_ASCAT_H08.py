"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/11/2020
Script for reshuffling ASCAT H08 data
"""

import os
import sys
import argparse
import numpy as np
from datetime import datetime

from pygeogrids import BasicGrid
# from grid_gldas import GLDAS025Cellgrid
from ascat.h_saf import H08img

from repurpose.img2ts import Img2Ts


def reshuffle(input_root, outputpath, startdate, enddate, parameters, imgbuffer=50):
    """
    Reshuffle method applied to GLDAS data.

    Parameters
    ----------
    input_root: string
        input path where gldas data was downloaded
    outputpath : string
        Output path.
    startdate : datetime
        Start date.
    enddate : datetime
        End date.
    parameters: list
        parameters to read and convert
    imgbuffer: int, optional
        How many images to read at once before writing time series.
    """
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)

    global_attr = {'product': 'H08'}

    input_dataset = H08img(input_root)
    # get time series attributes from first day of data.
    data = input_dataset.read(startdate)
    ts_attributes = data.metadata
    grid = GLDAS025Cellgrid()

    reshuffler = Img2Ts(input_dataset=input_dataset, outputpath=outputpath,
                        startdate=startdate, enddate=enddate, input_grid=grid,
                        imgbuffer=imgbuffer, cellsize_lat=5.0,
                        cellsize_lon=5.0, global_attr=global_attr, zlib=True,
                        unlim_chunksize=1000, ts_attributes=ts_attributes)
    reshuffler.calc()
