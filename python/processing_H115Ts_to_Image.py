"""""
Author: Nina del Rosario
Date: 6/11/2020
Script for converting H115Ts to Image set
"""""

from ascat.h_saf import H115Ts
import sm_config as config
from repurpose.ts2img import Ts2Img


ts_reader = H115Ts(cdr_path=config.product_inputs_dict['ASCAT 12.5 TS']['ts_dir'],
                   grid_path=config.product_inputs_dict['ASCAT 12.5 TS']['grid_dir'],
                   grid_filename=config.product_inputs_dict['ASCAT 12.5 TS']['grid_file'],
                   static_layer_path=config.product_inputs_dict['ASCAT 12.5 TS']['static_layers_dir'])

# Degero: 19.556539 64.182029
# ts = ts_reader.read(19.556539, 64.182029)
#
# print(ts)
# print(ts.data.columns)
# print('ts.data', ts.data.shape)
# print(ts.data['ssf'])

# help(ts_reader)

# def __init__(self, tsreader, imgwriter,
#              agg_func=None,
#              ts_buffer=1000):

ts_writer = Ts2Img(H115Ts, H115Ts)

print(type(ts_writer))
# help(ts_writer)
print(type(ts_writer.tsbulk()))
print(ts_writer.tsbulk.__dict__)