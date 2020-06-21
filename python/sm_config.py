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

year_timeframes = [2015, 2016, 2017, 2018]
season_timeframes = ['non-winter', 'winter', 'spring', 'summer', 'fall']

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
        "ts_dir": r"..\input_data\cci-0.25deg_active_global_reshuffle"
    },
    "CCI Passive": {
        "ts_dir": r"..\input_data\cci-0.25deg_passive_global_reshuffle"
    },
    "CCI Combined": {
        "ts_dir": r"..\input_data\cci-0.25deg_combined_global_reshuffle"
    },
    "GLDAS": {
        "ts_dir": r"..\input_data\GLDAS_nordic_reshuffle",
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
        "raw_dir": r"C:\git\soil-moisture-sweden\input_data\cgls-biopar-ssm-01km_nordic",
        "ts_dir": r"..\input_data\sentinel_ts",
        # in the situation where no timestamp is available (i.e. defaults to midnight)
        # set hours_shift to local overpass time in UTC
        "hours_shift": 18
    },
    "SMOS-BEC": {
        "ts_dir": None
    },
    "SMOS-IC": {
        "ts_dir": r"C:\git\soil-moisture-sweden\input_data\smos-ic-l3-25km_global_reshuffle\ASC"
    }
}

# for products that default to midnight, these dictionary values shift datetimeindex values to local overpass in UTC
# through the tools.get_timeshifted_data function
dict_timeshifts = {
    "ASCAT SM-OBS-2": None,
    # Timestamps are already present in TS
    "ASCAT 12.5 TS": None,
    # CCI Active Force Timestamp: 9:30AM CET, 8:30AM UTC based on ASCAT overpasses
    "CCI Active": (30600, 'S'),
    # CCI Passive Force Timestamp: 6AM CET, 5AM UTC
    "CCI Passive": (5, 'H'),
    # CCI Combined Force Timestamp: 8AM CET, 7AM UTC based on average of Active and Passive products
    "CCI Combined": (7, 'H'),
    # GLDAS Timestamps already present in ts
    "GLDAS": None,
    # SMAP L3 Force Timestamp: 6AM CET, 5AM UTC
    "SMAP L3": (5, 'H'),
    "SMAP L3 Enhanced": None,
    # SMAP L4 Timestamps already present in ts
    "SMAP L4": None,
    # Sentinel-1 timestamps present in data
    "Sentinel-1": None,
    "SMOS-BEC": None,
    "SMOS-IC": (5, 'H')
}

# open external dictionaries
# dictionary which defines timeframes to analyze
with open("dict_timeframes.json", "r") as f:
    dict_timeframes = json.load(f)

# dictionary which stores static fields (e.g. lat, lon, sm field)
with open("dict_product_fields.json", "r") as f:
    dict_product_fields = json.load(f)

# dictionary which stores ICOS stations
with open("dict_icos.json", "r") as f:
    dict_icos = json.load(f)

# dictionary which stores HOBE stations
with open("dict_hobe.json", "r") as f:
    dict_hobe = json.load(f)

# dictionary which stores GLDAS grid points
with open("dict_swe_gldas_points.json", "r") as f:
    dict_swe_gldas_points = json.load(f)

swe_shuffle_cells = [1397, 1398, 1399, 1433, 1434, 1435, 1470, 1471]
den_shuffle_cells = [1360, 1361, 1396, 1397, 1433]
nordic_shuffle_cells = [1326, 1360, 1361, 1362, 1396, 1397, 1398, 1399, 1433, 1434, 1435, 1436, 1469, 1470, 1471, 1472,
                        1506, 1507, 1508, 1542, 1543, 1544]