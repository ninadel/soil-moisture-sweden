"""
Author: Nina del Rosario
Date: 5/25/2020
Script for analyzing SM datasets
For icos analysis see sm_analysis_icos.py
"""
from datetime import datetime
import numpy
import os
import pandas

from ascat import H115Ts
import ismn.interface as ismn
from pytesmo import temporal_matching, scaling, df_metrics, metrics
import sm_tools as tools
import sm_config as config

# function which compares reference data to evaluation data
# reference can be either ISMN, ICOS, or GLDAS
# def evaluate(products, references, reference_loc_dict, product_reader, startdate, enddate):
def evaluate(products, references):
    product_list = tools.get_product_list(products)
    for product in product_list:
        for station in references:
            if str(type(station)) == "<class 'icos.ICOSTimeSeries'>":
                print(station.station, station.network)
            elif str(type(station)) == "<class 'ismn.interface.ISMN_station'>":
                print(station.station, station.network)
    # ICOS: see existing dictionary
    # ISMN: one network at a time
    # GLDAS: one big network, prefix existing networks e.g. ICOS_Degero


# Dictionary to set analyses to perform
analyses_dict = {
    "ASCAT 12.5 TS": {
        "analyze": True
    },
    "GLDAS": {
        "analyze": False
    },
    "SMAP L3": {
        "analyze": False
    },
    "SMAP L4": {
        "analyze": False
    }
}

icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
reference_list = ismn_readers + icos_readers

evaluate(analyses_dict, reference_list)