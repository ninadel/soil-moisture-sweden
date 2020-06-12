from datetime import datetime
from reshuffle_ASCAT_H08 import reshuffle
from ascat.h_saf import H08img

parameters = ['ssm', 'proc_flag', 'ssm_noise', 'corr_flag']
input_dir = r"../test_input_data"
output_dir = r"../test_output_data"

input_dataset = H08img(input_dir)

startdate = datetime(2018, 6, 1, 6, 15)
enddate = datetime(2018, 6, 30, 23, 59)

reshuffle(input_dir, output_dir, startdate, enddate, parameters, imgbuffer=50)

