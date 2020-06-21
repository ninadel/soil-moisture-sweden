"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 6/1/2020
Script to copy files for cells coinciding with Nordic Region & grid.nc
"""
import os
import shutil
import sm_config as config

input_folder = r"C:\Nina_PCTower_Share\PCTower_SM\SPL3SMP-smap-l3-36km_global_reshuffle"
output_folder = r"C:\Nina_PCTower_Share\PCTower_SM\SPL3SMP-smap-l3-36km_nordic_reshuffle"
region_cells = config.nordic_shuffle_cells
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# copy grid nc file
shutil.copy(os.path.join(input_folder, "grid.nc"), os.path.join(output_folder, "grid.nc"))

# copy cells in region
for cell in region_cells:
    input_file = os.path.join(input_folder, "{}.nc".format(cell))
    output_file = os.path.join(output_folder, "{}.nc".format(cell))
    shutil.copy(input_file, output_file)