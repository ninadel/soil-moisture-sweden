'''
Author: Nina del Rosario
Date: 6/2/2020
Configuration settings for sm analysis
'''
from datetime import datetime
import json

icos_input_dir = r'..\icos_data'
ismn_input_dir = r'..\ismn_data\HOBE_Data_2015-2018'

metrics_df_columns = ['network', 'station', 'ref_filtered', 'product', 'product_filtered', 'timeframe', 'anomaly', 'n',
                      'bias', 'rmsd', 'ubrmsd', 'pearsonr', 'pearsonr_p']

# dictionary for dataset parameters, for each reader in this dictionary, make sure the class is imported
datasets_dict = {'ASCAT 12.5 TS':
    {
        'ts_dir': r'..\input_data\ascat-h115-ts-2019',
        'grid_dir': r'..\ascat_ts_aux\warp5_grid',
        'grid_file': 'TUW_WARP5_grid_info_2_3.nc',
        'static_layers_dir': None,
        'sm_field': 'sm'
    },
    'GLDAS': {
        'ts_dir': r'..\input_data\GLDAS_global_reshuffle',
        'sm_field': 'SoilMoi0_10cm_inst'
    },
    'SMAP L3': {
        'ts_dir': r'..\input_data\SPL3SMP-smap-l3-36km_nordic_reshuffle',
        'sm_field': 'soil_moisture'
    },
    'SMAP L4': {
        'ts_dir': r'..\input_data\SPL4SMAU_nordic_reshuffle',
        'sm_field': 'sm_surface_analysis'
    }
}

# open external dictionaries
# dictionary which defines timeframes to analyze
with open('timeframes_dict.json', 'r') as f:
    timeframes_dict = json.load(f)

# dictionary which defines timeframes to analyze
# with open('icos_dict.json', 'r') as f:
#     icos_dict = json.load(f)
#
# # load networks_dict from external file
# with open('networks_dict.json', 'r') as f:
#     networks_dict = json.load(f)
