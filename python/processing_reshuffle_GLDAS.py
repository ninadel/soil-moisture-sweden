import os
from datetime import datetime
from gldas.interface import GLDAS_Noah_v21_025Ds
from reshuffle_GLDAS import reshuffle

# input folder template
# C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\gldas-noah-2.1-0.25deg_global\GLDAS Noah 0.25 2016
# output folder template
# C:\Nina_PCTower_Share\PCTower_SM\GLDAS_reshuffle\2015

input_root = r"C:\Users\ninad\OneDrive - Lund University\Dokument\SM_Data_ReadOnly\gldas-noah-2.1-0.25deg_global"
output_root = r"C:\Nina_PCTower_Share\PCTower_SM\GLDAS_reshuffle"

parameters = ['SoilMoi0_10cm_inst']

year_strs = ['2016', '2017', '2018', '2015']
# year_strs = ['2016', '2017', '2018']

for year in year_strs:
    year_int = int(year)
    input_subdir = "GLDAS Noah 0.25 {}".format(year)
    input_dir = os.path.join(input_root, input_subdir)
    print(input_dir)
    output_dir = os.path.join(output_root, year)
    print(output_dir)
    # assumes NC4 format
    # moving reader from reshuffle file to this file, passing reader to reshuffle instead of dir
    # suppressing landgrid since that seems to be out of date
    input_dataset = GLDAS_Noah_v21_025Ds(input_dir, parameters, array_1D=True)
    # input_dataset = GLDAS_Noah_v21_025Ds(input_root, parameters, landgrid=None, array_1D=True)
    # for some reason I havve to manually set this if I have my files flat?
    input_dataset.subpath_templ = []
    startdate = datetime(year_int, 1, 1)
    print(startdate)
    enddate = datetime(year_int, 12, 31, 23, 59)
    print(enddate)
    reshuffle(input_dataset, output_dir, startdate, enddate, parameters)

