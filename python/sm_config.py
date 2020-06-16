"""
Author: Nina del Rosario
Date: 6/2/2020
Configuration settings for sm analysis
"""
from datetime import datetime
import json

icos_input_dir = r"..\icos_data"
ismn_input_dir = r"..\ismn_data\HOBE_Data_2015-2018"

metrics_df_columns = ["network", "station", "ref_filtered", "product", "product_filtered", "timeframe", "anomaly", "n",
                      "bias", "rmsd", "ubrmsd", "pearsonr", "pearsonr_p"]

# dictionary for dataset parameters, for each reader in this dictionary, make sure the class is imported
dict_product_inputs = {
    "ASCAT SM-OBS-2": {
        "ts_dir": None
    },
    "ASCAT 12.5 TS": {
        "ts_dir": r"..\input_data\ascat-h115-ts-2019",
        "grid_dir": r"..\ascat_ts_aux\warp5_grid",
        "grid_file": "TUW_WARP5_grid_info_2_3.nc",
        "static_layers_dir": None
    },
    "CCI Active": {
        "ts_dir": None
    },
    "CCI Passive": {
        "ts_dir": None
    },
    "CCI Combined": {
        "ts_dir": r"C:\git\soil-moisture-sweden\input_data\cci-0.25deg_global_reshuffle"
    },
    "GLDAS": {
        "ts_dir": r"..\input_data\GLDAS_global_reshuffle",
    },
    "SMAP L3": {
        "ts_dir": r"..\input_data\SPL3SMP-smap-l3-36km_nordic_reshuffle"
    },
    "SMAP L3 Enhanced": {
        "ts_dir": None
    },
    "SMAP L4": {
        "ts_dir": r"..\input_data\SPL4SMAU_nordic_reshuffle"
    },
    "Sentinel-1": {
        "ts_dir": None
    },
    "SMOS-BEC": {
        "ts_dir": None
    },
    "SMOS-IC": {
        "ts_dir": r"C:\git\soil-moisture-sweden\input_data\smos-ic-l3-25km_global_reshuffle\ASC"
    }
}

# open external dictionaries
# dictionary which defines timeframes to analyze
with open("dict_timeframes.json", "r") as f:
    dict_timeframes = json.load(f)

# dictionary which stores static fields (e.g. lat, lon, sm field)
with open("dict_product_fields.json", "r") as f:
    dict_product_fields = json.load(f)

# dictionary which stores GLDAS grid points
with open("dict_swe_gldas_points.json", "r") as f:
    dict_swe_gldas_points = json.load(f)