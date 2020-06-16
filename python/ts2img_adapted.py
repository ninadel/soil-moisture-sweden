# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
module for conversion of time series data to image data
Created on Mon Apr 20 11:08:58 2015

@author: christoph.paulik@geo.tuwien.ac.at
'''

import numpy as np


def agg_tsmonthly(ts, **kwargs):
    """
    Parameters
    ----------
    ts : pandas.DataFrame
        time series of a point
    kwargs : dict
        any additional keyword arguments that are given to the ts2img object
        during initialization

    Returns
    -------
    ts_agg : pandas.DataFrame
        aggregated time series, they all must have the same length
        otherwise it can not work
        each column of this DataFrame will be a layer in the image
    """
    # very simple example
    # aggregate to monthly timestamp
    # should also make sure that the output has a certain length
    return ts.asfreq("M")


class Ts2Img(object):

    """
    Takes a time series dataset and converts it
    into an image dataset.
    A custom aggregate function should be given otherwise
    a daily mean will be used

    Parameters
    ----------
    tsreader: object
        object that implements a iter_ts method which iterates over
        pandas time series and has a grid attribute that is a pytesmo
        BasicGrid or CellGrid
    imgwriter: object
        writer object that implements a write_ts method that takes
        a list of grid point indices and a 2D array containing the time series data
    agg_func: function
        function that takes a pandas DataFrame and returns
        an aggregated pandas DataFrame
    ts_buffer: int
        how many time series to read before writing to disk,
        constrained by the working memory the process should use.

    """

    def __init__(self, tsreader, imgwriter,
                 agg_func=None,
                 ts_buffer=1000):

        self.agg_func = agg_func
        if self.agg_func is None:
            try:
                self.agg_func = tsreader.agg_ts2img
            except AttributeError:
                self.agg_func = agg_tsmonthly
        self.tsreader = tsreader
        self.imgwriter = imgwriter
        self.ts_buffer = ts_buffer

    def calc(self, **tsaggkw):
        """
        does the conversion from time series to images
        """
        for gpis, ts in self.tsbulk(**tsaggkw):
            self.imgwriter.write_ts(gpis, ts)

    def tsbulk(self, gpis=None, **tsaggkw):
        """
        iterator over gpi and time series arrays of size self.ts_buffer

        Parameters
        ----------
        gpis: iterable, optional
            if given these gpis will be used, can be practical
            if the gpis are managed by an external class e.g. for parallel
            processing
        tsaggkw: dict
            Keywords to give to the time series aggregation function


        Returns
        -------
        gpi_array: numpy.array
            numpy array of gpis in this batch
        ts_bulk: dict of numpy arrays
            for each variable one numpy array of shape
            (len(gpi_array), len(ts_aggregated))
        """
        # have to use the grid iteration as long as iter_ts only returns
        # data frame and no time series object including relevant metadata
        # of the time series
        i = 0
        gpi_bulk = []
        ts_bulk = {}
        ts_index = None
        if gpis is None:
            # get grid points can return either 3 or 4 values
            # depending on the grid type, gpis is the first in both cases
            gpi_info = list(self.tsreader.grid.grid_points())
            gpis = np.array(gpi_info[0], dtype=np.int)
        for gpi in gpis:
            gpi_bulk.append(gpi)
            ts = self.tsreader.read_ts(gpi)
            ts_agg = self.agg_func(ts, **tsaggkw)
            for column in ts_agg.columns:
                try:
                    ts_bulk[column].append(ts_agg[column].values)
                except KeyError:
                    ts_bulk[column] = []
                    ts_bulk[column].append(ts_agg[column].values)

            if ts_index is None:
                ts_index = ts_agg.index

            i += 1
            if i >= self.ts_buffer:
                for key in ts_bulk:
                    ts_bulk[key] = np.vstack(ts_bulk[key])
                gpi_array = np.hstack(gpi_bulk)
                yield gpi_array, ts_bulk
                ts_bulk = {}
                gpi_bulk = []
                i = 0
        if i > 0:
            for key in ts_bulk:
                ts_bulk[key] = np.vstack(ts_bulk[key])
            gpi_array = np.hstack(gpi_bulk)
            yield gpi_array, ts_bulk
