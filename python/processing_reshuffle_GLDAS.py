import os
from datetime import datetime
from gldas.interface import GLDAS_Noah_v21_025Ds
from reshuffle_GLDAS import reshuffle

input_root = r'C:\git\soil-moisture-sweden\sm_sample_files\gldas-noah-2.1-0.25deg'
outputpath = r'C:\git\soil-moisture-sweden\test_output_data\test_gldas_shuffle'
startdate = datetime(2018,6,1)
enddate = datetime(2018,6,30,23,59,59)
parameters = ['SoilMoi0_10cm_inst']

# assumes NC4 format
# moving reader from reshuffle file to this file, passing reader to reshuffle instead of dir
# suppressing landgrid since that seems to be out of date
input_dataset = GLDAS_Noah_v21_025Ds(input_root, parameters, array_1D=True)

# input_dataset = GLDAS_Noah_v21_025Ds(input_root, parameters, landgrid=None, array_1D=True)
# for some reason I havve to manually set this if I have my files flat?
input_dataset.subpath_templ = []

reshuffle(input_dataset, outputpath, startdate, enddate, parameters)

