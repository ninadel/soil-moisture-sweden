"""
Author: Nina del Rosario
Date: 6/2/2020
Configuration settings for sm analysis
"""
import json
import os
import sm_tools as tools

timestamp = tools.get_timestamp()

analysis_output_root = r"..\analysis_output"
analysis_output_dir = os.path.join(analysis_output_root,'{}_output'.format(timestamp))
icos_logfile = os.path.join(analysis_output_dir, "{}_ICOS_log.txt".format(timestamp))
ismn_logfile = os.path.join(analysis_output_dir, "{}_ISMN_log.txt".format(timestamp))

# directory that has ICOS in situ data, used to determine which stations to use in analysis
icos_input_dir = r"..\icos_data"
icos_files = tools.get_icos_stations(icos_input_dir)

# dictionary for dataset parameters, for each reader in this dictionary, make sure the class is imported
datasets_dict = {'ASCAT 12.5 TS':
    {
        'ts_dir': r'..\input_data\ascat-h115-ts-2019',
        'grid_dir': r'..\ascat_ts_aux\warp5_grid',
        'grid_file': 'TUW_WARP5_grid_info_2_3.nc',
        'static_layers_dir': r'..\ascat_ts_aux\static_layer',
        'reader_name': 'ascat_12-5_ts',
        'reader_class': 'H115Ts(ts_dir, grid_dir, grid_filename=grid_file, static_layer_path=static_layers_dir)',
        'sm_field': 'sm'
    }
}

# open external dictionaries
# dictionary which defines timeframes to analyze
with open('timeframes_dict.json', 'r') as f:
    timeframes_dict = json.load(f)

# dictionary which defines timeframes to analyze
with open('icos_dict.json', 'r') as f:
    icos_dict = json.load(f)

# load networks_dict from external file
with open('networks_dict.json', 'r') as f:
    networks_dict = json.load(f)
