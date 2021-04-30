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
# raw_data_dir = r"D:\sm_backup"

metrics_df_columns = ["network", "station", "product", "timeframe", "anomaly", "n", "bias", "rmsd", "ubrmsd",
                      "pearsonr", "pearsonr_p"]

year_timeframes = [2015, 2016, 2017, 2018]
season_timeframes = ['non-winter', 'winter', 'spring', 'summer', 'fall']

# dictionary for dataset parameters, for each reader in this dictionary, make sure the class is imported
dict_product_inputs = {
    "ASCAT 12.5 TS": {
        "ts_dir": r"D:\sm_backup\native\ascat-h115-ts-2019",
        "grid_dir": r"..\ascat_ts_aux\warp5_grid",
        "grid_file": "TUW_WARP5_grid_info_2_3.nc",
        "static_layers_dir": None,
        "csv_stations": r"..\input_data\csv_stations\ASCAT 12.5 TS",
        "csv_quarters": r"..\input_data\csv_quarters\ASCAT 12.5 TS"
    },
    "CCI Active": {
        "ts_dir": r"..\input_data\cci-0.25deg_active_global_reshuffle",
        "csv_stations": r"..\input_data\csv_stations\CCI Active",
        "csv_quarters": r"..\input_data\csv_quarters\CCI Active"
    },
    "CCI Passive": {
        "ts_dir": r"..\input_data\cci-0.25deg_passive_global_reshuffle",
        "csv_stations": r"..\input_data\csv_stations\CCI Passive",
        "csv_quarters": r"..\input_data\csv_quarters\CCI Passive"
    },
    "CCI Combined": {
        "ts_dir": r"..\input_data\cci-0.25deg_combined_global_reshuffle",
        "csv_stations": r"..\input_data\csv_stations\CCI Combined",
        "csv_quarters": r"..\input_data\csv_quarters\CCI Combined"
    },
    "ERA5 0-1": {
        "ts_dir": None,
        "csv_stations": r"..\input_data\csv_stations\ERA5 0-1",
        "csv_quarters": r"..\input_data\csv_quarters\ERA5 0-1"
    },
    "ERA5 0-25": {
        "ts_dir": None,
        "csv_stations": r"..\input_data\csv_stations\ERA5 0-25",
        "csv_quarters": None
    },
    "GLDAS": {
        "ts_dir": r"..\input_data\GLDAS_nordic_reshuffle",
        "csv_stations": r"..\input_data\csv_stations\GLDAS",
        "csv_quarters": r"..\input_data\csv_quarters\GLDAS"
    },
    "Sentinel-1": {
        "raw_dir": r"..\input_data\cgls-biopar-ssm-01km_nordic",
        "ts_dir": None,
        "csv_stations": r"..\input_data\csv_stations\Sentinel-1",
        "csv_quarters": r"..\input_data\csv_quarters\Sentinel-1"
    },
    "SMAP L3": {
        "ts_dir": r"..\input_data\SPL3SMP-smap-l3-36km_nordic_reshuffle",
        "csv_stations": r"..\input_data\csv_stations\SMAP L3",
        "csv_quarters": r"..\input_data\csv_quarters\SMAP L3"
    },
    "SMAP L3 Enhanced": {
        "ts_dir": None,
        "csv_stations": r"..\input_data\csv_stations\SMAP L3 Enhanced",
        "csv_quarters": r"..\input_data\csv_quarters\SMAP L3 Enhanced"
    },
    "SMAP L4": {
        "ts_dir": r"..\input_data\SPL4SMAU_nordic_reshuffle",
        "csv_stations": r"..\input_data\csv_stations\SMAP L4",
        "csv_quarters": r"..\input_data\csv_quarters\SMAP L4"
    },
    "SMOS-BEC": {
        "raw_dir": r"..\input_data\smos-bec-reprocessed-01km-nordic\ASC",
        "ts_dir": None,
        "csv_stations": r"..\input_data\csv_stations\SMOS-BEC",
        "csv_quarters": r"..\input_data\csv_quarters\SMOS-BEC"
    },
    "SMOS-IC": {
        "ts_dir": r"C:\git\soil-moisture-sweden\input_data\smos-ic-l3-25km_global_reshuffle\ASC",
        "csv_stations": r"..\input_data\csv_stations\SMOS-IC",
        "csv_quarters": r"..\input_data\csv_quarters\SMOS-IC"
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
    "ERA5 0-1": None,
    # GLDAS Timestamps already present in ts
    "ERA5 0-25": None,
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

ignore_veg_classes = ["missing value", "Ocean"]

dict_quarterdeg_files = {
    "ASCAT 12.5 TS": r"..\input_data\xr\regrid\ascat-h115_0-25-regrid.nc",
    "CCI Active": r"..\input_data\xr\cci-active-subset-nofilter.nc",
    "CCI Passive": r"..\input_data\xr\cci-passive-subset-nofilter.nc",
    "CCI Combined": r"..\input_data\xr\cci-combined-subset-nofilter.nc",
    "ERA5 0-1": r"..\input_data\xr\regrid\era-0-1_0-25-regrid.nc",
    "GLDAS": r"..\input_data\xr\gldas-subset-nofilter.nc",
    "SMAP L3": r"..\input_data\xr\regrid\smap-L3_0-25-regrid.nc",
    "SMAP L3 Enhanced": r"..\input_data\xr\regrid\smap-L3E_0-25-regrid.nc",
    "SMAP L4": r"..\input_data\xr\regrid\smap-L4_0-25-regrid.nc",
    "Sentinel-1": r"..\input_data\xr\regrid\sentinel_0-25-regrid.nc",
    "SMOS-BEC": r"..\input_data\xr\regrid\smos-bec_0-25-regrid.nc",
    "SMOS-IC": r"..\input_data\xr\regrid\smos-ic_0-25-regrid.nc"
}

dict_native_files = {
    "ASCAT 12.5 TS": r"..\input_data\xr\ascat-h115_rebuild-subset-nofilter.nc",
    "CCI Active": r"..\input_data\xr\cci-active-subset-nofilter.nc",
    "CCI Passive": r"..\input_data\xr\cci-passive-subset-nofilter.nc",
    "CCI Combined": r"..\input_data\xr\cci-combined-subset-nofilter.nc",
    "ERA5 0-1": r"..\input_data\ERA5-Land\0-1_ERA5-Land_hourly.nc",
    "ERA5 0-25": r"..\input_data\ERA5-Land\0-25_ERA5-Land_hourly.nc",
    "GLDAS": r"..\input_data\xr\gldas-subset-nofilter.nc",
    "SMAP L3": r"..\input_data\xr\smap-L3-36km-subset-nofilter.nc",
    "SMAP L3 Enhanced": r"..\input_data\xr\smap-L3E-09km-subset-nofilter.nc",
    "SMAP L4": r"..\input_data\xr\smap-L4-09km-subset-nofilter.nc",
    "Sentinel-1": r"..\input_data\xr\sentinel_01km-subset-nofilter.nc",
    "SMOS-BEC": r"..\input_data\xr\smos-bec_01km-subset-nofilter.nc",
    "SMOS-IC": r"..\input_data\xr\smos-ic_25km-subset-nofilter.nc"
}


# dictionary which sets timeframes to evaluate
dict_timeframes = {
  "2015": {
    "years": [
      2015
    ]
  },
  "2016": {
    "years": [
      2016
    ]
  },
  "2017": {
    "years": [
      2017
    ]
  },
  "2018": {
    "years": [
      2018
    ]
  },
  "winter": {
    "months": [
      12,
      1,
      2
    ]
  },
  "spring": {
    "months": [
      3,
      4,
      5
    ]
  },
  "summer": {
    "months": [
      6,
      7,
      8
    ]
  },
  "fall": {
    "months": [
      9,
      10,
      11
    ]
  },
  "warm-months": {
    "months": [
      4,
      5,
      6,
      7,
      8,
      9,
      10
    ]
  },
  "non-drought-years": {
    "years": [
      2015,
      2016,
      2017
    ]
  },
  "drought-years": {
    "years": [
      2018
    ]
  }
}


# dictionary which specifies coordinate and soil moisture fields in soil moisture source files
dict_product_fields = {
    "ASCAT 12.5 Swath": {
        "lon_field": "lon",
        "lat_field": "lat",
        "sm_field": "soil_moisture"
    },
    "ASCAT 12.5 TS": {
        "lon_field": "lon",
        "lat_field": "lat",
        "sm_field": "sm"
    },
    "CCI Active": {
        "lon_field": "lon",
        "lat_field": "lat",
        "sm_field": "sm"
    },
    "CCI Passive": {
        "lon_field": "lon",
        "lat_field": "lat",
        "sm_field": "sm"
    },
    "CCI Combined": {
        "lon_field": "lon",
        "lat_field": "lat",
        "sm_field": "sm"
    },
    "ERA5 0-1": {
        "lon_field": "longitude",
        "lat_field": "latitude",
        "sm_field": "swvl1"
    },
    "ERA5 0-25": {
        "lon_field": "longitude",
        "lat_field": "latitude",
        "sm_field": "swvl1"
    },
    "GLDAS": {
        "lon_field": "lon",
        "lat_field": "lat",
        "time_field": "time",
        "sm_field": "SoilMoi0_10cm_inst"
    },
    "Sentinel-1": {
        "lon_field": "lon",
        "lat_field": "lat",
        "time_field": "time",
        "sm_field": "ssm"
    },
    "SMAP L3": {
        "lon_field": "longitude",
        "lat_field": "latitude",
        "sm_field": "soil_moisture"
    },
    "SMAP L3 Enhanced": {
        "lon_field": "longitude",
        "lat_field": "latitude",
        "sm_field": "soil_moisture"
    },
    "SMAP L4": {
        "lon_field": "cell_lon",
        "lat_field": "cell_lat",
        "sm_field": "sm_surface_analysis"
    },
    "SMOS-BEC": {
        "lon_field": "lon",
        "lat_field": "lat",
        "time_field": "time",
        "sm_field": "SM"
    },
    "SMOS-IC": {
        "lon_field": "lon",
        "lat_field": "lat",
        "time_field": "Days",
        "sm_field": "Soil_Moisture"
    }
}


# dictionary with metadata for ICOS stations in Sweden
dict_icos = {
  "ICOS Degero": {
    "station": "Degero",
    "network": "ICOS",
    "latitude": 64.182029,
    "longitude": 19.556539,
    "elevation": 270,
    "cover": "Wetland",
    "code": "SE-Deg"
  },
  "ICOS Hyltemossa": {
    "station": "Hyltemossa",
    "network": "ICOS",
    "latitude": 56.097581,
    "longitude": 13.419064,
    "elevation": 115,
    "cover": "Forest",
    "code": "SE-Htm"
  },
  "ICOS Lanna": {
    "station": "Lanna",
    "network": "ICOS",
    "latitude": 58.340629,
    "longitude": 13.101768,
    "elevation": 75,
    "cover": "Agriculture",
    "code": "SE-Lnn"
  },
  "ICOS Norunda": {
    "station": "Norunda",
    "network": "ICOS",
    "latitude": 60.086441,
    "longitude": 17.479455,
    "elevation": 46,
    "cover": "Forest",
    "code": "SE-Nor"
  },
  "ICOS Ostergarnsholm": {
    "station": "Ostergarnsholm",
    "network": "ICOS",
    "latitude": 57.430061,
    "longitude": 18.984339,
    "elevation": 0,
    "cover": "Ocean",
    "code": "SE-Oes"
  },
  "ICOS Stordalen": {
    "station": "Stordalen",
    "network": "ICOS",
    "latitude": 68.356003,
    "longitude": 19.0452,
    "elevation": 360,
    "cover": "Wetland",
    "code": "SE-Sto"
  },
  "ICOS Svartberget": {
    "station": "Svartberget",
    "network": "ICOS",
    "latitude": 64.256125,
    "longitude": 19.774413,
    "elevation": 270,
    "cover": "Forest",
    "code": "SE-Svb"
  }
}


# metadata for HOBE stations in Denmark
dict_hobe = {
  "HOBE 1.01": {
    "station": "1.01",
    "network": "HOBE",
    "latitude": 56.0193,
    "longitude": 9.1809,
    "elevation": 58.0,
    "cover": "Heath",
    "code": "H101"
  },
  "HOBE 1.02": {
    "station": "1.02",
    "network": "HOBE",
    "latitude": 56.0376,
    "longitude": 9.161,
    "elevation": 67.0,
    "cover": "Agriculture",
    "code": "H102"
  },
  "HOBE 1.03": {
    "station": "1.03",
    "network": "HOBE",
    "latitude": 56.0283,
    "longitude": 9.1654,
    "elevation": 69.0,
    "cover": "Heath",
    "code": "H103"
  },
  "HOBE 1.04": {
    "station": "1.04",
    "network": "HOBE",
    "latitude": 56.0733,
    "longitude": 9.3337,
    "elevation": 90.0,
    "cover": "Forest",
    "code": "H104"
  },
  "HOBE 1.05": {
    "station": "1.05",
    "network": "HOBE",
    "latitude": 56.033,
    "longitude": 9.1912,
    "elevation": 80.0,
    "cover": "Forest",
    "code": "H105"
  },
  "HOBE 1.06": {
    "station": "1.06",
    "network": "HOBE",
    "latitude": 56.0513,
    "longitude": 9.161,
    "elevation": 60.0,
    "cover": "Agriculture",
    "code": "H106"
  },
  "HOBE 1.07": {
    "station": "1.07",
    "network": "HOBE",
    "latitude": 56.0426,
    "longitude": 9.1413,
    "elevation": 60.0,
    "cover": "Agriculture",
    "code": "H107"
  },
  "HOBE 1.08": {
    "station": "1.08",
    "network": "HOBE",
    "latitude": 56.0466,
    "longitude": 9.1239,
    "elevation": 55.0,
    "cover": "Agriculture",
    "code": "H108"
  },
  "HOBE 1.09": {
    "station": "1.09",
    "network": "HOBE",
    "latitude": 56.036,
    "longitude": 9.1304,
    "elevation": 59.0,
    "cover": "Agriculture",
    "code": "H109"
  },
  "HOBE 1.10": {
    "station": "1.10",
    "network": "HOBE",
    "latitude": 56.0348,
    "longitude": 9.2392,
    "elevation": 71.0,
    "cover": "Agriculture",
    "code": "H110"
  },
  "HOBE 2.01": {
    "station": "2.01",
    "network": "HOBE",
    "latitude": 55.9398,
    "longitude": 9.2207,
    "elevation": 63.0,
    "cover": "Forest",
    "code": "H201"
  },
  "HOBE 2.02": {
    "station": "2.02",
    "network": "HOBE",
    "latitude": 55.9839,
    "longitude": 9.1624,
    "elevation": 50.0,
    "cover": "Agriculture",
    "code": "H202"
  },
  "HOBE 2.03": {
    "station": "2.03",
    "network": "HOBE",
    "latitude": 55.9816,
    "longitude": 9.1526,
    "elevation": 53.0,
    "cover": "Agriculture",
    "code": "H203"
  },
  "HOBE 2.04": {
    "station": "2.04",
    "network": "HOBE",
    "latitude": 55.9759,
    "longitude": 9.0984,
    "elevation": 45.0,
    "cover": "Agriculture",
    "code": "H204"
  },
  "HOBE 2.05": {
    "station": "2.05",
    "network": "HOBE",
    "latitude": 55.9763,
    "longitude": 9.0967,
    "elevation": 46.0,
    "cover": "Agriculture",
    "code": "H205"
  },
  "HOBE 2.06b": {
    "station": "2.06b",
    "network": "HOBE",
    "latitude": 55.9797,
    "longitude": 9.0817,
    "elevation": 43.0,
    "cover": "Agriculture",
    "code": "H206"
  },
  "HOBE 2.07": {
    "station": "2.07",
    "network": "HOBE",
    "latitude": 55.9482,
    "longitude": 9.0337,
    "elevation": 41.0,
    "cover": "Agriculture",
    "code": "H207"
  },
  "HOBE 2.08b": {
    "station": "2.08b",
    "network": "HOBE",
    "latitude": 55.9397,
    "longitude": 9.03146,
    "elevation": 38.0,
    "cover": "Agriculture",
    "code": "H208"
  },
  "HOBE 2.09": {
    "station": "2.09",
    "network": "HOBE",
    "latitude": 55.9282,
    "longitude": 9.1153,
    "elevation": 73.0,
    "cover": "Agriculture",
    "code": "H209"
  },
  "HOBE 2.10": {
    "station": "2.10",
    "network": "HOBE",
    "latitude": 55.9861,
    "longitude": 9.0907,
    "elevation": 44.0,
    "cover": "Heath",
    "code": "H210"
  },
  "HOBE 2.11": {
    "station": "2.11",
    "network": "HOBE",
    "latitude": 55.9704,
    "longitude": 9.0225,
    "elevation": 40.0,
    "cover": "Heath",
    "code": "H211"
  },
  "HOBE 3.01": {
    "station": "3.01",
    "network": "HOBE",
    "latitude": 55.8807,
    "longitude": 9.0142,
    "elevation": 52.0,
    "cover": "Agriculture",
    "code": "H301"
  },
  "HOBE 3.02": {
    "station": "3.02",
    "network": "HOBE",
    "latitude": 55.9354,
    "longitude": 8.9221,
    "elevation": 28.0,
    "cover": "Agriculture",
    "code": "H302"
  },
  "HOBE 3.03": {
    "station": "3.03",
    "network": "HOBE",
    "latitude": 55.9121,
    "longitude": 8.9462,
    "elevation": 34.0,
    "cover": "Agriculture",
    "code": "H303"
  },
  "HOBE 3.04": {
    "station": "3.04",
    "network": "HOBE",
    "latitude": 55.9106,
    "longitude": 8.9357,
    "elevation": 30.0,
    "cover": "Agriculture",
    "code": "H304"
  },
  "HOBE 3.05": {
    "station": "3.05",
    "network": "HOBE",
    "latitude": 55.9025,
    "longitude": 8.9175,
    "elevation": 36.0,
    "cover": "Agriculture",
    "code": "H305"
  },
  "HOBE 3.06": {
    "station": "3.06",
    "network": "HOBE",
    "latitude": 55.9115,
    "longitude": 8.8831,
    "elevation": 38.0,
    "cover": "Forest",
    "code": "H306"
  },
  "HOBE 3.07": {
    "station": "3.07",
    "network": "HOBE",
    "latitude": 55.9096,
    "longitude": 8.8536,
    "elevation": 26.0,
    "cover": "Agriculture",
    "code": "H307"
  },
  "HOBE 3.08": {
    "station": "3.08",
    "network": "HOBE",
    "latitude": 55.8776,
    "longitude": 9.2683,
    "elevation": 88.0,
    "cover": "Agriculture",
    "code": "H308"
  },
  "HOBE 3.09": {
    "station": "3.09",
    "network": "HOBE",
    "latitude": 55.8609,
    "longitude": 9.2945,
    "elevation": 104.0,
    "cover": "Agriculture",
    "code": "H309"
  }
}


dict_swe_gldas_points = {
  "912322": {
    "latitude": 68.375,
    "longitude": 20.625,
    "veg_class_name": "Open Shrublands "
  },
  "903692": {
    "latitude": 66.875,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902249": {
    "latitude": 66.625,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902231": {
    "latitude": 66.625,
    "longitude": 17.875,
    "veg_class_name": "Open Shrublands "
  },
  "900813": {
    "latitude": 66.375,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851823": {
    "latitude": 57.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846059": {
    "latitude": 56.875,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "841731": {
    "latitude": 56.125,
    "longitude": 12.875,
    "veg_class_name": "Cropland"
  },
  "895043": {
    "latitude": 65.375,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876294": {
    "latitude": 62.125,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879189": {
    "latitude": 62.625,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874863": {
    "latitude": 61.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874865": {
    "latitude": 61.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912324": {
    "latitude": 68.375,
    "longitude": 21.125,
    "veg_class_name": "Open Shrublands "
  },
  "910892": {
    "latitude": 68.125,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909444": {
    "latitude": 67.875,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909452": {
    "latitude": 67.875,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906570": {
    "latitude": 67.375,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903693": {
    "latitude": 66.875,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900799": {
    "latitude": 66.375,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899353": {
    "latitude": 66.125,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866215": {
    "latitude": 60.375,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863335": {
    "latitude": 59.875,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856137": {
    "latitude": 58.625,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854686": {
    "latitude": 58.375,
    "longitude": 11.625,
    "veg_class_name": "Mixed Forest "
  },
  "853265": {
    "latitude": 58.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851814": {
    "latitude": 57.875,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850377": {
    "latitude": 57.625,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843171": {
    "latitude": 56.375,
    "longitude": 12.875,
    "veg_class_name": "Mixed Forest "
  },
  "841735": {
    "latitude": 56.125,
    "longitude": 13.875,
    "veg_class_name": "Mixed Forest "
  },
  "840296": {
    "latitude": 55.875,
    "longitude": 14.125,
    "veg_class_name": "Mixed Forest "
  },
  "893599": {
    "latitude": 65.125,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870545": {
    "latitude": 61.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883492": {
    "latitude": 63.375,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873411": {
    "latitude": 61.625,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867666": {
    "latitude": 60.625,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905109": {
    "latitude": 67.125,
    "longitude": 17.375,
    "veg_class_name": "Mixed Tundra "
  },
  "905119": {
    "latitude": 67.125,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902251": {
    "latitude": 66.625,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900788": {
    "latitude": 66.375,
    "longitude": 17.125,
    "veg_class_name": "Open Shrublands "
  },
  "899340": {
    "latitude": 66.125,
    "longitude": 15.125,
    "veg_class_name": "Wooded Tundra "
  },
  "857587": {
    "latitude": 58.875,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856128": {
    "latitude": 58.625,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850393": {
    "latitude": 57.625,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847493": {
    "latitude": 57.125,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897914": {
    "latitude": 65.875,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896467": {
    "latitude": 65.625,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896471": {
    "latitude": 65.625,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895030": {
    "latitude": 65.375,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895040": {
    "latitude": 65.375,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895041": {
    "latitude": 65.375,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889260": {
    "latitude": 64.375,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887833": {
    "latitude": 64.125,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887818": {
    "latitude": 64.125,
    "longitude": 14.625,
    "veg_class_name": "Open Shrublands "
  },
  "886384": {
    "latitude": 63.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886392": {
    "latitude": 63.875,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884932": {
    "latitude": 63.625,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884956": {
    "latitude": 63.625,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880608": {
    "latitude": 62.875,
    "longitude": 12.125,
    "veg_class_name": "Wooded Tundra "
  },
  "909438": {
    "latitude": 67.875,
    "longitude": 19.625,
    "veg_class_name": "Open Shrublands "
  },
  "905108": {
    "latitude": 67.125,
    "longitude": 17.125,
    "veg_class_name": "Mixed Tundra "
  },
  "899362": {
    "latitude": 66.125,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866221": {
    "latitude": 60.375,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861894": {
    "latitude": 59.625,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860460": {
    "latitude": 59.375,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859015": {
    "latitude": 59.125,
    "longitude": 13.875,
    "veg_class_name": "missing value"
  },
  "859018": {
    "latitude": 59.125,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856138": {
    "latitude": 58.625,
    "longitude": 14.625,
    "veg_class_name": "missing value"
  },
  "856141": {
    "latitude": 58.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850385": {
    "latitude": 57.625,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847498": {
    "latitude": 57.125,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844615": {
    "latitude": 56.625,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892137": {
    "latitude": 64.875,
    "longitude": 14.375,
    "veg_class_name": "Open Shrublands "
  },
  "892145": {
    "latitude": 64.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890712": {
    "latitude": 64.625,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889259": {
    "latitude": 64.375,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889282": {
    "latitude": 64.375,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870542": {
    "latitude": 61.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876289": {
    "latitude": 62.125,
    "longitude": 12.375,
    "veg_class_name": "Open Shrublands "
  },
  "876291": {
    "latitude": 62.125,
    "longitude": 12.875,
    "veg_class_name": "Open Shrublands "
  },
  "886377": {
    "latitude": 63.875,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "913761": {
    "latitude": 68.625,
    "longitude": 20.375,
    "veg_class_name": "Wooded Tundra "
  },
  "906552": {
    "latitude": 67.375,
    "longitude": 18.125,
    "veg_class_name": "Open Shrublands "
  },
  "903677": {
    "latitude": 66.875,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859027": {
    "latitude": 59.125,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859007": {
    "latitude": 59.125,
    "longitude": 11.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857588": {
    "latitude": 58.875,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857589": {
    "latitude": 58.875,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847489": {
    "latitude": 57.125,
    "longitude": 12.375,
    "veg_class_name": "Mixed Forest "
  },
  "846057": {
    "latitude": 56.875,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846064": {
    "latitude": 56.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896461": {
    "latitude": 65.625,
    "longitude": 15.375,
    "veg_class_name": "Open Shrublands "
  },
  "869091": {
    "latitude": 60.875,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883516": {
    "latitude": 63.375,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882064": {
    "latitude": 63.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880628": {
    "latitude": 62.875,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879181": {
    "latitude": 62.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912318": {
    "latitude": 68.375,
    "longitude": 19.625,
    "veg_class_name": "Open Shrublands "
  },
  "912320": {
    "latitude": 68.375,
    "longitude": 20.125,
    "veg_class_name": "Open Shrublands "
  },
  "909449": {
    "latitude": 67.875,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902243": {
    "latitude": 66.625,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902252": {
    "latitude": 66.625,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900806": {
    "latitude": 66.375,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899369": {
    "latitude": 66.125,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899374": {
    "latitude": 66.125,
    "longitude": 23.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864773": {
    "latitude": 60.125,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863332": {
    "latitude": 59.875,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863344": {
    "latitude": 59.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856125": {
    "latitude": 58.625,
    "longitude": 11.375,
    "veg_class_name": "Mixed Forest "
  },
  "856131": {
    "latitude": 58.625,
    "longitude": 12.875,
    "veg_class_name": "missing value"
  },
  "887838": {
    "latitude": 64.125,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886386": {
    "latitude": 63.875,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883490": {
    "latitude": 63.375,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882060": {
    "latitude": 63.125,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873410": {
    "latitude": 61.625,
    "longitude": 12.625,
    "veg_class_name": "Open Shrublands "
  },
  "873420": {
    "latitude": 61.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867662": {
    "latitude": 60.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864789": {
    "latitude": 60.125,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863350": {
    "latitude": 59.875,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857569": {
    "latitude": 58.875,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851821": {
    "latitude": 57.875,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846051": {
    "latitude": 56.875,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843177": {
    "latitude": 56.375,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893578": {
    "latitude": 65.125,
    "longitude": 14.625,
    "veg_class_name": "Open Shrublands "
  },
  "893583": {
    "latitude": 65.125,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892163": {
    "latitude": 64.875,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889270": {
    "latitude": 64.375,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886382": {
    "latitude": 63.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867658": {
    "latitude": 60.625,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912327": {
    "latitude": 68.375,
    "longitude": 21.875,
    "veg_class_name": "Open Shrublands "
  },
  "900791": {
    "latitude": 66.375,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866224": {
    "latitude": 60.375,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864772": {
    "latitude": 60.125,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864783": {
    "latitude": 60.125,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863339": {
    "latitude": 59.875,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861889": {
    "latitude": 59.625,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860463": {
    "latitude": 59.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856144": {
    "latitude": 58.625,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851812": {
    "latitude": 57.875,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850386": {
    "latitude": 57.625,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "841730": {
    "latitude": 56.125,
    "longitude": 12.625,
    "veg_class_name": "Ocean "
  },
  "893587": {
    "latitude": 65.125,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889276": {
    "latitude": 64.375,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869096": {
    "latitude": 60.875,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870544": {
    "latitude": 61.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887843": {
    "latitude": 64.125,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884944": {
    "latitude": 63.625,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879168": {
    "latitude": 62.625,
    "longitude": 12.125,
    "veg_class_name": "Open Shrublands "
  },
  "874861": {
    "latitude": 61.875,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871978": {
    "latitude": 61.375,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909451": {
    "latitude": 67.875,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906572": {
    "latitude": 67.375,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900796": {
    "latitude": 66.375,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866226": {
    "latitude": 60.375,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864781": {
    "latitude": 60.125,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863355": {
    "latitude": 59.875,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861907": {
    "latitude": 59.625,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856139": {
    "latitude": 58.625,
    "longitude": 14.875,
    "veg_class_name": "missing value"
  },
  "851816": {
    "latitude": 57.875,
    "longitude": 14.125,
    "veg_class_name": "Ocean "
  },
  "847502": {
    "latitude": 57.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897915": {
    "latitude": 65.875,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897933": {
    "latitude": 65.875,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897936": {
    "latitude": 65.875,
    "longitude": 24.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869089": {
    "latitude": 60.875,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876305": {
    "latitude": 62.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887841": {
    "latitude": 64.125,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867668": {
    "latitude": 60.625,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "908008": {
    "latitude": 67.625,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902239": {
    "latitude": 66.625,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899341": {
    "latitude": 66.125,
    "longitude": 15.375,
    "veg_class_name": "Wooded Tundra "
  },
  "899344": {
    "latitude": 66.125,
    "longitude": 16.125,
    "veg_class_name": "Open Shrublands "
  },
  "863329": {
    "latitude": 59.875,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863340": {
    "latitude": 59.875,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863348": {
    "latitude": 59.875,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861901": {
    "latitude": 59.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850369": {
    "latitude": 57.625,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850371": {
    "latitude": 57.625,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846050": {
    "latitude": 56.875,
    "longitude": 12.625,
    "veg_class_name": "Mixed Forest "
  },
  "844619": {
    "latitude": 56.625,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897934": {
    "latitude": 65.875,
    "longitude": 23.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896477": {
    "latitude": 65.625,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892141": {
    "latitude": 64.875,
    "longitude": 15.375,
    "veg_class_name": "Open Shrublands "
  },
  "892156": {
    "latitude": 64.875,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889266": {
    "latitude": 64.375,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887840": {
    "latitude": 64.125,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887820": {
    "latitude": 64.125,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887826": {
    "latitude": 64.125,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886380": {
    "latitude": 63.875,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884949": {
    "latitude": 63.625,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884952": {
    "latitude": 63.625,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882070": {
    "latitude": 63.125,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880624": {
    "latitude": 62.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873425": {
    "latitude": 61.625,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873426": {
    "latitude": 61.625,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867665": {
    "latitude": 60.625,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "908003": {
    "latitude": 67.625,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906568": {
    "latitude": 67.375,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903672": {
    "latitude": 66.875,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899363": {
    "latitude": 66.125,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866228": {
    "latitude": 60.375,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860467": {
    "latitude": 59.375,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859032": {
    "latitude": 59.125,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857568": {
    "latitude": 58.875,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854689": {
    "latitude": 58.375,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847496": {
    "latitude": 57.125,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843182": {
    "latitude": 56.375,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897929": {
    "latitude": 65.875,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892164": {
    "latitude": 64.875,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870540": {
    "latitude": 61.125,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883497": {
    "latitude": 63.375,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880626": {
    "latitude": 62.875,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873417": {
    "latitude": 61.625,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871982": {
    "latitude": 61.375,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909453": {
    "latitude": 67.875,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900792": {
    "latitude": 66.375,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866223": {
    "latitude": 60.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864774": {
    "latitude": 60.125,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861890": {
    "latitude": 59.625,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844620": {
    "latitude": 56.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897919": {
    "latitude": 65.875,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897922": {
    "latitude": 65.875,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870547": {
    "latitude": 61.125,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886376": {
    "latitude": 63.875,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884959": {
    "latitude": 63.625,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882049": {
    "latitude": 63.125,
    "longitude": 12.375,
    "veg_class_name": "Wooded Tundra "
  },
  "882055": {
    "latitude": 63.125,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882057": {
    "latitude": 63.125,
    "longitude": 14.375,
    "veg_class_name": "Ocean "
  },
  "877733": {
    "latitude": 62.375,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "913762": {
    "latitude": 68.625,
    "longitude": 20.625,
    "veg_class_name": "Wooded Tundra "
  },
  "900805": {
    "latitude": 66.375,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859009": {
    "latitude": 59.125,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859019": {
    "latitude": 59.125,
    "longitude": 14.875,
    "veg_class_name": "Mixed Forest "
  },
  "857575": {
    "latitude": 58.875,
    "longitude": 13.875,
    "veg_class_name": "missing value"
  },
  "848932": {
    "latitude": 57.375,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896476": {
    "latitude": 65.625,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896480": {
    "latitude": 65.625,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895023": {
    "latitude": 65.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892161": {
    "latitude": 64.875,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889264": {
    "latitude": 64.375,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889267": {
    "latitude": 64.375,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889271": {
    "latitude": 64.375,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886372": {
    "latitude": 63.875,
    "longitude": 13.125,
    "veg_class_name": "Open Shrublands "
  },
  "886374": {
    "latitude": 63.875,
    "longitude": 13.625,
    "veg_class_name": "Open Shrublands "
  },
  "882062": {
    "latitude": 63.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879177": {
    "latitude": 62.625,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867653": {
    "latitude": 60.625,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867657": {
    "latitude": 60.625,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "908004": {
    "latitude": 67.625,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906567": {
    "latitude": 67.375,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903681": {
    "latitude": 66.875,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903682": {
    "latitude": 66.875,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900809": {
    "latitude": 66.375,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900812": {
    "latitude": 66.375,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899346": {
    "latitude": 66.125,
    "longitude": 16.625,
    "veg_class_name": "Open Shrublands "
  },
  "899348": {
    "latitude": 66.125,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866225": {
    "latitude": 60.375,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866212": {
    "latitude": 60.375,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860456": {
    "latitude": 59.375,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859028": {
    "latitude": 59.125,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847499": {
    "latitude": 57.125,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843172": {
    "latitude": 56.375,
    "longitude": 13.125,
    "veg_class_name": "Mixed Forest "
  },
  "897900": {
    "latitude": 65.875,
    "longitude": 15.125,
    "veg_class_name": "Open Shrublands "
  },
  "897908": {
    "latitude": 65.875,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896472": {
    "latitude": 65.625,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892159": {
    "latitude": 64.875,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870546": {
    "latitude": 61.125,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887822": {
    "latitude": 64.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886400": {
    "latitude": 63.875,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883514": {
    "latitude": 63.375,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873422": {
    "latitude": 61.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "908012": {
    "latitude": 67.625,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906554": {
    "latitude": 67.375,
    "longitude": 18.625,
    "veg_class_name": "Wooded Tundra "
  },
  "903665": {
    "latitude": 66.875,
    "longitude": 16.375,
    "veg_class_name": "Mixed Tundra "
  },
  "902224": {
    "latitude": 66.625,
    "longitude": 16.125,
    "veg_class_name": "Wooded Tundra "
  },
  "900802": {
    "latitude": 66.375,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864780": {
    "latitude": 60.125,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863345": {
    "latitude": 59.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857583": {
    "latitude": 58.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854703": {
    "latitude": 58.375,
    "longitude": 15.875,
    "veg_class_name": "Mixed Forest "
  },
  "850383": {
    "latitude": 57.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897910": {
    "latitude": 65.875,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893580": {
    "latitude": 65.125,
    "longitude": 15.125,
    "veg_class_name": "Open Shrublands "
  },
  "887830": {
    "latitude": 64.125,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886393": {
    "latitude": 63.875,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886397": {
    "latitude": 63.875,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880614": {
    "latitude": 62.875,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879187": {
    "latitude": 62.625,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874854": {
    "latitude": 61.875,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909448": {
    "latitude": 67.875,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906557": {
    "latitude": 67.375,
    "longitude": 19.375,
    "veg_class_name": "Open Shrublands "
  },
  "903688": {
    "latitude": 66.875,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902235": {
    "latitude": 66.625,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899338": {
    "latitude": 66.125,
    "longitude": 14.625,
    "veg_class_name": "Wooded Tundra "
  },
  "899343": {
    "latitude": 66.125,
    "longitude": 15.875,
    "veg_class_name": "Open Shrublands "
  },
  "854704": {
    "latitude": 58.375,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853260": {
    "latitude": 58.125,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850374": {
    "latitude": 57.625,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847491": {
    "latitude": 57.125,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846056": {
    "latitude": 56.875,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844622": {
    "latitude": 56.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843175": {
    "latitude": 56.375,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "838856": {
    "latitude": 55.625,
    "longitude": 14.125,
    "veg_class_name": "Cropland"
  },
  "870535": {
    "latitude": 61.125,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870543": {
    "latitude": 61.125,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887835": {
    "latitude": 64.125,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887823": {
    "latitude": 64.125,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882063": {
    "latitude": 63.125,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874867": {
    "latitude": 61.875,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874868": {
    "latitude": 61.875,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "908013": {
    "latitude": 67.625,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903684": {
    "latitude": 66.875,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909442": {
    "latitude": 67.875,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909431": {
    "latitude": 67.875,
    "longitude": 17.875,
    "veg_class_name": "Mixed Tundra "
  },
  "907990": {
    "latitude": 67.625,
    "longitude": 17.625,
    "veg_class_name": "Mixed Tundra "
  },
  "903686": {
    "latitude": 66.875,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902236": {
    "latitude": 66.625,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900783": {
    "latitude": 66.375,
    "longitude": 15.875,
    "veg_class_name": "Mixed Tundra "
  },
  "900804": {
    "latitude": 66.375,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899373": {
    "latitude": 66.125,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866227": {
    "latitude": 60.375,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863328": {
    "latitude": 59.875,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859012": {
    "latitude": 59.125,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857586": {
    "latitude": 58.875,
    "longitude": 16.625,
    "veg_class_name": "Mixed Forest "
  },
  "856129": {
    "latitude": 58.625,
    "longitude": 12.375,
    "veg_class_name": "Mixed Forest "
  },
  "851817": {
    "latitude": 57.875,
    "longitude": 14.375,
    "veg_class_name": "Mixed Forest "
  },
  "848928": {
    "latitude": 57.375,
    "longitude": 12.125,
    "veg_class_name": "Mixed Forest "
  },
  "897905": {
    "latitude": 65.875,
    "longitude": 16.375,
    "veg_class_name": "Open Shrublands "
  },
  "896469": {
    "latitude": 65.625,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896484": {
    "latitude": 65.625,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896488": {
    "latitude": 65.625,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876303": {
    "latitude": 62.125,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887827": {
    "latitude": 64.125,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886401": {
    "latitude": 63.875,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886373": {
    "latitude": 63.875,
    "longitude": 13.375,
    "veg_class_name": "Open Shrublands "
  },
  "882058": {
    "latitude": 63.125,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880612": {
    "latitude": 62.875,
    "longitude": 13.125,
    "veg_class_name": "Open Shrublands "
  },
  "910879": {
    "latitude": 68.125,
    "longitude": 19.875,
    "veg_class_name": "Open Shrublands "
  },
  "910890": {
    "latitude": 68.125,
    "longitude": 22.625,
    "veg_class_name": "Open Shrublands "
  },
  "908009": {
    "latitude": 67.625,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906559": {
    "latitude": 67.375,
    "longitude": 19.875,
    "veg_class_name": "Open Shrublands "
  },
  "903673": {
    "latitude": 66.875,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900786": {
    "latitude": 66.375,
    "longitude": 16.625,
    "veg_class_name": "Open Shrublands "
  },
  "866214": {
    "latitude": 60.375,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859026": {
    "latitude": 59.125,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854698": {
    "latitude": 58.375,
    "longitude": 14.625,
    "veg_class_name": "missing value"
  },
  "851835": {
    "latitude": 57.875,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850384": {
    "latitude": 57.625,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846062": {
    "latitude": 56.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846065": {
    "latitude": 56.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895032": {
    "latitude": 65.375,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893589": {
    "latitude": 65.125,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886371": {
    "latitude": 63.875,
    "longitude": 12.875,
    "veg_class_name": "Open Shrublands "
  },
  "880620": {
    "latitude": 62.875,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880627": {
    "latitude": 62.875,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880615": {
    "latitude": 62.875,
    "longitude": 13.875,
    "veg_class_name": "Open Shrublands "
  },
  "879173": {
    "latitude": 62.625,
    "longitude": 13.375,
    "veg_class_name": "Open Shrublands "
  },
  "874866": {
    "latitude": 61.875,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871974": {
    "latitude": 61.375,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912328": {
    "latitude": 68.375,
    "longitude": 22.125,
    "veg_class_name": "Open Shrublands "
  },
  "910880": {
    "latitude": 68.125,
    "longitude": 20.125,
    "veg_class_name": "Open Shrublands "
  },
  "906562": {
    "latitude": 67.375,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903674": {
    "latitude": 66.875,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899370": {
    "latitude": 66.125,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899371": {
    "latitude": 66.125,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899372": {
    "latitude": 66.125,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864782": {
    "latitude": 60.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860448": {
    "latitude": 59.375,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857577": {
    "latitude": 58.875,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850376": {
    "latitude": 57.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "838854": {
    "latitude": 55.625,
    "longitude": 13.625,
    "veg_class_name": "Cropland"
  },
  "897899": {
    "latitude": 65.875,
    "longitude": 14.875,
    "veg_class_name": "Mixed Tundra "
  },
  "912313": {
    "latitude": 68.375,
    "longitude": 18.375,
    "veg_class_name": "Mixed Tundra "
  },
  "908010": {
    "latitude": 67.625,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899351": {
    "latitude": 66.125,
    "longitude": 17.875,
    "veg_class_name": "Ocean "
  },
  "899354": {
    "latitude": 66.125,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899358": {
    "latitude": 66.125,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864771": {
    "latitude": 60.125,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864791": {
    "latitude": 60.125,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864793": {
    "latitude": 60.125,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863341": {
    "latitude": 59.875,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863351": {
    "latitude": 59.875,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854695": {
    "latitude": 58.375,
    "longitude": 13.875,
    "veg_class_name": "Mixed Forest "
  },
  "853247": {
    "latitude": 58.125,
    "longitude": 11.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853262": {
    "latitude": 58.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850378": {
    "latitude": 57.625,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848943": {
    "latitude": 57.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "837412": {
    "latitude": 55.375,
    "longitude": 13.125,
    "veg_class_name": "Ocean "
  },
  "897930": {
    "latitude": 65.875,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895042": {
    "latitude": 65.375,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889258": {
    "latitude": 64.375,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886395": {
    "latitude": 63.875,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883511": {
    "latitude": 63.375,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877745": {
    "latitude": 62.375,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909439": {
    "latitude": 67.875,
    "longitude": 19.875,
    "veg_class_name": "Open Shrublands "
  },
  "906564": {
    "latitude": 67.375,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905129": {
    "latitude": 67.125,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903678": {
    "latitude": 66.875,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902238": {
    "latitude": 66.625,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864775": {
    "latitude": 60.125,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854699": {
    "latitude": 58.375,
    "longitude": 14.875,
    "veg_class_name": "Cropland"
  },
  "851819": {
    "latitude": 57.875,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848938": {
    "latitude": 57.375,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847504": {
    "latitude": 57.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869103": {
    "latitude": 60.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870541": {
    "latitude": 61.125,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880616": {
    "latitude": 62.875,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877729": {
    "latitude": 62.375,
    "longitude": 12.375,
    "veg_class_name": "Open Shrublands "
  },
  "908001": {
    "latitude": 67.625,
    "longitude": 20.375,
    "veg_class_name": "Open Shrublands "
  },
  "905130": {
    "latitude": 67.125,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902244": {
    "latitude": 66.625,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900794": {
    "latitude": 66.375,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860449": {
    "latitude": 59.375,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857570": {
    "latitude": 58.875,
    "longitude": 12.625,
    "veg_class_name": "missing value"
  },
  "857573": {
    "latitude": 58.875,
    "longitude": 13.375,
    "veg_class_name": "missing value"
  },
  "854687": {
    "latitude": 58.375,
    "longitude": 11.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848945": {
    "latitude": 57.375,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847500": {
    "latitude": 57.125,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844612": {
    "latitude": 56.625,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843176": {
    "latitude": 56.375,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "840293": {
    "latitude": 55.875,
    "longitude": 13.375,
    "veg_class_name": "Cropland"
  },
  "897917": {
    "latitude": 65.875,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895037": {
    "latitude": 65.375,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890714": {
    "latitude": 64.625,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870548": {
    "latitude": 61.125,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886390": {
    "latitude": 63.875,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883502": {
    "latitude": 63.375,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882068": {
    "latitude": 63.125,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873412": {
    "latitude": 61.625,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873427": {
    "latitude": 61.625,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871987": {
    "latitude": 61.375,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "913764": {
    "latitude": 68.625,
    "longitude": 21.125,
    "veg_class_name": "Open Shrublands "
  },
  "912330": {
    "latitude": 68.375,
    "longitude": 22.625,
    "veg_class_name": "Open Shrublands "
  },
  "906556": {
    "latitude": 67.375,
    "longitude": 19.125,
    "veg_class_name": "Open Shrublands "
  },
  "903687": {
    "latitude": 66.875,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903691": {
    "latitude": 66.875,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864794": {
    "latitude": 60.125,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863336": {
    "latitude": 59.875,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863354": {
    "latitude": 59.875,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861892": {
    "latitude": 59.625,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861897": {
    "latitude": 59.625,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861903": {
    "latitude": 59.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859017": {
    "latitude": 59.125,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856132": {
    "latitude": 58.625,
    "longitude": 13.125,
    "veg_class_name": "missing value"
  },
  "854685": {
    "latitude": 58.375,
    "longitude": 11.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854690": {
    "latitude": 58.375,
    "longitude": 12.625,
    "veg_class_name": "Ocean "
  },
  "848931": {
    "latitude": 57.375,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896479": {
    "latitude": 65.625,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895035": {
    "latitude": 65.375,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889273": {
    "latitude": 64.375,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869106": {
    "latitude": 60.875,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887837": {
    "latitude": 64.125,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877730": {
    "latitude": 62.375,
    "longitude": 12.625,
    "veg_class_name": "Open Shrublands "
  },
  "877732": {
    "latitude": 62.375,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867655": {
    "latitude": 60.625,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "913763": {
    "latitude": 68.625,
    "longitude": 20.875,
    "veg_class_name": "Wooded Tundra "
  },
  "907987": {
    "latitude": 67.625,
    "longitude": 16.875,
    "veg_class_name": "Mixed Tundra "
  },
  "906571": {
    "latitude": 67.375,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899359": {
    "latitude": 66.125,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861888": {
    "latitude": 59.625,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861912": {
    "latitude": 59.625,
    "longitude": 18.125,
    "veg_class_name": "Mixed Forest "
  },
  "853261": {
    "latitude": 58.125,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "841734": {
    "latitude": 56.125,
    "longitude": 13.625,
    "veg_class_name": "Mixed Forest "
  },
  "841736": {
    "latitude": 56.125,
    "longitude": 14.125,
    "veg_class_name": "Mixed Forest "
  },
  "895036": {
    "latitude": 65.375,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893598": {
    "latitude": 65.125,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890702": {
    "latitude": 64.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890719": {
    "latitude": 64.625,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886396": {
    "latitude": 63.875,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884940": {
    "latitude": 63.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884943": {
    "latitude": 63.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882048": {
    "latitude": 63.125,
    "longitude": 12.125,
    "veg_class_name": "Open Shrublands "
  },
  "882051": {
    "latitude": 63.125,
    "longitude": 12.875,
    "veg_class_name": "Open Shrublands "
  },
  "877746": {
    "latitude": 62.375,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874849": {
    "latitude": 61.875,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867660": {
    "latitude": 60.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909429": {
    "latitude": 67.875,
    "longitude": 17.375,
    "veg_class_name": "Mixed Tundra "
  },
  "907993": {
    "latitude": 67.625,
    "longitude": 18.375,
    "veg_class_name": "Open Shrublands "
  },
  "906558": {
    "latitude": 67.375,
    "longitude": 19.625,
    "veg_class_name": "Open Shrublands "
  },
  "906565": {
    "latitude": 67.375,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905131": {
    "latitude": 67.125,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902225": {
    "latitude": 66.625,
    "longitude": 16.375,
    "veg_class_name": "Open Shrublands "
  },
  "863331": {
    "latitude": 59.875,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897925": {
    "latitude": 65.875,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895018": {
    "latitude": 65.375,
    "longitude": 14.625,
    "veg_class_name": "Open Shrublands "
  },
  "893584": {
    "latitude": 65.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893600": {
    "latitude": 65.125,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883491": {
    "latitude": 63.375,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882052": {
    "latitude": 63.125,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879170": {
    "latitude": 62.625,
    "longitude": 12.625,
    "veg_class_name": "Open Shrublands "
  },
  "873418": {
    "latitude": 61.625,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909428": {
    "latitude": 67.875,
    "longitude": 17.125,
    "veg_class_name": "Mixed Tundra "
  },
  "909433": {
    "latitude": 67.875,
    "longitude": 18.375,
    "veg_class_name": "Mixed Tundra "
  },
  "899368": {
    "latitude": 66.125,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863342": {
    "latitude": 59.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844617": {
    "latitude": 56.625,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843173": {
    "latitude": 56.375,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895028": {
    "latitude": 65.375,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893597": {
    "latitude": 65.125,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892147": {
    "latitude": 64.875,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890722": {
    "latitude": 64.625,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890724": {
    "latitude": 64.625,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886394": {
    "latitude": 63.875,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883512": {
    "latitude": 63.375,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879179": {
    "latitude": 62.625,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871973": {
    "latitude": 61.375,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871981": {
    "latitude": 61.375,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909430": {
    "latitude": 67.875,
    "longitude": 17.625,
    "veg_class_name": "Wooded Tundra "
  },
  "905125": {
    "latitude": 67.125,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902246": {
    "latitude": 66.625,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899355": {
    "latitude": 66.125,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864792": {
    "latitude": 60.125,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854692": {
    "latitude": 58.375,
    "longitude": 13.125,
    "veg_class_name": "Cropland"
  },
  "854705": {
    "latitude": 58.375,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896460": {
    "latitude": 65.625,
    "longitude": 15.125,
    "veg_class_name": "Open Shrublands "
  },
  "896464": {
    "latitude": 65.625,
    "longitude": 16.125,
    "veg_class_name": "Open Shrublands "
  },
  "890695": {
    "latitude": 64.625,
    "longitude": 13.875,
    "veg_class_name": "Open Shrublands "
  },
  "890717": {
    "latitude": 64.625,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889262": {
    "latitude": 64.375,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876298": {
    "latitude": 62.125,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886379": {
    "latitude": 63.875,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886381": {
    "latitude": 63.875,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884954": {
    "latitude": 63.625,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883500": {
    "latitude": 63.375,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883504": {
    "latitude": 63.375,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882073": {
    "latitude": 63.125,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874855": {
    "latitude": 61.875,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910883": {
    "latitude": 68.125,
    "longitude": 20.875,
    "veg_class_name": "Open Shrublands "
  },
  "906574": {
    "latitude": 67.375,
    "longitude": 23.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906547": {
    "latitude": 67.375,
    "longitude": 16.875,
    "veg_class_name": "Wooded Tundra "
  },
  "905120": {
    "latitude": 67.125,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902255": {
    "latitude": 66.625,
    "longitude": 23.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864770": {
    "latitude": 60.125,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864779": {
    "latitude": 60.125,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857576": {
    "latitude": 58.875,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857578": {
    "latitude": 58.875,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854696": {
    "latitude": 58.375,
    "longitude": 14.125,
    "veg_class_name": "Mixed Forest "
  },
  "853263": {
    "latitude": 58.125,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848939": {
    "latitude": 57.375,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844614": {
    "latitude": 56.625,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893595": {
    "latitude": 65.125,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889275": {
    "latitude": 64.375,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889278": {
    "latitude": 64.375,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870537": {
    "latitude": 61.125,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876293": {
    "latitude": 62.125,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887842": {
    "latitude": 64.125,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883494": {
    "latitude": 63.375,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880625": {
    "latitude": 62.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877742": {
    "latitude": 62.375,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "907998": {
    "latitude": 67.625,
    "longitude": 19.625,
    "veg_class_name": "Open Shrublands "
  },
  "906545": {
    "latitude": 67.375,
    "longitude": 16.375,
    "veg_class_name": "Mixed Tundra "
  },
  "906553": {
    "latitude": 67.375,
    "longitude": 18.375,
    "veg_class_name": "Open Shrublands "
  },
  "905112": {
    "latitude": 67.125,
    "longitude": 18.125,
    "veg_class_name": "Open Shrublands "
  },
  "902234": {
    "latitude": 66.625,
    "longitude": 18.625,
    "veg_class_name": "Open Shrublands "
  },
  "900811": {
    "latitude": 66.375,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864787": {
    "latitude": 60.125,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859030": {
    "latitude": 59.125,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857585": {
    "latitude": 58.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856140": {
    "latitude": 58.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854706": {
    "latitude": 58.375,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853264": {
    "latitude": 58.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851813": {
    "latitude": 57.875,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848953": {
    "latitude": 57.375,
    "longitude": 18.375,
    "veg_class_name": "Mixed Forest "
  },
  "848929": {
    "latitude": 57.375,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848936": {
    "latitude": 57.375,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847490": {
    "latitude": 57.125,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895020": {
    "latitude": 65.375,
    "longitude": 15.125,
    "veg_class_name": "Open Shrublands "
  },
  "890715": {
    "latitude": 64.625,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889279": {
    "latitude": 64.375,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870539": {
    "latitude": 61.125,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887836": {
    "latitude": 64.125,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883501": {
    "latitude": 63.375,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "907995": {
    "latitude": 67.625,
    "longitude": 18.875,
    "veg_class_name": "Open Shrublands "
  },
  "906551": {
    "latitude": 67.375,
    "longitude": 17.875,
    "veg_class_name": "Mixed Tundra "
  },
  "905115": {
    "latitude": 67.125,
    "longitude": 18.875,
    "veg_class_name": "Open Shrublands "
  },
  "899352": {
    "latitude": 66.125,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866219": {
    "latitude": 60.375,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856126": {
    "latitude": 58.625,
    "longitude": 11.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853251": {
    "latitude": 58.125,
    "longitude": 12.875,
    "veg_class_name": "Mixed Forest "
  },
  "850367": {
    "latitude": 57.625,
    "longitude": 11.875,
    "veg_class_name": "Ocean "
  },
  "850370": {
    "latitude": 57.625,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850373": {
    "latitude": 57.625,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850380": {
    "latitude": 57.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844621": {
    "latitude": 56.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843181": {
    "latitude": 56.375,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892160": {
    "latitude": 64.875,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890697": {
    "latitude": 64.625,
    "longitude": 14.375,
    "veg_class_name": "Open Shrublands "
  },
  "869101": {
    "latitude": 60.875,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869108": {
    "latitude": 60.875,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870538": {
    "latitude": 61.125,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876292": {
    "latitude": 62.125,
    "longitude": 13.125,
    "veg_class_name": "Open Shrublands "
  },
  "884953": {
    "latitude": 63.625,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "913765": {
    "latitude": 68.625,
    "longitude": 21.375,
    "veg_class_name": "Open Shrublands "
  },
  "912325": {
    "latitude": 68.375,
    "longitude": 21.375,
    "veg_class_name": "Open Shrublands "
  },
  "902237": {
    "latitude": 66.625,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866232": {
    "latitude": 60.375,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864785": {
    "latitude": 60.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863330": {
    "latitude": 59.875,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863347": {
    "latitude": 59.875,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860452": {
    "latitude": 59.375,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860453": {
    "latitude": 59.375,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859023": {
    "latitude": 59.125,
    "longitude": 15.875,
    "veg_class_name": "Ocean "
  },
  "851811": {
    "latitude": 57.875,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848942": {
    "latitude": 57.375,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847494": {
    "latitude": 57.125,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896468": {
    "latitude": 65.625,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895039": {
    "latitude": 65.375,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893577": {
    "latitude": 65.125,
    "longitude": 14.375,
    "veg_class_name": "Wooded Tundra "
  },
  "893588": {
    "latitude": 65.125,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892142": {
    "latitude": 64.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890700": {
    "latitude": 64.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890705": {
    "latitude": 64.625,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869095": {
    "latitude": 60.875,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876299": {
    "latitude": 62.125,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886402": {
    "latitude": 63.875,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882056": {
    "latitude": 63.125,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879183": {
    "latitude": 62.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877743": {
    "latitude": 62.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903675": {
    "latitude": 66.875,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902248": {
    "latitude": 66.625,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902254": {
    "latitude": 66.625,
    "longitude": 23.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864778": {
    "latitude": 60.125,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861898": {
    "latitude": 59.625,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859008": {
    "latitude": 59.125,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856130": {
    "latitude": 58.625,
    "longitude": 12.625,
    "veg_class_name": "missing value"
  },
  "897902": {
    "latitude": 65.875,
    "longitude": 15.625,
    "veg_class_name": "Open Shrublands "
  },
  "897920": {
    "latitude": 65.875,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896473": {
    "latitude": 65.625,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892143": {
    "latitude": 64.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892146": {
    "latitude": 64.875,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890721": {
    "latitude": 64.625,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869104": {
    "latitude": 60.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886383": {
    "latitude": 63.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874856": {
    "latitude": 61.875,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "907992": {
    "latitude": 67.625,
    "longitude": 18.125,
    "veg_class_name": "Open Shrublands "
  },
  "902241": {
    "latitude": 66.625,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902228": {
    "latitude": 66.625,
    "longitude": 17.125,
    "veg_class_name": "Wooded Tundra "
  },
  "900803": {
    "latitude": 66.375,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863346": {
    "latitude": 59.875,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859029": {
    "latitude": 59.125,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859016": {
    "latitude": 59.125,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857581": {
    "latitude": 58.875,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856143": {
    "latitude": 58.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854688": {
    "latitude": 58.375,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851836": {
    "latitude": 57.875,
    "longitude": 19.125,
    "veg_class_name": "missing value"
  },
  "850382": {
    "latitude": 57.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848930": {
    "latitude": 57.375,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846058": {
    "latitude": 56.875,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846063": {
    "latitude": 56.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897931": {
    "latitude": 65.875,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896462": {
    "latitude": 65.625,
    "longitude": 15.625,
    "veg_class_name": "Open Shrublands "
  },
  "892140": {
    "latitude": 64.875,
    "longitude": 15.125,
    "veg_class_name": "Open Shrublands "
  },
  "892144": {
    "latitude": 64.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889280": {
    "latitude": 64.375,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876309": {
    "latitude": 62.125,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887839": {
    "latitude": 64.125,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887829": {
    "latitude": 64.125,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882061": {
    "latitude": 63.125,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877731": {
    "latitude": 62.375,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912323": {
    "latitude": 68.375,
    "longitude": 20.875,
    "veg_class_name": "Open Shrublands "
  },
  "909432": {
    "latitude": 67.875,
    "longitude": 18.125,
    "veg_class_name": "Mixed Tundra "
  },
  "900801": {
    "latitude": 66.375,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850372": {
    "latitude": 57.625,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897923": {
    "latitude": 65.875,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895025": {
    "latitude": 65.375,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895038": {
    "latitude": 65.375,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893590": {
    "latitude": 65.125,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890713": {
    "latitude": 64.625,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884933": {
    "latitude": 63.625,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910874": {
    "latitude": 68.125,
    "longitude": 18.625,
    "veg_class_name": "Mixed Tundra "
  },
  "910888": {
    "latitude": 68.125,
    "longitude": 22.125,
    "veg_class_name": "Open Shrublands "
  },
  "908000": {
    "latitude": 67.625,
    "longitude": 20.125,
    "veg_class_name": "Open Shrublands "
  },
  "906569": {
    "latitude": 67.375,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905114": {
    "latitude": 67.125,
    "longitude": 18.625,
    "veg_class_name": "Open Shrublands "
  },
  "902229": {
    "latitude": 66.625,
    "longitude": 17.375,
    "veg_class_name": "Open Shrublands "
  },
  "899349": {
    "latitude": 66.125,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854700": {
    "latitude": 58.375,
    "longitude": 15.125,
    "veg_class_name": "Cropland"
  },
  "853254": {
    "latitude": 58.125,
    "longitude": 13.625,
    "veg_class_name": "Mixed Forest "
  },
  "853259": {
    "latitude": 58.125,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848935": {
    "latitude": 57.375,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "841743": {
    "latitude": 56.125,
    "longitude": 15.875,
    "veg_class_name": "missing value"
  },
  "838855": {
    "latitude": 55.625,
    "longitude": 13.875,
    "veg_class_name": "Cropland"
  },
  "897916": {
    "latitude": 65.875,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895022": {
    "latitude": 65.375,
    "longitude": 15.625,
    "veg_class_name": "Open Shrublands "
  },
  "890718": {
    "latitude": 64.625,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876290": {
    "latitude": 62.125,
    "longitude": 12.625,
    "veg_class_name": "Open Shrublands "
  },
  "887832": {
    "latitude": 64.125,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884936": {
    "latitude": 63.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884946": {
    "latitude": 63.625,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882059": {
    "latitude": 63.125,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882065": {
    "latitude": 63.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880621": {
    "latitude": 62.875,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880633": {
    "latitude": 62.875,
    "longitude": 18.375,
    "veg_class_name": "missing value"
  },
  "877736": {
    "latitude": 62.375,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874851": {
    "latitude": 61.875,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871971": {
    "latitude": 61.375,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871976": {
    "latitude": 61.375,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867650": {
    "latitude": 60.625,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912317": {
    "latitude": 68.375,
    "longitude": 19.375,
    "veg_class_name": "Ocean "
  },
  "909441": {
    "latitude": 67.875,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "907991": {
    "latitude": 67.625,
    "longitude": 17.875,
    "veg_class_name": "Mixed Tundra "
  },
  "905111": {
    "latitude": 67.125,
    "longitude": 17.875,
    "veg_class_name": "Open Shrublands "
  },
  "903689": {
    "latitude": 66.875,
    "longitude": 22.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900785": {
    "latitude": 66.375,
    "longitude": 16.375,
    "veg_class_name": "Open Shrublands "
  },
  "900789": {
    "latitude": 66.375,
    "longitude": 17.375,
    "veg_class_name": "Open Shrublands "
  },
  "899350": {
    "latitude": 66.125,
    "longitude": 17.625,
    "veg_class_name": "Ocean "
  },
  "866231": {
    "latitude": 60.375,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863337": {
    "latitude": 59.875,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860464": {
    "latitude": 59.375,
    "longitude": 16.125,
    "veg_class_name": "Mixed Forest "
  },
  "854697": {
    "latitude": 58.375,
    "longitude": 14.375,
    "veg_class_name": "missing value"
  },
  "843183": {
    "latitude": 56.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897907": {
    "latitude": 65.875,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897913": {
    "latitude": 65.875,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896481": {
    "latitude": 65.625,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892155": {
    "latitude": 64.875,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889265": {
    "latitude": 64.375,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870531": {
    "latitude": 61.125,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876306": {
    "latitude": 62.125,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884945": {
    "latitude": 63.625,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884948": {
    "latitude": 63.625,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884958": {
    "latitude": 63.625,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883498": {
    "latitude": 63.375,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874858": {
    "latitude": 61.875,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873421": {
    "latitude": 61.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871975": {
    "latitude": 61.375,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906560": {
    "latitude": 67.375,
    "longitude": 20.125,
    "veg_class_name": "Open Shrublands "
  },
  "906549": {
    "latitude": 67.375,
    "longitude": 17.375,
    "veg_class_name": "Mixed Tundra "
  },
  "900797": {
    "latitude": 66.375,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854694": {
    "latitude": 58.375,
    "longitude": 13.625,
    "veg_class_name": "Mixed Forest "
  },
  "851807": {
    "latitude": 57.875,
    "longitude": 11.875,
    "veg_class_name": "Mixed Forest "
  },
  "847505": {
    "latitude": 57.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844623": {
    "latitude": 56.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897901": {
    "latitude": 65.875,
    "longitude": 15.375,
    "veg_class_name": "Open Shrublands "
  },
  "896486": {
    "latitude": 65.625,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896489": {
    "latitude": 65.625,
    "longitude": 22.375,
    "veg_class_name": "missing value"
  },
  "893601": {
    "latitude": 65.125,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892154": {
    "latitude": 64.875,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890696": {
    "latitude": 64.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876296": {
    "latitude": 62.125,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887828": {
    "latitude": 64.125,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886398": {
    "latitude": 63.875,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884937": {
    "latitude": 63.625,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877734": {
    "latitude": 62.375,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874853": {
    "latitude": 61.875,
    "longitude": 13.375,
    "veg_class_name": "Open Shrublands "
  },
  "867663": {
    "latitude": 60.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844618": {
    "latitude": 56.625,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910887": {
    "latitude": 68.125,
    "longitude": 21.875,
    "veg_class_name": "Open Shrublands "
  },
  "909436": {
    "latitude": 67.875,
    "longitude": 19.125,
    "veg_class_name": "Wooded Tundra "
  },
  "905128": {
    "latitude": 67.125,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903685": {
    "latitude": 66.875,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864790": {
    "latitude": 60.125,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861914": {
    "latitude": 59.625,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860455": {
    "latitude": 59.375,
    "longitude": 13.875,
    "veg_class_name": "Ocean "
  },
  "857572": {
    "latitude": 58.875,
    "longitude": 13.125,
    "veg_class_name": "missing value"
  },
  "851820": {
    "latitude": 57.875,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896458": {
    "latitude": 65.625,
    "longitude": 14.625,
    "veg_class_name": "Wooded Tundra "
  },
  "876302": {
    "latitude": 62.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874862": {
    "latitude": 61.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873409": {
    "latitude": 61.625,
    "longitude": 12.375,
    "veg_class_name": "Open Shrublands "
  },
  "910875": {
    "latitude": 68.125,
    "longitude": 18.875,
    "veg_class_name": "Mixed Tundra "
  },
  "909445": {
    "latitude": 67.875,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "907989": {
    "latitude": 67.625,
    "longitude": 17.375,
    "veg_class_name": "Wooded Tundra "
  },
  "908002": {
    "latitude": 67.625,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905110": {
    "latitude": 67.125,
    "longitude": 17.625,
    "veg_class_name": "Mixed Tundra "
  },
  "899366": {
    "latitude": 66.125,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847492": {
    "latitude": 57.125,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897918": {
    "latitude": 65.875,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897935": {
    "latitude": 65.875,
    "longitude": 23.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895044": {
    "latitude": 65.375,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869107": {
    "latitude": 60.875,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884950": {
    "latitude": 63.625,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883509": {
    "latitude": 63.375,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883510": {
    "latitude": 63.375,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882066": {
    "latitude": 63.125,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880618": {
    "latitude": 62.875,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877741": {
    "latitude": 62.375,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871986": {
    "latitude": 61.375,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903669": {
    "latitude": 66.875,
    "longitude": 17.375,
    "veg_class_name": "Wooded Tundra "
  },
  "866218": {
    "latitude": 60.375,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861896": {
    "latitude": 59.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853252": {
    "latitude": 58.125,
    "longitude": 13.125,
    "veg_class_name": "Mixed Forest "
  },
  "893582": {
    "latitude": 65.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893592": {
    "latitude": 65.125,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893603": {
    "latitude": 65.125,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889269": {
    "latitude": 64.375,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889283": {
    "latitude": 64.375,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884955": {
    "latitude": 63.625,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883503": {
    "latitude": 63.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883513": {
    "latitude": 63.375,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879174": {
    "latitude": 62.625,
    "longitude": 13.625,
    "veg_class_name": "Open Shrublands "
  },
  "879191": {
    "latitude": 62.625,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871985": {
    "latitude": 61.375,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867661": {
    "latitude": 60.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903695": {
    "latitude": 66.875,
    "longitude": 23.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861887": {
    "latitude": 59.625,
    "longitude": 11.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860458": {
    "latitude": 59.375,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857579": {
    "latitude": 58.875,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "840292": {
    "latitude": 55.875,
    "longitude": 13.125,
    "veg_class_name": "Cropland"
  },
  "897912": {
    "latitude": 65.875,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896465": {
    "latitude": 65.625,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896483": {
    "latitude": 65.625,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893586": {
    "latitude": 65.125,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892153": {
    "latitude": 64.875,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870533": {
    "latitude": 61.125,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886387": {
    "latitude": 63.875,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883489": {
    "latitude": 63.375,
    "longitude": 12.375,
    "veg_class_name": "Open Shrublands "
  },
  "873416": {
    "latitude": 61.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905106": {
    "latitude": 67.125,
    "longitude": 16.625,
    "veg_class_name": "Mixed Tundra "
  },
  "851824": {
    "latitude": 57.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843179": {
    "latitude": 56.375,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "841733": {
    "latitude": 56.125,
    "longitude": 13.375,
    "veg_class_name": "Mixed Forest "
  },
  "840291": {
    "latitude": 55.875,
    "longitude": 12.875,
    "veg_class_name": "Cropland"
  },
  "897932": {
    "latitude": 65.875,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895029": {
    "latitude": 65.375,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892150": {
    "latitude": 64.875,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890716": {
    "latitude": 64.625,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889263": {
    "latitude": 64.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869092": {
    "latitude": 60.875,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869098": {
    "latitude": 60.875,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883488": {
    "latitude": 63.375,
    "longitude": 12.125,
    "veg_class_name": "Open Shrublands "
  },
  "882053": {
    "latitude": 63.125,
    "longitude": 13.375,
    "veg_class_name": "Open Shrublands "
  },
  "880609": {
    "latitude": 62.875,
    "longitude": 12.375,
    "veg_class_name": "Wooded Tundra "
  },
  "879185": {
    "latitude": 62.625,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879182": {
    "latitude": 62.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867654": {
    "latitude": 60.625,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867659": {
    "latitude": 60.625,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912316": {
    "latitude": 68.375,
    "longitude": 19.125,
    "veg_class_name": "Open Shrublands "
  },
  "912329": {
    "latitude": 68.375,
    "longitude": 22.375,
    "veg_class_name": "Open Shrublands "
  },
  "909440": {
    "latitude": 67.875,
    "longitude": 20.125,
    "veg_class_name": "Open Shrublands "
  },
  "906566": {
    "latitude": 67.375,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905113": {
    "latitude": 67.125,
    "longitude": 18.375,
    "veg_class_name": "Open Shrublands "
  },
  "903668": {
    "latitude": 66.875,
    "longitude": 17.125,
    "veg_class_name": "Mixed Tundra "
  },
  "900784": {
    "latitude": 66.375,
    "longitude": 16.125,
    "veg_class_name": "Open Shrublands "
  },
  "861913": {
    "latitude": 59.625,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857565": {
    "latitude": 58.875,
    "longitude": 11.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857567": {
    "latitude": 58.875,
    "longitude": 11.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854701": {
    "latitude": 58.375,
    "longitude": 15.375,
    "veg_class_name": "Cropland"
  },
  "853253": {
    "latitude": 58.125,
    "longitude": 13.375,
    "veg_class_name": "Mixed Forest "
  },
  "846052": {
    "latitude": 56.875,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895031": {
    "latitude": 65.375,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892138": {
    "latitude": 64.875,
    "longitude": 14.625,
    "veg_class_name": "Open Shrublands "
  },
  "892151": {
    "latitude": 64.875,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890699": {
    "latitude": 64.625,
    "longitude": 14.875,
    "veg_class_name": "Open Shrublands "
  },
  "876307": {
    "latitude": 62.125,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886391": {
    "latitude": 63.875,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873415": {
    "latitude": 61.625,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873423": {
    "latitude": 61.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871983": {
    "latitude": 61.375,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "915201": {
    "latitude": 68.875,
    "longitude": 20.375,
    "veg_class_name": "Open Shrublands "
  },
  "913766": {
    "latitude": 68.625,
    "longitude": 21.625,
    "veg_class_name": "Open Shrublands "
  },
  "910872": {
    "latitude": 68.125,
    "longitude": 18.125,
    "veg_class_name": "Mixed Tundra "
  },
  "910876": {
    "latitude": 68.125,
    "longitude": 19.125,
    "veg_class_name": "Wooded Tundra "
  },
  "910882": {
    "latitude": 68.125,
    "longitude": 20.625,
    "veg_class_name": "Open Shrublands "
  },
  "909450": {
    "latitude": 67.875,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906573": {
    "latitude": 67.375,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899356": {
    "latitude": 66.125,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861900": {
    "latitude": 59.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860447": {
    "latitude": 59.375,
    "longitude": 11.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860454": {
    "latitude": 59.375,
    "longitude": 13.625,
    "veg_class_name": "Ocean "
  },
  "859014": {
    "latitude": 59.125,
    "longitude": 13.625,
    "veg_class_name": "missing value"
  },
  "856134": {
    "latitude": 58.625,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851834": {
    "latitude": 57.875,
    "longitude": 18.625,
    "veg_class_name": "Ocean "
  },
  "848933": {
    "latitude": 57.375,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844616": {
    "latitude": 56.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843174": {
    "latitude": 56.375,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "838852": {
    "latitude": 55.625,
    "longitude": 13.125,
    "veg_class_name": "Cropland"
  },
  "897909": {
    "latitude": 65.875,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869093": {
    "latitude": 60.875,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884942": {
    "latitude": 63.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880629": {
    "latitude": 62.875,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874860": {
    "latitude": 61.875,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874857": {
    "latitude": 61.875,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873424": {
    "latitude": 61.625,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "908011": {
    "latitude": 67.625,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905133": {
    "latitude": 67.125,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903676": {
    "latitude": 66.875,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902250": {
    "latitude": 66.625,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899361": {
    "latitude": 66.125,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899365": {
    "latitude": 66.125,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860466": {
    "latitude": 59.375,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859024": {
    "latitude": 59.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854702": {
    "latitude": 58.375,
    "longitude": 15.625,
    "veg_class_name": "Mixed Forest "
  },
  "850368": {
    "latitude": 57.625,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844613": {
    "latitude": 56.625,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897924": {
    "latitude": 65.875,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896487": {
    "latitude": 65.625,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892139": {
    "latitude": 64.875,
    "longitude": 14.875,
    "veg_class_name": "Open Shrublands "
  },
  "890709": {
    "latitude": 64.625,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887819": {
    "latitude": 64.125,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886385": {
    "latitude": 63.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886370": {
    "latitude": 63.875,
    "longitude": 12.625,
    "veg_class_name": "Open Shrublands "
  },
  "883496": {
    "latitude": 63.375,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882069": {
    "latitude": 63.125,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879178": {
    "latitude": 62.625,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877740": {
    "latitude": 62.375,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897904": {
    "latitude": 65.875,
    "longitude": 16.125,
    "veg_class_name": "Open Shrublands "
  },
  "895034": {
    "latitude": 65.375,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893593": {
    "latitude": 65.125,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890704": {
    "latitude": 64.625,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889261": {
    "latitude": 64.375,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887834": {
    "latitude": 64.125,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884957": {
    "latitude": 63.625,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880611": {
    "latitude": 62.875,
    "longitude": 12.875,
    "veg_class_name": "Open Shrublands "
  },
  "879188": {
    "latitude": 62.625,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871977": {
    "latitude": 61.375,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867651": {
    "latitude": 60.625,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910878": {
    "latitude": 68.125,
    "longitude": 19.625,
    "veg_class_name": "Open Shrublands "
  },
  "908007": {
    "latitude": 67.625,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906546": {
    "latitude": 67.375,
    "longitude": 16.625,
    "veg_class_name": "Wooded Tundra "
  },
  "902226": {
    "latitude": 66.625,
    "longitude": 16.625,
    "veg_class_name": "Open Shrublands "
  },
  "902232": {
    "latitude": 66.625,
    "longitude": 18.125,
    "veg_class_name": "Wooded Tundra "
  },
  "900798": {
    "latitude": 66.375,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899347": {
    "latitude": 66.125,
    "longitude": 16.875,
    "veg_class_name": "Open Shrublands "
  },
  "857574": {
    "latitude": 58.875,
    "longitude": 13.625,
    "veg_class_name": "missing value"
  },
  "848944": {
    "latitude": 57.375,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848937": {
    "latitude": 57.375,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844626": {
    "latitude": 56.625,
    "longitude": 16.625,
    "veg_class_name": "Mixed Forest "
  },
  "897903": {
    "latitude": 65.875,
    "longitude": 15.875,
    "veg_class_name": "Open Shrublands "
  },
  "893602": {
    "latitude": 65.125,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876301": {
    "latitude": 62.125,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883507": {
    "latitude": 63.375,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883508": {
    "latitude": 63.375,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867656": {
    "latitude": 60.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912314": {
    "latitude": 68.375,
    "longitude": 18.625,
    "veg_class_name": "Wooded Tundra "
  },
  "909435": {
    "latitude": 67.875,
    "longitude": 18.875,
    "veg_class_name": "Wooded Tundra "
  },
  "909437": {
    "latitude": 67.875,
    "longitude": 19.375,
    "veg_class_name": "Wooded Tundra "
  },
  "906550": {
    "latitude": 67.375,
    "longitude": 17.625,
    "veg_class_name": "Mixed Tundra "
  },
  "902245": {
    "latitude": 66.625,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899345": {
    "latitude": 66.125,
    "longitude": 16.375,
    "veg_class_name": "Open Shrublands "
  },
  "863352": {
    "latitude": 59.875,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859021": {
    "latitude": 59.125,
    "longitude": 15.375,
    "veg_class_name": "Mixed Forest "
  },
  "859011": {
    "latitude": 59.125,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846066": {
    "latitude": 56.875,
    "longitude": 16.625,
    "veg_class_name": "missing value"
  },
  "896478": {
    "latitude": 65.625,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869090": {
    "latitude": 60.875,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869105": {
    "latitude": 60.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884930": {
    "latitude": 63.625,
    "longitude": 12.625,
    "veg_class_name": "Open Shrublands "
  },
  "884934": {
    "latitude": 63.625,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877737": {
    "latitude": 62.375,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "915203": {
    "latitude": 68.875,
    "longitude": 20.875,
    "veg_class_name": "Open Shrublands "
  },
  "912312": {
    "latitude": 68.375,
    "longitude": 18.125,
    "veg_class_name": "Mixed Tundra "
  },
  "910889": {
    "latitude": 68.125,
    "longitude": 22.375,
    "veg_class_name": "Open Shrublands "
  },
  "905123": {
    "latitude": 67.125,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902223": {
    "latitude": 66.625,
    "longitude": 15.875,
    "veg_class_name": "Mixed Tundra "
  },
  "864788": {
    "latitude": 60.125,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861902": {
    "latitude": 59.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856142": {
    "latitude": 58.625,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854693": {
    "latitude": 58.375,
    "longitude": 13.375,
    "veg_class_name": "Mixed Forest "
  },
  "853256": {
    "latitude": 58.125,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851809": {
    "latitude": 57.875,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846054": {
    "latitude": 56.875,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843180": {
    "latitude": 56.375,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897926": {
    "latitude": 65.875,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896459": {
    "latitude": 65.625,
    "longitude": 14.875,
    "veg_class_name": "Open Shrublands "
  },
  "887821": {
    "latitude": 64.125,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880622": {
    "latitude": 62.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874859": {
    "latitude": 61.875,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "915202": {
    "latitude": 68.875,
    "longitude": 20.625,
    "veg_class_name": "Wooded Tundra "
  },
  "912321": {
    "latitude": 68.375,
    "longitude": 20.375,
    "veg_class_name": "Open Shrublands "
  },
  "910881": {
    "latitude": 68.125,
    "longitude": 20.375,
    "veg_class_name": "Open Shrublands "
  },
  "902240": {
    "latitude": 66.625,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900808": {
    "latitude": 66.375,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866230": {
    "latitude": 60.375,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866213": {
    "latitude": 60.375,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861908": {
    "latitude": 59.625,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857591": {
    "latitude": 58.875,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853248": {
    "latitude": 58.125,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853249": {
    "latitude": 58.125,
    "longitude": 12.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847497": {
    "latitude": 57.125,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "840294": {
    "latitude": 55.875,
    "longitude": 13.625,
    "veg_class_name": "Mixed Forest "
  },
  "897921": {
    "latitude": 65.875,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896470": {
    "latitude": 65.625,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886389": {
    "latitude": 63.875,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883515": {
    "latitude": 63.375,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877744": {
    "latitude": 62.375,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874852": {
    "latitude": 61.875,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910884": {
    "latitude": 68.125,
    "longitude": 21.125,
    "veg_class_name": "Open Shrublands "
  },
  "903671": {
    "latitude": 66.875,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900787": {
    "latitude": 66.375,
    "longitude": 16.875,
    "veg_class_name": "Open Shrublands "
  },
  "863334": {
    "latitude": 59.875,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857582": {
    "latitude": 58.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889268": {
    "latitude": 64.375,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884939": {
    "latitude": 63.625,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877735": {
    "latitude": 62.375,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877747": {
    "latitude": 62.375,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910886": {
    "latitude": 68.125,
    "longitude": 21.625,
    "veg_class_name": "Open Shrublands "
  },
  "909447": {
    "latitude": 67.875,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "907996": {
    "latitude": 67.625,
    "longitude": 19.125,
    "veg_class_name": "Open Shrublands "
  },
  "905132": {
    "latitude": 67.125,
    "longitude": 23.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903664": {
    "latitude": 66.875,
    "longitude": 16.125,
    "veg_class_name": "Wooded Tundra "
  },
  "900795": {
    "latitude": 66.375,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900814": {
    "latitude": 66.375,
    "longitude": 23.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899357": {
    "latitude": 66.125,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899360": {
    "latitude": 66.125,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866216": {
    "latitude": 60.375,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864777": {
    "latitude": 60.125,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861910": {
    "latitude": 59.625,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851818": {
    "latitude": 57.875,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850375": {
    "latitude": 57.625,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848940": {
    "latitude": 57.375,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "848954": {
    "latitude": 57.375,
    "longitude": 18.625,
    "veg_class_name": "Mixed Forest "
  },
  "848934": {
    "latitude": 57.375,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846060": {
    "latitude": 56.875,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "841738": {
    "latitude": 56.125,
    "longitude": 14.625,
    "veg_class_name": "Mixed Forest "
  },
  "897906": {
    "latitude": 65.875,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895021": {
    "latitude": 65.375,
    "longitude": 15.375,
    "veg_class_name": "Open Shrublands "
  },
  "895027": {
    "latitude": 65.375,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892136": {
    "latitude": 64.875,
    "longitude": 14.125,
    "veg_class_name": "Open Shrublands "
  },
  "890720": {
    "latitude": 64.625,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889281": {
    "latitude": 64.375,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879180": {
    "latitude": 62.625,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871988": {
    "latitude": 61.375,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909443": {
    "latitude": 67.875,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903683": {
    "latitude": 66.875,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899339": {
    "latitude": 66.125,
    "longitude": 14.875,
    "veg_class_name": "Wooded Tundra "
  },
  "866222": {
    "latitude": 60.375,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861895": {
    "latitude": 59.625,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860465": {
    "latitude": 59.375,
    "longitude": 16.375,
    "veg_class_name": "Mixed Forest "
  },
  "859022": {
    "latitude": 59.125,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857571": {
    "latitude": 58.875,
    "longitude": 12.875,
    "veg_class_name": "missing value"
  },
  "857580": {
    "latitude": 58.875,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851810": {
    "latitude": 57.875,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "841737": {
    "latitude": 56.125,
    "longitude": 14.375,
    "veg_class_name": "Mixed Forest "
  },
  "893591": {
    "latitude": 65.125,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892152": {
    "latitude": 64.875,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869097": {
    "latitude": 60.875,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869099": {
    "latitude": 60.875,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "874850": {
    "latitude": 61.875,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909427": {
    "latitude": 67.875,
    "longitude": 16.875,
    "veg_class_name": "Mixed Tundra "
  },
  "908005": {
    "latitude": 67.625,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905117": {
    "latitude": 67.125,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902227": {
    "latitude": 66.625,
    "longitude": 16.875,
    "veg_class_name": "Wooded Tundra "
  },
  "860462": {
    "latitude": 59.375,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853246": {
    "latitude": 58.125,
    "longitude": 11.625,
    "veg_class_name": "Mixed Forest "
  },
  "851815": {
    "latitude": 57.875,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850381": {
    "latitude": 57.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847503": {
    "latitude": 57.125,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893596": {
    "latitude": 65.125,
    "longitude": 19.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889257": {
    "latitude": 64.375,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887825": {
    "latitude": 64.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884951": {
    "latitude": 63.625,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882050": {
    "latitude": 63.125,
    "longitude": 12.625,
    "veg_class_name": "Wooded Tundra "
  },
  "880623": {
    "latitude": 62.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879172": {
    "latitude": 62.625,
    "longitude": 13.125,
    "veg_class_name": "Open Shrublands "
  },
  "879176": {
    "latitude": 62.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879186": {
    "latitude": 62.625,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871979": {
    "latitude": 61.375,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871984": {
    "latitude": 61.375,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867667": {
    "latitude": 60.625,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903679": {
    "latitude": 66.875,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900790": {
    "latitude": 66.375,
    "longitude": 17.625,
    "veg_class_name": "Open Shrublands "
  },
  "900793": {
    "latitude": 66.375,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866210": {
    "latitude": 60.375,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863349": {
    "latitude": 59.875,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861899": {
    "latitude": 59.625,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860451": {
    "latitude": 59.375,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860461": {
    "latitude": 59.375,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859025": {
    "latitude": 59.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857566": {
    "latitude": 58.875,
    "longitude": 11.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856147": {
    "latitude": 58.625,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893605": {
    "latitude": 65.125,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892162": {
    "latitude": 64.875,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869094": {
    "latitude": 60.875,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870536": {
    "latitude": 61.125,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876304": {
    "latitude": 62.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876308": {
    "latitude": 62.125,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884929": {
    "latitude": 63.625,
    "longitude": 12.375,
    "veg_class_name": "Open Shrublands "
  },
  "884941": {
    "latitude": 63.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882067": {
    "latitude": 63.125,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882071": {
    "latitude": 63.125,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880631": {
    "latitude": 62.875,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910885": {
    "latitude": 68.125,
    "longitude": 21.375,
    "veg_class_name": "Open Shrublands "
  },
  "906548": {
    "latitude": 67.375,
    "longitude": 17.125,
    "veg_class_name": "Mixed Tundra "
  },
  "905116": {
    "latitude": 67.125,
    "longitude": 19.125,
    "veg_class_name": "Open Shrublands "
  },
  "900800": {
    "latitude": 66.375,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900810": {
    "latitude": 66.375,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866229": {
    "latitude": 60.375,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863343": {
    "latitude": 59.875,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863353": {
    "latitude": 59.875,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861891": {
    "latitude": 59.625,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856135": {
    "latitude": 58.625,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "854691": {
    "latitude": 58.375,
    "longitude": 12.875,
    "veg_class_name": "Cropland"
  },
  "851808": {
    "latitude": 57.875,
    "longitude": 12.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896475": {
    "latitude": 65.625,
    "longitude": 18.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895024": {
    "latitude": 65.375,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890723": {
    "latitude": 64.625,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887816": {
    "latitude": 64.125,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906563": {
    "latitude": 67.375,
    "longitude": 20.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905124": {
    "latitude": 67.125,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903680": {
    "latitude": 66.875,
    "longitude": 20.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902253": {
    "latitude": 66.625,
    "longitude": 23.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899367": {
    "latitude": 66.125,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861893": {
    "latitude": 59.625,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860450": {
    "latitude": 59.375,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859031": {
    "latitude": 59.125,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853255": {
    "latitude": 58.125,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853257": {
    "latitude": 58.125,
    "longitude": 14.375,
    "veg_class_name": "missing value"
  },
  "847513": {
    "latitude": 57.125,
    "longitude": 18.375,
    "veg_class_name": "Mixed Forest "
  },
  "846061": {
    "latitude": 56.875,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895026": {
    "latitude": 65.375,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892158": {
    "latitude": 64.875,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889285": {
    "latitude": 64.375,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869102": {
    "latitude": 60.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887824": {
    "latitude": 64.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883495": {
    "latitude": 63.375,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883505": {
    "latitude": 63.375,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "909434": {
    "latitude": 67.875,
    "longitude": 18.625,
    "veg_class_name": "Mixed Tundra "
  },
  "907986": {
    "latitude": 67.625,
    "longitude": 16.625,
    "veg_class_name": "Mixed Tundra "
  },
  "903667": {
    "latitude": 66.875,
    "longitude": 16.875,
    "veg_class_name": "Wooded Tundra "
  },
  "900782": {
    "latitude": 66.375,
    "longitude": 15.625,
    "veg_class_name": "Mixed Tundra "
  },
  "859020": {
    "latitude": 59.125,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853258": {
    "latitude": 58.125,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847501": {
    "latitude": 57.125,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846055": {
    "latitude": 56.875,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "841732": {
    "latitude": 56.125,
    "longitude": 13.125,
    "veg_class_name": "Mixed Forest "
  },
  "897928": {
    "latitude": 65.875,
    "longitude": 22.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893585": {
    "latitude": 65.125,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890707": {
    "latitude": 64.625,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890711": {
    "latitude": 64.625,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887817": {
    "latitude": 64.125,
    "longitude": 14.375,
    "veg_class_name": "Open Shrublands "
  },
  "884931": {
    "latitude": 63.625,
    "longitude": 12.875,
    "veg_class_name": "Open Shrublands "
  },
  "879171": {
    "latitude": 62.625,
    "longitude": 12.875,
    "veg_class_name": "Open Shrublands "
  },
  "874864": {
    "latitude": 61.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873414": {
    "latitude": 61.625,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871980": {
    "latitude": 61.375,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912326": {
    "latitude": 68.375,
    "longitude": 21.625,
    "veg_class_name": "Open Shrublands "
  },
  "910891": {
    "latitude": 68.125,
    "longitude": 22.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "907994": {
    "latitude": 67.625,
    "longitude": 18.625,
    "veg_class_name": "Wooded Tundra "
  },
  "907997": {
    "latitude": 67.625,
    "longitude": 19.375,
    "veg_class_name": "Open Shrublands "
  },
  "908006": {
    "latitude": 67.625,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "906561": {
    "latitude": 67.375,
    "longitude": 20.375,
    "veg_class_name": "Open Shrublands "
  },
  "905107": {
    "latitude": 67.125,
    "longitude": 16.875,
    "veg_class_name": "Mixed Tundra "
  },
  "903666": {
    "latitude": 66.875,
    "longitude": 16.625,
    "veg_class_name": "Mixed Tundra "
  },
  "902230": {
    "latitude": 66.625,
    "longitude": 17.625,
    "veg_class_name": "Open Shrublands "
  },
  "866220": {
    "latitude": 60.375,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863338": {
    "latitude": 59.875,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "853250": {
    "latitude": 58.125,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "844624": {
    "latitude": 56.625,
    "longitude": 16.125,
    "veg_class_name": "Mixed Forest "
  },
  "840295": {
    "latitude": 55.875,
    "longitude": 13.875,
    "veg_class_name": "Mixed Forest "
  },
  "837413": {
    "latitude": 55.375,
    "longitude": 13.375,
    "veg_class_name": "Cropland"
  },
  "897927": {
    "latitude": 65.875,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895033": {
    "latitude": 65.375,
    "longitude": 18.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893579": {
    "latitude": 65.125,
    "longitude": 14.875,
    "veg_class_name": "Open Shrublands "
  },
  "890698": {
    "latitude": 64.625,
    "longitude": 14.625,
    "veg_class_name": "Open Shrublands "
  },
  "883493": {
    "latitude": 63.375,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880632": {
    "latitude": 62.875,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "907999": {
    "latitude": 67.625,
    "longitude": 19.875,
    "veg_class_name": "Open Shrublands "
  },
  "907988": {
    "latitude": 67.625,
    "longitude": 17.125,
    "veg_class_name": "Wooded Tundra "
  },
  "902242": {
    "latitude": 66.625,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899375": {
    "latitude": 66.125,
    "longitude": 23.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864786": {
    "latitude": 60.125,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "863333": {
    "latitude": 59.875,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859010": {
    "latitude": 59.125,
    "longitude": 12.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850394": {
    "latitude": 57.625,
    "longitude": 18.625,
    "veg_class_name": "Mixed Forest "
  },
  "848941": {
    "latitude": 57.375,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "847495": {
    "latitude": 57.125,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897911": {
    "latitude": 65.875,
    "longitude": 17.875,
    "veg_class_name": "Ocean "
  },
  "895045": {
    "latitude": 65.375,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "895019": {
    "latitude": 65.375,
    "longitude": 14.875,
    "veg_class_name": "Open Shrublands "
  },
  "890710": {
    "latitude": 64.625,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889277": {
    "latitude": 64.375,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "869100": {
    "latitude": 60.875,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "887831": {
    "latitude": 64.125,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884935": {
    "latitude": 63.625,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882072": {
    "latitude": 63.125,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880630": {
    "latitude": 62.875,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867664": {
    "latitude": 60.625,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866217": {
    "latitude": 60.375,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861904": {
    "latitude": 59.625,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861905": {
    "latitude": 59.625,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861906": {
    "latitude": 59.625,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860459": {
    "latitude": 59.375,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "860471": {
    "latitude": 59.375,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "850379": {
    "latitude": 57.625,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892148": {
    "latitude": 64.875,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892149": {
    "latitude": 64.875,
    "longitude": 17.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890706": {
    "latitude": 64.625,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870532": {
    "latitude": 61.125,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880617": {
    "latitude": 62.875,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880619": {
    "latitude": 62.875,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879169": {
    "latitude": 62.625,
    "longitude": 12.375,
    "veg_class_name": "Open Shrublands "
  },
  "879175": {
    "latitude": 62.625,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877739": {
    "latitude": 62.375,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "912315": {
    "latitude": 68.375,
    "longitude": 18.875,
    "veg_class_name": "Ocean "
  },
  "905118": {
    "latitude": 67.125,
    "longitude": 19.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905122": {
    "latitude": 67.125,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903690": {
    "latitude": 66.875,
    "longitude": 22.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903694": {
    "latitude": 66.875,
    "longitude": 23.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "900807": {
    "latitude": 66.375,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "866211": {
    "latitude": 60.375,
    "longitude": 12.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "864784": {
    "latitude": 60.125,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "857584": {
    "latitude": 58.875,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856127": {
    "latitude": 58.625,
    "longitude": 11.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "856133": {
    "latitude": 58.625,
    "longitude": 13.375,
    "veg_class_name": "missing value"
  },
  "856136": {
    "latitude": 58.625,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "846053": {
    "latitude": 56.875,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "838853": {
    "latitude": 55.625,
    "longitude": 13.375,
    "veg_class_name": "Cropland"
  },
  "893581": {
    "latitude": 65.125,
    "longitude": 15.375,
    "veg_class_name": "Open Shrublands "
  },
  "890703": {
    "latitude": 64.625,
    "longitude": 15.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876295": {
    "latitude": 62.125,
    "longitude": 13.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886399": {
    "latitude": 63.875,
    "longitude": 19.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886375": {
    "latitude": 63.875,
    "longitude": 13.875,
    "veg_class_name": "Open Shrublands "
  },
  "883506": {
    "latitude": 63.375,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "882054": {
    "latitude": 63.125,
    "longitude": 13.625,
    "veg_class_name": "Open Shrublands "
  },
  "909446": {
    "latitude": 67.875,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905126": {
    "latitude": 67.125,
    "longitude": 21.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "905127": {
    "latitude": 67.125,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "902233": {
    "latitude": 66.625,
    "longitude": 18.375,
    "veg_class_name": "Open Shrublands "
  },
  "860457": {
    "latitude": 59.375,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "859013": {
    "latitude": 59.125,
    "longitude": 13.375,
    "veg_class_name": "missing value"
  },
  "853266": {
    "latitude": 58.125,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "843178": {
    "latitude": 56.375,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "897898": {
    "latitude": 65.875,
    "longitude": 14.625,
    "veg_class_name": "Wooded Tundra "
  },
  "896463": {
    "latitude": 65.625,
    "longitude": 15.875,
    "veg_class_name": "Open Shrublands "
  },
  "896485": {
    "latitude": 65.625,
    "longitude": 21.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893594": {
    "latitude": 65.125,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "870534": {
    "latitude": 61.125,
    "longitude": 13.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886378": {
    "latitude": 63.875,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884938": {
    "latitude": 63.625,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880613": {
    "latitude": 62.875,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877748": {
    "latitude": 62.375,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910877": {
    "latitude": 68.125,
    "longitude": 19.375,
    "veg_class_name": "Open Shrublands "
  },
  "902247": {
    "latitude": 66.625,
    "longitude": 21.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "899342": {
    "latitude": 66.125,
    "longitude": 15.625,
    "veg_class_name": "Open Shrublands "
  },
  "899364": {
    "latitude": 66.125,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "861911": {
    "latitude": 59.625,
    "longitude": 17.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851822": {
    "latitude": 57.875,
    "longitude": 15.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "851825": {
    "latitude": 57.875,
    "longitude": 16.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896466": {
    "latitude": 65.625,
    "longitude": 16.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896474": {
    "latitude": 65.625,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "896482": {
    "latitude": 65.625,
    "longitude": 20.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889284": {
    "latitude": 64.375,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876297": {
    "latitude": 62.125,
    "longitude": 14.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "886388": {
    "latitude": 63.875,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "883499": {
    "latitude": 63.375,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "879184": {
    "latitude": 62.625,
    "longitude": 16.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "877738": {
    "latitude": 62.375,
    "longitude": 14.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "910873": {
    "latitude": 68.125,
    "longitude": 18.375,
    "veg_class_name": "Mixed Tundra "
  },
  "906555": {
    "latitude": 67.375,
    "longitude": 18.875,
    "veg_class_name": "Open Shrublands "
  },
  "905121": {
    "latitude": 67.125,
    "longitude": 20.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "903670": {
    "latitude": 66.875,
    "longitude": 17.625,
    "veg_class_name": "Wooded Tundra "
  },
  "864776": {
    "latitude": 60.125,
    "longitude": 14.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "893604": {
    "latitude": 65.125,
    "longitude": 21.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "892157": {
    "latitude": 64.875,
    "longitude": 19.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890701": {
    "latitude": 64.625,
    "longitude": 15.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "890708": {
    "latitude": 64.625,
    "longitude": 17.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889272": {
    "latitude": 64.375,
    "longitude": 18.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "889274": {
    "latitude": 64.375,
    "longitude": 18.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "876300": {
    "latitude": 62.125,
    "longitude": 15.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "884947": {
    "latitude": 63.625,
    "longitude": 16.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "880610": {
    "latitude": 62.875,
    "longitude": 12.625,
    "veg_class_name": "Open Shrublands "
  },
  "879190": {
    "latitude": 62.625,
    "longitude": 17.625,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873413": {
    "latitude": 61.625,
    "longitude": 13.375,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "873419": {
    "latitude": 61.625,
    "longitude": 14.875,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "871972": {
    "latitude": 61.375,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  },
  "867652": {
    "latitude": 60.625,
    "longitude": 13.125,
    "veg_class_name": "Evergreen Needleleaf Forest "
  }
}


# drawing a box around sweden
dict_extent_sweden = {
    "min_lat": 55.375,
    "max_lat": 68.875,
    "min_lon": 11.375,
    "max_lon": 24.125
}


# drawing a box around nordic
dict_extent_nordic = {
  "min_lat": 54.875,
  "max_lat": 70.875,
  "min_lon": 4.875,
  "max_lon": 31.375
}


# open external dictionaries
# dictionary which defines timeframes to analyze
try:

    # dictionary which stores GLDAS grid points
    with open("dict_extent_sweden.json", "r") as f:
        dict_extent_sweden = json.load(f)

    # dictionary which stores GLDAS grid points
    with open("dict_h115_coords.json", "r") as f:
        dict_h115_coords = json.load(f)
    coord_buffer = 2
    study_area = {
        "min_lat": 54.125,
        "max_lat": 68.875,
        "min_lon": 8.375,
        "max_lon": 24.125
    }

    regrid_lat = numpy.arange(study_area["min_lat"]-coord_buffer, study_area["max_lat"]+coord_buffer, 0.25)
    regrid_lon = numpy.arange(study_area["min_lon"]-coord_buffer, study_area["max_lon"]+coord_buffer, 0.25)
except:
    print("can't import dictionaries")


swe_shuffle_cells = [1397, 1398, 1399, 1433, 1434, 1435, 1470, 1471]
den_shuffle_cells = [1360, 1361, 1396, 1397, 1433]
nordic_shuffle_cells = [1326, 1360, 1361, 1362, 1396, 1397, 1398, 1399, 1433, 1434, 1435, 1436, 1469, 1470, 1471, 1472,
                        1506, 1507, 1508, 1542, 1543, 1544]

