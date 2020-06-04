"""
Author: Nina del Rosario
Date: 5/25/2020
Script for analyzing SM datasets
For icos analysis see sm_analysis_icos.py
"""

# function which compares reference data to evaluation data
# reference can be either ISMN, ICOS, or GLDAS
def evaluate(reference_type, reference_loc_dict, product_reader, startdate, enddate):
    # ICOS: see existing dictionary
    # ISMN: one network at a time
    # GLDAS: one big network, prefix existing networks e.g. ICOS_Degero
    # I
    pass
