import os
from datetime import datetime
from gldas.interface import GLDAS_Noah_v21_025Ds
from reshuffle_GLDAS import reshuffle

# input folder template
# C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\gldas-noah-2.1-0.25deg_global\GLDAS Noah 0.25 2016
# output folder template
# C:\Nina_PCTower_Share\PCTower_SM\GLDAS_reshuffle\2015

input_dir = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\gldas-noah-2.1-0.25deg_global\GLDAS_global"
output_dir = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\gldas-noah-2.1-0.25deg_global\GLDAS_global_reshuffle"

parameters = ['SoilMoi0_10cm_inst']

# assumes NC4 format
# moving reader from reshuffle file to this file, passing reader to reshuffle instead of dir
# suppressing landgrid since that seems to be out of date
input_dataset = GLDAS_Noah_v21_025Ds(input_dir, parameters, array_1D=True)
# input_dataset = GLDAS_Noah_v21_025Ds(input_root, parameters, landgrid=None, array_1D=True)
# for some reason I have to manually set this if I have my files flat?
input_dataset.subpath_templ = []
startdate = datetime(2015, 1, 1)
enddate = datetime(2018, 12, 31, 23, 59)
reshuffle(input_dataset, output_dir, startdate, enddate, parameters)

