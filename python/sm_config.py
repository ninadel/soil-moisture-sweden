"""
Author: Nina del Rosario
Date: 6/2/2020
Configuration settings for sm analysis
"""
from datetime import datetime
import json
import numpy
import warnings

icos_input_dir = r"..\icos_data"
ismn_input_dir = r"..\ismn_data\HOBE_Data_2015-2018"
raw_data_dir = r"D:\sm_backup"

metrics_df_columns = ["network", "station", "product", "timeframe", "anomaly", "n", "bias", "rmsd", "ubrmsd",
                      "pearsonr", "pearsonr_p"]

year_timeframes = [2015, 2016, 2017, 2018]
season_timeframes = ['non-winter', 'winter', 'spring', 'summer', 'fall']

# dictionary for dataset parameters, for each reader in this dictionary, make sure the class is imported
dict_product_inputs = {
    "ASCAT 12.5 TS": {
        "ts_dir": r"..\input_data\ascat-h115-ts-2019",
        "grid_dir": r"..\ascat_ts_aux\warp5_grid",
        "grid_file": "TUW_WARP5_grid_info_2_3.nc",
        "static_layers_dir": None,
        "csv_stations": None,
        "csv_quarters": None
    },
    "CCI Active": {
        "ts_dir": r"..\input_data\cci-0.25deg_active_global_reshuffle",
        "csv_stations": None,
        "csv_quarters": None
    },
    "CCI Passive": {
        "ts_dir": r"..\input_data\cci-0.25deg_passive_global_reshuffle",
        "csv_stations": None,
        "csv_quarters": None
    },
    "CCI Combined": {
        "ts_dir": r"..\input_data\cci-0.25deg_combined_global_reshuffle",
        "csv_stations": None,
        "csv_quarters": None
    },
    "ERA5": {
        "ts_dir": None,
        "csv_stations": None,
        "csv_quarters": None
    },
    "GLDAS": {
        "ts_dir": r"..\input_data\GLDAS_nordic_reshuffle",
        "csv_stations": None,
        "csv_quarters": None
    },
    "SMAP L3": {
        "ts_dir": r"..\input_data\SPL3SMP-smap-l3-36km_nordic_reshuffle",
        "csv_stations": None,
        "csv_quarters": None
    },
    "SMAP L3 Enhanced": {
        "ts_dir": None,
        "csv_stations": None,
        "csv_quarters": None
    },
    "SMAP L4": {
        "ts_dir": r"..\input_data\SPL4SMAU_nordic_reshuffle",
        "csv_stations": None,
        "csv_quarters": None
    },
    "Sentinel-1": {
        "raw_dir": r"..\input_data\cgls-biopar-ssm-01km_nordic",
        "ts_dir": r"..\input_data\csv_stations\sentinel_ts",
        "csv_stations": r"..\input_data\csv_stations\sentinel_ts",
        "csv_quarters": None
    },
    "SMOS-BEC": {
        "raw_dir": r"..\input_data\smos-bec-reprocessed-01km-nordic\ASC",
        "ts_dir": r"..\input_data\csv_stations\smos-bec_ts",
        "csv_stations": r"..\input_data\csv_stations\smos-bec_ts",
        "csv_quarters": None
    },
    "SMOS-IC": {
        "ts_dir": r"C:\git\soil-moisture-sweden\input_data\smos-ic-l3-25km_global_reshuffle\ASC",
        "csv_stations": None,
        "csv_quarters": None
    }
}

# for products that default to midnight, these dictionary values shift datetimeindex values to local overpass in UTC
# through the tools.get_timeshifted_data function
dict_timeshifts = {
    # Timestamps are already present in TS
    "ASCAT 12.5 TS": None,
    # CCI Active Force Timestamp: 9:30AM CET, 8:30AM UTC based on ASCAT overpasses
    "CCI Active": (30600, 'S'),
    # CCI Passive Force Timestamp: 6AM CET, 5AM UTC
    "CCI Passive": (5, 'H'),
    # CCI Combined Force Timestamp: 8AM CET, 7AM UTC based on average of Active and Passive products
    "CCI Combined": (7, 'H'),
    # ERA5 Timestamps already present in ts
    "ERA5": None,
    # GLDAS Timestamps already present in ts
    "GLDAS": None,
    # SMAP L3 Force Timestamp: 6AM CET, 5AM UTC
    "SMAP L3": (5, 'H'),
    # SMAP L3E Force Timestamp: 6AM CET, 5AM UTC
    "SMAP L3 Enhanced": (5, 'H'),
    # SMAP L4 Timestamps already present in ts
    "SMAP L4": None,
    # Sentinel-1 timestamps present in data
    "Sentinel-1": (18, 'H'),
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

# dictionary which stores GLDAS grid points
with open("dict_extent_sweden.json", "r") as f:
    dict_extent_sweden = json.load(f)

regrid_lat = numpy.arange(dict_extent_sweden["min_lat"]-1, dict_extent_sweden["max_lat"]+1, 0.25)
regrid_lon = numpy.arange(dict_extent_sweden["min_lon"]-1, dict_extent_sweden["max_lon"]+1, 0.25)
regrid_lat_b = numpy.arange(dict_extent_sweden["min_lat"]-1.125, dict_extent_sweden["max_lat"]+1.125, 0.25)
regrid_lon_b = numpy.arange(dict_extent_sweden["min_lon"]-1.125, dict_extent_sweden["max_lon"]+1.125, 0.25)
interp_lat = numpy.arange(dict_extent_sweden["min_lat"]-2, dict_extent_sweden["max_lat"]+2, 0.25)
interp_lon = numpy.arange(dict_extent_sweden["min_lon"]-2, dict_extent_sweden["max_lon"]+2, 0.25)


swe_shuffle_cells = [1397, 1398, 1399, 1433, 1434, 1435, 1470, 1471]
den_shuffle_cells = [1360, 1361, 1396, 1397, 1433]
nordic_shuffle_cells = [1326, 1360, 1361, 1362, 1396, 1397, 1398, 1399, 1433, 1434, 1435, 1436, 1469, 1470, 1471, 1472,
                        1506, 1507, 1508, 1542, 1543, 1544]

