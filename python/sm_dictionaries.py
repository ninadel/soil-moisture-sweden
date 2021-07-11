"""
Author: Nina del Rosario
Date: 6/2/2020
UPDATE_DESCRIPTION
This is for metadata dictionaries that are static (will probably not need to be changed between analyses)
"""

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


# dictionary specifying cell coordinates of ASCAT 12.5 TS within region of interest
dict_h115_coords = {"lat": [70.83866882324219, 70.72663116455078, 70.61459350585938, 70.50255584716797, 70.39051055908203, 70.27847290039062, 70.16642761230469, 70.05438232421875, 69.94233703613281, 69.83029174804688, 69.7182388305664, 69.60619354248047, 69.494140625, 69.38208770751953, 69.27003479003906, 69.15797424316406, 69.0459213256836, 68.9338607788086, 68.8218002319336, 68.7097396850586, 68.59767150878906, 68.48561096191406, 68.37354278564453, 68.261474609375, 68.14940643310547, 68.0373306274414, 67.92526245117188, 67.81318664550781, 67.70111083984375, 67.58903503417969, 67.4769515991211, 67.36487579345703, 67.25279235839844, 67.14070892333984, 67.02862548828125, 66.91653442382812, 66.80445098876953, 66.6923599243164, 66.58026885986328, 66.46817016601562, 66.3560791015625, 66.24398040771484, 66.13188171386719, 66.01978302001953, 65.90768432617188, 65.79557800292969, 65.6834716796875, 65.57136535644531, 65.45925903320312, 65.34715270996094, 65.23503875732422, 65.1229248046875, 65.01081085205078, 64.89869689941406, 64.78657531738281, 64.67445373535156, 64.56233215332031, 64.45021057128906, 64.33808898925781, 64.22595977783203, 64.11383056640625, 64.00170135498047, 63.88956832885742, 63.777435302734375, 63.66530227661133, 63.55316162109375, 63.44102478027344, 63.32888412475586, 63.216739654541016, 63.10459518432617, 62.99245071411133, 62.88030242919922, 62.76815414428711, 62.656002044677734, 62.543846130371094, 62.43169403076172, 62.31953430175781, 62.207374572753906, 62.09521484375, 61.98305130004883, 61.870887756347656, 61.758724212646484, 61.64655303955078, 61.534385681152344, 61.42221450805664, 61.31003952026367, 61.1978645324707, 61.08568572998047, 60.973506927490234, 60.861324310302734, 60.749141693115234, 60.636959075927734, 60.52477264404297, 60.41258239746094, 60.300392150878906, 60.18819808959961, 60.07600402832031, 59.963809967041016, 59.85160827636719, 59.739410400390625, 59.6272087097168, 59.5150032043457, 59.40279769897461, 59.29058837890625, 59.17837905883789, 59.066165924072266, 58.95395278930664, 58.841739654541016, 58.72951889038086, 58.61730194091797, 58.50507736206055, 58.39285659790039, 58.2806282043457, 58.16840362548828, 58.05617141723633, 57.943939208984375, 57.83170700073242, 57.7194709777832, 57.607234954833984, 57.4949951171875, 57.38275146484375, 57.2705078125, 57.15826416015625, 57.046016693115234, 56.93376541137695, 56.82151412963867, 56.709259033203125, 56.59700393676758, 56.484745025634766, 56.37248611450195, 56.260223388671875, 56.1479606628418, 56.03569412231445, 55.923423767089844, 55.811153411865234, 55.698883056640625, 55.58660888671875, 55.47433090209961, 55.36205291748047, 55.24977493286133, 55.137489318847656, 55.02520751953125, 54.91291809082031, 54.800628662109375, 54.68833923339844, 54.576045989990234, 54.463748931884766, 54.3514518737793, 54.23915481567383, 54.126853942871094, 54.014549255371094, 53.902244567871094, 53.78993606567383, 53.6776237487793, 53.565311431884766, 53.452999114990234, 53.34068298339844, 53.228363037109375, 53.11604309082031, 53.003719329833984, 52.891395568847656, 52.77906799316406, 52.66674041748047, 52.55440902709961, 52.442073822021484, 52.32973861694336, 52.217403411865234], "0": [7.5038251876831055, 7.844908237457275, 8.185991287231445, 8.527073860168457, 8.868157386779785, 9.209239959716797, 9.550323486328125, 9.891406059265137, 10.232488632202148, 10.573572158813477, 10.914654731750488, 11.255738258361816, 11.596820831298828, 11.93790340423584, 12.278986930847168, 12.62006950378418, 12.961153030395508, 13.30223560333252, 13.643319129943848, 13.98440170288086, 14.325484275817871, 14.6665678024292, 15.007650375366211, 15.348733901977539, 15.68981647491455, 16.030899047851562, 16.37198257446289, 16.71306610107422, 17.054147720336914, 17.395231246948242, 17.73631477355957, 18.077396392822266, 18.418479919433594, 18.759563446044922, 19.10064697265625, 19.441728591918945, 19.782812118530273, 20.1238956451416, 20.464977264404297, 20.806060791015625, 21.147144317626953, 21.48822784423828, 21.829309463500977, 22.170392990112305, 22.511476516723633, 22.852558135986328, 23.193641662597656, 23.534725189208984, 23.87580680847168, 24.216890335083008, 24.557973861694336, 24.899057388305664, 25.24013900756836, 25.581222534179688, 25.922306060791016, 26.26338768005371, 26.60447120666504, 26.945554733276367, 27.286638259887695, 27.62771987915039, 27.96880340576172, 28.309886932373047, 28.650968551635742, 28.99205207824707, 29.3331356048584, 29.674217224121094, 30.015300750732422, 30.35638427734375, 30.697467803955078, 31.038549423217773, 31.3796329498291, 31.72071647644043, 32.061798095703125, 32.40288162231445, 32.74396514892578, 33.08504867553711, 33.42613220214844, 33.7672119140625, 34.10829544067383, 34.449378967285156, 34.790462493896484, 35.13154602050781, 35.47262954711914, 35.81371307373047, 36.15479278564453, 36.49587631225586, 36.83695983886719, 37.178043365478516, 37.519126892089844, 37.86021041870117, 38.2012939453125, 38.54237365722656, 38.88345718383789, 39.22454071044922, 39.56562423706055, 39.906707763671875, 40.2477912902832, 40.58887481689453, 40.929954528808594, 41.27103805541992, 41.61212158203125, 41.95320510864258, 42.294288635253906, 42.635372161865234, 42.97645568847656, 43.317535400390625, 43.65861892700195, 43.99970245361328, 44.34078598022461, 44.68186950683594, 45.022953033447266, 45.36403274536133, 45.705116271972656, 46.046199798583984, 46.38728332519531, 46.72836685180664, 47.06945037841797, 47.4105339050293, 47.75161361694336, 48.09269714355469], "1": [7.461879730224609, 7.801055908203125, 8.14023208618164, 8.479408264160156, 8.818585395812988, 9.157761573791504, 9.49693775177002, 9.836113929748535, 10.17529010772705, 10.514466285705566, 10.853643417358398, 11.192819595336914, 11.53199577331543, 11.871171951293945, 12.210348129272461, 12.549524307250977, 12.888701438903809, 13.227877616882324, 13.56705379486084, 13.906229972839355, 14.245406150817871, 14.584582328796387, 14.923759460449219, 15.262935638427734, 15.60211181640625, 15.941287994384766, 16.28046417236328, 16.619640350341797, 16.958816528320312, 17.297992706298828, 17.637170791625977, 17.976346969604492, 18.315523147583008, 18.654699325561523, 18.99387550354004, 19.333051681518555, 19.67222785949707, 20.011404037475586, 20.3505802154541, 20.689756393432617, 21.028932571411133, 21.36810874938965, 21.707286834716797, 22.046463012695312, 22.385639190673828, 22.724815368652344, 23.06399154663086, 23.403167724609375, 23.74234390258789, 24.081520080566406, 24.420696258544922, 24.759872436523438, 25.099048614501953, 25.4382266998291, 25.777402877807617, 26.116579055786133, 26.45575523376465, 26.794931411743164, 27.13410758972168, 27.473283767700195, 27.81245994567871, 28.151636123657227, 28.490812301635742, 28.829988479614258, 29.169164657592773, 29.508342742919922, 29.847518920898438, 30.186695098876953, 30.52587127685547, 30.865047454833984, 31.2042236328125, 31.543399810791016, 31.88257598876953, 32.22175216674805, 32.56092834472656, 32.90010452270508, 33.239280700683594, 33.57845687866211, 33.917633056640625, 34.25680923461914, 34.595985412597656, 34.93516159057617, 35.27434158325195, 35.61351776123047, 35.952693939208984, 36.2918701171875, 36.631046295166016, 36.97022247314453, 37.30939865112305, 37.64857482910156, 37.98775100708008, 38.326927185058594, 38.66610336303711, 39.005279541015625, 39.34445571899414, 39.683631896972656, 40.02280807495117, 40.36198425292969, 40.7011604309082, 41.04033660888672, 41.379512786865234, 41.71868896484375, 42.057865142822266, 42.39704132080078, 42.7362174987793, 43.07539749145508, 43.414573669433594, 43.75374984741211, 44.092926025390625, 44.43210220336914, 44.771278381347656, 45.11045455932617, 45.44963073730469, 45.7888069152832, 46.12798309326172, 46.467159271240234, 46.80633544921875, 47.145511627197266, 47.48468780517578, 47.8238639831543], "2": [7.420428276062012, 7.757720470428467, 8.095012664794922, 8.432305335998535, 8.769597053527832, 9.106889724731445, 9.444181442260742, 9.781474113464355, 10.118765830993652, 10.456058502197266, 10.793350219726562, 11.130642890930176, 11.467934608459473, 11.805227279663086, 12.142518997192383, 12.479811668395996, 12.817103385925293, 13.154396057128906, 13.491687774658203, 13.828980445861816, 14.166272163391113, 14.503564834594727, 14.840856552124023, 15.178149223327637, 15.515440940856934, 15.852733612060547, 16.190025329589844, 16.52731704711914, 16.86461067199707, 17.201902389526367, 17.539194107055664, 17.87648582458496, 18.21377944946289, 18.551071166992188, 18.888362884521484, 19.22565460205078, 19.56294822692871, 19.900239944458008, 20.237531661987305, 20.5748233795166, 20.91211700439453, 21.249408721923828, 21.586700439453125, 21.923992156982422, 22.26128578186035, 22.59857749938965, 22.935869216918945, 23.273160934448242, 23.610454559326172, 23.94774627685547, 24.285037994384766, 24.622329711914062, 24.959623336791992, 25.29691505432129, 25.634206771850586, 25.971498489379883, 26.308792114257812, 26.64608383178711, 26.983375549316406, 27.320667266845703, 27.657960891723633, 27.99525260925293, 28.332544326782227, 28.669836044311523, 29.007129669189453, 29.34442138671875, 29.681713104248047, 30.019004821777344, 30.356298446655273, 30.69359016418457, 31.030881881713867, 31.368173599243164, 31.705467224121094, 32.04275894165039, 32.38005065917969, 32.717342376708984, 33.05463409423828, 33.391929626464844, 33.72922134399414, 34.06651306152344, 34.403804779052734, 34.74109649658203, 35.07838821411133, 35.415679931640625, 35.75297164916992, 36.090267181396484, 36.42755889892578, 36.76485061645508, 37.102142333984375, 37.43943405151367, 37.77672576904297, 38.114017486572266, 38.45130920410156, 38.788604736328125, 39.12589645385742, 39.46318817138672, 39.800479888916016, 40.13777160644531, 40.47506332397461, 40.812355041503906, 41.1496467590332, 41.486942291259766, 41.82423400878906, 42.16152572631836, 42.498817443847656, 42.83610916137695, 43.17340087890625, 43.51069259643555, 43.847984313964844, 44.185279846191406, 44.5225715637207, 44.85986328125, 45.1971549987793, 45.534446716308594, 45.87173843383789, 46.20903015136719, 46.546321868896484, 46.88361740112305, 47.220909118652344, 47.55820083618164], "3": [7.379463195800781, 7.714893341064453, 8.050323486328125, 8.385753631591797, 8.721183776855469, 9.05661392211914, 9.392044067382812, 9.727474212646484, 10.062904357910156, 10.398334503173828, 10.7337646484375, 11.069194793701172, 11.404624938964844, 11.740055084228516, 12.075485229492188, 12.41091537475586, 12.746345520019531, 13.081775665283203, 13.417205810546875, 13.752635955810547, 14.088066101074219, 14.42349624633789, 14.758926391601562, 15.094356536865234, 15.429786682128906, 15.765216827392578, 16.10064697265625, 16.436077117919922, 16.771507263183594, 17.106937408447266, 17.442367553710938, 17.77779769897461, 18.11322784423828, 18.448657989501953, 18.784088134765625, 19.119518280029297, 19.45494842529297, 19.79037857055664, 20.125808715820312, 20.461238861083984, 20.796669006347656, 21.132099151611328, 21.467529296875, 21.802959442138672, 22.138389587402344, 22.473819732666016, 22.809249877929688, 23.14468002319336, 23.48011016845703, 23.815540313720703, 24.150970458984375, 24.486400604248047, 24.82183074951172, 25.15726089477539, 25.492691040039062, 25.828121185302734, 26.163551330566406, 26.498981475830078, 26.83441162109375, 27.169841766357422, 27.505271911621094, 27.840702056884766, 28.176132202148438, 28.51156234741211, 28.84699249267578, 29.182422637939453, 29.517852783203125, 29.853282928466797, 30.18871307373047, 30.52414321899414, 30.859573364257812, 31.195003509521484, 31.530433654785156, 31.865863800048828, 32.2012939453125, 32.53672409057617, 32.872154235839844, 33.207584381103516, 33.54301452636719, 33.87844467163086, 34.21387481689453, 34.5493049621582, 34.884735107421875, 35.22016525268555, 35.55559539794922, 35.89102554321289, 36.22645568847656, 36.561885833740234, 36.897315979003906, 37.23274612426758, 37.56817626953125, 37.90360641479492, 38.239036560058594, 38.574466705322266, 38.90989685058594, 39.24532699584961, 39.58075714111328, 39.91618728637695, 40.251617431640625, 40.5870475769043, 40.92247772216797, 41.25790786743164, 41.59333801269531, 41.928768157958984, 42.264198303222656, 42.59962844848633, 42.93505859375, 43.27048873901367, 43.605918884277344, 43.941349029541016, 44.27677917480469, 44.61220932006836, 44.94763946533203, 45.2830696105957, 45.618499755859375, 45.95392990112305, 46.28936004638672, 46.62479019165039, 46.96022033691406, 47.295650482177734], "4": [7.33897590637207, 7.672565460205078, 8.006155014038086, 8.33974552154541, 8.673335075378418, 9.006924629211426, 9.340514183044434, 9.674104690551758, 10.007694244384766, 10.341283798217773, 10.674874305725098, 11.008463859558105, 11.342053413391113, 11.675642967224121, 12.009233474731445, 12.342823028564453, 12.676412582397461, 13.010002136230469, 13.343592643737793, 13.6771821975708, 14.010771751403809, 14.344361305236816, 14.67795181274414, 15.011541366577148, 15.345130920410156, 15.67872142791748, 16.012310028076172, 16.345901489257812, 16.67949104309082, 17.013080596923828, 17.346670150756836, 17.680259704589844, 18.01384925842285, 18.34743881225586, 18.681028366088867, 19.014619827270508, 19.348209381103516, 19.681798934936523, 20.01538848876953, 20.34897804260254, 20.682567596435547, 21.016157150268555, 21.349748611450195, 21.683338165283203, 22.01692771911621, 22.35051727294922, 22.684106826782227, 23.017696380615234, 23.351285934448242, 23.68487548828125, 24.01846694946289, 24.3520565032959, 24.685646057128906, 25.019235610961914, 25.352825164794922, 25.68641471862793, 26.020004272460938, 26.353595733642578, 26.687185287475586, 27.020774841308594, 27.3543643951416, 27.68795394897461, 28.021543502807617, 28.355133056640625, 28.688722610473633, 29.022314071655273, 29.35590362548828, 29.68949317932129, 30.023082733154297, 30.356672286987305, 30.690261840820312, 31.02385139465332, 31.35744285583496, 31.69103240966797, 32.024620056152344, 32.358211517333984, 32.691802978515625, 33.025390625, 33.35898208618164, 33.692569732666016, 34.026161193847656, 34.35974884033203, 34.69334030151367, 35.02693176269531, 35.36051940917969, 35.69411087036133, 36.0276985168457, 36.361289978027344, 36.69487762451172, 37.02846908569336, 37.362056732177734, 37.695648193359375, 38.029239654541016, 38.36282730102539, 38.69641876220703, 39.030006408691406, 39.36359786987305, 39.69718551635742, 40.03077697753906, 40.3643684387207, 40.69795608520508, 41.03154754638672, 41.365135192871094, 41.698726654052734, 42.03231430053711, 42.36590576171875, 42.69949722290039, 43.033084869384766, 43.366676330566406, 43.70026397705078, 44.03385543823242, 44.3674430847168, 44.70103454589844, 45.03462600708008, 45.36821365356445, 45.701805114746094, 46.03539276123047, 46.36898422241211, 46.702571868896484, 47.036163330078125], "5": [7.298957824707031, 7.630728721618652, 7.962499618530273, 8.294270515441895, 8.626041412353516, 8.957812309265137, 9.289583206176758, 9.621353149414062, 9.953124046325684, 10.284894943237305, 10.616665840148926, 10.948436737060547, 11.280207633972168, 11.611978530883789, 11.94374942779541, 12.275520324707031, 12.607291221618652, 12.939062118530273, 13.270833015441895, 13.6026029586792, 13.93437385559082, 14.266144752502441, 14.597915649414062, 14.929686546325684, 15.261457443237305, 15.593228340148926, 15.924999237060547, 16.25676918029785, 16.58854103088379, 16.920310974121094, 17.25208282470703, 17.583852767944336, 17.915624618530273, 18.247394561767578, 18.579166412353516, 18.91093635559082, 19.242706298828125, 19.574478149414062, 19.906248092651367, 20.238019943237305, 20.56978988647461, 20.901561737060547, 21.23333168029785, 21.56510353088379, 21.896873474121094, 22.22864532470703, 22.560415267944336, 22.892187118530273, 23.223957061767578, 23.555727005004883, 23.88749885559082, 24.219268798828125, 24.551040649414062, 24.882810592651367, 25.214582443237305, 25.54635238647461, 25.878124237060547, 26.20989418029785, 26.54166603088379, 26.873435974121094, 27.2052059173584, 27.536977767944336, 27.86874771118164, 28.200519561767578, 28.532289505004883, 28.86406135559082, 29.195831298828125, 29.527603149414062, 29.859373092651367, 30.191144943237305, 30.52291488647461, 30.854684829711914, 31.18645668029785, 31.518226623535156, 31.849998474121094, 32.18177032470703, 32.5135383605957, 32.84531021118164, 33.17708206176758, 33.508853912353516, 33.84062194824219, 34.172393798828125, 34.50416564941406, 34.835933685302734, 35.16770553588867, 35.49947738647461, 35.83124923706055, 36.16301727294922, 36.494789123535156, 36.826560974121094, 37.15833282470703, 37.4901008605957, 37.82187271118164, 38.15364456176758, 38.48541259765625, 38.81718444824219, 39.148956298828125, 39.48072814941406, 39.812496185302734, 40.14426803588867, 40.47603988647461, 40.80781173706055, 41.13957977294922, 41.471351623535156, 41.803123474121094, 42.13489532470703, 42.4666633605957, 42.79843521118164, 43.13020706176758, 43.46197509765625, 43.79374694824219, 44.125518798828125, 44.45729064941406, 44.789058685302734, 45.12083053588867, 45.45260238647461, 45.78437423706055, 46.11614227294922, 46.447914123535156, 46.779685974121094], "6": [7.259401798248291, 7.589374542236328, 7.919347286224365, 8.249320030212402, 8.579293251037598, 8.909265518188477, 9.239238739013672, 9.56921100616455, 9.899184226989746, 10.229156494140625, 10.55912971496582, 10.889102935791016, 11.219075202941895, 11.54904842376709, 11.879020690917969, 12.208993911743164, 12.538966178894043, 12.868939399719238, 13.198912620544434, 13.528884887695312, 13.858858108520508, 14.188830375671387, 14.518803596496582, 14.848775863647461, 15.178749084472656, 15.508721351623535, 15.83869457244873, 16.16866683959961, 16.498640060424805, 16.82861328125, 17.158586502075195, 17.488557815551758, 17.818531036376953, 18.14850425720215, 18.478477478027344, 18.80845069885254, 19.1384220123291, 19.468395233154297, 19.798368453979492, 20.128341674804688, 20.45831298828125, 20.788286209106445, 21.11825942993164, 21.448232650756836, 21.77820587158203, 22.108177185058594, 22.43815040588379, 22.768123626708984, 23.09809684753418, 23.428068161010742, 23.758041381835938, 24.088014602661133, 24.417987823486328, 24.747961044311523, 25.077932357788086, 25.40790557861328, 25.737878799438477, 26.067852020263672, 26.397825241088867, 26.72779655456543, 27.057769775390625, 27.38774299621582, 27.717716217041016, 28.047687530517578, 28.377660751342773, 28.70763397216797, 29.037607192993164, 29.36758041381836, 29.697551727294922, 30.027524948120117, 30.357498168945312, 30.687471389770508, 31.01744270324707, 31.347415924072266, 31.67738914489746, 32.007362365722656, 32.33733367919922, 32.66730880737305, 32.99728012084961, 33.32725143432617, 33.6572265625, 33.98719787597656, 34.31717300415039, 34.64714431762695, 34.977115631103516, 35.307090759277344, 35.637062072753906, 35.967037200927734, 36.2970085144043, 36.62697982788086, 36.95695495605469, 37.28692626953125, 37.61690139770508, 37.94687271118164, 38.2768440246582, 38.60681915283203, 38.936790466308594, 39.26676559448242, 39.596736907958984, 39.92670822143555, 40.256683349609375, 40.58665466308594, 40.9166259765625, 41.24660110473633, 41.57657241821289, 41.90654754638672, 42.23651885986328, 42.566490173339844, 42.89646530151367, 43.226436614990234, 43.55641174316406, 43.886383056640625, 44.21635437011719, 44.546329498291016, 44.87630081176758, 45.206275939941406, 45.53624725341797, 45.86621856689453, 46.19619369506836, 46.52616500854492], "7": [7.220299243927002, 7.548494815826416, 7.87669038772583, 8.204885482788086, 8.5330810546875, 8.861276626586914, 9.189472198486328, 9.517667770385742, 9.84586238861084, 10.174057960510254, 10.502253532409668, 10.830449104309082, 11.158644676208496, 11.48684024810791, 11.815034866333008, 12.143230438232422, 12.471426010131836, 12.79962158203125, 13.127817153930664, 13.456012725830078, 13.784208297729492, 14.11240291595459, 14.440598487854004, 14.768794059753418, 15.096989631652832, 15.425185203552246, 15.75338077545166, 16.081575393676758, 16.409770965576172, 16.737966537475586, 17.066162109375, 17.394357681274414, 17.722553253173828, 18.050748825073242, 18.378944396972656, 18.70713996887207, 19.035335540771484, 19.363529205322266, 19.69172477722168, 20.019920349121094, 20.348115921020508, 20.676311492919922, 21.004507064819336, 21.33270263671875, 21.660898208618164, 21.989093780517578, 22.317289352416992, 22.645484924316406, 22.97368049621582, 23.301876068115234, 23.630069732666016, 23.95826530456543, 24.286460876464844, 24.614656448364258, 24.942852020263672, 25.271047592163086, 25.5992431640625, 25.927438735961914, 26.255634307861328, 26.583829879760742, 26.912025451660156, 27.24022102355957, 27.568416595458984, 27.896610260009766, 28.22480583190918, 28.553001403808594, 28.881196975708008, 29.209392547607422, 29.537588119506836, 29.86578369140625, 30.193979263305664, 30.522174835205078, 30.850370407104492, 31.178565979003906, 31.50676155090332, 31.834957122802734, 32.163150787353516, 32.49134826660156, 32.819541931152344, 33.14773941040039, 33.47593307495117, 33.80413055419922, 34.13232421875, 34.46051788330078, 34.78871536254883, 35.11690902709961, 35.445106506347656, 35.77330017089844, 36.101497650146484, 36.429691314697266, 36.75788879394531, 37.086082458496094, 37.41427993774414, 37.74247360229492, 38.07067108154297, 38.39886474609375, 38.72705841064453, 39.05525588989258, 39.38344955444336, 39.711647033691406, 40.03984069824219, 40.368038177490234, 40.696231842041016, 41.02442932128906, 41.352622985839844, 41.68082046508789, 42.00901412963867, 42.33721160888672, 42.6654052734375, 42.99359893798828, 43.32179641723633, 43.64999008178711, 43.978187561035156, 44.30638122558594, 44.634578704833984, 44.962772369384766, 45.29096984863281, 45.619163513183594, 45.94736099243164, 46.27555465698242], "8": [7.181643486022949, 7.508081436157227, 7.834519863128662, 8.160958290100098, 8.487396240234375, 8.813835144042969, 9.140273094177246, 9.46671199798584, 9.793149948120117, 10.119587898254395, 10.446026802062988, 10.772464752197266, 11.09890365600586, 11.425341606140137, 11.751779556274414, 12.078218460083008, 12.404656410217285, 12.731095314025879, 13.057533264160156, 13.383971214294434, 13.710410118103027, 14.036848068237305, 14.363286972045898, 14.689724922180176, 15.016162872314453, 15.342601776123047, 15.669039726257324, 15.995478630065918, 16.321916580200195, 16.64835548400879, 16.97479248046875, 17.301231384277344, 17.627670288085938, 17.9541072845459, 18.280546188354492, 18.606985092163086, 18.93342399597168, 19.25986099243164, 19.586299896240234, 19.912738800048828, 20.23917579650879, 20.565614700317383, 20.892053604125977, 21.218490600585938, 21.54492950439453, 21.871368408203125, 22.19780731201172, 22.52424430847168, 22.850683212280273, 23.177122116088867, 23.503559112548828, 23.829998016357422, 24.156436920166016, 24.482873916625977, 24.80931282043457, 25.135751724243164, 25.462190628051758, 25.78862762451172, 26.115066528320312, 26.441505432128906, 26.767942428588867, 27.09438133239746, 27.420820236206055, 27.747257232666016, 28.07369613647461, 28.400135040283203, 28.726573944091797, 29.053010940551758, 29.37944984436035, 29.705888748168945, 30.032325744628906, 30.3587646484375, 30.685203552246094, 31.011640548706055, 31.33807945251465, 31.664518356323242, 31.990957260131836, 32.3173942565918, 32.64383316040039, 32.970272064208984, 33.29671096801758, 33.62314987182617, 33.9495849609375, 34.276023864746094, 34.60246276855469, 34.92890167236328, 35.255340576171875, 35.58177947998047, 35.9082145690918, 36.23465347290039, 36.561092376708984, 36.88753128051758, 37.21397018432617, 37.540409088134766, 37.86684799194336, 38.19328308105469, 38.51972198486328, 38.846160888671875, 39.17259979248047, 39.49903869628906, 39.825477600097656, 40.15191650390625, 40.47835159301758, 40.80479049682617, 41.131229400634766, 41.45766830444336, 41.78410720825195, 42.11054611206055, 42.436981201171875, 42.76342010498047, 43.08985900878906, 43.416297912597656, 43.74273681640625, 44.069175720214844, 44.39561462402344, 44.722049713134766, 45.04848861694336, 45.37492752075195, 45.70136642456055, 46.02780532836914], "9": [7.143425941467285, 7.468127250671387, 7.792828559875488, 8.11752986907959, 8.442231178283691, 8.766931533813477, 9.091632843017578, 9.41633415222168, 9.741035461425781, 10.065736770629883, 10.390438079833984, 10.715139389038086, 11.039840698242188, 11.364541053771973, 11.689242362976074, 12.013943672180176, 12.338644981384277, 12.663346290588379, 12.98804759979248, 13.312748908996582, 13.637450218200684, 13.962150573730469, 14.28685188293457, 14.611553192138672, 14.936254501342773, 15.260955810546875, 15.585657119750977, 15.910358428955078, 16.23505973815918, 16.55976104736328, 16.884462356567383, 17.209163665771484, 17.533863067626953, 17.858564376831055, 18.183265686035156, 18.507966995239258, 18.83266830444336, 19.15736961364746, 19.482070922851562, 19.806772232055664, 20.131473541259766, 20.456174850463867, 20.78087615966797, 21.10557746887207, 21.430278778076172, 21.754980087280273, 22.079681396484375, 22.404380798339844, 22.729082107543945, 23.053783416748047, 23.37848472595215, 23.70318603515625, 24.02788734436035, 24.352588653564453, 24.677289962768555, 25.001991271972656, 25.326692581176758, 25.65139389038086, 25.97609519958496, 26.300796508789062, 26.625497817993164, 26.950199127197266, 27.274900436401367, 27.599599838256836, 27.924301147460938, 28.24900245666504, 28.57370376586914, 28.898405075073242, 29.223106384277344, 29.547807693481445, 29.872509002685547, 30.19721031188965, 30.52191162109375, 30.84661293029785, 31.171314239501953, 31.496015548706055, 31.820716857910156, 32.145416259765625, 32.47011947631836, 32.79481887817383, 33.11952209472656, 33.44422149658203, 33.768924713134766, 34.093624114990234, 34.41832733154297, 34.74302673339844, 35.067726135253906, 35.39242935180664, 35.71712875366211, 36.041831970214844, 36.36653137207031, 36.69123458862305, 37.015933990478516, 37.34063720703125, 37.66533660888672, 37.99003982543945, 38.31473922729492, 38.639442443847656, 38.964141845703125, 39.28884506225586, 39.61354446411133, 39.9382438659668, 40.26294708251953, 40.587646484375, 40.912349700927734, 41.2370491027832, 41.56175231933594, 41.886451721191406, 42.21115493774414, 42.53585433959961, 42.860557556152344, 43.18525695800781, 43.50996017456055, 43.834659576416016, 44.15936279296875, 44.48406219482422, 44.80876159667969, 45.13346481323242, 45.45816421508789, 45.782867431640625], "10": [7.105640411376953, 7.428624153137207, 7.751607894897461, 8.074591636657715, 8.397575378417969, 8.720559120178223, 9.043542861938477, 9.366525650024414, 9.689509391784668, 10.012493133544922, 10.335476875305176, 10.65846061706543, 10.981444358825684, 11.304428100585938, 11.627411842346191, 11.950395584106445, 12.2733793258667, 12.596363067626953, 12.91934585571289, 13.242329597473145, 13.565313339233398, 13.888297080993652, 14.211280822753906, 14.53426456451416, 14.857248306274414, 15.180232048034668, 15.503215789794922, 15.826199531555176, 16.14918327331543, 16.472166061401367, 16.795150756835938, 17.118133544921875, 17.441118240356445, 17.764101028442383, 18.087085723876953, 18.41006851196289, 18.733051300048828, 19.0560359954834, 19.379018783569336, 19.702003479003906, 20.024986267089844, 20.347970962524414, 20.67095375061035, 20.993938446044922, 21.31692123413086, 21.63990592956543, 21.962888717651367, 22.285871505737305, 22.608856201171875, 22.931838989257812, 23.254823684692383, 23.57780647277832, 23.90079116821289, 24.223773956298828, 24.5467586517334, 24.869741439819336, 25.192726135253906, 25.515708923339844, 25.83869171142578, 26.16167640686035, 26.48465919494629, 26.80764389038086, 27.130626678466797, 27.453611373901367, 27.776594161987305, 28.099578857421875, 28.422561645507812, 28.745546340942383, 29.06852912902832, 29.391511917114258, 29.714496612548828, 30.037479400634766, 30.360464096069336, 30.683446884155273, 31.006431579589844, 31.32941436767578, 31.65239906311035, 31.97538185119629, 32.29836654663086, 32.6213493347168, 32.944332122802734, 33.26731491088867, 33.590301513671875, 33.91328430175781, 34.23626708984375, 34.55924987792969, 34.88223648071289, 35.20521926879883, 35.528202056884766, 35.8511848449707, 36.174171447753906, 36.497154235839844, 36.82013702392578, 37.14311981201172, 37.466102600097656, 37.78908920288086, 38.1120719909668, 38.435054779052734, 38.75803756713867, 39.081024169921875, 39.40400695800781, 39.72698974609375, 40.04997253417969, 40.372955322265625, 40.69594192504883, 41.018924713134766, 41.3419075012207, 41.66489028930664, 41.987876892089844, 42.31085968017578, 42.63384246826172, 42.956825256347656, 43.27981185913086, 43.6027946472168, 43.925777435302734, 44.24876022338867, 44.57174301147461, 44.89472961425781, 45.21771240234375, 45.54069519042969], "11": [7.068279266357422, 7.3895649909973145, 7.710850238800049, 8.032135963439941, 8.353421211242676, 8.67470645904541, 8.995991706848145, 9.317276954650879, 9.63856315612793, 9.959848403930664, 10.281133651733398, 10.602418899536133, 10.923704147338867, 11.244990348815918, 11.566275596618652, 11.887560844421387, 12.208846092224121, 12.530131340026855, 12.85141658782959, 13.17270278930664, 13.493988037109375, 13.81527328491211, 14.136558532714844, 14.457843780517578, 14.779129981994629, 15.100415229797363, 15.421700477600098, 15.742985725402832, 16.064271926879883, 16.385557174682617, 16.70684242248535, 17.028127670288086, 17.34941291809082, 17.670698165893555, 17.99198341369629, 18.313268661499023, 18.634553909301758, 18.955839157104492, 19.27712631225586, 19.598411560058594, 19.919696807861328, 20.240982055664062, 20.562267303466797, 20.88355255126953, 21.204837799072266, 21.526123046875, 21.847408294677734, 22.16869354248047, 22.489980697631836, 22.81126594543457, 23.132551193237305, 23.45383644104004, 23.775121688842773, 24.096406936645508, 24.417692184448242, 24.738977432250977, 25.06026268005371, 25.381547927856445, 25.70283317565918, 26.024120330810547, 26.34540557861328, 26.666690826416016, 26.98797607421875, 27.309261322021484, 27.63054656982422, 27.951831817626953, 28.273117065429688, 28.594402313232422, 28.915687561035156, 29.23697280883789, 29.558259963989258, 29.879545211791992, 30.200830459594727, 30.52211570739746, 30.843400955200195, 31.16468620300293, 31.485971450805664, 31.8072566986084, 32.128543853759766, 32.4498291015625, 32.771114349365234, 33.09239959716797, 33.4136848449707, 33.73497009277344, 34.05625534057617, 34.377540588378906, 34.69882583618164, 35.020111083984375, 35.34139633178711, 35.662681579589844, 35.98396682739258, 36.30525207519531, 36.62653732299805, 36.94782257080078, 37.269107818603516, 37.59039306640625, 37.911678314208984, 38.232967376708984, 38.55425262451172, 38.87553787231445, 39.19682312011719, 39.51810836791992, 39.839393615722656, 40.16067886352539, 40.481964111328125, 40.80324935913086, 41.124534606933594, 41.44581985473633, 41.76710510253906, 42.0883903503418, 42.40967559814453, 42.730960845947266, 43.05224609375, 43.373531341552734, 43.69481658935547, 44.0161018371582, 44.33738708496094, 44.65867233276367, 44.97996139526367, 45.301246643066406], "12": [7.031335830688477, 7.350942134857178, 7.670547962188721, 7.990154266357422, 8.309760093688965, 8.629366874694824, 8.948972702026367, 9.268579483032227, 9.58818531036377, 9.907791137695312, 10.227397918701172, 10.547003746032715, 10.866609573364258, 11.186216354370117, 11.50582218170166, 11.825428009033203, 12.145034790039062, 12.464640617370605, 12.784247398376465, 13.103853225708008, 13.42345905303955, 13.74306583404541, 14.062671661376953, 14.382277488708496, 14.701884269714355, 15.021490097045898, 15.341095924377441, 15.6607027053833, 15.980308532714844, 16.299915313720703, 16.61952018737793, 16.93912696838379, 17.25873374938965, 17.578338623046875, 17.897945404052734, 18.217552185058594, 18.537158966064453, 18.85676383972168, 19.17637062072754, 19.4959774017334, 19.815582275390625, 20.135189056396484, 20.454795837402344, 20.77440071105957, 21.09400749206543, 21.41361427307129, 21.733219146728516, 22.052825927734375, 22.372432708740234, 22.69203758239746, 23.01164436340332, 23.33125114440918, 23.650856018066406, 23.970462799072266, 24.290069580078125, 24.60967445373535, 24.92928123474121, 25.24888801574707, 25.56849479675293, 25.888099670410156, 26.207706451416016, 26.527313232421875, 26.8469181060791, 27.16652488708496, 27.48613166809082, 27.805736541748047, 28.125343322753906, 28.444950103759766, 28.764554977416992, 29.08416175842285, 29.40376853942871, 29.723373413085938, 30.042980194091797, 30.362586975097656, 30.682191848754883, 31.001798629760742, 31.3214054107666, 31.641010284423828, 31.960617065429688, 32.28022384643555, 32.599830627441406, 32.919437408447266, 33.23904037475586, 33.55864715576172, 33.87825393676758, 34.19786071777344, 34.5174674987793, 34.837074279785156, 35.15667724609375, 35.47628402709961, 35.79589080810547, 36.11549758911133, 36.43510437011719, 36.75471115112305, 37.074317932128906, 37.3939208984375, 37.71352767944336, 38.03313446044922, 38.35274124145508, 38.67234802246094, 38.9919548034668, 39.31155776977539, 39.63116455078125, 39.95077133178711, 40.27037811279297, 40.58998489379883, 40.90959167480469, 41.22919464111328, 41.54880142211914, 41.868408203125, 42.18801498413086, 42.50762176513672, 42.82722854614258, 43.14683151245117, 43.46643829345703, 43.78604507446289, 44.10565185546875, 44.42525863647461, 44.74486541748047, 45.06447219848633], "13": [6.994802951812744, 7.312748432159424, 7.630694389343262, 7.948639869689941, 8.266585350036621, 8.5845308303833, 8.90247631072998, 9.22042179107666, 9.538368225097656, 9.856313705444336, 10.174259185791016, 10.492204666137695, 10.810150146484375, 11.128095626831055, 11.446041107177734, 11.763986587524414, 12.081932067871094, 12.39987850189209, 12.71782398223877, 13.03576946258545, 13.353714942932129, 13.671660423278809, 13.989605903625488, 14.307551383972168, 14.625496864318848, 14.943443298339844, 15.261388778686523, 15.579334259033203, 15.897279739379883, 16.215225219726562, 16.533170700073242, 16.851116180419922, 17.1690616607666, 17.48700714111328, 17.80495262145996, 18.12289810180664, 18.44084358215332, 18.7587890625, 19.076736450195312, 19.394681930541992, 19.712627410888672, 20.03057289123535, 20.34851837158203, 20.66646385192871, 20.98440933227539, 21.30235481262207, 21.62030029296875, 21.93824577331543, 22.25619125366211, 22.57413673400879, 22.89208221435547, 23.21002769470215, 23.527973175048828, 23.845918655395508, 24.163864135742188, 24.4818115234375, 24.79975700378418, 25.11770248413086, 25.43564796447754, 25.75359344482422, 26.0715389251709, 26.389484405517578, 26.707429885864258, 27.025375366210938, 27.343320846557617, 27.661266326904297, 27.979211807250977, 28.297157287597656, 28.615102767944336, 28.933048248291016, 29.250993728637695, 29.568939208984375, 29.886886596679688, 30.204832077026367, 30.522777557373047, 30.840723037719727, 31.158668518066406, 31.476613998413086, 31.794559478759766, 32.11250305175781, 32.430450439453125, 32.74839782714844, 33.066341400146484, 33.3842887878418, 33.702232360839844, 34.020179748535156, 34.3381233215332, 34.656070709228516, 34.97401428222656, 35.291961669921875, 35.60990524291992, 35.927852630615234, 36.24579620361328, 36.563743591308594, 36.88168716430664, 37.19963455200195, 37.517578125, 37.83552551269531, 38.153472900390625, 38.47141647338867, 38.789363861083984, 39.10730743408203, 39.425254821777344, 39.74319839477539, 40.0611457824707, 40.37908935546875, 40.69703674316406, 41.01498031616211, 41.33292770385742, 41.65087127685547, 41.96881866455078, 42.28676223754883, 42.60470962524414, 42.92265319824219, 43.2406005859375, 43.55854797363281, 43.87649154663086, 44.19443893432617, 44.51238250732422, 44.83032989501953], "14": [6.958674430847168, 7.274977684020996, 7.591280937194824, 7.9075846672058105, 8.22388744354248, 8.540191650390625, 8.856494903564453, 9.172798156738281, 9.48910140991211, 9.805404663085938, 10.121707916259766, 10.438011169433594, 10.754315376281738, 11.070618629455566, 11.386921882629395, 11.703225135803223, 12.01952838897705, 12.335831642150879, 12.652134895324707, 12.968438148498535, 13.28474235534668, 13.601045608520508, 13.917348861694336, 14.233652114868164, 14.549955368041992, 14.86625862121582, 15.182561874389648, 15.498866081237793, 15.815169334411621, 16.131471633911133, 16.44777488708496, 16.764080047607422, 17.08038330078125, 17.396686553955078, 17.712989807128906, 18.029293060302734, 18.345596313476562, 18.66189956665039, 18.97820281982422, 19.294506072998047, 19.610809326171875, 19.927112579345703, 20.24341583251953, 20.55971908569336, 20.876022338867188, 21.192325592041016, 21.508630752563477, 21.824934005737305, 22.141237258911133, 22.45754051208496, 22.77384376525879, 23.090147018432617, 23.406450271606445, 23.722753524780273, 24.0390567779541, 24.35536003112793, 24.671663284301758, 24.987966537475586, 25.304269790649414, 25.620573043823242, 25.93687629699707, 26.25318145751953, 26.56948471069336, 26.885787963867188, 27.202091217041016, 27.518394470214844, 27.834697723388672, 28.1510009765625, 28.467304229736328, 28.783607482910156, 29.099910736083984, 29.416213989257812, 29.73251724243164, 30.04882049560547, 30.365123748779297, 30.681427001953125, 30.997732162475586, 31.314035415649414, 31.630338668823242, 31.94664192199707, 32.262943267822266, 32.579246520996094, 32.89554977416992, 33.211856842041016, 33.528160095214844, 33.84446334838867, 34.1607666015625, 34.47706985473633, 34.793373107910156, 35.109676361083984, 35.42597961425781, 35.74228286743164, 36.05858612060547, 36.3748893737793, 36.691192626953125, 37.00749588012695, 37.32379913330078, 37.64010238647461, 37.95640563964844, 38.272708892822266, 38.589012145996094, 38.90531539916992, 39.22161865234375, 39.53792190551758, 39.854225158691406, 40.170528411865234, 40.48683166503906, 40.80313491821289, 41.11943817138672, 41.43574142456055, 41.752044677734375, 42.0683479309082, 42.38465118408203, 42.700958251953125, 43.01726150512695, 43.33356475830078, 43.64986801147461, 43.96617126464844, 44.282474517822266, 44.598777770996094], "15": [6.922943115234375, 7.2376227378845215, 7.55230188369751, 7.866981029510498, 8.181660652160645, 8.496339797973633, 8.811018943786621, 9.12569808959961, 9.440377235412598, 9.755056381225586, 10.069735527038574, 10.384414672851562, 10.69909381866455, 11.013773918151855, 11.328453063964844, 11.643132209777832, 11.95781135559082, 12.272490501403809, 12.587169647216797, 12.901848793029785, 13.216527938842773, 13.531207084655762, 13.84588623046875, 14.160566329956055, 14.475245475769043, 14.789924621582031, 15.10460376739502, 15.419282913208008, 15.733962059020996, 16.048641204833984, 16.36332130432129, 16.67799949645996, 16.992679595947266, 17.307357788085938, 17.622037887573242, 17.936716079711914, 18.25139617919922, 18.56607437133789, 18.880754470825195, 19.1954345703125, 19.510112762451172, 19.824792861938477, 20.13947105407715, 20.454151153564453, 20.768829345703125, 21.08350944519043, 21.3981876373291, 21.712867736816406, 22.02754783630371, 22.342226028442383, 22.656906127929688, 22.97158432006836, 23.286264419555664, 23.600942611694336, 23.91562271118164, 24.230300903320312, 24.544981002807617, 24.85965919494629, 25.174339294433594, 25.4890193939209, 25.80369758605957, 26.118377685546875, 26.433055877685547, 26.74773597717285, 27.062414169311523, 27.377094268798828, 27.6917724609375, 28.006452560424805, 28.32113265991211, 28.63581085205078, 28.950490951538086, 29.265169143676758, 29.579849243164062, 29.894527435302734, 30.20920753479004, 30.52388572692871, 30.838565826416016, 31.153244018554688, 31.467924118041992, 31.782604217529297, 32.09728240966797, 32.41196060180664, 32.72664260864258, 33.04132080078125, 33.35599899291992, 33.670677185058594, 33.98535919189453, 34.3000373840332, 34.614715576171875, 34.92939758300781, 35.244075775146484, 35.558753967285156, 35.87343215942383, 36.188114166259766, 36.50279235839844, 36.81747055053711, 37.13214874267578, 37.44683074951172, 37.76150894165039, 38.07618713378906, 38.390869140625, 38.70554733276367, 39.020225524902344, 39.334903717041016, 39.64958572387695, 39.964263916015625, 40.2789421081543, 40.593624114990234, 40.908302307128906, 41.22298049926758, 41.53765869140625, 41.85234069824219, 42.16701889038086, 42.48169708251953, 42.7963752746582, 43.11105728149414, 43.42573547363281, 43.740413665771484, 44.05509567260742, 44.369773864746094], "16": [6.887603759765625, 7.200676441192627, 7.513749122619629, 7.826822280883789, 8.13989543914795, 8.452967643737793, 8.766040802001953, 9.079113960266113, 9.392186164855957, 9.705259323120117, 10.018332481384277, 10.331405639648438, 10.644477844238281, 10.957551002502441, 11.270624160766602, 11.583697319030762, 11.896769523620605, 12.209842681884766, 12.522915840148926, 12.83598804473877, 13.14906120300293, 13.46213436126709, 13.77520751953125, 14.088279724121094, 14.401352882385254, 14.714426040649414, 15.027498245239258, 15.340571403503418, 15.653644561767578, 15.966717720031738, 16.2797908782959, 16.592863082885742, 16.905935287475586, 17.219009399414062, 17.532081604003906, 17.84515380859375, 18.158227920532227, 18.47130012512207, 18.784372329711914, 19.09744644165039, 19.410518646240234, 19.72359275817871, 20.036664962768555, 20.3497371673584, 20.662811279296875, 20.97588348388672, 21.288955688476562, 21.60202980041504, 21.915102005004883, 22.228174209594727, 22.541248321533203, 22.854320526123047, 23.167394638061523, 23.480466842651367, 23.79353904724121, 24.106613159179688, 24.41968536376953, 24.732757568359375, 25.04583168029785, 25.358903884887695, 25.67197608947754, 25.985050201416016, 26.29812240600586, 26.611194610595703, 26.92426872253418, 27.237340927124023, 27.5504150390625, 27.863487243652344, 28.176559448242188, 28.489633560180664, 28.802705764770508, 29.11577796936035, 29.428852081298828, 29.741924285888672, 30.054996490478516, 30.368070602416992, 30.681142807006836, 30.99421501159668, 31.307289123535156, 31.620361328125, 31.933435440063477, 32.24650573730469, 32.5595817565918, 32.87265396118164, 33.185726165771484, 33.49879837036133, 33.81187057495117, 34.12494659423828, 34.438018798828125, 34.75109100341797, 35.06416320800781, 35.377235412597656, 35.6903076171875, 36.00338363647461, 36.31645584106445, 36.6295280456543, 36.94260025024414, 37.255672454833984, 37.56874465942383, 37.88182067871094, 38.19489288330078, 38.507965087890625, 38.82103729248047, 39.13410949707031, 39.44718551635742, 39.760257720947266, 40.07332992553711, 40.38640213012695, 40.6994743347168, 41.01254653930664, 41.32562255859375, 41.638694763183594, 41.95176696777344, 42.26483917236328, 42.577911376953125, 42.890987396240234, 43.20405960083008, 43.51713180541992, 43.830204010009766, 44.14327621459961], "17": [6.852648735046387, 7.164132595062256, 7.475616931915283, 7.787100791931152, 8.09858512878418, 8.41006851196289, 8.721552848815918, 9.033037185668945, 9.344521522521973, 9.656004905700684, 9.967489242553711, 10.278973579406738, 10.59045696258545, 10.901941299438477, 11.213425636291504, 11.524909019470215, 11.836393356323242, 12.14787769317627, 12.45936107635498, 12.770845413208008, 13.082329750061035, 13.393813133239746, 13.705297470092773, 14.0167818069458, 14.328265190124512, 14.639749526977539, 14.951233863830566, 15.262717247009277, 15.574201583862305, 15.885685920715332, 16.19717025756836, 16.50865364074707, 16.82013702392578, 17.131622314453125, 17.443105697631836, 17.754589080810547, 18.06607437133789, 18.3775577545166, 18.689043045043945, 19.000526428222656, 19.312009811401367, 19.62349510192871, 19.934978485107422, 20.246461868286133, 20.557947158813477, 20.869430541992188, 21.1809139251709, 21.492399215698242, 21.803882598876953, 22.115365982055664, 22.426851272583008, 22.73833465576172, 23.04981803894043, 23.361303329467773, 23.672786712646484, 23.984270095825195, 24.29575538635254, 24.60723876953125, 24.91872215270996, 25.230207443237305, 25.541690826416016, 25.853174209594727, 26.16465950012207, 26.47614288330078, 26.787626266479492, 27.099111557006836, 27.410594940185547, 27.722078323364258, 28.0335636138916, 28.345046997070312, 28.656530380249023, 28.968015670776367, 29.279499053955078, 29.59098243713379, 29.902467727661133, 30.213951110839844, 30.525434494018555, 30.8369197845459, 31.14840316772461, 31.459888458251953, 31.771371841430664, 32.082855224609375, 32.39434051513672, 32.7058219909668, 33.01730728149414, 33.328792572021484, 33.64027404785156, 33.951759338378906, 34.26324462890625, 34.57472610473633, 34.88621139526367, 35.197696685791016, 35.509178161621094, 35.82066345214844, 36.13214874267578, 36.44363021850586, 36.7551155090332, 37.06660079956055, 37.37808609008789, 37.68956756591797, 38.00105285644531, 38.312538146972656, 38.624019622802734, 38.93550491333008, 39.24699020385742, 39.5584716796875, 39.869956970214844, 40.18144226074219, 40.492923736572266, 40.80440902709961, 41.11589431762695, 41.42737579345703, 41.738861083984375, 42.05034637451172, 42.3618278503418, 42.67331314086914, 42.984798431396484, 43.29627990722656, 43.607765197753906, 43.91925048828125], "18": [6.81807279586792, 7.12798547744751, 7.437897682189941, 7.747810363769531, 8.057722091674805, 8.367634773254395, 8.677547454833984, 8.987460136413574, 9.297371864318848, 9.607284545898438, 9.917197227478027, 10.2271089553833, 10.53702163696289, 10.84693431854248, 11.15684700012207, 11.466758728027344, 11.776671409606934, 12.086584091186523, 12.396495819091797, 12.706408500671387, 13.016321182250977, 13.326233863830566, 13.63614559173584, 13.94605827331543, 14.25597095489502, 14.565882682800293, 14.875795364379883, 15.185708045959473, 15.495620727539062, 15.805532455444336, 16.11544418334961, 16.425357818603516, 16.73526954650879, 17.045183181762695, 17.35509490966797, 17.665006637573242, 17.97492027282715, 18.284832000732422, 18.594743728637695, 18.9046573638916, 19.214569091796875, 19.52448081970215, 19.834394454956055, 20.144306182861328, 20.4542179107666, 20.764131546020508, 21.07404327392578, 21.383956909179688, 21.69386863708496, 22.003780364990234, 22.31369400024414, 22.623605728149414, 22.933517456054688, 23.243431091308594, 23.553342819213867, 23.86325454711914, 24.173168182373047, 24.48307991027832, 24.792991638183594, 25.1029052734375, 25.412817001342773, 25.722728729248047, 26.032642364501953, 26.342554092407227, 26.652467727661133, 26.962379455566406, 27.27229118347168, 27.582204818725586, 27.89211654663086, 28.202028274536133, 28.51194190979004, 28.821853637695312, 29.131765365600586, 29.441679000854492, 29.751590728759766, 30.06150245666504, 30.371416091918945, 30.68132781982422, 30.991241455078125, 31.3011531829834, 31.611064910888672, 31.920978546142578, 32.23088836669922, 32.540802001953125, 32.85071563720703, 33.16062927246094, 33.47053909301758, 33.780452728271484, 34.09036636352539, 34.40027618408203, 34.71018981933594, 35.020103454589844, 35.330013275146484, 35.63992691040039, 35.9498405456543, 36.25975036621094, 36.569664001464844, 36.87957763671875, 37.18948745727539, 37.4994010925293, 37.8093147277832, 38.119224548339844, 38.42913818359375, 38.739051818847656, 39.0489616394043, 39.3588752746582, 39.66878890991211, 39.97869873046875, 40.288612365722656, 40.59852600097656, 40.9084358215332, 41.21834945678711, 41.528263092041016, 41.838172912597656, 42.14808654785156, 42.45800018310547, 42.767913818359375, 43.077823638916016, 43.38773727416992, 43.69765090942383], "19": [6.783870220184326, 7.092227935791016, 7.400585651397705, 7.7089433670043945, 8.017300605773926, 8.325658798217773, 8.634016036987305, 8.942374229431152, 9.250731468200684, 9.559089660644531, 9.867446899414062, 10.17580509185791, 10.484162330627441, 10.792520523071289, 11.100878715515137, 11.409235954284668, 11.717594146728516, 12.025951385498047, 12.334309577941895, 12.642666816711426, 12.951025009155273, 13.259382247924805, 13.567740440368652, 13.876097679138184, 14.184455871582031, 14.492813110351562, 14.80117130279541, 15.109528541564941, 15.417886734008789, 15.72624397277832, 16.03460121154785, 16.342960357666016, 16.651317596435547, 16.959674835205078, 17.26803207397461, 17.576391220092773, 17.884748458862305, 18.193105697631836, 18.501462936401367, 18.80982208251953, 19.118179321289062, 19.426536560058594, 19.734893798828125, 20.04325294494629, 20.35161018371582, 20.65996742248535, 20.968324661254883, 21.276683807373047, 21.585041046142578, 21.89339828491211, 22.201757431030273, 22.510114669799805, 22.818471908569336, 23.126829147338867, 23.43518829345703, 23.743545532226562, 24.051902770996094, 24.360260009765625, 24.66861915588379, 24.97697639465332, 25.28533363342285, 25.593690872192383, 25.902050018310547, 26.210407257080078, 26.51876449584961, 26.82712173461914, 27.135480880737305, 27.443838119506836, 27.752195358276367, 28.0605525970459, 28.368911743164062, 28.677268981933594, 28.985626220703125, 29.293983459472656, 29.60234260559082, 29.91069984436035, 30.219057083129883, 30.527414321899414, 30.835773468017578, 31.14413070678711, 31.45248794555664, 31.760845184326172, 32.0692024230957, 32.3775634765625, 32.68592071533203, 32.99427795410156, 33.302635192871094, 33.610992431640625, 33.919349670410156, 34.22770690917969, 34.53606414794922, 34.844425201416016, 35.15278244018555, 35.46113967895508, 35.76949691772461, 36.07785415649414, 36.38621139526367, 36.6945686340332, 37.002925872802734, 37.31128692626953, 37.61964416503906, 37.928001403808594, 38.236358642578125, 38.544715881347656, 38.85307312011719, 39.16143035888672, 39.46978759765625, 39.77814865112305, 40.08650588989258, 40.39486312866211, 40.70322036743164, 41.01157760620117, 41.3199348449707, 41.628292083740234, 41.936649322509766, 42.24501037597656, 42.553367614746094, 42.861724853515625, 43.170082092285156, 43.47843933105469], "20": [6.750034332275391, 7.056854248046875, 7.363673686981201, 7.6704936027526855, 7.977313041687012, 8.284132957458496, 8.59095287322998, 8.897772789001465, 9.204591751098633, 9.511411666870117, 9.818231582641602, 10.125051498413086, 10.43187141418457, 10.738691329956055, 11.045510292053223, 11.352330207824707, 11.659150123596191, 11.965970039367676, 12.27278995513916, 12.579608917236328, 12.886428833007812, 13.193248748779297, 13.500068664550781, 13.806888580322266, 14.11370849609375, 14.420527458190918, 14.727347373962402, 15.034167289733887, 15.340987205505371, 15.647807121276855, 15.954626083374023, 16.261445999145508, 16.568265914916992, 16.875085830688477, 17.18190574645996, 17.488725662231445, 17.79554557800293, 18.102365493774414, 18.409183502197266, 18.71600341796875, 19.022823333740234, 19.32964324951172, 19.636463165283203, 19.943283081054688, 20.250102996826172, 20.556922912597656, 20.86374282836914, 21.170562744140625, 21.47738265991211, 21.78420066833496, 22.091020584106445, 22.39784049987793, 22.704660415649414, 23.0114803314209, 23.318300247192383, 23.625120162963867, 23.93194007873535, 24.238759994506836, 24.54557991027832, 24.852399826049805, 25.159217834472656, 25.46603775024414, 25.772857666015625, 26.07967758178711, 26.386497497558594, 26.693317413330078, 27.000137329101562, 27.306957244873047, 27.61377716064453, 27.920597076416016, 28.2274169921875, 28.53423500061035, 28.841054916381836, 29.14787483215332, 29.454694747924805, 29.76151466369629, 30.068334579467773, 30.375154495239258, 30.681974411010742, 30.988794326782227, 31.29561424255371, 31.602432250976562, 31.909252166748047, 32.21607208251953, 32.522891998291016, 32.8297119140625, 33.136531829833984, 33.44335174560547, 33.75017166137695, 34.05699157714844, 34.36381149291992, 34.670631408691406, 34.97745132446289, 35.284271240234375, 35.59109115600586, 35.897911071777344, 36.20473098754883, 36.51155090332031, 36.81836700439453, 37.125186920166016, 37.4320068359375, 37.738826751708984, 38.04564666748047, 38.35246658325195, 38.65928649902344, 38.96610641479492, 39.272926330566406, 39.57974624633789, 39.886566162109375, 40.19338607788086, 40.500205993652344, 40.80702590942383, 41.11384582519531, 41.4206657409668, 41.72748565673828, 42.034305572509766, 42.34112548828125, 42.647945404052734, 42.95476531982422, 43.26158142089844], "21": [6.716559886932373, 7.021858215332031, 7.327156066894531, 7.6324543952941895, 7.937752723693848, 8.243050575256348, 8.548349380493164, 8.853647232055664, 9.158945083618164, 9.46424388885498, 9.76954174041748, 10.07483959197998, 10.380138397216797, 10.685436248779297, 10.990734100341797, 11.296032905578613, 11.601330757141113, 11.906628608703613, 12.21192741394043, 12.51722526550293, 12.82252311706543, 13.127821922302246, 13.433119773864746, 13.738417625427246, 14.043716430664062, 14.349014282226562, 14.654312133789062, 14.959610939025879, 15.264908790588379, 15.570206642150879, 15.875505447387695, 16.180803298950195, 16.486101150512695, 16.791399002075195, 17.096698760986328, 17.401996612548828, 17.707294464111328, 18.012592315673828, 18.317890167236328, 18.623188018798828, 18.92848777770996, 19.23378562927246, 19.53908348083496, 19.84438133239746, 20.14967918395996, 20.45497703552246, 20.760276794433594, 21.065574645996094, 21.370872497558594, 21.676170349121094, 21.981468200683594, 22.286766052246094, 22.592065811157227, 22.897363662719727, 23.202661514282227, 23.507959365844727, 23.813257217407227, 24.118555068969727, 24.42385482788086, 24.72915267944336, 25.03445053100586, 25.33974838256836, 25.64504623413086, 25.950345993041992, 26.255643844604492, 26.560941696166992, 26.866239547729492, 27.171537399291992, 27.476835250854492, 27.782135009765625, 28.087432861328125, 28.392730712890625, 28.698028564453125, 29.003326416015625, 29.308624267578125, 29.613924026489258, 29.919221878051758, 30.224519729614258, 30.529817581176758, 30.835115432739258, 31.140413284301758, 31.44571304321289, 31.75101089477539, 32.05630874633789, 32.36160659790039, 32.66690444946289, 32.97220230102539, 33.27750015258789, 33.58279800415039, 33.88809585571289, 34.193397521972656, 34.498695373535156, 34.803993225097656, 35.109291076660156, 35.414588928222656, 35.719886779785156, 36.025184631347656, 36.330482482910156, 36.635780334472656, 36.941078186035156, 37.246376037597656, 37.55167770385742, 37.85697555541992, 38.16227340698242, 38.46757125854492, 38.77286911010742, 39.07816696166992, 39.38346481323242, 39.68876266479492, 39.99406051635742, 40.29935836791992, 40.60465621948242, 40.90995407104492, 41.21525573730469, 41.52055358886719, 41.82585144042969, 42.13114929199219, 42.43644714355469, 42.74174499511719, 43.04704284667969], "22": [6.683441162109375, 6.987234115600586, 7.291027069091797, 7.59481954574585, 7.8986124992370605, 8.202404975891113, 8.506197929382324, 8.809990882873535, 9.113783836364746, 9.417576789855957, 9.721368789672852, 10.025161743164062, 10.328954696655273, 10.632747650146484, 10.936540603637695, 11.240333557128906, 11.5441255569458, 11.847918510437012, 12.151711463928223, 12.455504417419434, 12.759297370910645, 13.063089370727539, 13.36688232421875, 13.670675277709961, 13.974468231201172, 14.278261184692383, 14.582054138183594, 14.885846138000488, 15.1896390914917, 15.49343204498291, 15.797224998474121, 16.101016998291016, 16.404809951782227, 16.708602905273438, 17.01239585876465, 17.31618881225586, 17.61998176574707, 17.92377471923828, 18.227567672729492, 18.531360626220703, 18.835153579711914, 19.138944625854492, 19.442737579345703, 19.746530532836914, 20.050323486328125, 20.354116439819336, 20.657909393310547, 20.961702346801758, 21.26549530029297, 21.56928825378418, 21.87308120727539, 22.1768741607666, 22.480667114257812, 22.78445816040039, 23.0882511138916, 23.392044067382812, 23.695837020874023, 23.999629974365234, 24.303422927856445, 24.607215881347656, 24.911008834838867, 25.214801788330078, 25.51859474182129, 25.8223876953125, 26.126178741455078, 26.42997169494629, 26.7337646484375, 27.03755760192871, 27.341350555419922, 27.645143508911133, 27.948936462402344, 28.252729415893555, 28.556522369384766, 28.860315322875977, 29.164108276367188, 29.4679012298584, 29.771692276000977, 30.075485229492188, 30.3792781829834, 30.68307113647461, 30.98686408996582, 31.29065704345703, 31.594449996948242, 31.898242950439453, 32.20203399658203, 32.505828857421875, 32.80961990356445, 33.1134147644043, 33.417205810546875, 33.72100067138672, 34.0247917175293, 34.32858657836914, 34.63237762451172, 34.9361686706543, 35.23996353149414, 35.54375457763672, 35.84754943847656, 36.15134048461914, 36.455135345458984, 36.75892639160156, 37.062721252441406, 37.366512298583984, 37.67030715942383, 37.974098205566406, 38.277889251708984, 38.58168411254883, 38.885475158691406, 39.18927001953125, 39.49306106567383, 39.79685592651367, 40.10064697265625, 40.404441833496094, 40.70823287963867, 41.012027740478516, 41.315818786621094, 41.61961364746094, 41.923404693603516, 42.227195739746094, 42.53099060058594, 42.834781646728516], "23": [6.650672912597656, 6.952976226806641, 7.255279541015625, 7.557582855224609, 7.859886169433594, 8.162189483642578, 8.464492797851562, 8.766796112060547, 9.069099426269531, 9.371402740478516, 9.6737060546875, 9.976009368896484, 10.278312683105469, 10.580615997314453, 10.882919311523438, 11.185222625732422, 11.487525939941406, 11.78982925415039, 12.092132568359375, 12.39443588256836, 12.696739196777344, 12.999042510986328, 13.301345825195312, 13.603649139404297, 13.905952453613281, 14.208255767822266, 14.51055908203125, 14.812862396240234, 15.115165710449219, 15.417469024658203, 15.719772338867188, 16.022075653076172, 16.324378967285156, 16.62668228149414, 16.928985595703125, 17.23128890991211, 17.533592224121094, 17.835895538330078, 18.138198852539062, 18.440502166748047, 18.74280548095703, 19.045108795166016, 19.347412109375, 19.649715423583984, 19.95201873779297, 20.254322052001953, 20.556625366210938, 20.858928680419922, 21.161231994628906, 21.46353530883789, 21.765838623046875, 22.06814193725586, 22.370445251464844, 22.672748565673828, 22.975051879882812, 23.277355194091797, 23.57965850830078, 23.881961822509766, 24.18426513671875, 24.486568450927734, 24.78887176513672, 25.091175079345703, 25.393478393554688, 25.695781707763672, 25.998085021972656, 26.30038833618164, 26.602691650390625, 26.90499496459961, 27.207298278808594, 27.509601593017578, 27.811904907226562, 28.114208221435547, 28.41651153564453, 28.718814849853516, 29.0211181640625, 29.323421478271484, 29.62572479248047, 29.928028106689453, 30.230331420898438, 30.532634735107422, 30.834938049316406, 31.13724136352539, 31.439544677734375, 31.74184799194336, 32.044151306152344, 32.34645462036133, 32.64875793457031, 32.9510612487793, 33.25336456298828, 33.555667877197266, 33.85797119140625, 34.160274505615234, 34.46257781982422, 34.7648811340332, 35.06718444824219, 35.36948776245117, 35.671791076660156, 35.97409439086914, 36.276397705078125, 36.57870101928711, 36.881004333496094, 37.18330764770508, 37.48561096191406, 37.78791427612305, 38.09021759033203, 38.392520904541016, 38.69482421875, 38.997127532958984, 39.29943084716797, 39.60173416137695, 39.90403747558594, 40.20634078979492, 40.508644104003906, 40.81094741821289, 41.113250732421875, 41.41555404663086, 41.717857360839844, 42.02016067504883, 42.32246398925781, 42.6247673034668], "24": [6.618249893188477, 6.919079303741455, 7.219908714294434, 7.520738124847412, 7.821568012237549, 8.122397422790527, 8.423227310180664, 8.724056243896484, 9.024886131286621, 9.325715065002441, 9.626544952392578, 9.927374839782715, 10.228203773498535, 10.529033660888672, 10.829863548278809, 11.130692481994629, 11.431522369384766, 11.732351303100586, 12.033181190490723, 12.33401107788086, 12.63484001159668, 12.935669898986816, 13.236499786376953, 13.537328720092773, 13.83815860748291, 14.13898754119873, 14.439817428588867, 14.740647315979004, 15.041476249694824, 15.342306137084961, 15.643136024475098, 15.943964958190918, 16.244794845581055, 16.545623779296875, 16.846454620361328, 17.14728355407715, 17.44811248779297, 17.74894142150879, 18.049772262573242, 18.350601196289062, 18.651430130004883, 18.952260971069336, 19.253089904785156, 19.553918838500977, 19.85474967956543, 20.15557861328125, 20.45640754699707, 20.757238388061523, 21.058067321777344, 21.358896255493164, 21.659727096557617, 21.960556030273438, 22.261384963989258, 22.562213897705078, 22.86304473876953, 23.16387367248535, 23.464702606201172, 23.765533447265625, 24.066362380981445, 24.367191314697266, 24.66802215576172, 24.96885108947754, 25.26968002319336, 25.570510864257812, 25.871339797973633, 26.172168731689453, 26.472999572753906, 26.773828506469727, 27.074657440185547, 27.375486373901367, 27.67631721496582, 27.97714614868164, 28.27797508239746, 28.578805923461914, 28.879634857177734, 29.180463790893555, 29.481294631958008, 29.782123565673828, 30.08295249938965, 30.3837833404541, 30.684612274169922, 30.985441207885742, 31.286272048950195, 31.587100982666016, 31.887929916381836, 32.188758850097656, 32.48958969116211, 32.79042053222656, 33.09124755859375, 33.3920783996582, 33.692909240722656, 33.993736267089844, 34.2945671081543, 34.595394134521484, 34.89622497558594, 35.19705581665039, 35.49788284301758, 35.79871368408203, 36.099544525146484, 36.40037155151367, 36.701202392578125, 37.00203323364258, 37.302860260009766, 37.60369110107422, 37.90452194213867, 38.20534896850586, 38.50617980957031, 38.807010650634766, 39.10783767700195, 39.408668518066406, 39.70949935913086, 40.01032638549805, 40.3111572265625, 40.61198806762695, 40.91281509399414, 41.213645935058594, 41.51447677612305, 41.815303802490234, 42.11613464355469, 42.41696548461914], "25": [6.586165904998779, 6.885537147521973, 7.184908390045166, 7.484279632568359, 7.783650875091553, 8.083022117614746, 8.382392883300781, 8.681764602661133, 8.981135368347168, 9.280506134033203, 9.579877853393555, 9.87924861907959, 10.178620338439941, 10.477991104125977, 10.777362823486328, 11.076733589172363, 11.376104354858398, 11.67547607421875, 11.974846839904785, 12.274218559265137, 12.573589324951172, 12.872961044311523, 13.172331809997559, 13.47170352935791, 13.771074295043945, 14.07044506072998, 14.369816780090332, 14.669187545776367, 14.968559265136719, 15.267930030822754, 15.567301750183105, 15.86667251586914, 16.166044235229492, 16.46541404724121, 16.764785766601562, 17.064157485961914, 17.363529205322266, 17.662899017333984, 17.962270736694336, 18.261642456054688, 18.561012268066406, 18.860383987426758, 19.15975570678711, 19.45912742614746, 19.75849723815918, 20.05786895751953, 20.357240676879883, 20.6566104888916, 20.955982208251953, 21.255353927612305, 21.554725646972656, 21.854095458984375, 22.153467178344727, 22.452838897705078, 22.752208709716797, 23.05158042907715, 23.3509521484375, 23.65032386779785, 23.94969367980957, 24.249065399169922, 24.548437118530273, 24.847808837890625, 25.147178649902344, 25.446550369262695, 25.745922088623047, 26.045291900634766, 26.344663619995117, 26.64403533935547, 26.94340705871582, 27.24277687072754, 27.54214859008789, 27.841520309448242, 28.14089012145996, 28.440261840820312, 28.739633560180664, 29.039005279541016, 29.338375091552734, 29.637746810913086, 29.937118530273438, 30.236488342285156, 30.535860061645508, 30.83523178100586, 31.13460350036621, 31.43397331237793, 31.73334503173828, 32.03271484375, 32.332088470458984, 32.6314582824707, 32.93082809448242, 33.230201721191406, 33.529571533203125, 33.82894515991211, 34.12831497192383, 34.42768478393555, 34.72705841064453, 35.02642822265625, 35.32579803466797, 35.62517166137695, 35.92454147338867, 36.22391128540039, 36.523284912109375, 36.822654724121094, 37.12202453613281, 37.4213981628418, 37.720767974853516, 38.0201416015625, 38.31951141357422, 38.61888122558594, 38.91825485229492, 39.21762466430664, 39.51699447631836, 39.816368103027344, 40.11573791503906, 40.41510772705078, 40.714481353759766, 41.013851165771484, 41.3132209777832, 41.61259460449219, 41.911964416503906, 42.21133804321289], "26": [6.554416656494141, 6.852344989776611, 7.150272846221924, 7.448200702667236, 7.746129035949707, 8.04405689239502, 8.341984748840332, 8.639912605285645, 8.937841415405273, 9.235769271850586, 9.533697128295898, 9.831624984741211, 10.129552841186523, 10.427481651306152, 10.725409507751465, 11.023337364196777, 11.32126522064209, 11.619193077087402, 11.917120933532715, 12.215049743652344, 12.512977600097656, 12.810905456542969, 13.108833312988281, 13.406761169433594, 13.704689979553223, 14.002617835998535, 14.300545692443848, 14.59847354888916, 14.896401405334473, 15.194329261779785, 15.492258071899414, 15.790185928344727, 16.08811378479004, 16.38604164123535, 16.683969497680664, 16.981897354125977, 17.27982521057129, 17.5777530670166, 17.875682830810547, 18.17361068725586, 18.471538543701172, 18.769466400146484, 19.067394256591797, 19.36532211303711, 19.663249969482422, 19.961177825927734, 20.259105682373047, 20.55703353881836, 20.854963302612305, 21.152891159057617, 21.45081901550293, 21.748746871948242, 22.046674728393555, 22.344602584838867, 22.64253044128418, 22.940458297729492, 23.238386154174805, 23.536314010620117, 23.83424186706543, 24.132171630859375, 24.430099487304688, 24.72802734375, 25.025955200195312, 25.323883056640625, 25.621810913085938, 25.91973876953125, 26.217666625976562, 26.515594482421875, 26.813522338867188, 27.1114501953125, 27.409379959106445, 27.707307815551758, 28.00523567199707, 28.303163528442383, 28.601091384887695, 28.899019241333008, 29.19694709777832, 29.494874954223633, 29.792802810668945, 30.090730667114258, 30.38865852355957, 30.686588287353516, 30.984516143798828, 31.28244400024414, 31.580371856689453, 31.878299713134766, 32.17622756958008, 32.47415542602539, 32.7720832824707, 33.070011138916016, 33.36793899536133, 33.66586685180664, 33.96379470825195, 34.261722564697266, 34.55965042114258, 34.85757827758789, 35.1555061340332, 35.45343780517578, 35.751365661621094, 36.049293518066406, 36.34722137451172, 36.64514923095703, 36.943077087402344, 37.241004943847656, 37.53893280029297, 37.83686065673828, 38.134788513183594, 38.432716369628906, 38.73064422607422, 39.02857208251953, 39.326499938964844, 39.624427795410156, 39.92235565185547, 40.22028350830078, 40.518211364746094, 40.816139221191406, 41.11406707763672, 41.41199493408203, 41.70992660522461, 42.00785446166992], "27": [6.52299690246582, 6.8194966316223145, 7.115996837615967, 7.412496566772461, 7.708996295928955, 8.00549602508545, 8.301996231079102, 8.598496437072754, 8.89499568939209, 9.191495895385742, 9.487995147705078, 9.78449535369873, 10.080995559692383, 10.377494812011719, 10.673995018005371, 10.970495223999023, 11.26699447631836, 11.563494682312012, 11.859994888305664, 12.156494140625, 12.452994346618652, 12.749494552612305, 13.04599380493164, 13.342494010925293, 13.638993263244629, 13.935493469238281, 14.231993675231934, 14.52849292755127, 14.824993133544922, 15.121493339538574, 15.41799259185791, 15.714492797851562, 16.0109920501709, 16.307493209838867, 16.603992462158203, 16.90049171447754, 17.196992874145508, 17.493492126464844, 17.78999137878418, 18.08649253845215, 18.382991790771484, 18.67949104309082, 18.975990295410156, 19.272491455078125, 19.56899070739746, 19.865489959716797, 20.161991119384766, 20.4584903717041, 20.754989624023438, 21.051490783691406, 21.347990036010742, 21.644489288330078, 21.940990447998047, 22.237489700317383, 22.53398895263672, 22.830490112304688, 23.126989364624023, 23.42348861694336, 23.719989776611328, 24.016489028930664, 24.31298828125, 24.60948944091797, 24.905988693237305, 25.20248794555664, 25.49898910522461, 25.795488357543945, 26.09198760986328, 26.388486862182617, 26.684988021850586, 26.981487274169922, 27.277986526489258, 27.574487686157227, 27.870986938476562, 28.1674861907959, 28.463987350463867, 28.760486602783203, 29.05698585510254, 29.353487014770508, 29.649986267089844, 29.94648551940918, 30.24298667907715, 30.539485931396484, 30.83598518371582, 31.13248634338379, 31.428985595703125, 31.72548484802246, 32.0219841003418, 32.318485260009766, 32.614986419677734, 32.91148376464844, 33.207984924316406, 33.504486083984375, 33.80098342895508, 34.09748458862305, 34.393985748291016, 34.69048309326172, 34.98698425292969, 35.283485412597656, 35.57998275756836, 35.87648391723633, 36.1729850769043, 36.469482421875, 36.76598358154297, 37.06248474121094, 37.35898208618164, 37.65548324584961, 37.95198059082031, 38.24848175048828, 38.54498291015625, 38.84148025512695, 39.13798141479492, 39.43448257446289, 39.730979919433594, 40.02748107910156, 40.32398223876953, 40.620479583740234, 40.9169807434082, 41.21348190307617, 41.509979248046875, 41.806480407714844], "28": [6.491901874542236, 6.786988258361816, 7.0820746421813965, 7.377161026000977, 7.672247409820557, 7.967333793640137, 8.262420654296875, 8.557506561279297, 8.852593421936035, 9.147679328918457, 9.442766189575195, 9.737852096557617, 10.032938957214355, 10.328025817871094, 10.623111724853516, 10.918198585510254, 11.213284492492676, 11.508371353149414, 11.803457260131836, 12.098544120788574, 12.393630981445312, 12.688716888427734, 12.983803749084473, 13.278889656066895, 13.573976516723633, 13.869062423706055, 14.164149284362793, 14.459235191345215, 14.754322052001953, 15.049408912658691, 15.344494819641113, 15.639581680297852, 15.934667587280273, 16.229753494262695, 16.52484130859375, 16.819927215576172, 17.115013122558594, 17.41010093688965, 17.70518684387207, 18.000272750854492, 18.295358657836914, 18.59044647216797, 18.88553237915039, 19.180618286132812, 19.475704193115234, 19.77079200744629, 20.06587791442871, 20.360963821411133, 20.656051635742188, 20.95113754272461, 21.24622344970703, 21.541309356689453, 21.836397171020508, 22.13148307800293, 22.42656898498535, 22.721656799316406, 23.016742706298828, 23.31182861328125, 23.606914520263672, 23.902002334594727, 24.19708824157715, 24.49217414855957, 24.787261962890625, 25.082347869873047, 25.37743377685547, 25.67251968383789, 25.967607498168945, 26.262693405151367, 26.55777931213379, 26.852867126464844, 27.147953033447266, 27.443038940429688, 27.73812484741211, 28.033212661743164, 28.328298568725586, 28.623384475708008, 28.91847038269043, 29.213558197021484, 29.508644104003906, 29.803730010986328, 30.098817825317383, 30.393903732299805, 30.688989639282227, 30.98407554626465, 31.279163360595703, 31.574249267578125, 31.869335174560547, 32.16442108154297, 32.45950698852539, 32.75459671020508, 33.0496826171875, 33.34476852416992, 33.639854431152344, 33.934940338134766, 34.23002624511719, 34.52511215209961, 34.8202018737793, 35.11528778076172, 35.41037368774414, 35.70545959472656, 36.000545501708984, 36.295631408691406, 36.59071731567383, 36.885807037353516, 37.18089294433594, 37.47597885131836, 37.77106475830078, 38.0661506652832, 38.361236572265625, 38.65632247924805, 38.95140838623047, 39.246498107910156, 39.54158401489258, 39.836669921875, 40.13175582885742, 40.426841735839844, 40.721927642822266, 41.01701354980469, 41.312103271484375, 41.6071891784668], "29": [6.46112585067749, 6.7548136711120605, 7.048501014709473, 7.342188835144043, 7.635876178741455, 7.929563999176025, 8.223251342773438, 8.516939163208008, 8.810626029968262, 9.104313850402832, 9.398001670837402, 9.691689491271973, 9.985376358032227, 10.279064178466797, 10.572751998901367, 10.866438865661621, 11.160126686096191, 11.453814506530762, 11.747502326965332, 12.041189193725586, 12.334877014160156, 12.628564834594727, 12.92225170135498, 13.21593952178955, 13.509627342224121, 13.803315162658691, 14.097002029418945, 14.390689849853516, 14.684377670288086, 14.97806453704834, 15.27175235748291, 15.56544017791748, 15.85912799835205, 16.152814865112305, 16.446502685546875, 16.740190505981445, 17.033878326416016, 17.327566146850586, 17.621252059936523, 17.914939880371094, 18.208627700805664, 18.502315521240234, 18.796003341674805, 19.089691162109375, 19.383378982543945, 19.677064895629883, 19.970752716064453, 20.264440536499023, 20.558128356933594, 20.851816177368164, 21.145503997802734, 21.439191818237305, 21.732877731323242, 22.026565551757812, 22.320253372192383, 22.613941192626953, 22.907629013061523, 23.201316833496094, 23.495004653930664, 23.7886905670166, 24.082378387451172, 24.376066207885742, 24.669754028320312, 24.963441848754883, 25.257129669189453, 25.550817489624023, 25.84450340270996, 26.13819122314453, 26.4318790435791, 26.725566864013672, 27.019254684448242, 27.312942504882812, 27.606630325317383, 27.90031623840332, 28.19400405883789, 28.48769187927246, 28.78137969970703, 29.0750675201416, 29.368755340576172, 29.662443161010742, 29.95612907409668, 30.24981689453125, 30.54350471496582, 30.83719253540039, 31.13088035583496, 31.42456817626953, 31.7182559967041, 32.01194381713867, 32.30562973022461, 32.59931945800781, 32.89300537109375, 33.18669128417969, 33.48038101196289, 33.77406692504883, 34.06775665283203, 34.36144256591797, 34.65513229370117, 34.94881820678711, 35.24250411987305, 35.53619384765625, 35.82987976074219, 36.12356948852539, 36.41725540161133, 36.71094512939453, 37.00463104248047, 37.298316955566406, 37.59200668334961, 37.88569259643555, 38.17938232421875, 38.47306823730469, 38.76675796508789, 39.06044387817383, 39.354129791259766, 39.64781951904297, 39.941505432128906, 40.23519515991211, 40.52888107299805, 40.82257080078125, 41.11625671386719, 41.409942626953125], "30": [6.430665493011475, 6.722968101501465, 7.015271186828613, 7.307574272155762, 7.59987735748291, 7.8921799659729, 8.184483528137207, 8.476785659790039, 8.769088745117188, 9.061391830444336, 9.353694915771484, 9.645998001098633, 9.938301086425781, 10.23060417175293, 10.522907257080078, 10.815210342407227, 11.107512474060059, 11.399815559387207, 11.692118644714355, 11.984421730041504, 12.276724815368652, 12.5690279006958, 12.86133098602295, 13.153634071350098, 13.44593620300293, 13.738239288330078, 14.030542373657227, 14.322845458984375, 14.615148544311523, 14.907451629638672, 15.19975471496582, 15.492057800292969, 15.7843599319458, 16.076663970947266, 16.368967056274414, 16.661270141601562, 16.953571319580078, 17.245874404907227, 17.538177490234375, 17.830480575561523, 18.122783660888672, 18.41508674621582, 18.70738983154297, 18.999692916870117, 19.291996002197266, 19.584299087524414, 19.876602172851562, 20.16890525817871, 20.46120834350586, 20.753511428833008, 21.045814514160156, 21.338117599487305, 21.630420684814453, 21.92272186279297, 22.215024948120117, 22.507328033447266, 22.799631118774414, 23.091934204101562, 23.38423728942871, 23.67654037475586, 23.968843460083008, 24.261146545410156, 24.553449630737305, 24.845752716064453, 25.1380558013916, 25.43035888671875, 25.7226619720459, 26.014965057373047, 26.307268142700195, 26.59956932067871, 26.89187240600586, 27.184175491333008, 27.476478576660156, 27.768781661987305, 28.061084747314453, 28.3533878326416, 28.64569091796875, 28.9379940032959, 29.230297088623047, 29.522600173950195, 29.814903259277344, 30.107206344604492, 30.39950942993164, 30.69181251525879, 30.984115600585938, 31.276418685913086, 31.5687198638916, 31.86102294921875, 32.15332794189453, 32.44562911987305, 32.73793411254883, 33.030235290527344, 33.322540283203125, 33.61484146118164, 33.907142639160156, 34.19944763183594, 34.49174880981445, 34.784053802490234, 35.07635498046875, 35.36865997314453, 35.66096115112305, 35.95326614379883, 36.245567321777344, 36.537872314453125, 36.83017349243164, 37.12247848510742, 37.41477966308594, 37.70708465576172, 37.999385833740234, 38.291690826416016, 38.58399200439453, 38.87629318237305, 39.16859817504883, 39.460899353027344, 39.753204345703125, 40.04550552368164, 40.33781051635742, 40.63011169433594, 40.92241668701172, 41.214717864990234], "31": [6.400514602661133, 6.6914472579956055, 6.982379913330078, 7.273312091827393, 7.564244747161865, 7.855177402496338, 8.146109580993652, 8.437042236328125, 8.727974891662598, 9.01890754699707, 9.309839248657227, 9.6007719039917, 9.891704559326172, 10.182637214660645, 10.473569869995117, 10.76450252532959, 11.055434226989746, 11.346366882324219, 11.637299537658691, 11.928232192993164, 12.219164848327637, 12.51009750366211, 12.801029205322266, 13.091961860656738, 13.382894515991211, 13.673827171325684, 13.964759826660156, 14.255692481994629, 14.546624183654785, 14.837556838989258, 15.12848949432373, 15.419422149658203, 15.710354804992676, 16.00128746032715, 16.292219161987305, 16.583152770996094, 16.87408447265625, 17.165016174316406, 17.455949783325195, 17.74688148498535, 18.03781509399414, 18.328746795654297, 18.619678497314453, 18.910612106323242, 19.2015438079834, 19.492477416992188, 19.783409118652344, 20.074342727661133, 20.36527442932129, 20.656206130981445, 20.947139739990234, 21.23807144165039, 21.52900505065918, 21.819936752319336, 22.110868453979492, 22.40180206298828, 22.692733764648438, 22.983667373657227, 23.274599075317383, 23.565532684326172, 23.856464385986328, 24.147396087646484, 24.438329696655273, 24.72926139831543, 25.02019500732422, 25.311126708984375, 25.60205841064453, 25.89299201965332, 26.183923721313477, 26.474857330322266, 26.765789031982422, 27.056720733642578, 27.347654342651367, 27.638586044311523, 27.929519653320312, 28.22045135498047, 28.511384963989258, 28.802316665649414, 29.09324836730957, 29.38418197631836, 29.675113677978516, 29.966047286987305, 30.25697898864746, 30.547910690307617, 30.838844299316406, 31.129776000976562, 31.42070960998535, 31.711641311645508, 32.0025749206543, 32.29350662231445, 32.58443832397461, 32.875370025634766, 33.16630554199219, 33.457237243652344, 33.7481689453125, 34.039100646972656, 34.33003234863281, 34.620967864990234, 34.91189956665039, 35.20283126831055, 35.4937629699707, 35.78469467163086, 36.07563018798828, 36.36656188964844, 36.657493591308594, 36.94842529296875, 37.239356994628906, 37.53029251098633, 37.821224212646484, 38.11215591430664, 38.4030876159668, 38.69402313232422, 38.984954833984375, 39.27588653564453, 39.56681823730469, 39.857749938964844, 40.148685455322266, 40.43961715698242, 40.73054885864258, 41.021480560302734], "32": [6.370669841766357, 6.660245895385742, 6.949821949005127, 7.2393975257873535, 7.528973579406738, 7.818549633026123, 8.108125686645508, 8.397701263427734, 8.687276840209961, 8.976853370666504, 9.26642894744873, 9.556004524230957, 9.8455810546875, 10.135156631469727, 10.424732208251953, 10.714308738708496, 11.003884315490723, 11.29345989227295, 11.583036422729492, 11.872611999511719, 12.162187576293945, 12.451764106750488, 12.741339683532715, 13.030915260314941, 13.320491790771484, 13.610067367553711, 13.899643898010254, 14.18921947479248, 14.478795051574707, 14.76837158203125, 15.057947158813477, 15.347522735595703, 15.637099266052246, 15.926674842834473, 16.216251373291016, 16.505826950073242, 16.79540252685547, 17.084978103637695, 17.374553680419922, 17.66412925720215, 17.953706741333008, 18.243282318115234, 18.53285789489746, 18.822433471679688, 19.112009048461914, 19.401586532592773, 19.691162109375, 19.980737686157227, 20.270313262939453, 20.55988883972168, 20.849464416503906, 21.139041900634766, 21.428617477416992, 21.71819305419922, 22.007768630981445, 22.297344207763672, 22.5869197845459, 22.876497268676758, 23.166072845458984, 23.45564842224121, 23.745223999023438, 24.034799575805664, 24.32437515258789, 24.61395263671875, 24.903528213500977, 25.193103790283203, 25.48267936706543, 25.772254943847656, 26.061830520629883, 26.351408004760742, 26.64098358154297, 26.930559158325195, 27.220134735107422, 27.50971031188965, 27.799287796020508, 28.088863372802734, 28.37843894958496, 28.668014526367188, 28.957590103149414, 29.24716567993164, 29.5367431640625, 29.826318740844727, 30.115894317626953, 30.40546989440918, 30.695045471191406, 30.984621047973633, 31.274198532104492, 31.56377410888672, 31.853349685668945, 32.14292526245117, 32.43250274658203, 32.722076416015625, 33.011653900146484, 33.30122756958008, 33.59080505371094, 33.8803825378418, 34.16995620727539, 34.45953369140625, 34.749107360839844, 35.0386848449707, 35.3282585144043, 35.617835998535156, 35.907413482666016, 36.19698715209961, 36.48656463623047, 36.77613830566406, 37.06571578979492, 37.35529327392578, 37.644866943359375, 37.934444427490234, 38.22401809692383, 38.51359558105469, 38.80317306518555, 39.09274673461914, 39.38232421875, 39.671897888183594, 39.96147537231445, 40.25104904174805, 40.540626525878906, 40.830204010009766], "33": [6.341125965118408, 6.629359245300293, 6.9175920486450195, 7.205825328826904, 7.494058132171631, 7.782291412353516, 8.070524215698242, 8.358757019042969, 8.646989822387695, 8.935223579406738, 9.223456382751465, 9.511689186096191, 9.799921989440918, 10.088155746459961, 10.376388549804688, 10.664621353149414, 10.95285415649414, 11.241086959838867, 11.52932071685791, 11.817553520202637, 12.105786323547363, 12.39401912689209, 12.682251930236816, 12.97048568725586, 13.258718490600586, 13.546951293945312, 13.835184097290039, 14.123417854309082, 14.411650657653809, 14.699883460998535, 14.988116264343262, 15.276349067687988, 15.564582824707031, 15.852815628051758, 16.141048431396484, 16.42928123474121, 16.717514038085938, 17.005746841430664, 17.29397964477539, 17.58221435546875, 17.870447158813477, 18.158679962158203, 18.44691276550293, 18.735145568847656, 19.023378372192383, 19.31161117553711, 19.599843978881836, 19.888076782226562, 20.176311492919922, 20.46454429626465, 20.752777099609375, 21.0410099029541, 21.329242706298828, 21.617475509643555, 21.90570831298828, 22.193941116333008, 22.482173919677734, 22.77040672302246, 23.05864143371582, 23.346874237060547, 23.635107040405273, 23.92333984375, 24.211572647094727, 24.499805450439453, 24.78803825378418, 25.076271057128906, 25.364503860473633, 25.652738571166992, 25.94097137451172, 26.229204177856445, 26.517436981201172, 26.8056697845459, 27.093902587890625, 27.38213539123535, 27.670368194580078, 27.958600997924805, 28.246835708618164, 28.53506851196289, 28.823301315307617, 29.111534118652344, 29.39976692199707, 29.687999725341797, 29.976232528686523, 30.26446533203125, 30.552698135375977, 30.840930938720703, 31.129165649414062, 31.41739845275879, 31.705631256103516, 31.993864059448242, 32.28209686279297, 32.57033157348633, 32.85856246948242, 33.14679718017578, 33.435028076171875, 33.723262786865234, 34.01149368286133, 34.29972839355469, 34.58795928955078, 34.87619400024414, 35.1644287109375, 35.452659606933594, 35.74089431762695, 36.02912521362305, 36.317359924316406, 36.6055908203125, 36.89382553100586, 37.18205642700195, 37.47029113769531, 37.75852584838867, 38.046756744384766, 38.334991455078125, 38.62322235107422, 38.91145706176758, 39.19968795776367, 39.48792266845703, 39.776153564453125, 40.064388275146484, 40.352622985839844, 40.64085388183594], "34": [6.3118791580200195, 6.598783016204834, 6.88568639755249, 7.172590255737305, 7.459493637084961, 7.746397018432617, 8.033300399780273, 8.320204734802246, 8.607108116149902, 8.894011497497559, 9.180914878845215, 9.467819213867188, 9.754722595214844, 10.0416259765625, 10.328529357910156, 10.615433692932129, 10.902337074279785, 11.189240455627441, 11.476143836975098, 11.763047218322754, 12.049951553344727, 12.336854934692383, 12.623758316040039, 12.910661697387695, 13.197566032409668, 13.484469413757324, 13.77137279510498, 14.058276176452637, 14.34518051147461, 14.632083892822266, 14.918987274169922, 15.205890655517578, 15.492794036865234, 15.779698371887207, 16.066600799560547, 16.353506088256836, 16.640409469604492, 16.92731285095215, 17.214216232299805, 17.50111961364746, 17.788022994995117, 18.074926376342773, 18.36182975769043, 18.648733139038086, 18.935638427734375, 19.22254180908203, 19.509445190429688, 19.796348571777344, 20.083251953125, 20.370155334472656, 20.657058715820312, 20.94396209716797, 21.230867385864258, 21.517770767211914, 21.80467414855957, 22.091577529907227, 22.378480911254883, 22.66538429260254, 22.952287673950195, 23.23919105529785, 23.526094436645508, 23.812999725341797, 24.099903106689453, 24.38680648803711, 24.673709869384766, 24.960613250732422, 25.247516632080078, 25.534420013427734, 25.82132339477539, 26.108226776123047, 26.395132064819336, 26.682035446166992, 26.96893882751465, 27.255842208862305, 27.54274559020996, 27.829648971557617, 28.116552352905273, 28.40345573425293, 28.69036102294922, 28.977264404296875, 29.26416778564453, 29.551071166992188, 29.837974548339844, 30.1248779296875, 30.411781311035156, 30.698684692382812, 30.98558807373047, 31.272493362426758, 31.559396743774414, 31.84630012512207, 32.133201599121094, 32.420108795166016, 32.70701217651367, 32.99391555786133, 33.280818939208984, 33.56772232055664, 33.8546257019043, 34.14152908325195, 34.42843246459961, 34.715335845947266, 35.00223922729492, 35.28914260864258, 35.576045989990234, 35.86294937133789, 36.14985275268555, 36.4367561340332, 36.72365951538086, 37.010562896728516, 37.29746627807617, 37.584373474121094, 37.87127685546875, 38.158180236816406, 38.44508361816406, 38.73198699951172, 39.018890380859375, 39.30579376220703, 39.59269714355469, 39.879600524902344, 40.16650390625, 40.453407287597656], "35": [6.282924652099609, 6.568512439727783, 6.854099750518799, 7.1396870613098145, 7.425274848937988, 7.710862159729004, 7.9964494705200195, 8.282036781311035, 8.567625045776367, 8.853212356567383, 9.138799667358398, 9.424386978149414, 9.70997428894043, 9.995561599731445, 10.281149864196777, 10.566737174987793, 10.852324485778809, 11.137911796569824, 11.42349910736084, 11.709087371826172, 11.994674682617188, 12.280261993408203, 12.565849304199219, 12.851436614990234, 13.137024879455566, 13.422612190246582, 13.708199501037598, 13.993786811828613, 14.279374122619629, 14.564961433410645, 14.850549697875977, 15.136137008666992, 15.421724319458008, 15.707311630249023, 15.992898941040039, 16.278486251831055, 16.56407356262207, 16.849660873413086, 17.135250091552734, 17.42083740234375, 17.706424713134766, 17.99201202392578, 18.277599334716797, 18.563186645507812, 18.848773956298828, 19.134361267089844, 19.41994857788086, 19.705535888671875, 19.99112319946289, 20.27671241760254, 20.562299728393555, 20.84788703918457, 21.133474349975586, 21.4190616607666, 21.704648971557617, 21.990236282348633, 22.27582359313965, 22.561410903930664, 22.84699821472168, 23.132585525512695, 23.418174743652344, 23.70376205444336, 23.989349365234375, 24.27493667602539, 24.560523986816406, 24.846111297607422, 25.131698608398438, 25.417285919189453, 25.70287322998047, 25.988460540771484, 26.274049758911133, 26.55963706970215, 26.845224380493164, 27.13081169128418, 27.416399002075195, 27.70198631286621, 27.987573623657227, 28.273160934448242, 28.558748245239258, 28.844335556030273, 29.12992286682129, 29.415512084960938, 29.701099395751953, 29.98668670654297, 30.272274017333984, 30.557861328125, 30.843448638916016, 31.12903594970703, 31.414623260498047, 31.700210571289062, 31.985797882080078, 32.271385192871094, 32.55697250366211, 32.842559814453125, 33.12814712524414, 33.413734436035156, 33.69932174682617, 33.98491287231445, 34.27050018310547, 34.556087493896484, 34.8416748046875, 35.127262115478516, 35.41284942626953, 35.69843673706055, 35.98402404785156, 36.26961135864258, 36.555198669433594, 36.84078598022461, 37.126373291015625, 37.41196060180664, 37.697547912597656, 37.98313522338867, 38.26872253417969, 38.5543098449707, 38.83989715576172, 39.125484466552734, 39.41107177734375, 39.696659088134766, 39.98224639892578, 40.26783752441406], "36": [6.254258632659912, 6.538542747497559, 6.822827339172363, 7.107111930847168, 7.391396522521973, 7.675680637359619, 7.959965229034424, 8.24424934387207, 8.528533935546875, 8.81281852722168, 9.097103118896484, 9.381387710571289, 9.665672302246094, 9.949956893920898, 10.234241485595703, 10.518525123596191, 10.802809715270996, 11.0870943069458, 11.371378898620605, 11.65566349029541, 11.939948081970215, 12.22423267364502, 12.508517265319824, 12.792801856994629, 13.077085494995117, 13.361370086669922, 13.645654678344727, 13.929939270019531, 14.214223861694336, 14.49850845336914, 14.782793045043945, 15.06707763671875, 15.351361274719238, 15.635645866394043, 15.919930458068848, 16.20421600341797, 16.48849868774414, 16.772783279418945, 17.05706787109375, 17.341352462768555, 17.62563705444336, 17.909921646118164, 18.19420623779297, 18.478490829467773, 18.762775421142578, 19.047060012817383, 19.331344604492188, 19.615629196166992, 19.899913787841797, 20.1841983795166, 20.468482971191406, 20.75276756286621, 21.037050247192383, 21.321334838867188, 21.605619430541992, 21.889904022216797, 22.1741886138916, 22.458473205566406, 22.74275779724121, 23.027042388916016, 23.31132698059082, 23.595611572265625, 23.87989616394043, 24.164180755615234, 24.44846534729004, 24.732749938964844, 25.01703453063965, 25.301319122314453, 25.585603713989258, 25.86988639831543, 26.154170989990234, 26.43845558166504, 26.722740173339844, 27.00702476501465, 27.291309356689453, 27.575593948364258, 27.859878540039062, 28.144163131713867, 28.428447723388672, 28.712732315063477, 28.99701690673828, 29.281301498413086, 29.56558609008789, 29.849870681762695, 30.1341552734375, 30.418437957763672, 30.702722549438477, 30.98700714111328, 31.271291732788086, 31.55557632446289, 31.839860916137695, 32.1241455078125, 32.40843200683594, 32.69271469116211, 32.97699737548828, 33.26128387451172, 33.54556655883789, 33.82985305786133, 34.1141357421875, 34.39842224121094, 34.68270492553711, 34.96699142456055, 35.25127410888672, 35.535560607910156, 35.81984329223633, 36.104129791259766, 36.38841247558594, 36.672698974609375, 36.95698165893555, 37.241268157958984, 37.525550842285156, 37.80983352661133, 38.094120025634766, 38.37840270996094, 38.662689208984375, 38.94697189331055, 39.231258392333984, 39.515541076660156, 39.799827575683594, 40.084110260009766], "37": [6.225876331329346, 6.508870601654053, 6.79186487197876, 7.074859619140625, 7.357853889465332, 7.640848159790039, 7.923842430114746, 8.206836700439453, 8.48983097076416, 8.772825241088867, 9.05582046508789, 9.338814735412598, 9.621809005737305, 9.904803276062012, 10.187797546386719, 10.470791816711426, 10.753786087036133, 11.03678035736084, 11.319774627685547, 11.60276985168457, 11.885764122009277, 12.168758392333984, 12.451752662658691, 12.734746932983398, 13.017741203308105, 13.300735473632812, 13.58372974395752, 13.866724014282227, 14.14971923828125, 14.432713508605957, 14.715707778930664, 14.998702049255371, 15.281696319580078, 15.564690589904785, 15.847684860229492, 16.130680084228516, 16.413673400878906, 16.69666862487793, 16.97966194152832, 17.262657165527344, 17.545650482177734, 17.828645706176758, 18.11164093017578, 18.394634246826172, 18.677629470825195, 18.960622787475586, 19.24361801147461, 19.526611328125, 19.809606552124023, 20.092599868774414, 20.375595092773438, 20.65859031677246, 20.94158363342285, 21.224578857421875, 21.507572174072266, 21.79056739807129, 22.07356071472168, 22.356555938720703, 22.639549255371094, 22.922544479370117, 23.20553970336914, 23.48853302001953, 23.771528244018555, 24.054521560668945, 24.33751678466797, 24.62051010131836, 24.903505325317383, 25.186498641967773, 25.469493865966797, 25.75248908996582, 26.03548240661621, 26.318477630615234, 26.601470947265625, 26.88446617126465, 27.16745948791504, 27.450454711914062, 27.733448028564453, 28.016443252563477, 28.2994384765625, 28.58243179321289, 28.865427017211914, 29.148420333862305, 29.431415557861328, 29.71440887451172, 29.997404098510742, 30.280397415161133, 30.563392639160156, 30.84638786315918, 31.12938117980957, 31.412376403808594, 31.695369720458984, 31.978364944458008, 32.26136016845703, 32.54435348510742, 32.82734680175781, 33.11034393310547, 33.39333724975586, 33.67633056640625, 33.95932388305664, 34.2423210144043, 34.52531433105469, 34.80830764770508, 35.09130096435547, 35.374298095703125, 35.657291412353516, 35.940284729003906, 36.22328186035156, 36.50627517700195, 36.789268493652344, 37.072261810302734, 37.35525894165039, 37.63825225830078, 37.92124557495117, 38.20424270629883, 38.48723602294922, 38.77022933959961, 39.05322265625, 39.336219787597656, 39.61921310424805, 39.90220642089844], "38": [6.1977739334106445, 6.479491233825684, 6.7612080574035645, 7.0429253578186035, 7.324642181396484, 7.606359004974365, 7.888076305389404, 8.169793128967285, 8.451510429382324, 8.733226776123047, 9.014944076538086, 9.296661376953125, 9.578378677368164, 9.860095024108887, 10.141812324523926, 10.423529624938965, 10.705245971679688, 10.986963272094727, 11.268680572509766, 11.550396919250488, 11.832114219665527, 12.113831520080566, 12.395547866821289, 12.677265167236328, 12.958982467651367, 13.24069881439209, 13.522416114807129, 13.804133415222168, 14.085850715637207, 14.36756706237793, 14.649284362792969, 14.931001663208008, 15.21271800994873, 15.49443531036377, 15.776152610778809, 16.05786895751953, 16.33958625793457, 16.62130355834961, 16.90302085876465, 17.184738159179688, 17.466453552246094, 17.748170852661133, 18.029888153076172, 18.31160545349121, 18.59332275390625, 18.87504005432129, 19.156757354736328, 19.438472747802734, 19.720190048217773, 20.001907348632812, 20.28362464904785, 20.56534194946289, 20.84705924987793, 21.128774642944336, 21.410491943359375, 21.692209243774414, 21.973926544189453, 22.255643844604492, 22.53736114501953, 22.819076538085938, 23.100793838500977, 23.382511138916016, 23.664228439331055, 23.945945739746094, 24.227663040161133, 24.509380340576172, 24.791095733642578, 25.072813034057617, 25.354530334472656, 25.636247634887695, 25.917964935302734, 26.199682235717773, 26.48139762878418, 26.76311492919922, 27.044832229614258, 27.326549530029297, 27.608266830444336, 27.889984130859375, 28.171701431274414, 28.45341682434082, 28.73513412475586, 29.0168514251709, 29.298568725585938, 29.580286026000977, 29.862003326416016, 30.143718719482422, 30.42543601989746, 30.7071533203125, 30.98887062072754, 31.270587921142578, 31.552305221557617, 31.834022521972656, 32.11573791503906, 32.397457122802734, 32.67917251586914, 32.96088790893555, 33.24260711669922, 33.524322509765625, 33.8060417175293, 34.0877571105957, 34.369476318359375, 34.65119171142578, 34.93290710449219, 35.21462631225586, 35.496341705322266, 35.77806091308594, 36.059776306152344, 36.341495513916016, 36.62321090698242, 36.90492630004883, 37.1866455078125, 37.468360900878906, 37.75008010864258, 38.031795501708984, 38.313514709472656, 38.59523010253906, 38.87694549560547, 39.15866470336914, 39.44038009643555, 39.72209930419922], "39": [6.169948101043701, 6.450400352478027, 6.7308526039123535, 7.0113043785095215, 7.291756629943848, 7.572208881378174, 7.8526611328125, 8.133112907409668, 8.413565635681152, 8.69401741027832, 8.974470138549805, 9.254921913146973, 9.535374641418457, 9.815826416015625, 10.096278190612793, 10.376730918884277, 10.657182693481445, 10.93763542175293, 11.218087196350098, 11.498539924621582, 11.77899169921875, 12.059443473815918, 12.339896202087402, 12.62034797668457, 12.900800704956055, 13.181252479553223, 13.461705207824707, 13.742156982421875, 14.022608757019043, 14.303061485290527, 14.583513259887695, 14.86396598815918, 15.144417762756348, 15.424870491027832, 15.705322265625, 15.985774040222168, 16.266225814819336, 16.54667854309082, 16.827131271362305, 17.10758399963379, 17.38803482055664, 17.668487548828125, 17.94894027709961, 18.22939109802246, 18.509843826293945, 18.79029655456543, 19.070749282836914, 19.351200103759766, 19.63165283203125, 19.912105560302734, 20.192556381225586, 20.47300910949707, 20.753461837768555, 21.03391456604004, 21.31436538696289, 21.594818115234375, 21.87527084350586, 22.15572166442871, 22.436174392700195, 22.71662712097168, 22.997079849243164, 23.277530670166016, 23.5579833984375, 23.838436126708984, 24.118886947631836, 24.39933967590332, 24.679792404174805, 24.96024513244629, 25.24069595336914, 25.521148681640625, 25.80160140991211, 26.08205223083496, 26.362504959106445, 26.64295768737793, 26.923410415649414, 27.203861236572266, 27.48431396484375, 27.764766693115234, 28.045217514038086, 28.32567024230957, 28.606122970581055, 28.88657569885254, 29.16702651977539, 29.447479248046875, 29.72793197631836, 30.00838279724121, 30.288835525512695, 30.56928825378418, 30.849740982055664, 31.130191802978516, 31.41064453125, 31.691097259521484, 31.971548080444336, 32.25200271606445, 32.53245162963867, 32.812904357910156, 33.09335708618164, 33.373809814453125, 33.65426254272461, 33.934715270996094, 34.21516799926758, 34.4956169128418, 34.77606964111328, 35.056522369384766, 35.33697509765625, 35.617427825927734, 35.89788055419922, 36.1783332824707, 36.45878219604492, 36.739234924316406, 37.01968765258789, 37.300140380859375, 37.58059310913086, 37.861045837402344, 38.14149856567383, 38.42194747924805, 38.70240020751953, 38.982852935791016, 39.2633056640625, 39.543758392333984], "40": [6.142394065856934, 6.42159366607666, 6.700793266296387, 6.9799933433532715, 7.259192943572998, 7.538392543792725, 7.817592620849609, 8.096792221069336, 8.375991821289062, 8.655191421508789, 8.934391021728516, 9.213590621948242, 9.492791175842285, 9.771990776062012, 10.051190376281738, 10.330389976501465, 10.609589576721191, 10.888789176940918, 11.167988777160645, 11.447189331054688, 11.726388931274414, 12.00558853149414, 12.284788131713867, 12.563987731933594, 12.84318733215332, 13.122386932373047, 13.401586532592773, 13.680787086486816, 13.959986686706543, 14.23918628692627, 14.518385887145996, 14.797585487365723, 15.07678508758545, 15.355984687805176, 15.635185241699219, 15.914384841918945, 16.193584442138672, 16.4727840423584, 16.751983642578125, 17.03118324279785, 17.310382843017578, 17.589582443237305, 17.86878204345703, 18.147981643676758, 18.427181243896484, 18.706382751464844, 18.98558235168457, 19.264781951904297, 19.543981552124023, 19.82318115234375, 20.102380752563477, 20.381580352783203, 20.66077995300293, 20.939979553222656, 21.219179153442383, 21.49837875366211, 21.777578353881836, 22.056777954101562, 22.33597755432129, 22.615177154541016, 22.894378662109375, 23.1735782623291, 23.452777862548828, 23.731977462768555, 24.01117706298828, 24.290376663208008, 24.569576263427734, 24.84877586364746, 25.127975463867188, 25.407175064086914, 25.68637466430664, 25.965574264526367, 26.244773864746094, 26.52397346496582, 26.803173065185547, 27.082374572753906, 27.361574172973633, 27.64077377319336, 27.919973373413086, 28.199172973632812, 28.47837257385254, 28.757572174072266, 29.036771774291992, 29.31597137451172, 29.595170974731445, 29.874370574951172, 30.1535701751709, 30.432769775390625, 30.71196937561035, 30.991168975830078, 31.270370483398438, 31.549570083618164, 31.82876968383789, 32.107967376708984, 32.387168884277344, 32.66636657714844, 32.9455680847168, 33.224769592285156, 33.50396728515625, 33.78316879272461, 34.0623664855957, 34.34156799316406, 34.620765686035156, 34.899967193603516, 35.17916488647461, 35.45836639404297, 35.73756408691406, 36.01676559448242, 36.295963287353516, 36.575164794921875, 36.85436248779297, 37.13356399536133, 37.41276550292969, 37.69196319580078, 37.97116470336914, 38.250362396240234, 38.529563903808594, 38.80876159667969, 39.08796310424805, 39.36716079711914], "41": [6.115108489990234, 6.393067836761475, 6.671027183532715, 6.948986530303955, 7.2269463539123535, 7.504905700683594, 7.782865047454834, 8.060824394226074, 8.338784217834473, 8.616743087768555, 8.894702911376953, 9.172662734985352, 9.450621604919434, 9.728581428527832, 10.00654125213623, 10.284500122070312, 10.562459945678711, 10.84041976928711, 11.118378639221191, 11.39633846282959, 11.674297332763672, 11.95225715637207, 12.230216979980469, 12.50817584991455, 12.78613567352295, 13.064095497131348, 13.34205436706543, 13.620014190673828, 13.89797306060791, 14.175932884216309, 14.453892707824707, 14.731851577758789, 15.009811401367188, 15.287771224975586, 15.565730094909668, 15.843689918518066, 16.12164878845215, 16.399608612060547, 16.677568435668945, 16.955528259277344, 17.23348617553711, 17.511445999145508, 17.789405822753906, 18.067365646362305, 18.345325469970703, 18.6232852935791, 18.901243209838867, 19.179203033447266, 19.457162857055664, 19.735122680664062, 20.01308250427246, 20.291040420532227, 20.569000244140625, 20.846960067749023, 21.124919891357422, 21.40287971496582, 21.68083953857422, 21.958797454833984, 22.236757278442383, 22.51471710205078, 22.79267692565918, 23.070636749267578, 23.348594665527344, 23.626554489135742, 23.90451431274414, 24.18247413635254, 24.460433959960938, 24.738391876220703, 25.0163516998291, 25.2943115234375, 25.5722713470459, 25.850231170654297, 26.128190994262695, 26.40614891052246, 26.68410873413086, 26.962068557739258, 27.240028381347656, 27.517988204956055, 27.79594612121582, 28.07390594482422, 28.351865768432617, 28.629825592041016, 28.907785415649414, 29.18574333190918, 29.463703155517578, 29.741662979125977, 30.019622802734375, 30.297582626342773, 30.575542449951172, 30.853500366210938, 31.131460189819336, 31.409420013427734, 31.687379837036133, 31.96533966064453, 32.2432975769043, 32.52125930786133, 32.799217224121094, 33.07717514038086, 33.35513687133789, 33.633094787597656, 33.91105651855469, 34.18901443481445, 34.46697235107422, 34.74493408203125, 35.022891998291016, 35.30085372924805, 35.57881164550781, 35.856773376464844, 36.13473129272461, 36.412689208984375, 36.690650939941406, 36.96860885620117, 37.2465705871582, 37.52452850341797, 37.802486419677734, 38.080448150634766, 38.35840606689453, 38.63636779785156, 38.91432571411133, 39.192283630371094], "42": [6.08808708190918, 6.364818572998047, 6.641549587249756, 6.918280601501465, 7.195012092590332, 7.471743106842041, 7.748474597930908, 8.025205612182617, 8.301937103271484, 8.578668594360352, 8.855399131774902, 9.13213062286377, 9.408862113952637, 9.685593605041504, 9.962324142456055, 10.239055633544922, 10.515787124633789, 10.79251766204834, 11.069249153137207, 11.345980644226074, 11.622712135314941, 11.899442672729492, 12.17617416381836, 12.452905654907227, 12.729637145996094, 13.006367683410645, 13.283099174499512, 13.559830665588379, 13.83656120300293, 14.113292694091797, 14.390024185180664, 14.666755676269531, 14.943486213684082, 15.22021770477295, 15.496949195861816, 15.773680686950684, 16.050411224365234, 16.3271427154541, 16.60387420654297, 16.880605697631836, 17.157337188720703, 17.434066772460938, 17.710798263549805, 17.987529754638672, 18.26426124572754, 18.540992736816406, 18.817724227905273, 19.09445571899414, 19.371187210083008, 19.647916793823242, 19.92464828491211, 20.201379776000977, 20.478111267089844, 20.75484275817871, 21.031574249267578, 21.308305740356445, 21.58503532409668, 21.861766815185547, 22.138498306274414, 22.41522979736328, 22.69196128845215, 22.968692779541016, 23.245424270629883, 23.52215576171875, 23.798885345458984, 24.07561683654785, 24.35234832763672, 24.629079818725586, 24.905811309814453, 25.18254280090332, 25.459274291992188, 25.736003875732422, 26.01273536682129, 26.289466857910156, 26.566198348999023, 26.84292984008789, 27.119661331176758, 27.396392822265625, 27.67312240600586, 27.949853897094727, 28.226585388183594, 28.50331687927246, 28.780048370361328, 29.056779861450195, 29.333511352539062, 29.61024284362793, 29.886972427368164, 30.16370391845703, 30.4404354095459, 30.717166900634766, 30.993898391723633, 31.2706298828125, 31.547361373901367, 31.8240909576416, 32.10082244873047, 32.37755584716797, 32.6542854309082, 32.93101501464844, 33.20774841308594, 33.48447799682617, 33.76121139526367, 34.037940979003906, 34.314674377441406, 34.59140396118164, 34.868133544921875, 35.144866943359375, 35.42159652709961, 35.69832992553711, 35.975059509277344, 36.251792907714844, 36.52852249145508, 36.80525588989258, 37.08198547363281, 37.35871505737305, 37.63544845581055, 37.91217803955078, 38.18891143798828, 38.465641021728516, 38.742374420166016, 39.01910400390625], "43": [6.06132698059082, 6.336841583251953, 6.612356662750244, 6.887871265411377, 7.163386344909668, 7.438900947570801, 7.714416027069092, 7.989930629730225, 8.265445709228516, 8.540960311889648, 8.816474914550781, 9.09199047088623, 9.367505073547363, 9.643019676208496, 9.918534278869629, 10.194049835205078, 10.469564437866211, 10.745079040527344, 11.020594596862793, 11.296109199523926, 11.571623802185059, 11.847138404846191, 12.12265396118164, 12.398168563842773, 12.673683166503906, 12.949197769165039, 13.224713325500488, 13.500227928161621, 13.775742530822754, 14.051257133483887, 14.326772689819336, 14.602287292480469, 14.877801895141602, 15.153316497802734, 15.428832054138184, 15.704346656799316, 15.97986125946045, 16.2553768157959, 16.53089141845703, 16.806406021118164, 17.081920623779297, 17.35743522644043, 17.632949829101562, 17.908466339111328, 18.18398094177246, 18.459495544433594, 18.735010147094727, 19.01052474975586, 19.286039352416992, 19.561553955078125, 19.837068557739258, 20.112585067749023, 20.388099670410156, 20.66361427307129, 20.939128875732422, 21.214643478393555, 21.490158081054688, 21.76567268371582, 22.041189193725586, 22.31670379638672, 22.59221839904785, 22.867733001708984, 23.143247604370117, 23.41876220703125, 23.694276809692383, 23.969791412353516, 24.24530792236328, 24.520822525024414, 24.796337127685547, 25.07185173034668, 25.347366333007812, 25.622880935668945, 25.898395538330078, 26.17391014099121, 26.449426651000977, 26.72494125366211, 27.000455856323242, 27.275970458984375, 27.551485061645508, 27.82699966430664, 28.102514266967773, 28.37803077697754, 28.653545379638672, 28.929059982299805, 29.204574584960938, 29.48008918762207, 29.755603790283203, 30.031118392944336, 30.30663299560547, 30.582149505615234, 30.857664108276367, 31.1331787109375, 31.408693313598633, 31.684207916259766, 31.9597225189209, 32.23523712158203, 32.5107536315918, 32.7862663269043, 33.06178283691406, 33.33729553222656, 33.61281204223633, 33.888328552246094, 34.163841247558594, 34.43935775756836, 34.71487045288086, 34.990386962890625, 35.265899658203125, 35.54141616821289, 35.816932678222656, 36.092445373535156, 36.36796188354492, 36.64347457885742, 36.91899108886719, 37.19450378417969, 37.47002029418945, 37.74553680419922, 38.02104949951172, 38.296566009521484, 38.572078704833984, 38.84759521484375], "44": [6.034823417663574, 6.309134006500244, 6.583444118499756, 6.857754230499268, 7.132064342498779, 7.406374454498291, 7.680684566497803, 7.9549946784973145, 8.229305267333984, 8.503615379333496, 8.777925491333008, 9.05223560333252, 9.326545715332031, 9.600855827331543, 9.875165939331055, 10.149476051330566, 10.423786163330078, 10.69809627532959, 10.972406387329102, 11.246716499328613, 11.521026611328125, 11.795336723327637, 12.069646835327148, 12.34395694732666, 12.618268013000488, 12.892578125, 13.166888236999512, 13.441198348999023, 13.715508460998535, 13.989818572998047, 14.264128684997559, 14.53843879699707, 14.812748908996582, 15.087059020996094, 15.361369132995605, 15.635679244995117, 15.909989356994629, 16.18429946899414, 16.45861053466797, 16.732919692993164, 17.007230758666992, 17.281539916992188, 17.555850982666016, 17.83016014099121, 18.10447120666504, 18.378780364990234, 18.653091430664062, 18.927400588989258, 19.201711654663086, 19.47602081298828, 19.75033187866211, 20.024641036987305, 20.298952102661133, 20.57326316833496, 20.847572326660156, 21.121883392333984, 21.39619255065918, 21.670503616333008, 21.944812774658203, 22.21912384033203, 22.493432998657227, 22.767744064331055, 23.04205322265625, 23.316364288330078, 23.590673446655273, 23.8649845123291, 24.139293670654297, 24.413604736328125, 24.68791389465332, 24.96222496032715, 25.236536026000977, 25.510845184326172, 25.78515625, 26.059465408325195, 26.333776473999023, 26.60808563232422, 26.882396697998047, 27.156705856323242, 27.43101692199707, 27.705326080322266, 27.979637145996094, 28.25394630432129, 28.528257369995117, 28.802566528320312, 29.07687759399414, 29.351186752319336, 29.625497817993164, 29.89980697631836, 30.174118041992188, 30.448429107666016, 30.72273826599121, 30.99704933166504, 31.271358489990234, 31.545669555664062, 31.819978713989258, 32.09428787231445, 32.36859893798828, 32.64291000366211, 32.91722106933594, 33.1915283203125, 33.46583938598633, 33.740150451660156, 34.014461517333984, 34.28876876831055, 34.563079833984375, 34.8373908996582, 35.11170196533203, 35.38601303100586, 35.66032028198242, 35.93463134765625, 36.20894241333008, 36.483253479003906, 36.75756072998047, 37.0318717956543, 37.306182861328125, 37.58049392700195, 37.854801177978516, 38.129112243652344, 38.40342330932617, 38.677734375], "45": [6.00857400894165, 6.281691074371338, 6.554808139801025, 6.827925205230713, 7.1010422706604, 7.37415885925293, 7.647275924682617, 7.920392990112305, 8.193510055541992, 8.46662712097168, 8.739744186401367, 9.012861251831055, 9.285978317260742, 9.55909538269043, 9.832212448120117, 10.105329513549805, 10.378446578979492, 10.651562690734863, 10.92467975616455, 11.197796821594238, 11.470913887023926, 11.744030952453613, 12.0171480178833, 12.290265083312988, 12.563382148742676, 12.836499214172363, 13.10961627960205, 13.382733345031738, 13.655850410461426, 13.928967475891113, 14.2020845413208, 14.475201606750488, 14.74831771850586, 15.021434783935547, 15.294551849365234, 15.567668914794922, 15.84078598022461, 16.113903045654297, 16.387020111083984, 16.660137176513672, 16.93325424194336, 17.206371307373047, 17.479488372802734, 17.752605438232422, 18.02572250366211, 18.298839569091797, 18.571956634521484, 18.845073699951172, 19.11819076538086, 19.391307830810547, 19.664424896240234, 19.937541961669922, 20.21065902709961, 20.483776092529297, 20.756893157958984, 21.030010223388672, 21.303125381469727, 21.576242446899414, 21.8493595123291, 22.12247657775879, 22.395593643188477, 22.668710708618164, 22.94182777404785, 23.21494483947754, 23.488061904907227, 23.761178970336914, 24.0342960357666, 24.30741310119629, 24.580530166625977, 24.853647232055664, 25.12676429748535, 25.39988136291504, 25.672998428344727, 25.946115493774414, 26.2192325592041, 26.49234962463379, 26.765466690063477, 27.038583755493164, 27.31170082092285, 27.58481788635254, 27.857934951782227, 28.131052017211914, 28.4041690826416, 28.67728614807129, 28.950403213500977, 29.223520278930664, 29.49663543701172, 29.769752502441406, 30.042869567871094, 30.31598663330078, 30.58910369873047, 30.862220764160156, 31.135337829589844, 31.40845489501953, 31.68157196044922, 31.954689025878906, 32.227806091308594, 32.50092315673828, 32.77404022216797, 33.047157287597656, 33.320274353027344, 33.59339141845703, 33.86650848388672, 34.139625549316406, 34.412742614746094, 34.68585968017578, 34.95897674560547, 35.232093811035156, 35.505210876464844, 35.77832794189453, 36.05144500732422, 36.324562072753906, 36.597679138183594, 36.87079620361328, 37.14391326904297, 37.417030334472656, 37.690147399902344, 37.96326446533203, 38.23638153076172, 38.509498596191406], "46": [5.982574462890625, 6.254509925842285, 6.526444911956787, 6.798380374908447, 7.070315361022949, 7.342250823974609, 7.614185810089111, 7.8861212730407715, 8.158056259155273, 8.429991722106934, 8.701927185058594, 8.973861694335938, 9.245797157287598, 9.517732620239258, 9.789668083190918, 10.061602592468262, 10.333538055419922, 10.605473518371582, 10.877408981323242, 11.149343490600586, 11.421278953552246, 11.693214416503906, 11.96514892578125, 12.23708438873291, 12.50901985168457, 12.78095531463623, 13.052889823913574, 13.324825286865234, 13.596760749816895, 13.868696212768555, 14.140630722045898, 14.412566184997559, 14.684501647949219, 14.956437110900879, 15.228371620178223, 15.500307083129883, 15.772242546081543, 16.044178009033203, 16.316112518310547, 16.588048934936523, 16.859983444213867, 17.13191795349121, 17.403854370117188, 17.67578887939453, 17.947723388671875, 18.21965980529785, 18.491594314575195, 18.76352882385254, 19.035465240478516, 19.30739974975586, 19.579336166381836, 19.85127067565918, 20.123205184936523, 20.3951416015625, 20.667076110839844, 20.939010620117188, 21.210947036743164, 21.482881546020508, 21.754817962646484, 22.026752471923828, 22.298686981201172, 22.57062339782715, 22.842557907104492, 23.114492416381836, 23.386428833007812, 23.658363342285156, 23.9302978515625, 24.202234268188477, 24.47416877746582, 24.746105194091797, 25.01803970336914, 25.289974212646484, 25.56191062927246, 25.833845138549805, 26.10577964782715, 26.377716064453125, 26.64965057373047, 26.921586990356445, 27.19352149963379, 27.465456008911133, 27.73739242553711, 28.009326934814453, 28.281261444091797, 28.553197860717773, 28.825132369995117, 29.09706687927246, 29.369003295898438, 29.64093780517578, 29.912874221801758, 30.1848087310791, 30.456743240356445, 30.728679656982422, 31.000614166259766, 31.27254867553711, 31.544485092163086, 31.81641960144043, 32.088356018066406, 32.36029052734375, 32.632225036621094, 32.90415954589844, 33.17609786987305, 33.44803237915039, 33.719966888427734, 33.99190139770508, 34.26383590698242, 34.535770416259766, 34.807708740234375, 35.07964324951172, 35.35157775878906, 35.623512268066406, 35.89544677734375, 36.16738510131836, 36.4393196105957, 36.71125411987305, 36.98318862915039, 37.255123138427734, 37.52705764770508, 37.79899597167969, 38.07093048095703, 38.342864990234375], "47": [5.956821918487549, 6.22758674621582, 6.498351097106934, 6.769115924835205, 7.039880752563477, 7.31064510345459, 7.581409931182861, 7.852174282073975, 8.122939109802246, 8.39370346069336, 8.664468765258789, 8.935233116149902, 9.205997467041016, 9.476762771606445, 9.747527122497559, 10.018291473388672, 10.289055824279785, 10.559821128845215, 10.830585479736328, 11.101349830627441, 11.372115135192871, 11.642879486083984, 11.913643836975098, 12.184409141540527, 12.45517349243164, 12.725937843322754, 12.996702194213867, 13.267467498779297, 13.53823184967041, 13.808996200561523, 14.079761505126953, 14.350525856018066, 14.62129020690918, 14.89205551147461, 15.162819862365723, 15.433584213256836, 15.70434856414795, 15.975113868713379, 16.245878219604492, 16.516643524169922, 16.78740692138672, 17.05817222595215, 17.328937530517578, 17.599700927734375, 17.870466232299805, 18.141231536865234, 18.41199493408203, 18.68276023864746, 18.95352554321289, 19.224288940429688, 19.495054244995117, 19.765817642211914, 20.036582946777344, 20.307348251342773, 20.57811164855957, 20.848876953125, 21.11964225769043, 21.390405654907227, 21.661170959472656, 21.931936264038086, 22.202699661254883, 22.473464965820312, 22.744230270385742, 23.01499366760254, 23.28575897216797, 23.5565242767334, 23.827287673950195, 24.098052978515625, 24.368818283081055, 24.63958168029785, 24.91034698486328, 25.181110382080078, 25.451875686645508, 25.722640991210938, 25.993404388427734, 26.264169692993164, 26.534934997558594, 26.80569839477539, 27.07646369934082, 27.34722900390625, 27.617992401123047, 27.888757705688477, 28.159523010253906, 28.430286407470703, 28.701051712036133, 28.971817016601562, 29.24258041381836, 29.51334571838379, 29.78411102294922, 30.054874420166016, 30.325639724731445, 30.596403121948242, 30.867168426513672, 31.1379337310791, 31.4086971282959, 31.679462432861328, 31.950227737426758, 32.22099304199219, 32.491756439208984, 32.76251983642578, 33.033287048339844, 33.30405044555664, 33.57481384277344, 33.8455810546875, 34.1163444519043, 34.387107849121094, 34.657875061035156, 34.92863845825195, 35.19940185546875, 35.47016906738281, 35.74093246459961, 36.011695861816406, 36.28246307373047, 36.553226470947266, 36.82398986816406, 37.094757080078125, 37.36552047729492, 37.63628387451172, 37.90705108642578, 38.17781448364258], "48": [5.931312561035156, 6.200917720794678, 6.470522880554199, 6.740128040313721, 7.009733200073242, 7.279338359832764, 7.548943519592285, 7.818548679351807, 8.088153839111328, 8.357758522033691, 8.627364158630371, 8.896968841552734, 9.166574478149414, 9.436179161071777, 9.705784797668457, 9.97538948059082, 10.244994163513184, 10.514599800109863, 10.784204483032227, 11.053810119628906, 11.32341480255127, 11.59302043914795, 11.862625122070312, 12.132230758666992, 12.401835441589355, 12.671441078186035, 12.941045761108398, 13.210651397705078, 13.480256080627441, 13.749860763549805, 14.019466400146484, 14.289071083068848, 14.558676719665527, 14.82828140258789, 15.09788703918457, 15.367491722106934, 15.637097358703613, 15.906702041625977, 16.176307678222656, 16.445913314819336, 16.715517044067383, 16.985122680664062, 17.254728317260742, 17.52433204650879, 17.79393768310547, 18.06354331970215, 18.333148956298828, 18.602752685546875, 18.872358322143555, 19.141963958740234, 19.411569595336914, 19.68117332458496, 19.95077896118164, 20.22038459777832, 20.489988327026367, 20.759593963623047, 21.029199600219727, 21.298805236816406, 21.568408966064453, 21.838014602661133, 22.107620239257812, 22.377225875854492, 22.64682960510254, 22.91643524169922, 23.1860408782959, 23.455646514892578, 23.725250244140625, 23.994855880737305, 24.264461517333984, 24.53406524658203, 24.80367088317871, 25.07327651977539, 25.34288215637207, 25.612485885620117, 25.882091522216797, 26.151697158813477, 26.421302795410156, 26.690906524658203, 26.960512161254883, 27.230117797851562, 27.49972152709961, 27.76932716369629, 28.03893280029297, 28.30853843688965, 28.578142166137695, 28.847747802734375, 29.117353439331055, 29.386959075927734, 29.65656280517578, 29.92616844177246, 30.19577407836914, 30.46537971496582, 30.734983444213867, 31.004589080810547, 31.274194717407227, 31.543798446655273, 31.813404083251953, 32.0830078125, 32.35261535644531, 32.62221908569336, 32.89182662963867, 33.16143035888672, 33.431034088134766, 33.70064163208008, 33.970245361328125, 34.23984909057617, 34.509456634521484, 34.77906036376953, 35.04866409301758, 35.31827163696289, 35.58787536621094, 35.85748291015625, 36.1270866394043, 36.396690368652344, 36.666297912597656, 36.9359016418457, 37.20550537109375, 37.47511291503906, 37.74471664428711, 38.014320373535156], "49": [5.906043529510498, 6.174499988555908, 6.442956447601318, 6.7114129066467285, 6.979869365692139, 7.248325824737549, 7.516782283782959, 7.785239219665527, 8.053695678710938, 8.322152137756348, 8.590608596801758, 8.859065055847168, 9.127521514892578, 9.395977973937988, 9.664434432983398, 9.932890892028809, 10.201347351074219, 10.469803810119629, 10.738260269165039, 11.006717681884766, 11.275174140930176, 11.543630599975586, 11.812087059020996, 12.080543518066406, 12.348999977111816, 12.617456436157227, 12.885912895202637, 13.154369354248047, 13.422825813293457, 13.691282272338867, 13.959738731384277, 14.228195190429688, 14.496651649475098, 14.765108108520508, 15.033564567565918, 15.302021980285645, 15.570478439331055, 15.838934898376465, 16.107391357421875, 16.37584686279297, 16.644304275512695, 16.91275978088379, 17.181217193603516, 17.44967269897461, 17.718130111694336, 17.986587524414062, 18.255043029785156, 18.523500442504883, 18.791955947875977, 19.060413360595703, 19.328868865966797, 19.597326278686523, 19.865781784057617, 20.134239196777344, 20.402694702148438, 20.671152114868164, 20.939607620239258, 21.208065032958984, 21.476520538330078, 21.744977951049805, 22.01343536376953, 22.281890869140625, 22.55034828186035, 22.818803787231445, 23.087261199951172, 23.355716705322266, 23.624174118041992, 23.892629623413086, 24.161087036132812, 24.429542541503906, 24.697999954223633, 24.966455459594727, 25.234912872314453, 25.503368377685547, 25.771825790405273, 26.040281295776367, 26.308738708496094, 26.57719612121582, 26.845651626586914, 27.11410903930664, 27.382564544677734, 27.65102195739746, 27.919477462768555, 28.18793487548828, 28.456390380859375, 28.7248477935791, 28.993303298950195, 29.261760711669922, 29.530216217041016, 29.798673629760742, 30.067129135131836, 30.335586547851562, 30.60404396057129, 30.872499465942383, 31.14095687866211, 31.409412384033203, 31.67786979675293, 31.946325302124023, 32.21478271484375, 32.483238220214844, 32.75169372558594, 33.0201530456543, 33.28860855102539, 33.557064056396484, 33.82551956176758, 34.09397888183594, 34.36243438720703, 34.630889892578125, 34.89934539794922, 35.16780471801758, 35.43626022338867, 35.704715728759766, 35.973175048828125, 36.24163055419922, 36.51008605957031, 36.778541564941406, 37.047000885009766, 37.31545639038086, 37.58391189575195, 37.85236740112305], "50": [5.881011009216309, 6.148329734802246, 6.415648460388184, 6.682966709136963, 6.9502854347229, 7.217604160308838, 7.484922885894775, 7.752241611480713, 8.019559860229492, 8.28687858581543, 8.554197311401367, 8.821516036987305, 9.088834762573242, 9.35615348815918, 9.623472213745117, 9.890790939331055, 10.158109664916992, 10.42542839050293, 10.692747116088867, 10.960065841674805, 11.227384567260742, 11.49470329284668, 11.762022018432617, 12.029340744018555, 12.296659469604492, 12.56397819519043, 12.831296920776367, 13.098614692687988, 13.365933418273926, 13.633252143859863, 13.9005708694458, 14.167889595031738, 14.435208320617676, 14.702527046203613, 14.96984577178955, 15.237164497375488, 15.504483222961426, 15.771801948547363, 16.039119720458984, 16.306438446044922, 16.57375717163086, 16.841075897216797, 17.108394622802734, 17.375713348388672, 17.64303207397461, 17.910350799560547, 18.177669525146484, 18.444988250732422, 18.71230697631836, 18.979625701904297, 19.246944427490234, 19.514263153076172, 19.78158187866211, 20.048900604248047, 20.316219329833984, 20.583538055419922, 20.85085678100586, 21.118175506591797, 21.385494232177734, 21.652812957763672, 21.92013168334961, 22.187450408935547, 22.454769134521484, 22.722087860107422, 22.98940658569336, 23.256725311279297, 23.524044036865234, 23.791362762451172, 24.05868148803711, 24.326000213623047, 24.593318939208984, 24.860637664794922, 25.12795639038086, 25.395275115966797, 25.662593841552734, 25.929912567138672, 26.197229385375977, 26.464548110961914, 26.73186683654785, 26.99918556213379, 27.266504287719727, 27.533823013305664, 27.8011417388916, 28.06846046447754, 28.335779190063477, 28.603097915649414, 28.87041664123535, 29.13773536682129, 29.405054092407227, 29.672372817993164, 29.9396915435791, 30.20701026916504, 30.474328994750977, 30.741647720336914, 31.00896644592285, 31.27628517150879, 31.543603897094727, 31.810922622680664, 32.07823944091797, 32.345558166503906, 32.612876892089844, 32.88019561767578, 33.14751434326172, 33.414833068847656, 33.682151794433594, 33.94947052001953, 34.21678924560547, 34.484107971191406, 34.751426696777344, 35.01874542236328, 35.28606414794922, 35.553382873535156, 35.820701599121094, 36.08802032470703, 36.35533905029297, 36.622657775878906, 36.889976501464844, 37.15729522705078, 37.42461395263672, 37.691932678222656], "51": [5.856212139129639, 6.122403621673584, 6.388595104217529, 6.654786109924316, 6.920977592468262, 7.187169075012207, 7.453360557556152, 7.719552040100098, 7.985743522644043, 8.251935005187988, 8.518126487731934, 8.784317970275879, 9.050509452819824, 9.31670093536377, 9.582892417907715, 9.84908390045166, 10.115275382995605, 10.38146686553955, 10.647658348083496, 10.913849830627441, 11.180041313171387, 11.446232795715332, 11.712424278259277, 11.978615760803223, 12.244807243347168, 12.510998725891113, 12.777190208435059, 13.043381690979004, 13.309572219848633, 13.575763702392578, 13.841955184936523, 14.108146667480469, 14.374338150024414, 14.64052963256836, 14.906721115112305, 15.17291259765625, 15.439104080200195, 15.70529556274414, 15.971487045288086, 16.23767852783203, 16.503870010375977, 16.770061492919922, 17.036252975463867, 17.302444458007812, 17.568635940551758, 17.834827423095703, 18.10101890563965, 18.367210388183594, 18.63340187072754, 18.899593353271484, 19.16578483581543, 19.431976318359375, 19.69816780090332, 19.964359283447266, 20.23055076599121, 20.496742248535156, 20.7629337310791, 21.029125213623047, 21.295316696166992, 21.561508178710938, 21.827699661254883, 22.093891143798828, 22.360082626342773, 22.62627410888672, 22.892465591430664, 23.15865707397461, 23.424848556518555, 23.6910400390625, 23.957231521606445, 24.22342300415039, 24.489614486694336, 24.75580596923828, 25.021997451782227, 25.288188934326172, 25.554380416870117, 25.820571899414062, 26.086763381958008, 26.352954864501953, 26.619144439697266, 26.88533592224121, 27.151527404785156, 27.4177188873291, 27.683910369873047, 27.950101852416992, 28.216293334960938, 28.482484817504883, 28.748676300048828, 29.014867782592773, 29.28105926513672, 29.547250747680664, 29.81344223022461, 30.079633712768555, 30.3458251953125, 30.612016677856445, 30.87820816040039, 31.144399642944336, 31.41059112548828, 31.676782608032227, 31.942974090576172, 32.20916748046875, 32.47535705566406, 32.74155044555664, 33.00774002075195, 33.27393341064453, 33.540122985839844, 33.80631637573242, 34.072505950927734, 34.33869934082031, 34.604888916015625, 34.8710823059082, 35.137271881103516, 35.403465270996094, 35.669654846191406, 35.93584442138672, 36.2020378112793, 36.46822738647461, 36.73442077636719, 37.0006103515625, 37.26680374145508, 37.53299331665039], "52": [5.831643581390381, 6.0967183113098145, 6.361793041229248, 6.626867771148682, 6.891942501068115, 7.157017230987549, 7.422091960906982, 7.687166690826416, 7.95224142074585, 8.217315673828125, 8.482390403747559, 8.747465133666992, 9.012539863586426, 9.27761459350586, 9.542689323425293, 9.807764053344727, 10.07283878326416, 10.337913513183594, 10.602988243103027, 10.868062973022461, 11.133137702941895, 11.398212432861328, 11.663287162780762, 11.928361892700195, 12.193436622619629, 12.458511352539062, 12.723586082458496, 12.98866081237793, 13.253735542297363, 13.518810272216797, 13.78388500213623, 14.048959732055664, 14.314034461975098, 14.579109191894531, 14.844183921813965, 15.109258651733398, 15.374333381652832, 15.639408111572266, 15.9044828414917, 16.169557571411133, 16.43463134765625, 16.69970703125, 16.964780807495117, 17.229856491088867, 17.494930267333984, 17.760005950927734, 18.02507972717285, 18.2901554107666, 18.55522918701172, 18.82030487060547, 19.085378646850586, 19.350454330444336, 19.615528106689453, 19.880603790283203, 20.14567756652832, 20.41075325012207, 20.675827026367188, 20.940902709960938, 21.205976486206055, 21.471052169799805, 21.736125946044922, 22.001201629638672, 22.26627540588379, 22.531349182128906, 22.796424865722656, 23.061498641967773, 23.326574325561523, 23.59164810180664, 23.85672378540039, 24.121797561645508, 24.386873245239258, 24.651947021484375, 24.917022705078125, 25.182096481323242, 25.447172164916992, 25.71224594116211, 25.97732162475586, 26.242395401000977, 26.507471084594727, 26.772544860839844, 27.037620544433594, 27.30269432067871, 27.56777000427246, 27.832843780517578, 28.097919464111328, 28.362993240356445, 28.628068923950195, 28.893142700195312, 29.158218383789062, 29.42329216003418, 29.68836784362793, 29.953441619873047, 30.218517303466797, 30.483591079711914, 30.748666763305664, 31.01374053955078, 31.27881622314453, 31.54388999938965, 31.8089656829834, 32.074039459228516, 32.339115142822266, 32.604190826416016, 32.8692626953125, 33.13433837890625, 33.3994140625, 33.664485931396484, 33.929561614990234, 34.194637298583984, 34.459712982177734, 34.72478485107422, 34.98986053466797, 35.25493621826172, 35.52001190185547, 35.78508377075195, 36.0501594543457, 36.31523513793945, 36.5803108215332, 36.84538269042969, 37.11045837402344, 37.37553405761719], "53": [5.807302474975586, 6.071270942687988, 6.335238933563232, 6.599207401275635, 6.863175868988037, 7.127143859863281, 7.391112327575684, 7.655080795288086, 7.91904878616333, 8.183016777038574, 8.446985244750977, 8.710953712463379, 8.974922180175781, 9.238890647888184, 9.502859115600586, 9.766826629638672, 10.030795097351074, 10.294763565063477, 10.558732032775879, 10.822700500488281, 11.086668014526367, 11.35063648223877, 11.614604949951172, 11.878573417663574, 12.142541885375977, 12.406510353088379, 12.670477867126465, 12.934446334838867, 13.19841480255127, 13.462383270263672, 13.726351737976074, 13.99031925201416, 14.254287719726562, 14.518256187438965, 14.782224655151367, 15.04619312286377, 15.310161590576172, 15.574129104614258, 15.83809757232666, 16.102066040039062, 16.36603355407715, 16.630002975463867, 16.893970489501953, 17.157939910888672, 17.421907424926758, 17.685874938964844, 17.949844360351562, 18.21381187438965, 18.477781295776367, 18.741748809814453, 19.005718231201172, 19.269685745239258, 19.533653259277344, 19.797622680664062, 20.06159019470215, 20.325559616088867, 20.589527130126953, 20.85349464416504, 21.117464065551758, 21.381431579589844, 21.645401000976562, 21.90936851501465, 22.173336029052734, 22.437305450439453, 22.70127296447754, 22.965242385864258, 23.229209899902344, 23.493179321289062, 23.75714683532715, 24.021114349365234, 24.285083770751953, 24.54905128479004, 24.813020706176758, 25.076988220214844, 25.34095573425293, 25.60492515563965, 25.868892669677734, 26.132862091064453, 26.39682960510254, 26.660797119140625, 26.924766540527344, 27.18873405456543, 27.45270347595215, 27.716670989990234, 27.98063850402832, 28.24460792541504, 28.508575439453125, 28.772544860839844, 29.03651237487793, 29.30048179626465, 29.564449310302734, 29.82841682434082, 30.09238624572754, 30.356353759765625, 30.620323181152344, 30.88429069519043, 31.148258209228516, 31.412227630615234, 31.67619514465332, 31.94016456604004, 32.204132080078125, 32.468101501464844, 32.7320671081543, 32.996036529541016, 33.260005950927734, 33.52397537231445, 33.787940979003906, 34.051910400390625, 34.315879821777344, 34.5798454284668, 34.843814849853516, 35.107784271240234, 35.37174987792969, 35.635719299316406, 35.899688720703125, 36.163658142089844, 36.4276237487793, 36.691593170166016, 36.955562591552734, 37.21952819824219], "54": [5.783185958862305, 6.046058177947998, 6.308929920196533, 6.571802139282227, 6.83467435836792, 7.097546100616455, 7.360418319702148, 7.623290538787842, 7.886162757873535, 8.14903450012207, 8.411907196044922, 8.674778938293457, 8.937650680541992, 9.200523376464844, 9.463395118713379, 9.726266860961914, 9.989139556884766, 10.2520112991333, 10.514883041381836, 10.777755737304688, 11.040627479553223, 11.303499221801758, 11.56637191772461, 11.829243659973145, 12.092116355895996, 12.354988098144531, 12.617859840393066, 12.880732536315918, 13.143604278564453, 13.406476020812988, 13.66934871673584, 13.932220458984375, 14.19509220123291, 14.457964897155762, 14.720836639404297, 14.983709335327148, 15.246581077575684, 15.509452819824219, 15.77232551574707, 16.03519630432129, 16.29806900024414, 16.560941696166992, 16.823814392089844, 17.086685180664062, 17.349557876586914, 17.612430572509766, 17.875301361083984, 18.138174057006836, 18.401046752929688, 18.663917541503906, 18.926790237426758, 19.18966293334961, 19.452533721923828, 19.71540641784668, 19.97827911376953, 20.24114990234375, 20.5040225982666, 20.766895294189453, 21.029766082763672, 21.292638778686523, 21.555511474609375, 21.818382263183594, 22.081254959106445, 22.344127655029297, 22.606998443603516, 22.869871139526367, 23.13274383544922, 23.39561653137207, 23.65848731994629, 23.92136001586914, 24.184232711791992, 24.44710350036621, 24.709976196289062, 24.972848892211914, 25.235719680786133, 25.498592376708984, 25.761465072631836, 26.024335861206055, 26.287208557128906, 26.550081253051758, 26.812952041625977, 27.075824737548828, 27.33869743347168, 27.6015682220459, 27.86444091796875, 28.1273136138916, 28.39018440246582, 28.653057098388672, 28.915929794311523, 29.178800582885742, 29.441673278808594, 29.704545974731445, 29.967418670654297, 30.230289459228516, 30.493162155151367, 30.75603485107422, 31.018905639648438, 31.28177833557129, 31.54465103149414, 31.80752182006836, 32.07039260864258, 32.33326721191406, 32.59613800048828, 32.8590087890625, 33.121883392333984, 33.3847541809082, 33.64762878417969, 33.910499572753906, 34.173370361328125, 34.43624496459961, 34.69911575317383, 34.96198654174805, 35.22486114501953, 35.48773193359375, 35.75060272216797, 36.01347732543945, 36.27634811401367, 36.53921890258789, 36.802093505859375, 37.064964294433594], "55": [5.75929069519043, 6.021076679229736, 6.282862663269043, 6.54464864730835, 6.806434154510498, 7.068220138549805, 7.330006122589111, 7.591792106628418, 7.853578090667725, 8.115364074707031, 8.37714958190918, 8.638936042785645, 8.900721549987793, 9.162508010864258, 9.424293518066406, 9.686079978942871, 9.94786548614502, 10.209651947021484, 10.471437454223633, 10.733223915100098, 10.995009422302246, 11.256794929504395, 11.51858139038086, 11.780366897583008, 12.042153358459473, 12.303938865661621, 12.565725326538086, 12.827510833740234, 13.0892972946167, 13.351082801818848, 13.612868309020996, 13.874654769897461, 14.13644027709961, 14.398226737976074, 14.660012245178223, 14.921798706054688, 15.183584213256836, 15.4453706741333, 15.70715618133545, 15.968942642211914, 16.230728149414062, 16.49251365661621, 16.75429916381836, 17.01608657836914, 17.27787208557129, 17.539657592773438, 17.801443099975586, 18.063230514526367, 18.325016021728516, 18.586801528930664, 18.848587036132812, 19.11037254333496, 19.372159957885742, 19.63394546508789, 19.89573097229004, 20.157516479492188, 20.41930389404297, 20.681089401245117, 20.942874908447266, 21.204660415649414, 21.466447830200195, 21.728233337402344, 21.990018844604492, 22.25180435180664, 22.51358985900879, 22.77537727355957, 23.03716278076172, 23.298948287963867, 23.560733795166016, 23.822521209716797, 24.084306716918945, 24.346092224121094, 24.607877731323242, 24.86966323852539, 25.131450653076172, 25.39323616027832, 25.65502166748047, 25.916807174682617, 26.1785945892334, 26.440380096435547, 26.702165603637695, 26.963951110839844, 27.225736618041992, 27.487524032592773, 27.749309539794922, 28.01109504699707, 28.27288055419922, 28.53466796875, 28.79645347595215, 29.058238983154297, 29.320024490356445, 29.581811904907227, 29.843597412109375, 30.105382919311523, 30.367168426513672, 30.62895393371582, 30.8907413482666, 31.15252685546875, 31.4143123626709, 31.676097869873047, 31.937885284423828, 32.199668884277344, 32.461456298828125, 32.723243713378906, 32.98502731323242, 33.2468147277832, 33.50859832763672, 33.7703857421875, 34.03217315673828, 34.2939567565918, 34.55574417114258, 34.81753158569336, 35.079315185546875, 35.341102600097656, 35.60288619995117, 35.86467361450195, 36.126461029052734, 36.38824462890625, 36.65003204345703, 36.91181564331055], "56": [5.735613822937012, 5.996323585510254, 6.257033348083496, 6.517743110656738, 6.7784528732299805, 7.039162635803223, 7.299872398376465, 7.560582160949707, 7.821291446685791, 8.082001686096191, 8.342711448669434, 8.603421211242676, 8.864130973815918, 9.12484073638916, 9.385549545288086, 9.646259307861328, 9.90696907043457, 10.167678833007812, 10.428388595581055, 10.689098358154297, 10.949808120727539, 11.210517883300781, 11.471227645874023, 11.731937408447266, 11.992647171020508, 12.25335693359375, 12.514066696166992, 12.774776458740234, 13.035486221313477, 13.296195983886719, 13.556905746459961, 13.817615509033203, 14.078325271606445, 14.339035034179688, 14.59974479675293, 14.860454559326172, 15.121164321899414, 15.381874084472656, 15.642582893371582, 15.903292655944824, 16.164003372192383, 16.424713134765625, 16.685422897338867, 16.94613265991211, 17.20684242248535, 17.467552185058594, 17.728261947631836, 17.988971710205078, 18.24968147277832, 18.51038932800293, 18.771099090576172, 19.031808853149414, 19.292518615722656, 19.5532283782959, 19.81393814086914, 20.074647903442383, 20.335357666015625, 20.596067428588867, 20.85677719116211, 21.11748695373535, 21.378196716308594, 21.638906478881836, 21.899616241455078, 22.16032600402832, 22.421035766601562, 22.681745529174805, 22.942455291748047, 23.20316505432129, 23.46387481689453, 23.724584579467773, 23.985294342041016, 24.246004104614258, 24.5067138671875, 24.767423629760742, 25.028133392333984, 25.288843154907227, 25.54955291748047, 25.81026268005371, 26.070972442626953, 26.331682205200195, 26.592391967773438, 26.85310173034668, 27.113811492919922, 27.374521255493164, 27.635231018066406, 27.89594078063965, 28.15665054321289, 28.417360305786133, 28.678070068359375, 28.938779830932617, 29.19948959350586, 29.4601993560791, 29.720909118652344, 29.981618881225586, 30.242328643798828, 30.50303840637207, 30.763748168945312, 31.024456024169922, 31.285165786743164, 31.545875549316406, 31.80658531188965, 32.06729507446289, 32.328006744384766, 32.588714599609375, 32.84942626953125, 33.11013412475586, 33.370845794677734, 33.631553649902344, 33.89226531982422, 34.15297317504883, 34.4136848449707, 34.67439270019531, 34.93510437011719, 35.1958122253418, 35.45652389526367, 35.71723175048828, 35.977943420410156, 36.238651275634766, 36.49936294555664, 36.76007080078125], "57": [5.71215295791626, 5.971796035766602, 6.231439590454102, 6.491082668304443, 6.750726222991943, 7.010369300842285, 7.270012855529785, 7.529655933380127, 7.789299011230469, 8.048942565917969, 8.308586120605469, 8.568228721618652, 8.827872276306152, 9.087515830993652, 9.347159385681152, 9.606801986694336, 9.866445541381836, 10.126089096069336, 10.385732650756836, 10.64537525177002, 10.90501880645752, 11.16466236114502, 11.42430591583252, 11.683948516845703, 11.943592071533203, 12.203235626220703, 12.462879180908203, 12.722521781921387, 12.982165336608887, 13.241808891296387, 13.501452445983887, 13.76109504699707, 14.02073860168457, 14.28038215637207, 14.54002571105957, 14.799668312072754, 15.059311866760254, 15.318955421447754, 15.578598022460938, 15.838241577148438, 16.097885131835938, 16.357528686523438, 16.617172241210938, 16.876815795898438, 17.136457443237305, 17.396100997924805, 17.655744552612305, 17.915388107299805, 18.175031661987305, 18.434675216674805, 18.694318771362305, 18.953962326049805, 19.213603973388672, 19.473247528076172, 19.732891082763672, 19.992534637451172, 20.252178192138672, 20.511821746826172, 20.771465301513672, 21.031108856201172, 21.29075050354004, 21.55039405822754, 21.81003761291504, 22.06968116760254, 22.32932472229004, 22.58896827697754, 22.84861183166504, 23.108253479003906, 23.367897033691406, 23.627540588378906, 23.887184143066406, 24.146827697753906, 24.406471252441406, 24.666114807128906, 24.925758361816406, 25.185400009155273, 25.445043563842773, 25.704687118530273, 25.964330673217773, 26.223974227905273, 26.483617782592773, 26.743261337280273, 27.002904891967773, 27.26254653930664, 27.52219009399414, 27.78183364868164, 28.04147720336914, 28.30112075805664, 28.56076431274414, 28.82040786743164, 29.08005142211914, 29.339693069458008, 29.599336624145508, 29.858980178833008, 30.118623733520508, 30.378267288208008, 30.637910842895508, 30.897554397583008, 31.157196044921875, 31.416839599609375, 31.676483154296875, 31.936126708984375, 32.195770263671875, 32.455413818359375, 32.715057373046875, 32.974700927734375, 33.234344482421875, 33.493988037109375, 33.753631591796875, 34.013275146484375, 34.27291488647461, 34.53255844116211, 34.79220199584961, 35.05184555053711, 35.31148910522461, 35.57113265991211, 35.83077621459961, 36.09041976928711, 36.35006332397461, 36.60970687866211], "58": [5.688904285430908, 5.94749116897583, 6.206077575683594, 6.464663982391357, 6.723250865936279, 6.981837272644043, 7.240423679351807, 7.4990105628967285, 7.757596969604492, 8.016183853149414, 8.27476978302002, 8.533356666564941, 8.791943550109863, 9.050529479980469, 9.30911636352539, 9.567703247070312, 9.826289176940918, 10.08487606048584, 10.343462944030762, 10.602048873901367, 10.860635757446289, 11.119222640991211, 11.377808570861816, 11.636395454406738, 11.89498233795166, 12.153568267822266, 12.412155151367188, 12.67074203491211, 12.929327964782715, 13.187914848327637, 13.446501731872559, 13.705087661743164, 13.963674545288086, 14.222261428833008, 14.480847358703613, 14.739434242248535, 14.998021125793457, 15.256607055664062, 15.515193939208984, 15.773780822753906, 16.032367706298828, 16.29095458984375, 16.54953956604004, 16.80812644958496, 17.066713333129883, 17.325300216674805, 17.583887100219727, 17.84247398376465, 18.101058959960938, 18.35964584350586, 18.61823272705078, 18.876819610595703, 19.135406494140625, 19.393993377685547, 19.652578353881836, 19.911165237426758, 20.16975212097168, 20.4283390045166, 20.686925888061523, 20.945512771606445, 21.204097747802734, 21.462684631347656, 21.721271514892578, 21.9798583984375, 22.238445281982422, 22.497032165527344, 22.755617141723633, 23.014204025268555, 23.272790908813477, 23.5313777923584, 23.78996467590332, 24.048551559448242, 24.30713653564453, 24.565723419189453, 24.824310302734375, 25.082897186279297, 25.34148406982422, 25.60007095336914, 25.85865592956543, 26.11724281311035, 26.375829696655273, 26.634416580200195, 26.893003463745117, 27.15159034729004, 27.410175323486328, 27.66876220703125, 27.927349090576172, 28.185935974121094, 28.444522857666016, 28.703109741210938, 28.961694717407227, 29.22028160095215, 29.47886848449707, 29.737455368041992, 29.996042251586914, 30.254629135131836, 30.513214111328125, 30.771800994873047, 31.03038787841797, 31.28897476196289, 31.547561645507812, 31.806148529052734, 32.064735412597656, 32.32332229614258, 32.5819091796875, 32.840492248535156, 33.09907913208008, 33.357666015625, 33.61625289916992, 33.874839782714844, 34.133426666259766, 34.39201354980469, 34.65060043334961, 34.90918731689453, 35.16777420043945, 35.426361083984375, 35.6849479675293, 35.94353103637695, 36.202117919921875, 36.4607048034668], "59": [5.665866374969482, 5.923405647277832, 6.180944919586182, 6.438484191894531, 6.696023941040039, 6.953563213348389, 7.211102485656738, 7.468641757965088, 7.7261810302734375, 7.983720779418945, 8.241259574890137, 8.498799324035645, 8.756339073181152, 9.013877868652344, 9.271417617797852, 9.528956413269043, 9.78649616241455, 10.044035911560059, 10.30157470703125, 10.559114456176758, 10.816654205322266, 11.074193000793457, 11.331732749938965, 11.589271545410156, 11.846811294555664, 12.104351043701172, 12.361889839172363, 12.619429588317871, 12.876968383789062, 13.13450813293457, 13.392047882080078, 13.64958667755127, 13.907126426696777, 14.164665222167969, 14.422204971313477, 14.679744720458984, 14.937283515930176, 15.194823265075684, 15.452362060546875, 15.709901809692383, 15.96744155883789, 16.2249813079834, 16.482519149780273, 16.74005889892578, 16.99759864807129, 17.255138397216797, 17.512678146362305, 17.77021598815918, 18.027755737304688, 18.285295486450195, 18.542835235595703, 18.80037498474121, 19.057912826538086, 19.315452575683594, 19.5729923248291, 19.83053207397461, 20.088071823120117, 20.345609664916992, 20.6031494140625, 20.860689163208008, 21.118228912353516, 21.375768661499023, 21.63330841064453, 21.890846252441406, 22.148386001586914, 22.405925750732422, 22.66346549987793, 22.921005249023438, 23.178543090820312, 23.43608283996582, 23.693622589111328, 23.951162338256836, 24.208702087402344, 24.46623992919922, 24.723779678344727, 24.981319427490234, 25.238859176635742, 25.49639892578125, 25.753936767578125, 26.011476516723633, 26.26901626586914, 26.52655601501465, 26.784095764160156, 27.04163360595703, 27.29917335510254, 27.556713104248047, 27.814252853393555, 28.071792602539062, 28.329330444335938, 28.586870193481445, 28.844409942626953, 29.10194969177246, 29.35948944091797, 29.617027282714844, 29.87456703186035, 30.13210678100586, 30.389646530151367, 30.647186279296875, 30.90472412109375, 31.162263870239258, 31.419803619384766, 31.677343368530273, 31.93488311767578, 32.192420959472656, 32.4499626159668, 32.70750045776367, 32.96503829956055, 33.22257995605469, 33.48011779785156, 33.7376594543457, 33.99519729614258, 34.25273513793945, 34.510276794433594, 34.76781463623047, 35.02535629272461, 35.282894134521484, 35.54043197631836, 35.7979736328125, 36.055511474609375, 36.313053131103516], "60": [5.643035411834717, 5.899537086486816, 6.156038761138916, 6.412539958953857, 6.669041633605957, 6.925543308258057, 7.182044982910156, 7.438546657562256, 7.6950483322143555, 7.951550006866455, 8.208051681518555, 8.464552879333496, 8.721055030822754, 8.977556228637695, 9.234057426452637, 9.490559577941895, 9.747060775756836, 10.003562927246094, 10.260064125061035, 10.516566276550293, 10.773067474365234, 11.029568672180176, 11.286070823669434, 11.542572021484375, 11.799074172973633, 12.055575370788574, 12.312077522277832, 12.568578720092773, 12.825079917907715, 13.081582069396973, 13.338083267211914, 13.594585418701172, 13.851086616516113, 14.107588768005371, 14.364089965820312, 14.620591163635254, 14.877093315124512, 15.133594512939453, 15.390096664428711, 15.646597862243652, 15.90310001373291, 16.15960121154785, 16.41610336303711, 16.672603607177734, 16.929105758666992, 17.18560791015625, 17.442110061645508, 17.698610305786133, 17.95511245727539, 18.21161460876465, 18.468114852905273, 18.72461700439453, 18.98111915588379, 19.237621307373047, 19.494121551513672, 19.75062370300293, 20.007125854492188, 20.263626098632812, 20.52012825012207, 20.776630401611328, 21.033132553100586, 21.28963279724121, 21.54613494873047, 21.802637100219727, 22.05913734436035, 22.31563949584961, 22.572141647338867, 22.828643798828125, 23.08514404296875, 23.341646194458008, 23.598148345947266, 23.85464859008789, 24.11115074157715, 24.367652893066406, 24.624155044555664, 24.88065528869629, 25.137157440185547, 25.393659591674805, 25.65015983581543, 25.906661987304688, 26.163164138793945, 26.419666290283203, 26.676166534423828, 26.932668685913086, 27.189170837402344, 27.44567108154297, 27.702173233032227, 27.958675384521484, 28.215177536010742, 28.471677780151367, 28.728179931640625, 28.984682083129883, 29.241182327270508, 29.497684478759766, 29.754186630249023, 30.01068878173828, 30.267189025878906, 30.523691177368164, 30.780193328857422, 31.036693572998047, 31.293195724487305, 31.549697875976562, 31.80620002746582, 32.06270217895508, 32.3192024230957, 32.57570266723633, 32.83220672607422, 33.088706970214844, 33.34520721435547, 33.60171127319336, 33.858211517333984, 34.114715576171875, 34.3712158203125, 34.627716064453125, 34.884220123291016, 35.14072036743164, 35.397220611572266, 35.653724670410156, 35.91022491455078, 36.166725158691406], "61": [5.62040901184082, 5.875882148742676, 6.131355285644531, 6.386828422546387, 6.642301559448242, 6.897774696350098, 7.153247833251953, 7.408720970153809, 7.664194107055664, 7.9196672439575195, 8.175140380859375, 8.43061351776123, 8.686086654663086, 8.941559791564941, 9.197032928466797, 9.452506065368652, 9.707979202270508, 9.963452339172363, 10.218925476074219, 10.474398612976074, 10.72987174987793, 10.985344886779785, 11.24081802368164, 11.496291160583496, 11.751764297485352, 12.007237434387207, 12.262710571289062, 12.518183708190918, 12.773656845092773, 13.029129981994629, 13.284603118896484, 13.54007625579834, 13.795549392700195, 14.05102252960205, 14.306495666503906, 14.561968803405762, 14.817441940307617, 15.072915077209473, 15.328388214111328, 15.583861351013184, 15.839334487915039, 16.09480857849121, 16.35028076171875, 16.605754852294922, 16.86122703552246, 17.116701126098633, 17.372173309326172, 17.627647399902344, 17.883119583129883, 18.138593673706055, 18.394065856933594, 18.649539947509766, 18.905012130737305, 19.160486221313477, 19.415958404541016, 19.671432495117188, 19.926904678344727, 20.1823787689209, 20.437850952148438, 20.69332504272461, 20.94879722595215, 21.20427131652832, 21.45974349975586, 21.71521759033203, 21.97068977355957, 22.226163864135742, 22.48163604736328, 22.737110137939453, 22.992582321166992, 23.248056411743164, 23.503528594970703, 23.759002685546875, 24.014474868774414, 24.269948959350586, 24.525421142578125, 24.780895233154297, 25.036367416381836, 25.291841506958008, 25.547313690185547, 25.80278778076172, 26.058259963989258, 26.31373405456543, 26.56920623779297, 26.82468032836914, 27.08015251159668, 27.33562660217285, 27.59109878540039, 27.846572875976562, 28.1020450592041, 28.357519149780273, 28.612991333007812, 28.868465423583984, 29.123937606811523, 29.379411697387695, 29.634883880615234, 29.890357971191406, 30.145830154418945, 30.401304244995117, 30.656776428222656, 30.912250518798828, 31.167722702026367, 31.42319679260254, 31.678668975830078, 31.93414306640625, 32.18961715698242, 32.44508743286133, 32.7005615234375, 32.95603561401367, 33.211509704589844, 33.46697998046875, 33.72245407104492, 33.977928161621094, 34.233402252197266, 34.48887252807617, 34.744346618652344, 34.999820709228516, 35.25529479980469, 35.510765075683594, 35.766239166259766, 36.02171325683594], "62": [5.597984790802002, 5.852438926696777, 6.1068925857543945, 6.36134672164917, 6.615800380706787, 6.870254039764404, 7.12470817565918, 7.379161834716797, 7.633615970611572, 7.8880696296691895, 8.142523765563965, 8.396977424621582, 8.6514310836792, 8.905884742736816, 9.16033935546875, 9.414793014526367, 9.669246673583984, 9.923700332641602, 10.178153991699219, 10.432608604431152, 10.68706226348877, 10.941515922546387, 11.195969581604004, 11.450424194335938, 11.704877853393555, 11.959331512451172, 12.213785171508789, 12.468238830566406, 12.72269344329834, 12.977147102355957, 13.231600761413574, 13.486054420471191, 13.740508079528809, 13.994962692260742, 14.24941635131836, 14.503870010375977, 14.758323669433594, 15.012777328491211, 15.267231941223145, 15.521685600280762, 15.776139259338379, 16.030593872070312, 16.28504753112793, 16.539501190185547, 16.793954849243164, 17.04840850830078, 17.3028621673584, 17.557315826416016, 17.811769485473633, 18.066225051879883, 18.3206787109375, 18.575132369995117, 18.829586029052734, 19.08403968811035, 19.33849334716797, 19.592947006225586, 19.847400665283203, 20.10185432434082, 20.356307983398438, 20.610763549804688, 20.865217208862305, 21.119670867919922, 21.37412452697754, 21.628578186035156, 21.883031845092773, 22.13748550415039, 22.391939163208008, 22.646392822265625, 22.900848388671875, 23.155302047729492, 23.40975570678711, 23.664209365844727, 23.918663024902344, 24.17311668395996, 24.427570343017578, 24.682024002075195, 24.936477661132812, 25.19093132019043, 25.44538688659668, 25.699840545654297, 25.954294204711914, 26.20874786376953, 26.46320152282715, 26.717655181884766, 26.972108840942383, 27.2265625, 27.481016159057617, 27.735471725463867, 27.989925384521484, 28.2443790435791, 28.49883270263672, 28.753286361694336, 29.007740020751953, 29.26219367980957, 29.516647338867188, 29.771100997924805, 30.025554656982422, 30.280010223388672, 30.53446388244629, 30.788917541503906, 31.043371200561523, 31.29782485961914, 31.552278518676758, 31.806732177734375, 32.061187744140625, 32.31563949584961, 32.57009506225586, 32.824546813964844, 33.079002380371094, 33.33345413208008, 33.58790969848633, 33.84236526489258, 34.09681701660156, 34.35127258300781, 34.6057243347168, 34.86017990112305, 35.11463165283203, 35.36908721923828, 35.623538970947266, 35.877994537353516], "63": [5.575760364532471, 5.829204082489014, 6.082647323608398, 6.336091041564941, 6.589534759521484, 6.842978477478027, 7.09642219543457, 7.349865913391113, 7.603309631347656, 7.856752872467041, 8.110197067260742, 8.363640785217285, 8.617083549499512, 8.870527267456055, 9.123970985412598, 9.37741470336914, 9.630858421325684, 9.884302139282227, 10.13774585723877, 10.391189575195312, 10.644633293151855, 10.898077011108398, 11.151520729064941, 11.404964447021484, 11.658408164978027, 11.911850929260254, 12.165294647216797, 12.41873836517334, 12.672182083129883, 12.925625801086426, 13.179069519042969, 13.432513236999512, 13.685956954956055, 13.939400672912598, 14.19284439086914, 14.446288108825684, 14.699731826782227, 14.95317554473877, 15.206619262695312, 15.460062026977539, 15.713505744934082, 15.966949462890625, 16.220394134521484, 16.47383689880371, 16.72728157043457, 16.980724334716797, 17.234167098999023, 17.487611770629883, 17.74105453491211, 17.99449920654297, 18.247941970825195, 18.501386642456055, 18.75482940673828, 19.00827407836914, 19.261716842651367, 19.515161514282227, 19.768604278564453, 20.022048950195312, 20.27549171447754, 20.528934478759766, 20.782379150390625, 21.03582191467285, 21.28926658630371, 21.542709350585938, 21.796154022216797, 22.049596786499023, 22.303041458129883, 22.55648422241211, 22.80992889404297, 23.063371658325195, 23.316816329956055, 23.57025909423828, 23.823701858520508, 24.077146530151367, 24.330589294433594, 24.584033966064453, 24.83747673034668, 25.09092140197754, 25.344364166259766, 25.597808837890625, 25.85125160217285, 26.10469627380371, 26.358139038085938, 26.611583709716797, 26.865026473999023, 27.11846923828125, 27.37191390991211, 27.625356674194336, 27.878801345825195, 28.132244110107422, 28.38568878173828, 28.639131546020508, 28.892576217651367, 29.146018981933594, 29.399463653564453, 29.65290641784668, 29.90635108947754, 30.159793853759766, 30.413238525390625, 30.66668128967285, 30.920124053955078, 31.173568725585938, 31.427011489868164, 31.680456161499023, 31.93389892578125, 32.18734359741211, 32.44078826904297, 32.69422912597656, 32.94767379760742, 33.20111846923828, 33.45456314086914, 33.708003997802734, 33.961448669433594, 34.21489334106445, 34.46833419799805, 34.721778869628906, 34.975223541259766, 35.228668212890625, 35.48210906982422, 35.73555374145508], "64": [5.553732395172119, 5.8061747550964355, 6.058617115020752, 6.311059474945068, 6.563501834869385, 6.815944194793701, 7.068386554718018, 7.320828914642334, 7.57327127456665, 7.825714111328125, 8.078156471252441, 8.330598831176758, 8.583041191101074, 8.83548355102539, 9.087925910949707, 9.340368270874023, 9.59281063079834, 9.845252990722656, 10.097695350646973, 10.350137710571289, 10.602580070495605, 10.855022430419922, 11.107464790344238, 11.359907150268555, 11.612349510192871, 11.864791870117188, 12.117234230041504, 12.36967658996582, 12.622118949890137, 12.874561309814453, 13.12700366973877, 13.379446029663086, 13.631888389587402, 13.884330749511719, 14.136773109436035, 14.389215469360352, 14.641657829284668, 14.894100189208984, 15.1465425491333, 15.398985862731934, 15.65142822265625, 15.903870582580566, 16.156312942504883, 16.408754348754883, 16.661197662353516, 16.913639068603516, 17.16608238220215, 17.41852378845215, 17.67096710205078, 17.92340850830078, 18.175851821899414, 18.428293228149414, 18.680736541748047, 18.933177947998047, 19.18562126159668, 19.43806266784668, 19.690505981445312, 19.942947387695312, 20.195390701293945, 20.447834014892578, 20.700275421142578, 20.95271873474121, 21.20516014099121, 21.457603454589844, 21.710044860839844, 21.962488174438477, 22.214929580688477, 22.46737289428711, 22.71981430053711, 22.972257614135742, 23.224699020385742, 23.477142333984375, 23.729583740234375, 23.982027053833008, 24.234468460083008, 24.48691177368164, 24.73935317993164, 24.991796493530273, 25.244237899780273, 25.496681213378906, 25.749122619628906, 26.00156593322754, 26.25400733947754, 26.506450653076172, 26.758892059326172, 27.011335372924805, 27.263776779174805, 27.516220092773438, 27.768661499023438, 28.02110481262207, 28.27354621887207, 28.525989532470703, 28.778430938720703, 29.030874252319336, 29.283315658569336, 29.53575897216797, 29.78820037841797, 30.0406436920166, 30.2930850982666, 30.545528411865234, 30.797971725463867, 31.050413131713867, 31.3028564453125, 31.5552978515625, 31.807741165161133, 32.060184478759766, 32.312625885009766, 32.565067291259766, 32.817508697509766, 33.06995391845703, 33.32239532470703, 33.57483673095703, 33.82727813720703, 34.0797233581543, 34.3321647644043, 34.5846061706543, 34.8370475769043, 35.08949279785156, 35.34193420410156, 35.59437561035156], "65": [5.5318989753723145, 5.78334903717041, 6.034799098968506, 6.286249160766602, 6.537698745727539, 6.789148807525635, 7.0405988693237305, 7.292048931121826, 7.543498992919922, 7.794948577880859, 8.046399116516113, 8.29784870147705, 8.549298286437988, 8.800748825073242, 9.05219841003418, 9.303648948669434, 9.555098533630371, 9.806548118591309, 10.057998657226562, 10.3094482421875, 10.560897827148438, 10.812348365783691, 11.063797950744629, 11.315248489379883, 11.56669807434082, 11.818147659301758, 12.069598197937012, 12.32104778289795, 12.572498321533203, 12.82394790649414, 13.075397491455078, 13.326848030090332, 13.57829761505127, 13.829748153686523, 14.081197738647461, 14.332647323608398, 14.584097862243652, 14.83554744720459, 15.086997985839844, 15.338447570800781, 15.589897155761719, 15.841347694396973, 16.092798233032227, 16.344247817993164, 16.5956974029541, 16.84714698791504, 17.098596572875977, 17.350048065185547, 17.601497650146484, 17.852947235107422, 18.10439682006836, 18.355846405029297, 18.607297897338867, 18.858747482299805, 19.110197067260742, 19.36164665222168, 19.613096237182617, 19.864545822143555, 20.115997314453125, 20.367446899414062, 20.618896484375, 20.870346069335938, 21.121795654296875, 21.373247146606445, 21.624696731567383, 21.87614631652832, 22.127595901489258, 22.379045486450195, 22.630496978759766, 22.881946563720703, 23.13339614868164, 23.384845733642578, 23.636295318603516, 23.887746810913086, 24.139196395874023, 24.39064598083496, 24.6420955657959, 24.893545150756836, 25.144996643066406, 25.396446228027344, 25.64789581298828, 25.89934539794922, 26.150794982910156, 26.402246475219727, 26.653696060180664, 26.9051456451416, 27.15659523010254, 27.408044815063477, 27.659496307373047, 27.910945892333984, 28.162395477294922, 28.41384506225586, 28.665294647216797, 28.916746139526367, 29.168195724487305, 29.419645309448242, 29.67109489440918, 29.922544479370117, 30.173995971679688, 30.425445556640625, 30.676895141601562, 30.9283447265625, 31.179794311523438, 31.431245803833008, 31.682695388793945, 31.934144973754883, 32.18559646606445, 32.43704605102539, 32.68849563598633, 32.939945220947266, 33.1913948059082, 33.44284439086914, 33.69429397583008, 33.945743560791016, 34.19719314575195, 34.44864273071289, 34.700096130371094, 34.95154571533203, 35.20299530029297, 35.454444885253906], "66": [5.510257720947266, 5.760724067687988, 6.011190414428711, 6.261656761169434, 6.512122631072998, 6.762588977813721, 7.013055324554443, 7.263521671295166, 7.513988018035889, 7.764453887939453, 8.014920234680176, 8.265386581420898, 8.515852928161621, 8.766319274902344, 9.016785621643066, 9.267251968383789, 9.517718315124512, 9.768183708190918, 10.01865005493164, 10.269116401672363, 10.519582748413086, 10.770049095153809, 11.020515441894531, 11.270981788635254, 11.521448135375977, 11.7719144821167, 12.022380828857422, 12.272847175598145, 12.523313522338867, 12.773778915405273, 13.024245262145996, 13.274711608886719, 13.525177955627441, 13.775644302368164, 14.026110649108887, 14.27657699584961, 14.527043342590332, 14.777509689331055, 15.027976036071777, 15.2784423828125, 15.528907775878906, 15.779374122619629, 16.02984046936035, 16.28030776977539, 16.530773162841797, 16.781238555908203, 17.031705856323242, 17.28217124938965, 17.532638549804688, 17.783103942871094, 18.033571243286133, 18.28403663635254, 18.534503936767578, 18.784969329833984, 19.035436630249023, 19.28590202331543, 19.536367416381836, 19.786834716796875, 20.03730010986328, 20.28776741027832, 20.538232803344727, 20.788700103759766, 21.039165496826172, 21.28963279724121, 21.540098190307617, 21.790565490722656, 22.041030883789062, 22.2914981842041, 22.541963577270508, 22.792428970336914, 23.042896270751953, 23.29336166381836, 23.5438289642334, 23.794294357299805, 24.044761657714844, 24.29522705078125, 24.54569435119629, 24.796159744262695, 25.046627044677734, 25.29709243774414, 25.547557830810547, 25.798025131225586, 26.048490524291992, 26.29895782470703, 26.549423217773438, 26.799890518188477, 27.050355911254883, 27.300823211669922, 27.551288604736328, 27.801755905151367, 28.052221298217773, 28.30268669128418, 28.55315399169922, 28.803619384765625, 29.054086685180664, 29.30455207824707, 29.55501937866211, 29.805484771728516, 30.055952072143555, 30.30641746520996, 30.556884765625, 30.807350158691406, 31.057815551757812, 31.30828285217285, 31.558748245239258, 31.809215545654297, 32.0596809387207, 32.31014633178711, 32.56061553955078, 32.81108093261719, 33.061546325683594, 33.31201171875, 33.562477111816406, 33.81294631958008, 34.063411712646484, 34.31387710571289, 34.5643424987793, 34.81481170654297, 35.065277099609375, 35.31574249267578], "67": [5.488805770874023, 5.738296985626221, 5.987788200378418, 6.237279415130615, 6.4867706298828125, 6.73626184463501, 6.985753059387207, 7.235244274139404, 7.484735488891602, 7.734226703643799, 7.983717918395996, 8.233208656311035, 8.48270034790039, 8.73219108581543, 8.981682777404785, 9.231173515319824, 9.48066520690918, 9.730155944824219, 9.979647636413574, 10.229138374328613, 10.478629112243652, 10.728120803833008, 10.977611541748047, 11.227103233337402, 11.476593971252441, 11.726085662841797, 11.975576400756836, 12.225068092346191, 12.47455883026123, 12.724050521850586, 12.973541259765625, 13.22303295135498, 13.47252368927002, 13.722015380859375, 13.971506118774414, 14.220996856689453, 14.470488548278809, 14.719979286193848, 14.969470977783203, 15.218961715698242, 15.468453407287598, 15.717944145202637, 15.967435836791992, 16.21692657470703, 16.46641731262207, 16.715909957885742, 16.96540069580078, 17.21489143371582, 17.46438217163086, 17.7138729095459, 17.96336555480957, 18.21285629272461, 18.46234703063965, 18.711837768554688, 18.96133041381836, 19.2108211517334, 19.460311889648438, 19.709802627563477, 19.95929527282715, 20.208786010742188, 20.458276748657227, 20.707767486572266, 20.957258224487305, 21.206750869750977, 21.456241607666016, 21.705732345581055, 21.955223083496094, 22.204715728759766, 22.454206466674805, 22.703697204589844, 22.953187942504883, 23.202680587768555, 23.452171325683594, 23.701662063598633, 23.951152801513672, 24.200645446777344, 24.450136184692383, 24.699626922607422, 24.94911766052246, 25.1986083984375, 25.448101043701172, 25.69759178161621, 25.94708251953125, 26.19657325744629, 26.44606590270996, 26.695556640625, 26.94504737854004, 27.194538116455078, 27.44403076171875, 27.69352149963379, 27.943012237548828, 28.192502975463867, 28.441993713378906, 28.691486358642578, 28.940977096557617, 29.190467834472656, 29.439958572387695, 29.689451217651367, 29.938941955566406, 30.188432693481445, 30.437923431396484, 30.687416076660156, 30.936906814575195, 31.186397552490234, 31.435888290405273, 31.685379028320312, 31.934871673583984, 32.18436050415039, 32.43385314941406, 32.683345794677734, 32.93283462524414, 33.18232727050781, 33.431819915771484, 33.68130874633789, 33.93080139160156, 34.18029022216797, 34.42978286743164, 34.67927551269531, 34.92876434326172, 35.17825698852539], "68": [5.467541217803955, 5.716065883636475, 5.964590549468994, 6.213115215301514, 6.461639881134033, 6.710164546966553, 6.958689212799072, 7.207213878631592, 7.455738067626953, 7.704262733459473, 7.952787399291992, 8.201312065124512, 8.449836730957031, 8.69836139678955, 8.94688606262207, 9.19541072845459, 9.44393539428711, 9.692460060119629, 9.940984725952148, 10.189509391784668, 10.438034057617188, 10.68655776977539, 10.93508243560791, 11.18360710144043, 11.43213176727295, 11.680656433105469, 11.929181098937988, 12.177705764770508, 12.426230430603027, 12.674755096435547, 12.923279762268066, 13.171804428100586, 13.420329093933105, 13.668853759765625, 13.917378425598145, 14.165903091430664, 14.414427757263184, 14.662952423095703, 14.911476135253906, 15.160000801086426, 15.408525466918945, 15.657050132751465, 15.905574798583984, 16.15410041809082, 16.402624130249023, 16.65114974975586, 16.899673461914062, 17.148197174072266, 17.3967227935791, 17.645246505737305, 17.89377212524414, 18.142295837402344, 18.39082145690918, 18.639345169067383, 18.88787078857422, 19.136394500732422, 19.384920120239258, 19.63344383239746, 19.881969451904297, 20.1304931640625, 20.379018783569336, 20.62754249572754, 20.876068115234375, 21.124591827392578, 21.37311553955078, 21.621641159057617, 21.87016487121582, 22.118690490722656, 22.36721420288086, 22.615739822387695, 22.8642635345459, 23.112789154052734, 23.361312866210938, 23.609838485717773, 23.858362197875977, 24.106887817382812, 24.355411529541016, 24.60393714904785, 24.852460861206055, 25.10098648071289, 25.349510192871094, 25.598033905029297, 25.846559524536133, 26.095083236694336, 26.343608856201172, 26.592132568359375, 26.84065818786621, 27.089181900024414, 27.33770751953125, 27.586231231689453, 27.83475685119629, 28.083280563354492, 28.331806182861328, 28.58032989501953, 28.828855514526367, 29.07737922668457, 29.325904846191406, 29.57442855834961, 29.822952270507812, 30.07147789001465, 30.32000160217285, 30.568527221679688, 30.81705093383789, 31.065576553344727, 31.31410026550293, 31.562625885009766, 31.81114959716797, 32.05967330932617, 32.30820083618164, 32.556724548339844, 32.80524826049805, 33.05377197265625, 33.30229949951172, 33.55082321166992, 33.799346923828125, 34.04787063598633, 34.29639434814453, 34.544921875, 34.7934455871582, 35.041969299316406], "69": [5.4464616775512695, 5.694028377532959, 5.94159460067749, 6.18916130065918, 6.436727523803711, 6.684293746948242, 6.931860446929932, 7.179426670074463, 7.426993370056152, 7.674559593200684, 7.922126293182373, 8.169692993164062, 8.417259216308594, 8.664825439453125, 8.912391662597656, 9.159958839416504, 9.407525062561035, 9.655091285705566, 9.902657508850098, 10.150223731994629, 10.397790908813477, 10.645357131958008, 10.892923355102539, 11.14048957824707, 11.388056755065918, 11.63562297821045, 11.88318920135498, 12.130755424499512, 12.37832260131836, 12.62588882446289, 12.873455047607422, 13.121021270751953, 13.368587493896484, 13.616154670715332, 13.863720893859863, 14.111287117004395, 14.358853340148926, 14.606420516967773, 14.853986740112305, 15.101552963256836, 15.349119186401367, 15.596686363220215, 15.844252586364746, 16.09181785583496, 16.339385986328125, 16.586952209472656, 16.834518432617188, 17.08208465576172, 17.32965087890625, 17.57721710205078, 17.824783325195312, 18.072349548339844, 18.319917678833008, 18.56748390197754, 18.81505012512207, 19.0626163482666, 19.310182571411133, 19.557748794555664, 19.805315017700195, 20.052881240844727, 20.300447463989258, 20.548015594482422, 20.795581817626953, 21.043148040771484, 21.290714263916016, 21.538280487060547, 21.785846710205078, 22.03341293334961, 22.28097915649414, 22.528545379638672, 22.776113510131836, 23.023679733276367, 23.2712459564209, 23.51881217956543, 23.76637840270996, 24.013944625854492, 24.261510848999023, 24.509077072143555, 24.75664520263672, 25.00421142578125, 25.25177764892578, 25.499343872070312, 25.746910095214844, 25.994476318359375, 26.242042541503906, 26.489608764648438, 26.73717498779297, 26.984743118286133, 27.232309341430664, 27.479875564575195, 27.727441787719727, 27.975008010864258, 28.22257423400879, 28.47014045715332, 28.71770668029785, 28.965272903442383, 29.212841033935547, 29.460407257080078, 29.70797348022461, 29.95553970336914, 30.203105926513672, 30.450672149658203, 30.698238372802734, 30.945804595947266, 31.19337272644043, 31.44093894958496, 31.688505172729492, 31.936071395874023, 32.18363571166992, 32.43120574951172, 32.67877197265625, 32.92633819580078, 33.17390441894531, 33.421470642089844, 33.669036865234375, 33.916603088378906, 34.16416931152344, 34.41173553466797, 34.6593017578125, 34.90686798095703], "70": [5.425564765930176, 5.672181129455566, 5.918797969818115, 6.165414333343506, 6.412031173706055, 6.658647537231445, 6.905263900756836, 7.151880741119385, 7.398497104644775, 7.645113945007324, 7.891730308532715, 8.138346672058105, 8.384963989257812, 8.631580352783203, 8.878196716308594, 9.124813079833984, 9.371429443359375, 9.618046760559082, 9.864663124084473, 10.111279487609863, 10.357895851135254, 10.604513168334961, 10.851129531860352, 11.097745895385742, 11.344362258911133, 11.590978622436523, 11.83759593963623, 12.084212303161621, 12.330828666687012, 12.577445030212402, 12.82406234741211, 13.0706787109375, 13.31729507446289, 13.563911437988281, 13.810527801513672, 14.057145118713379, 14.30376148223877, 14.55037784576416, 14.79699420928955, 15.043611526489258, 15.290227890014648, 15.536844253540039, 15.78346061706543, 16.03007698059082, 16.27669334411621, 16.5233097076416, 16.769927978515625, 17.016544342041016, 17.263160705566406, 17.509777069091797, 17.756393432617188, 18.003009796142578, 18.24962615966797, 18.49624252319336, 18.74285888671875, 18.989477157592773, 19.236093521118164, 19.482709884643555, 19.729326248168945, 19.975942611694336, 20.222558975219727, 20.469175338745117, 20.715791702270508, 20.9624080657959, 21.209026336669922, 21.455642700195312, 21.702259063720703, 21.948875427246094, 22.195491790771484, 22.442108154296875, 22.688724517822266, 22.935340881347656, 23.181957244873047, 23.42857551574707, 23.67519187927246, 23.92180824279785, 24.168424606323242, 24.415040969848633, 24.661657333374023, 24.908273696899414, 25.154890060424805, 25.401506423950195, 25.64812469482422, 25.89474105834961, 26.141357421875, 26.38797378540039, 26.63459014892578, 26.881206512451172, 27.127822875976562, 27.374439239501953, 27.621055603027344, 27.867673873901367, 28.114290237426758, 28.36090660095215, 28.60752296447754, 28.85413932800293, 29.10075569152832, 29.34737205505371, 29.5939884185791, 29.840604782104492, 30.087223052978516, 30.333839416503906, 30.580455780029297, 30.827072143554688, 31.073688507080078, 31.32030487060547, 31.56692123413086, 31.81353759765625, 32.06015396118164, 32.30677032470703, 32.55338668823242, 32.80000305175781, 33.0466194152832, 33.29323959350586, 33.53985595703125, 33.78647232055664, 34.03308868408203, 34.27970504760742, 34.52632141113281, 34.7729377746582], "71": [5.404848098754883, 5.650522708892822, 5.89619779586792, 6.141872882843018, 6.387547492980957, 6.633222579956055, 6.878897190093994, 7.124572277069092, 7.3702473640441895, 7.615921974182129, 7.861597061157227, 8.107272148132324, 8.352947235107422, 8.598621368408203, 8.8442964553833, 9.089971542358398, 9.335646629333496, 9.581321716308594, 9.826995849609375, 10.072670936584473, 10.31834602355957, 10.564021110534668, 10.809696197509766, 11.055370330810547, 11.301045417785645, 11.546720504760742, 11.79239559173584, 12.038070678710938, 12.283745765686035, 12.529419898986816, 12.775094985961914, 13.020770072937012, 13.26644515991211, 13.512120246887207, 13.757794380187988, 14.003469467163086, 14.249144554138184, 14.494819641113281, 14.740494728088379, 14.98616886138916, 15.231843948364258, 15.477519035339355, 15.723194122314453, 15.96886920928955, 16.21454429626465, 16.46021842956543, 16.705894470214844, 16.951568603515625, 17.197242736816406, 17.44291877746582, 17.6885929107666, 17.934268951416016, 18.179943084716797, 18.425617218017578, 18.671293258666992, 18.916967391967773, 19.162643432617188, 19.40831756591797, 19.65399169921875, 19.899667739868164, 20.145341873168945, 20.39101791381836, 20.63669204711914, 20.882366180419922, 21.128042221069336, 21.373716354370117, 21.61939239501953, 21.865066528320312, 22.110740661621094, 22.356416702270508, 22.60209083557129, 22.847766876220703, 23.093441009521484, 23.339115142822266, 23.58479118347168, 23.83046531677246, 24.076141357421875, 24.321815490722656, 24.56749153137207, 24.81316566467285, 25.058839797973633, 25.304515838623047, 25.550189971923828, 25.795866012573242, 26.041540145874023, 26.287214279174805, 26.53289031982422, 26.778564453125, 27.024240493774414, 27.269914627075195, 27.515588760375977, 27.76126480102539, 28.006938934326172, 28.252614974975586, 28.498289108276367, 28.74396324157715, 28.989639282226562, 29.235313415527344, 29.480989456176758, 29.72666358947754, 29.97233772277832, 30.218013763427734, 30.463687896728516, 30.70936393737793, 30.95503807067871, 31.200712203979492, 31.446388244628906, 31.692062377929688, 31.9377384185791, 32.183414459228516, 32.4290885925293, 32.67476272583008, 32.92043685913086, 33.16611099243164, 33.41178894042969, 33.65746307373047, 33.90313720703125, 34.14881134033203, 34.39448547363281, 34.64016342163086], "72": [5.3843092918396, 5.6290507316589355, 5.8737921714782715, 6.118533134460449, 6.363274574279785, 6.608016014099121, 6.852757453918457, 7.097498416900635, 7.342239856719971, 7.586981296539307, 7.831722736358643, 8.07646369934082, 8.321205139160156, 8.565946578979492, 8.810688018798828, 9.055429458618164, 9.3001708984375, 9.544912338256836, 9.789653778076172, 10.034394264221191, 10.279135704040527, 10.523877143859863, 10.7686185836792, 11.013360023498535, 11.258101463317871, 11.502842903137207, 11.747584342956543, 11.992324829101562, 12.237066268920898, 12.481807708740234, 12.72654914855957, 12.971290588378906, 13.216032028198242, 13.460773468017578, 13.705514907836914, 13.95025634765625, 14.19499683380127, 14.439738273620605, 14.684479713439941, 14.929221153259277, 15.173962593078613, 15.41870403289795, 15.663445472717285, 15.908186912536621, 16.15292739868164, 16.397668838500977, 16.642410278320312, 16.88715171813965, 17.131893157958984, 17.37663459777832, 17.621376037597656, 17.866117477416992, 18.110858917236328, 18.355600357055664, 18.600341796875, 18.845083236694336, 19.089824676513672, 19.334566116333008, 19.579307556152344, 19.824047088623047, 20.068788528442383, 20.31352996826172, 20.558271408081055, 20.80301284790039, 21.047754287719727, 21.292495727539062, 21.5372371673584, 21.781978607177734, 22.02672004699707, 22.271461486816406, 22.516202926635742, 22.760944366455078, 23.005685806274414, 23.25042724609375, 23.495168685913086, 23.739910125732422, 23.984649658203125, 24.22939109802246, 24.474132537841797, 24.718873977661133, 24.96361541748047, 25.208356857299805, 25.45309829711914, 25.697839736938477, 25.942581176757812, 26.18732261657715, 26.432064056396484, 26.67680549621582, 26.921546936035156, 27.166288375854492, 27.411029815673828, 27.655771255493164, 27.9005126953125, 28.145254135131836, 28.38999366760254, 28.634735107421875, 28.87947654724121, 29.124217987060547, 29.368959426879883, 29.61370086669922, 29.858442306518555, 30.10318374633789, 30.347925186157227, 30.592666625976562, 30.8374080657959, 31.082149505615234, 31.32689094543457, 31.571632385253906, 31.816373825073242, 32.06111526489258, 32.30585479736328, 32.55059814453125, 32.79533767700195, 33.04008102416992, 33.284820556640625, 33.529563903808594, 33.7743034362793, 34.019046783447266, 34.26378631591797, 34.50852966308594], "73": [5.363946437835693, 5.607762336730957, 5.851578235626221, 6.095394134521484, 6.33920955657959, 6.5830254554748535, 6.826841354370117, 7.070656776428223, 7.314472675323486, 7.55828857421875, 7.8021039962768555, 8.045920372009277, 8.289735794067383, 8.533551216125488, 8.77736759185791, 9.021183013916016, 9.264998435974121, 9.508814811706543, 9.752630233764648, 9.996445655822754, 10.240262031555176, 10.484077453613281, 10.727892875671387, 10.971709251403809, 11.215524673461914, 11.459341049194336, 11.703156471252441, 11.946971893310547, 12.190788269042969, 12.434603691101074, 12.67841911315918, 12.922235488891602, 13.166050910949707, 13.409866333007812, 13.653682708740234, 13.89749813079834, 14.141313552856445, 14.385129928588867, 14.628945350646973, 14.872760772705078, 15.1165771484375, 15.360392570495605, 15.604207992553711, 15.848024368286133, 16.091840744018555, 16.335655212402344, 16.579471588134766, 16.823287963867188, 17.067102432250977, 17.3109188079834, 17.55473518371582, 17.79854965209961, 18.04236602783203, 18.286182403564453, 18.529996871948242, 18.773813247680664, 19.017629623413086, 19.261444091796875, 19.505260467529297, 19.74907684326172, 19.992891311645508, 20.23670768737793, 20.48052406311035, 20.72433853149414, 20.968154907226562, 21.211971282958984, 21.455785751342773, 21.699602127075195, 21.943418502807617, 22.187232971191406, 22.431049346923828, 22.67486572265625, 22.918682098388672, 23.16249656677246, 23.406312942504883, 23.650129318237305, 23.893943786621094, 24.137760162353516, 24.381576538085938, 24.625391006469727, 24.86920738220215, 25.11302375793457, 25.35683822631836, 25.60065460205078, 25.844470977783203, 26.088285446166992, 26.332101821899414, 26.575918197631836, 26.819732666015625, 27.063549041748047, 27.30736541748047, 27.551179885864258, 27.79499626159668, 28.0388126373291, 28.28262710571289, 28.526443481445312, 28.770259857177734, 29.014074325561523, 29.257890701293945, 29.501707077026367, 29.745521545410156, 29.989337921142578, 30.233154296875, 30.47696876525879, 30.72078514099121, 30.964601516723633, 31.208415985107422, 31.452232360839844, 31.696048736572266, 31.939865112304688, 32.18368148803711, 32.427494049072266, 32.67131042480469, 32.91512680053711, 33.15894317626953, 33.40275955200195, 33.646575927734375, 33.89038848876953, 34.13420486450195, 34.378021240234375], "74": [5.343757629394531, 5.586656093597412, 5.829554080963135, 6.072452068328857, 6.31535005569458, 6.558248043060303, 6.801146507263184, 7.044044494628906, 7.286942481994629, 7.529840469360352, 7.772738456726074, 8.015636444091797, 8.25853443145752, 8.501432418823242, 8.744331359863281, 8.987229347229004, 9.230127334594727, 9.47302532196045, 9.715923309326172, 9.958821296691895, 10.201719284057617, 10.44461727142334, 10.687515258789062, 10.930413246154785, 11.173312187194824, 11.416210174560547, 11.65910816192627, 11.902006149291992, 12.144904136657715, 12.387802124023438, 12.63070011138916, 12.873598098754883, 13.116496086120605, 13.359394073486328, 13.602293014526367, 13.84519100189209, 14.088088989257812, 14.330986976623535, 14.573884963989258, 14.81678295135498, 15.059680938720703, 15.302578926086426, 15.545476913452148, 15.788374900817871, 16.031272888183594, 16.274171829223633, 16.51706886291504, 16.759967803955078, 17.002864837646484, 17.245763778686523, 17.488662719726562, 17.73155975341797, 17.974458694458008, 18.217355728149414, 18.460254669189453, 18.70315170288086, 18.9460506439209, 19.188947677612305, 19.431846618652344, 19.674745559692383, 19.91764259338379, 20.160541534423828, 20.403438568115234, 20.646337509155273, 20.88923454284668, 21.13213348388672, 21.375030517578125, 21.617929458618164, 21.86082649230957, 22.10372543334961, 22.34662437438965, 22.589521408081055, 22.832420349121094, 23.0753173828125, 23.31821632385254, 23.561113357543945, 23.804012298583984, 24.04690933227539, 24.28980827331543, 24.53270721435547, 24.775604248046875, 25.018503189086914, 25.26140022277832, 25.50429916381836, 25.747196197509766, 25.990095138549805, 26.23299217224121, 26.47589111328125, 26.718788146972656, 26.961687088012695, 27.204586029052734, 27.44748306274414, 27.69038200378418, 27.933279037475586, 28.176177978515625, 28.41907501220703, 28.66197395324707, 28.904870986938477, 29.147769927978516, 29.390666961669922, 29.63356590270996, 29.87646484375, 30.119361877441406, 30.362260818481445, 30.60515785217285, 30.84805679321289, 31.090953826904297, 31.333852767944336, 31.576749801635742, 31.81964874267578, 32.06254577636719, 32.30544662475586, 32.548343658447266, 32.79124069213867, 33.03413772583008, 33.27703857421875, 33.519935607910156, 33.76283264160156, 34.00572967529297, 34.24863052368164], "75": [5.323740482330322, 5.565728664398193, 5.8077168464660645, 6.049705505371094, 6.291693687438965, 6.533681869506836, 6.775670051574707, 7.017658233642578, 7.259646415710449, 7.50163459777832, 7.743622779846191, 7.9856109619140625, 8.227599143981934, 8.469587326049805, 8.711575508117676, 8.953563690185547, 9.195551872253418, 9.437540054321289, 9.67952823638916, 9.921516418457031, 10.163504600524902, 10.405492782592773, 10.647480964660645, 10.889469146728516, 11.131457328796387, 11.373445510864258, 11.615433692932129, 11.857421875, 12.099411010742188, 12.341399192810059, 12.58338737487793, 12.8253755569458, 13.067363739013672, 13.309351921081543, 13.551340103149414, 13.793328285217285, 14.035316467285156, 14.277304649353027, 14.519292831420898, 14.76128101348877, 15.00326919555664, 15.245257377624512, 15.487245559692383, 15.729233741760254, 15.971221923828125, 16.213211059570312, 16.455198287963867, 16.697187423706055, 16.93917465209961, 17.181163787841797, 17.42315101623535, 17.66514015197754, 17.907127380371094, 18.14911651611328, 18.391103744506836, 18.633092880249023, 18.875080108642578, 19.117069244384766, 19.35905647277832, 19.601045608520508, 19.843032836914062, 20.08502197265625, 20.327009201049805, 20.568998336791992, 20.810985565185547, 21.052974700927734, 21.29496192932129, 21.536951065063477, 21.77893829345703, 22.02092742919922, 22.262914657592773, 22.50490379333496, 22.746891021728516, 22.988880157470703, 23.230867385864258, 23.472856521606445, 23.71484375, 23.956832885742188, 24.198822021484375, 24.44080924987793, 24.682798385620117, 24.924785614013672, 25.16677474975586, 25.408761978149414, 25.6507511138916, 25.892738342285156, 26.134727478027344, 26.3767147064209, 26.618703842163086, 26.86069107055664, 27.102680206298828, 27.344667434692383, 27.58665657043457, 27.828643798828125, 28.070632934570312, 28.312620162963867, 28.554609298706055, 28.79659652709961, 29.038585662841797, 29.28057289123535, 29.52256202697754, 29.764549255371094, 30.00653839111328, 30.248525619506836, 30.490514755249023, 30.732501983642578, 30.974491119384766, 31.21647834777832, 31.458467483520508, 31.700454711914062, 31.94244384765625, 32.18443298339844, 32.426422119140625, 32.66840744018555, 32.910396575927734, 33.15238571166992, 33.39437484741211, 33.63636016845703, 33.87834930419922, 34.120338439941406], "76": [5.303893089294434, 5.544979095458984, 5.786065101623535, 6.027151107788086, 6.268237113952637, 6.5093231201171875, 6.7504096031188965, 6.991495609283447, 7.232581615447998, 7.473667621612549, 7.7147536277771, 7.95583963394165, 8.19692611694336, 8.43801212310791, 8.679098129272461, 8.920184135437012, 9.161270141601562, 9.402356147766113, 9.643442153930664, 9.884528160095215, 10.125614166259766, 10.366700172424316, 10.607786178588867, 10.848872184753418, 11.089958190917969, 11.33104419708252, 11.57213020324707, 11.813216209411621, 12.054302215576172, 12.295388221740723, 12.536474227905273, 12.777560234069824, 13.018646240234375, 13.259733200073242, 13.500819206237793, 13.741905212402344, 13.982991218566895, 14.224077224731445, 14.465163230895996, 14.706249237060547, 14.947335243225098, 15.188421249389648, 15.4295072555542, 15.67059326171875, 15.9116792678833, 16.15276527404785, 16.39385223388672, 16.634937286376953, 16.87602424621582, 17.117109298706055, 17.358196258544922, 17.599281311035156, 17.840368270874023, 18.081453323364258, 18.322540283203125, 18.56362533569336, 18.804712295532227, 19.04579734802246, 19.286884307861328, 19.527969360351562, 19.76905632019043, 20.010141372680664, 20.25122833251953, 20.492313385009766, 20.733400344848633, 20.9744873046875, 21.215572357177734, 21.4566593170166, 21.697744369506836, 21.938831329345703, 22.179916381835938, 22.421003341674805, 22.66208839416504, 22.903175354003906, 23.14426040649414, 23.385347366333008, 23.626432418823242, 23.86751937866211, 24.108604431152344, 24.34969139099121, 24.590776443481445, 24.831863403320312, 25.072948455810547, 25.314035415649414, 25.55512046813965, 25.796207427978516, 26.03729248046875, 26.278379440307617, 26.519466400146484, 26.76055145263672, 27.001638412475586, 27.24272346496582, 27.483810424804688, 27.724895477294922, 27.96598243713379, 28.207067489624023, 28.44815444946289, 28.689239501953125, 28.930326461791992, 29.171411514282227, 29.412498474121094, 29.653583526611328, 29.894670486450195, 30.13575553894043, 30.376842498779297, 30.61792755126953, 30.8590145111084, 31.100099563598633, 31.3411865234375, 31.582273483276367, 31.8233585357666, 32.06444549560547, 32.3055305480957, 32.54661560058594, 32.78770446777344, 33.02878952026367, 33.269874572753906, 33.51095962524414, 33.75204849243164, 33.993133544921875], "77": [5.284213066101074, 5.524404525756836, 5.764595985412598, 6.004787445068359, 6.244979381561279, 6.485170841217041, 6.725362300872803, 6.9655537605285645, 7.205745220184326, 7.445936679840088, 7.68612813949585, 7.926319599151611, 8.166511535644531, 8.406702995300293, 8.646894454956055, 8.887085914611816, 9.127277374267578, 9.36746883392334, 9.607660293579102, 9.847851753234863, 10.088043212890625, 10.328234672546387, 10.568426132202148, 10.80861759185791, 11.048809051513672, 11.289000511169434, 11.529191970825195, 11.769383430480957, 12.009574890136719, 12.249767303466797, 12.489958763122559, 12.73015022277832, 12.970341682434082, 13.210533142089844, 13.450724601745605, 13.690916061401367, 13.931107521057129, 14.17129898071289, 14.411490440368652, 14.651681900024414, 14.891873359680176, 15.132064819335938, 15.3722562789917, 15.612447738647461, 15.852639198303223, 16.092830657958984, 16.333023071289062, 16.573213577270508, 16.813405990600586, 17.05359649658203, 17.29378890991211, 17.533979415893555, 17.774171829223633, 18.014362335205078, 18.254554748535156, 18.4947452545166, 18.73493766784668, 18.975128173828125, 19.215320587158203, 19.45551300048828, 19.695703506469727, 19.935895919799805, 20.17608642578125, 20.416278839111328, 20.656469345092773, 20.89666175842285, 21.136852264404297, 21.377044677734375, 21.61723518371582, 21.8574275970459, 22.097618103027344, 22.337810516357422, 22.578001022338867, 22.818193435668945, 23.05838394165039, 23.29857635498047, 23.538766860961914, 23.778959274291992, 24.019149780273438, 24.259342193603516, 24.499534606933594, 24.73972511291504, 24.979917526245117, 25.220108032226562, 25.46030044555664, 25.700490951538086, 25.940683364868164, 26.18087387084961, 26.421066284179688, 26.661256790161133, 26.90144920349121, 27.141639709472656, 27.381832122802734, 27.62202262878418, 27.862215042114258, 28.102405548095703, 28.34259796142578, 28.582788467407227, 28.822980880737305, 29.06317138671875, 29.303363800048828, 29.543556213378906, 29.78374671936035, 30.02393913269043, 30.264129638671875, 30.504322052001953, 30.7445125579834, 30.984704971313477, 31.224895477294922, 31.465087890625, 31.705278396606445, 31.945470809936523, 32.18566131591797, 32.42585372924805, 32.666046142578125, 32.90623474121094, 33.146427154541016, 33.386619567871094, 33.62681198120117, 33.867000579833984], "78": [5.2646989822387695, 5.504003047943115, 5.743307590484619, 5.982612133026123, 6.221916675567627, 6.461221218109131, 6.700525760650635, 6.939830303192139, 7.179134845733643, 7.4184393882751465, 7.657743453979492, 7.897047996520996, 8.1363525390625, 8.375657081604004, 8.614961624145508, 8.854266166687012, 9.093570709228516, 9.33287525177002, 9.572179794311523, 9.811484336853027, 10.050788879394531, 10.290093421936035, 10.529397964477539, 10.768702507019043, 11.00800609588623, 11.247310638427734, 11.486615180969238, 11.725919723510742, 11.965224266052246, 12.20452880859375, 12.443833351135254, 12.683137893676758, 12.922442436218262, 13.161746978759766, 13.40105152130127, 13.640356063842773, 13.879660606384277, 14.118965148925781, 14.358269691467285, 14.597574234008789, 14.836878776550293, 15.076183319091797, 15.315486907958984, 15.554791450500488, 15.794095993041992, 16.033401489257812, 16.272705078125, 16.51201057434082, 16.751314163208008, 16.990619659423828, 17.229923248291016, 17.469226837158203, 17.708532333374023, 17.94783592224121, 18.18714141845703, 18.42644500732422, 18.66575050354004, 18.905054092407227, 19.144359588623047, 19.383663177490234, 19.622968673706055, 19.862272262573242, 20.101577758789062, 20.34088134765625, 20.58018684387207, 20.819490432739258, 21.058795928955078, 21.298099517822266, 21.537405014038086, 21.776708602905273, 22.01601219177246, 22.25531768798828, 22.49462127685547, 22.73392677307129, 22.973230361938477, 23.212535858154297, 23.451839447021484, 23.691144943237305, 23.930448532104492, 24.169754028320312, 24.4090576171875, 24.64836311340332, 24.887666702270508, 25.126972198486328, 25.366275787353516, 25.605581283569336, 25.844884872436523, 26.08418846130371, 26.32349395751953, 26.56279754638672, 26.80210304260254, 27.041406631469727, 27.280712127685547, 27.520015716552734, 27.759321212768555, 27.998624801635742, 28.237930297851562, 28.47723388671875, 28.71653938293457, 28.955842971801758, 29.195148468017578, 29.434452056884766, 29.673757553100586, 29.913061141967773, 30.152366638183594, 30.39167022705078, 30.63097381591797, 30.87027931213379, 31.109582901000977, 31.348888397216797, 31.588191986083984, 31.827497482299805, 32.066802978515625, 32.30610656738281, 32.54541015625, 32.78471374511719, 33.02402114868164, 33.26332473754883, 33.502628326416016, 33.7419319152832], "79": [5.24534797668457, 5.4837727546691895, 5.722198009490967, 5.960622787475586, 6.199047565460205, 6.437472343444824, 6.675897598266602, 6.914322376251221, 7.15274715423584, 7.391171932220459, 7.629597187042236, 7.8680219650268555, 8.106447219848633, 8.344871520996094, 8.583296775817871, 8.821722030639648, 9.06014633178711, 9.298571586608887, 9.536995887756348, 9.775421142578125, 10.013846397399902, 10.252270698547363, 10.49069595336914, 10.729121208190918, 10.967545509338379, 11.205970764160156, 11.444396018981934, 11.682820320129395, 11.921245574951172, 12.159669876098633, 12.39809513092041, 12.636520385742188, 12.874944686889648, 13.113369941711426, 13.351795196533203, 13.590219497680664, 13.828644752502441, 14.067070007324219, 14.30549430847168, 14.543919563293457, 14.782343864440918, 15.020769119262695, 15.259194374084473, 15.497618675231934, 15.736043930053711, 15.974469184875488, 16.212894439697266, 16.451318740844727, 16.689743041992188, 16.92816925048828, 17.166593551635742, 17.405017852783203, 17.643444061279297, 17.881868362426758, 18.12029266357422, 18.358718872070312, 18.597143173217773, 18.835567474365234, 19.073991775512695, 19.31241798400879, 19.55084228515625, 19.78926658630371, 20.027692794799805, 20.266117095947266, 20.504541397094727, 20.74296760559082, 20.98139190673828, 21.219816207885742, 21.458242416381836, 21.696666717529297, 21.935091018676758, 22.17351722717285, 22.411941528320312, 22.650365829467773, 22.888792037963867, 23.127216339111328, 23.36564064025879, 23.604066848754883, 23.842491149902344, 24.080915451049805, 24.319339752197266, 24.55776596069336, 24.79619026184082, 25.03461456298828, 25.273040771484375, 25.511465072631836, 25.749889373779297, 25.98831558227539, 26.22673988342285, 26.465164184570312, 26.703590393066406, 26.942014694213867, 27.180438995361328, 27.418865203857422, 27.657289505004883, 27.895713806152344, 28.134140014648438, 28.3725643157959, 28.61098861694336, 28.849414825439453, 29.087839126586914, 29.326263427734375, 29.564687728881836, 29.80311393737793, 30.04153823852539, 30.27996253967285, 30.518388748168945, 30.756813049316406, 30.995237350463867, 31.23366355895996, 31.472087860107422, 31.710512161254883, 31.948938369750977, 32.18736267089844, 32.42578887939453, 32.66421127319336, 32.90263748168945, 33.14106369018555, 33.379486083984375, 33.61791229248047], "80": [5.22615909576416, 5.463711738586426, 5.701264381408691, 5.938817024230957, 6.176369667053223, 6.413922309875488, 6.651474952697754, 6.8890275955200195, 7.126580238342285, 7.364132881164551, 7.601685523986816, 7.839238166809082, 8.076790809631348, 8.314343452453613, 8.551896095275879, 8.789448738098145, 9.02700138092041, 9.264554023742676, 9.502106666564941, 9.739659309387207, 9.977211952209473, 10.214764595031738, 10.45231819152832, 10.689870834350586, 10.927423477172852, 11.164976119995117, 11.402528762817383, 11.640081405639648, 11.877634048461914, 12.11518669128418, 12.352739334106445, 12.590291976928711, 12.827844619750977, 13.065397262573242, 13.302949905395508, 13.540502548217773, 13.778055191040039, 14.015607833862305, 14.25316047668457, 14.490713119506836, 14.728265762329102, 14.965818405151367, 15.203371047973633, 15.440923690795898, 15.678476333618164, 15.91602897644043, 16.153581619262695, 16.39113426208496, 16.628686904907227, 16.866239547729492, 17.103792190551758, 17.341344833374023, 17.57889747619629, 17.816450119018555, 18.05400276184082, 18.291555404663086, 18.52910804748535, 18.766660690307617, 19.004213333129883, 19.24176597595215, 19.479318618774414, 19.71687126159668, 19.954423904418945, 20.19197654724121, 20.429529190063477, 20.667081832885742, 20.90463638305664, 21.142189025878906, 21.379741668701172, 21.617294311523438, 21.854846954345703, 22.09239959716797, 22.329952239990234, 22.5675048828125, 22.805057525634766, 23.04261016845703, 23.280162811279297, 23.517715454101562, 23.755268096923828, 23.992820739746094, 24.23037338256836, 24.467926025390625, 24.70547866821289, 24.943031311035156, 25.180583953857422, 25.418136596679688, 25.655689239501953, 25.89324188232422, 26.130794525146484, 26.36834716796875, 26.605899810791016, 26.84345245361328, 27.081005096435547, 27.318557739257812, 27.556110382080078, 27.793663024902344, 28.03121566772461, 28.268768310546875, 28.50632095336914, 28.743873596191406, 28.981426239013672, 29.218978881835938, 29.456531524658203, 29.69408416748047, 29.931636810302734, 30.169189453125, 30.406742095947266, 30.64429473876953, 30.881847381591797, 31.119400024414062, 31.356952667236328, 31.594505310058594, 31.83205795288086, 32.069610595703125, 32.30716323852539, 32.544715881347656, 32.78226852416992, 33.01982116699219, 33.25737380981445, 33.49492645263672], "81": [5.20712947845459, 5.443817138671875, 5.68050479888916, 5.917192459106445, 6.1538801193237305, 6.390567779541016, 6.627255916595459, 6.863943576812744, 7.100631237030029, 7.3373188972473145, 7.5740065574646, 7.810694217681885, 8.047382354736328, 8.284070014953613, 8.520757675170898, 8.757445335388184, 8.994132995605469, 9.230820655822754, 9.467508316040039, 9.704195976257324, 9.94088363647461, 10.177571296691895, 10.41425895690918, 10.650946617126465, 10.88763427734375, 11.124321937561035, 11.36100959777832, 11.597697257995605, 11.83438491821289, 12.071072578430176, 12.307760238647461, 12.544447898864746, 12.781135559082031, 13.017823219299316, 13.254511833190918, 13.491199493408203, 13.727887153625488, 13.964574813842773, 14.201262474060059, 14.437950134277344, 14.674637794494629, 14.911325454711914, 15.1480131149292, 15.384700775146484, 15.62138843536377, 15.858076095581055, 16.094764709472656, 16.331451416015625, 16.568140029907227, 16.804826736450195, 17.041515350341797, 17.278202056884766, 17.514890670776367, 17.751577377319336, 17.988265991210938, 18.224952697753906, 18.461641311645508, 18.698328018188477, 18.935016632080078, 19.171703338623047, 19.40839195251465, 19.645078659057617, 19.88176727294922, 20.118453979492188, 20.35514259338379, 20.591829299926758, 20.82851791381836, 21.06520652770996, 21.30189323425293, 21.53858184814453, 21.7752685546875, 22.0119571685791, 22.24864387512207, 22.485332489013672, 22.72201919555664, 22.958707809448242, 23.19539451599121, 23.432083129882812, 23.66876983642578, 23.905458450317383, 24.14214515686035, 24.378833770751953, 24.615520477294922, 24.852209091186523, 25.088895797729492, 25.325584411621094, 25.562271118164062, 25.798959732055664, 26.035646438598633, 26.272335052490234, 26.509023666381836, 26.745710372924805, 26.982398986816406, 27.219085693359375, 27.455774307250977, 27.692461013793945, 27.929149627685547, 28.165836334228516, 28.402524948120117, 28.639211654663086, 28.875900268554688, 29.112586975097656, 29.349275588989258, 29.585962295532227, 29.822650909423828, 30.059337615966797, 30.2960262298584, 30.532712936401367, 30.76940155029297, 31.006088256835938, 31.24277687072754, 31.47946548461914, 31.71615219116211, 31.95284080505371, 32.18952941894531, 32.42621612548828, 32.66290283203125, 32.89958953857422, 33.13628005981445, 33.37296676635742], "82": [5.188258171081543, 5.424088001251221, 5.659917831420898, 5.895747661590576, 6.131577491760254, 6.367407321929932, 6.603237152099609, 6.839067459106445, 7.074897289276123, 7.310727119445801, 7.5465569496154785, 7.782386779785156, 8.018217086791992, 8.254046440124512, 8.489876747131348, 8.725706100463867, 8.961536407470703, 9.197366714477539, 9.433196067810059, 9.669026374816895, 9.904855728149414, 10.14068603515625, 10.376516342163086, 10.612345695495605, 10.848176002502441, 11.084005355834961, 11.319835662841797, 11.555665016174316, 11.791495323181152, 12.027325630187988, 12.263154983520508, 12.498985290527344, 12.734814643859863, 12.9706449508667, 13.206474304199219, 13.442304611206055, 13.67813491821289, 13.91396427154541, 14.149794578552246, 14.385623931884766, 14.621454238891602, 14.857284545898438, 15.093113899230957, 15.328944206237793, 15.564773559570312, 15.800603866577148, 16.036434173583984, 16.27226448059082, 16.508092880249023, 16.74392318725586, 16.979753494262695, 17.21558380126953, 17.451412200927734, 17.68724250793457, 17.923072814941406, 18.158903121948242, 18.394733428955078, 18.63056182861328, 18.866392135620117, 19.102222442626953, 19.33805274963379, 19.573883056640625, 19.809711456298828, 20.045541763305664, 20.2813720703125, 20.517202377319336, 20.753032684326172, 20.988861083984375, 21.22469139099121, 21.460521697998047, 21.696352005004883, 21.932180404663086, 22.168010711669922, 22.403841018676758, 22.639671325683594, 22.87550163269043, 23.111330032348633, 23.34716033935547, 23.582990646362305, 23.81882095336914, 24.054651260375977, 24.29047966003418, 24.526309967041016, 24.76214027404785, 24.997970581054688, 25.233800888061523, 25.469629287719727, 25.705459594726562, 25.9412899017334, 26.177120208740234, 26.412948608398438, 26.648778915405273, 26.88460922241211, 27.120439529418945, 27.35626983642578, 27.592098236083984, 27.82792854309082, 28.063758850097656, 28.299589157104492, 28.535419464111328, 28.77124786376953, 29.007078170776367, 29.242908477783203, 29.47873878479004, 29.714569091796875, 29.950397491455078, 30.186227798461914, 30.42205810546875, 30.657888412475586, 30.89371681213379, 31.129547119140625, 31.36537742614746, 31.601207733154297, 31.837038040161133, 32.07286834716797, 32.30869674682617, 32.54452896118164, 32.780357360839844, 33.01618576049805, 33.252017974853516], "83": [5.16954231262207, 5.404521465301514, 5.639500617980957, 5.874480247497559, 6.109459400177002, 6.344438552856445, 6.579417705535889, 6.814396858215332, 7.049376010894775, 7.284355163574219, 7.519334316253662, 7.7543134689331055, 7.989292621612549, 8.224271774291992, 8.459251403808594, 8.694230079650879, 8.92920970916748, 9.164188385009766, 9.399168014526367, 9.634147644042969, 9.869126319885254, 10.104105949401855, 10.33908462524414, 10.574064254760742, 10.809042930603027, 11.044022560119629, 11.279001235961914, 11.513980865478516, 11.748960494995117, 11.983939170837402, 12.218918800354004, 12.453897476196289, 12.68887710571289, 12.923855781555176, 13.158835411071777, 13.393814086914062, 13.628793716430664, 13.86377239227295, 14.09875202178955, 14.333731651306152, 14.568710327148438, 14.803689956665039, 15.038668632507324, 15.273648262023926, 15.508626937866211, 15.743606567382812, 15.978585243225098, 16.213563919067383, 16.448543548583984, 16.683523178100586, 16.918502807617188, 17.15348243713379, 17.388460159301758, 17.62343978881836, 17.85841941833496, 18.093399047851562, 18.32837677001953, 18.563356399536133, 18.798336029052734, 19.033315658569336, 19.268295288085938, 19.503273010253906, 19.738252639770508, 19.97323226928711, 20.20821189880371, 20.44318962097168, 20.67816925048828, 20.913148880004883, 21.148128509521484, 21.383108139038086, 21.618085861206055, 21.853065490722656, 22.088045120239258, 22.32302474975586, 22.558002471923828, 22.79298210144043, 23.02796173095703, 23.262941360473633, 23.497920989990234, 23.732898712158203, 23.967878341674805, 24.202857971191406, 24.437837600708008, 24.672815322875977, 24.907794952392578, 25.14277458190918, 25.37775421142578, 25.612733840942383, 25.84771156311035, 26.082691192626953, 26.317670822143555, 26.552650451660156, 26.787628173828125, 27.022607803344727, 27.257587432861328, 27.49256706237793, 27.7275447845459, 27.9625244140625, 28.1975040435791, 28.432483673095703, 28.667463302612305, 28.902441024780273, 29.137420654296875, 29.372400283813477, 29.607379913330078, 29.842357635498047, 30.07733726501465, 30.31231689453125, 30.54729652404785, 30.782276153564453, 31.017253875732422, 31.252233505249023, 31.487213134765625, 31.722192764282227, 31.957170486450195, 32.1921501159668, 32.427127838134766, 32.662109375, 32.89708709716797, 33.1320686340332], "84": [5.1509809494018555, 5.3851165771484375, 5.6192522048950195, 5.853387355804443, 6.087522983551025, 6.321658611297607, 6.5557942390441895, 6.789929389953613, 7.024065017700195, 7.258200645446777, 7.492336273193359, 7.726471424102783, 7.960607051849365, 8.194742202758789, 8.428877830505371, 8.663013458251953, 8.897149085998535, 9.131284713745117, 9.3654203414917, 9.599555969238281, 9.833691596984863, 10.067826271057129, 10.301961898803711, 10.536097526550293, 10.770233154296875, 11.004368782043457, 11.238504409790039, 11.472640037536621, 11.706774711608887, 11.940910339355469, 12.17504596710205, 12.409181594848633, 12.643317222595215, 12.877452850341797, 13.111588478088379, 13.345724105834961, 13.579858779907227, 13.813994407653809, 14.04813003540039, 14.282265663146973, 14.516401290893555, 14.750536918640137, 14.984672546386719, 15.2188081741333, 15.452942848205566, 15.687078475952148, 15.92121410369873, 16.155349731445312, 16.389484405517578, 16.623620986938477, 16.857755661010742, 17.09189224243164, 17.326026916503906, 17.560163497924805, 17.79429817199707, 18.028432846069336, 18.262569427490234, 18.4967041015625, 18.7308406829834, 18.964975357055664, 19.199111938476562, 19.433246612548828, 19.667383193969727, 19.901517868041992, 20.135652542114258, 20.369789123535156, 20.603923797607422, 20.83806037902832, 21.072195053100586, 21.306331634521484, 21.54046630859375, 21.774600982666016, 22.008737564086914, 22.24287223815918, 22.477008819580078, 22.711143493652344, 22.945280075073242, 23.179414749145508, 23.413549423217773, 23.647686004638672, 23.881820678710938, 24.115957260131836, 24.3500919342041, 24.584228515625, 24.818363189697266, 25.052499771118164, 25.28663444519043, 25.520769119262695, 25.754905700683594, 25.98904037475586, 26.223176956176758, 26.457311630249023, 26.691448211669922, 26.925582885742188, 27.159717559814453, 27.39385414123535, 27.627988815307617, 27.862125396728516, 28.09626007080078, 28.33039665222168, 28.564531326293945, 28.79866600036621, 29.03280258178711, 29.266937255859375, 29.501073837280273, 29.73520851135254, 29.969345092773438, 30.203479766845703, 30.4376163482666, 30.671751022338867, 30.905885696411133, 31.14002227783203, 31.374156951904297, 31.608293533325195, 31.84242820739746, 32.07656478881836, 32.310699462890625, 32.54483413696289, 32.778968811035156, 33.01310729980469], "85": [5.132572174072266, 5.365870952606201, 5.599169731140137, 5.832468509674072, 6.06576681137085, 6.299065589904785, 6.532364368438721, 6.765663146972656, 6.998961925506592, 7.232260704040527, 7.465559482574463, 7.698858261108398, 7.932157039642334, 8.16545581817627, 8.398754119873047, 8.63205337524414, 8.865351676940918, 9.098650932312012, 9.331949234008789, 9.565248489379883, 9.79854679107666, 10.031845092773438, 10.265144348144531, 10.498442649841309, 10.731741905212402, 10.96504020690918, 11.198339462280273, 11.43163776397705, 11.664937019348145, 11.898235321044922, 12.1315336227417, 12.364832878112793, 12.59813117980957, 12.831430435180664, 13.064728736877441, 13.298027992248535, 13.531326293945312, 13.764625549316406, 13.997923851013184, 14.231223106384277, 14.464521408081055, 14.697819709777832, 14.931118965148926, 15.164417266845703, 15.397716522216797, 15.631014823913574, 15.864314079284668, 16.097612380981445, 16.33091163635254, 16.564210891723633, 16.797508239746094, 17.030807495117188, 17.26410675048828, 17.497404098510742, 17.730703353881836, 17.96400260925293, 18.197301864624023, 18.430599212646484, 18.663898468017578, 18.897197723388672, 19.130496978759766, 19.363794326782227, 19.59709358215332, 19.830392837524414, 20.063690185546875, 20.29698944091797, 20.530288696289062, 20.763587951660156, 20.996885299682617, 21.23018455505371, 21.463483810424805, 21.6967830657959, 21.93008041381836, 22.163379669189453, 22.396678924560547, 22.629976272583008, 22.8632755279541, 23.096574783325195, 23.32987403869629, 23.56317138671875, 23.796470642089844, 24.029769897460938, 24.2630672454834, 24.496366500854492, 24.729665756225586, 24.96296501159668, 25.19626235961914, 25.429561614990234, 25.662860870361328, 25.896160125732422, 26.129457473754883, 26.362756729125977, 26.59605598449707, 26.82935333251953, 27.062652587890625, 27.29595184326172, 27.529251098632812, 27.762548446655273, 27.995847702026367, 28.22914695739746, 28.462446212768555, 28.695743560791016, 28.92904281616211, 29.162342071533203, 29.395639419555664, 29.628938674926758, 29.86223793029785, 30.095537185668945, 30.328834533691406, 30.5621337890625, 30.795433044433594, 31.028732299804688, 31.26202964782715, 31.495328903198242, 31.728628158569336, 31.961925506591797, 32.19522476196289, 32.428524017333984, 32.66182327270508, 32.89512252807617], "86": [5.11431360244751, 5.346782684326172, 5.579251289367676, 5.811720371246338, 6.044188976287842, 6.276657581329346, 6.509126663208008, 6.741595268249512, 6.974064350128174, 7.206532955169678, 7.43900203704834, 7.671470642089844, 7.903939247131348, 8.136407852172852, 8.368877410888672, 8.601346015930176, 8.83381462097168, 9.066283226013184, 9.298752784729004, 9.531221389770508, 9.763689994812012, 9.996158599853516, 10.22862720489502, 10.46109676361084, 10.693565368652344, 10.926033973693848, 11.158502578735352, 11.390971183776855, 11.623440742492676, 11.85590934753418, 12.088377952575684, 12.320846557617188, 12.553315162658691, 12.785784721374512, 13.018253326416016, 13.25072193145752, 13.483190536499023, 13.715660095214844, 13.948128700256348, 14.180597305297852, 14.413065910339355, 14.64553451538086, 14.87800407409668, 15.110472679138184, 15.342941284179688, 15.575409889221191, 15.807878494262695, 16.040348052978516, 16.272815704345703, 16.505285263061523, 16.737754821777344, 16.97022247314453, 17.20269203186035, 17.43515968322754, 17.66762924194336, 17.90009880065918, 18.132566452026367, 18.365036010742188, 18.597505569458008, 18.829973220825195, 19.062442779541016, 19.294910430908203, 19.527379989624023, 19.759849548339844, 19.99231719970703, 20.22478675842285, 20.45725440979004, 20.68972396850586, 20.92219352722168, 21.154661178588867, 21.387130737304688, 21.619598388671875, 21.852067947387695, 22.084537506103516, 22.317005157470703, 22.549474716186523, 22.78194236755371, 23.01441192626953, 23.24688148498535, 23.47934913635254, 23.71181869506836, 23.944286346435547, 24.176755905151367, 24.409225463867188, 24.641693115234375, 24.874162673950195, 25.106630325317383, 25.339099884033203, 25.571569442749023, 25.80403709411621, 26.03650665283203, 26.26897621154785, 26.50144386291504, 26.73391342163086, 26.966381072998047, 27.198850631713867, 27.431320190429688, 27.663787841796875, 27.896257400512695, 28.128725051879883, 28.361194610595703, 28.593664169311523, 28.82613182067871, 29.05860137939453, 29.29106903076172, 29.52353858947754, 29.75600814819336, 29.988475799560547, 30.220945358276367, 30.453413009643555, 30.685882568359375, 30.918352127075195, 31.150819778442383, 31.383289337158203, 31.61575698852539, 31.84822654724121, 32.08069610595703, 32.31316375732422, 32.545631408691406, 32.77810287475586], "87": [5.0962042808532715, 5.327849864959717, 5.559495449066162, 5.791141033172607, 6.022787094116211, 6.254432678222656, 6.486078262329102, 6.717723846435547, 6.949369430541992, 7.1810150146484375, 7.412660598754883, 7.644306659698486, 7.875952243804932, 8.107597351074219, 8.33924388885498, 8.570889472961426, 8.802535057067871, 9.034180641174316, 9.265826225280762, 9.497471809387207, 9.729117393493652, 9.960762977600098, 10.192408561706543, 10.424054145812988, 10.655699729919434, 10.887345314025879, 11.118990898132324, 11.35063648223877, 11.582282066345215, 11.813928604125977, 12.045574188232422, 12.277219772338867, 12.508865356445312, 12.740510940551758, 12.972156524658203, 13.203802108764648, 13.435447692871094, 13.667093276977539, 13.898738861083984, 14.13038444519043, 14.362030029296875, 14.59367561340332, 14.825321197509766, 15.056967735290527, 15.288613319396973, 15.520258903503418, 15.751904487609863, 15.983550071716309, 16.215194702148438, 16.446840286254883, 16.67848777770996, 16.910133361816406, 17.14177894592285, 17.373424530029297, 17.605070114135742, 17.836715698242188, 18.068361282348633, 18.300006866455078, 18.531652450561523, 18.76329803466797, 18.994943618774414, 19.22658920288086, 19.458234786987305, 19.68988037109375, 19.921525955200195, 20.15317153930664, 20.384817123413086, 20.61646270751953, 20.848108291625977, 21.079753875732422, 21.311399459838867, 21.543045043945312, 21.774690628051758, 22.006336212158203, 22.23798179626465, 22.469627380371094, 22.70127296447754, 22.932918548583984, 23.16456413269043, 23.396211624145508, 23.627857208251953, 23.8595027923584, 24.091148376464844, 24.32279396057129, 24.554439544677734, 24.78608512878418, 25.017730712890625, 25.24937629699707, 25.481021881103516, 25.71266746520996, 25.944313049316406, 26.17595863342285, 26.407604217529297, 26.639249801635742, 26.870895385742188, 27.102540969848633, 27.334186553955078, 27.565832138061523, 27.79747772216797, 28.029123306274414, 28.26076889038086, 28.492414474487305, 28.72406005859375, 28.955705642700195, 29.18735122680664, 29.418996810913086, 29.65064239501953, 29.882287979125977, 30.113935470581055, 30.3455810546875, 30.577226638793945, 30.80887222290039, 31.040517807006836, 31.27216339111328, 31.503808975219727, 31.735454559326172, 31.967100143432617, 32.19874572753906, 32.430389404296875, 32.66203689575195], "88": [5.07824182510376, 5.309071063995361, 5.539900302886963, 5.7707295417785645, 6.001558780670166, 6.232388019561768, 6.463217258453369, 6.694046497344971, 6.924875259399414, 7.155704498291016, 7.386533737182617, 7.617362976074219, 7.84819221496582, 8.079021453857422, 8.309850692749023, 8.540679931640625, 8.771509170532227, 9.002338409423828, 9.23316764831543, 9.463996887207031, 9.694825172424316, 9.925654411315918, 10.15648365020752, 10.387312889099121, 10.618142127990723, 10.848971366882324, 11.079800605773926, 11.310629844665527, 11.541459083557129, 11.77228832244873, 12.003117561340332, 12.233946800231934, 12.464776039123535, 12.695605278015137, 12.926434516906738, 13.15726375579834, 13.388092994689941, 13.618921279907227, 13.849750518798828, 14.08057975769043, 14.311408996582031, 14.542238235473633, 14.773067474365234, 15.003896713256836, 15.234725952148438, 15.465555191040039, 15.69638442993164, 15.927213668823242, 16.158042907714844, 16.388872146606445, 16.619701385498047, 16.85053062438965, 17.08135986328125, 17.31218910217285, 17.543018341064453, 17.773847579956055, 18.004676818847656, 18.235506057739258, 18.46633529663086, 18.69716453552246, 18.927993774414062, 19.158823013305664, 19.389650344848633, 19.620479583740234, 19.851308822631836, 20.082138061523438, 20.31296730041504, 20.54379653930664, 20.774625778198242, 21.005455017089844, 21.236284255981445, 21.467113494873047, 21.69794273376465, 21.92877197265625, 22.15960121154785, 22.390430450439453, 22.621259689331055, 22.852088928222656, 23.082918167114258, 23.31374740600586, 23.54457664489746, 23.775405883789062, 24.006235122680664, 24.237064361572266, 24.467893600463867, 24.69872283935547, 24.92955207824707, 25.160381317138672, 25.391210556030273, 25.622039794921875, 25.852869033813477, 26.083698272705078, 26.31452751159668, 26.54535675048828, 26.776185989379883, 27.007015228271484, 27.237842559814453, 27.468671798706055, 27.699501037597656, 27.930330276489258, 28.16115951538086, 28.39198875427246, 28.622817993164062, 28.853647232055664, 29.084476470947266, 29.315305709838867, 29.54613494873047, 29.77696418762207, 30.007793426513672, 30.238622665405273, 30.469451904296875, 30.700281143188477, 30.931110382080078, 31.16193962097168, 31.39276885986328, 31.623598098754883, 31.854427337646484, 32.08525466918945, 32.31608581542969, 32.546913146972656], "89": [5.060425281524658, 5.290444374084473, 5.520463943481445, 5.75048303604126, 5.980502605438232, 6.210521697998047, 6.4405412673950195, 6.670560359954834, 6.900579929351807, 7.130599021911621, 7.360618591308594, 7.590637683868408, 7.820657253265381, 8.050676345825195, 8.280695915222168, 8.51071548461914, 8.740734100341797, 8.97075366973877, 9.200773239135742, 9.430792808532715, 9.660811424255371, 9.890830993652344, 10.120850563049316, 10.350870132446289, 10.580888748168945, 10.810908317565918, 11.04092788696289, 11.270947456359863, 11.50096607208252, 11.730985641479492, 11.961005210876465, 12.191023826599121, 12.421043395996094, 12.651062965393066, 12.881082534790039, 13.111101150512695, 13.341120719909668, 13.57114028930664, 13.801159858703613, 14.03117847442627, 14.261198043823242, 14.491217613220215, 14.721237182617188, 14.951255798339844, 15.181275367736816, 15.411294937133789, 15.641314506530762, 15.871333122253418, 16.10135269165039, 16.331371307373047, 16.561391830444336, 16.791410446166992, 17.02143096923828, 17.251449584960938, 17.481468200683594, 17.711488723754883, 17.94150733947754, 18.171525955200195, 18.401546478271484, 18.63156509399414, 18.86158561706543, 19.091604232788086, 19.321622848510742, 19.55164337158203, 19.781661987304688, 20.011680603027344, 20.241701126098633, 20.47171974182129, 20.701740264892578, 20.931758880615234, 21.16177749633789, 21.39179801940918, 21.621816635131836, 21.851835250854492, 22.08185577392578, 22.311874389648438, 22.541894912719727, 22.771913528442383, 23.00193214416504, 23.231952667236328, 23.461971282958984, 23.69198989868164, 23.92201042175293, 24.152029037475586, 24.382047653198242, 24.61206817626953, 24.842086791992188, 25.072107315063477, 25.302125930786133, 25.53214454650879, 25.762165069580078, 25.992183685302734, 26.22220230102539, 26.45222282409668, 26.682241439819336, 26.912261962890625, 27.14228057861328, 27.372299194335938, 27.602319717407227, 27.832338333129883, 28.06235694885254, 28.292377471923828, 28.522396087646484, 28.752416610717773, 28.98243522644043, 29.212453842163086, 29.442474365234375, 29.67249298095703, 29.902511596679688, 30.132532119750977, 30.362550735473633, 30.592571258544922, 30.822589874267578, 31.052608489990234, 31.282629013061523, 31.51264762878418, 31.742666244506836, 31.972686767578125, 32.20270538330078, 32.43272399902344], "90": [5.042752265930176, 5.271968364715576, 5.501183986663818, 5.730400085449219, 5.959616184234619, 6.1888322830200195, 6.41804838180542, 6.647264003753662, 6.8764801025390625, 7.105696201324463, 7.334912300109863, 7.564128398895264, 7.793344020843506, 8.022560119628906, 8.251776695251465, 8.480992317199707, 8.71020793914795, 8.939424514770508, 9.16864013671875, 9.397856712341309, 9.62707233428955, 9.856287956237793, 10.085504531860352, 10.314720153808594, 10.543936729431152, 10.773152351379395, 11.002367973327637, 11.231584548950195, 11.460800170898438, 11.690016746520996, 11.919232368469238, 12.14844799041748, 12.377664566040039, 12.606880187988281, 12.83609676361084, 13.065312385559082, 13.294528007507324, 13.523744583129883, 13.752960205078125, 13.982176780700684, 14.211392402648926, 14.440608024597168, 14.669824600219727, 14.899040222167969, 15.128256797790527, 15.35747241973877, 15.586688041687012, 15.81590461730957, 16.045120239257812, 16.274335861206055, 16.50355339050293, 16.732769012451172, 16.961984634399414, 17.191200256347656, 17.4204158782959, 17.649633407592773, 17.878849029541016, 18.108064651489258, 18.3372802734375, 18.566495895385742, 18.795713424682617, 19.02492904663086, 19.2541446685791, 19.483360290527344, 19.712575912475586, 19.94179344177246, 20.171009063720703, 20.400224685668945, 20.629440307617188, 20.85865592956543, 21.087873458862305, 21.317089080810547, 21.54630470275879, 21.77552032470703, 22.004735946655273, 22.23395347595215, 22.46316909790039, 22.692384719848633, 22.921600341796875, 23.150815963745117, 23.380033493041992, 23.609249114990234, 23.838464736938477, 24.06768035888672, 24.29689598083496, 24.526113510131836, 24.755329132080078, 24.98454475402832, 25.213760375976562, 25.442975997924805, 25.67219352722168, 25.901409149169922, 26.130624771118164, 26.359840393066406, 26.58905601501465, 26.818273544311523, 27.047489166259766, 27.276704788208008, 27.50592041015625, 27.735136032104492, 27.964353561401367, 28.19356918334961, 28.42278480529785, 28.652000427246094, 28.881216049194336, 29.11043357849121, 29.339649200439453, 29.568864822387695, 29.798080444335938, 30.02729606628418, 30.256513595581055, 30.485729217529297, 30.71494483947754, 30.94416046142578, 31.173376083374023, 31.4025936126709, 31.63180923461914, 31.861024856567383, 32.090240478515625, 32.3194580078125], "91": [5.025221347808838, 5.253640651702881, 5.482059478759766, 5.710478782653809, 5.938898086547852, 6.167316913604736, 6.395736217498779, 6.624155521392822, 6.852574348449707, 7.08099365234375, 7.309412956237793, 7.537831783294678, 7.766251087188721, 7.994670391082764, 8.223089218139648, 8.451508522033691, 8.679927825927734, 8.908347129821777, 9.13676643371582, 9.365184783935547, 9.59360408782959, 9.822023391723633, 10.050442695617676, 10.278861999511719, 10.507281303405762, 10.735699653625488, 10.964118957519531, 11.192538261413574, 11.420957565307617, 11.64937686920166, 11.877796173095703, 12.106215476989746, 12.334633827209473, 12.563053131103516, 12.791472434997559, 13.019891738891602, 13.248311042785645, 13.476730346679688, 13.705148696899414, 13.933568000793457, 14.1619873046875, 14.390406608581543, 14.618825912475586, 14.847245216369629, 15.075663566589355, 15.304082870483398, 15.532502174377441, 15.760921478271484, 15.989340782165527, 16.21776008605957, 16.446178436279297, 16.674598693847656, 16.903017044067383, 17.131437301635742, 17.35985565185547, 17.588274002075195, 17.816694259643555, 18.04511260986328, 18.27353286743164, 18.501951217651367, 18.730369567871094, 18.958789825439453, 19.18720817565918, 19.41562843322754, 19.644046783447266, 19.872467041015625, 20.10088539123535, 20.329303741455078, 20.557723999023438, 20.786142349243164, 21.014562606811523, 21.24298095703125, 21.471399307250977, 21.699819564819336, 21.928237915039062, 22.156658172607422, 22.38507652282715, 22.613496780395508, 22.841915130615234, 23.07033348083496, 23.29875373840332, 23.527172088623047, 23.755592346191406, 23.984010696411133, 24.212430953979492, 24.44084930419922, 24.669267654418945, 24.897687911987305, 25.12610626220703, 25.35452651977539, 25.582944869995117, 25.811363220214844, 26.039783477783203, 26.26820182800293, 26.49662208557129, 26.725040435791016, 26.953460693359375, 27.1818790435791, 27.410297393798828, 27.638717651367188, 27.867136001586914, 28.095556259155273, 28.323974609375, 28.55239486694336, 28.780813217163086, 29.009231567382812, 29.237651824951172, 29.4660701751709, 29.694490432739258, 29.922908782958984, 30.15132713317871, 30.37974739074707, 30.608165740966797, 30.836585998535156, 31.065004348754883, 31.293424606323242, 31.52184295654297, 31.750261306762695, 31.978681564331055, 32.20709991455078], "92": [5.00783109664917, 5.235459804534912, 5.463088512420654, 5.6907172203063965, 5.918345928192139, 6.145974636077881, 6.373603343963623, 6.601232051849365, 6.828860759735107, 7.05648946762085, 7.284117698669434, 7.511746406555176, 7.739375114440918, 7.96700382232666, 8.194632530212402, 8.422261238098145, 8.649889945983887, 8.877518653869629, 9.105147361755371, 9.332776069641113, 9.560404777526855, 9.788033485412598, 10.01566219329834, 10.243290901184082, 10.470919609069824, 10.698548316955566, 10.926177024841309, 11.15380573272705, 11.381434440612793, 11.609063148498535, 11.836691856384277, 12.06432056427002, 12.291949272155762, 12.519577980041504, 12.747206687927246, 12.974835395812988, 13.20246410369873, 13.430092811584473, 13.657721519470215, 13.885350227355957, 14.1129789352417, 14.340606689453125, 14.568235397338867, 14.79586410522461, 15.023492813110352, 15.251121520996094, 15.478750228881836, 15.706378936767578, 15.93400764465332, 16.161636352539062, 16.389265060424805, 16.616893768310547, 16.84452247619629, 17.07215118408203, 17.299779891967773, 17.527408599853516, 17.755037307739258, 17.982666015625, 18.210294723510742, 18.437923431396484, 18.665552139282227, 18.89318084716797, 19.12080955505371, 19.348438262939453, 19.576066970825195, 19.803695678710938, 20.03132438659668, 20.258953094482422, 20.486581802368164, 20.714210510253906, 20.94183921813965, 21.16946792602539, 21.397096633911133, 21.624725341796875, 21.852354049682617, 22.07998275756836, 22.3076114654541, 22.535240173339844, 22.762868881225586, 22.990497589111328, 23.21812629699707, 23.445755004882812, 23.673383712768555, 23.901012420654297, 24.12864112854004, 24.35626983642578, 24.583898544311523, 24.811527252197266, 25.039155960083008, 25.26678466796875, 25.494413375854492, 25.722042083740234, 25.949670791625977, 26.17729949951172, 26.40492820739746, 26.632556915283203, 26.860185623168945, 27.087814331054688, 27.31544303894043, 27.543071746826172, 27.770700454711914, 27.998329162597656, 28.2259578704834, 28.45358657836914, 28.68121337890625, 28.908842086791992, 29.136470794677734, 29.364099502563477, 29.59172821044922, 29.81935691833496, 30.046985626220703, 30.274614334106445, 30.502243041992188, 30.72987174987793, 30.957500457763672, 31.185129165649414, 31.412757873535156, 31.6403865814209, 31.86801528930664, 32.095645904541016], "93": [4.990579605102539, 5.217424392700195, 5.444268703460693, 5.67111349105835, 5.897957801818848, 6.124802589416504, 6.351646900177002, 6.578491687774658, 6.805335998535156, 7.0321807861328125, 7.2590250968933105, 7.485869884490967, 7.712714195251465, 7.939558982849121, 8.166403770446777, 8.393247604370117, 8.620092391967773, 8.84693717956543, 9.07378101348877, 9.300625801086426, 9.527470588684082, 9.754315376281738, 9.981159210205078, 10.208003997802734, 10.43484878540039, 10.661693572998047, 10.888537406921387, 11.115382194519043, 11.3422269821167, 11.569071769714355, 11.795915603637695, 12.022760391235352, 12.249605178833008, 12.476449012756348, 12.703293800354004, 12.93013858795166, 13.156983375549316, 13.383827209472656, 13.610671997070312, 13.837516784667969, 14.064361572265625, 14.291205406188965, 14.518050193786621, 14.744894981384277, 14.971739768981934, 15.198583602905273, 15.42542839050293, 15.652273178100586, 15.879117965698242, 16.1059627532959, 16.332807540893555, 16.559650421142578, 16.786495208740234, 17.01333999633789, 17.240184783935547, 17.467029571533203, 17.69387435913086, 17.920719146728516, 18.14756202697754, 18.374406814575195, 18.60125160217285, 18.828096389770508, 19.054941177368164, 19.28178596496582, 19.508630752563477, 19.735475540161133, 19.962318420410156, 20.189163208007812, 20.41600799560547, 20.642852783203125, 20.86969757080078, 21.096542358398438, 21.323387145996094, 21.550230026245117, 21.777074813842773, 22.00391960144043, 22.230764389038086, 22.457609176635742, 22.6844539642334, 22.911298751831055, 23.13814353942871, 23.364986419677734, 23.59183120727539, 23.818675994873047, 24.045520782470703, 24.27236557006836, 24.499210357666016, 24.726055145263672, 24.952898025512695, 25.17974281311035, 25.406587600708008, 25.633432388305664, 25.86027717590332, 26.087121963500977, 26.313966751098633, 26.54081153869629, 26.767654418945312, 26.99449920654297, 27.221343994140625, 27.44818878173828, 27.675033569335938, 27.901878356933594, 28.12872314453125, 28.355567932128906, 28.58241081237793, 28.809255599975586, 29.036100387573242, 29.2629451751709, 29.489789962768555, 29.71663475036621, 29.943479537963867, 30.17032241821289, 30.397167205810547, 30.624011993408203, 30.85085678100586, 31.077701568603516, 31.304546356201172, 31.531391143798828, 31.758235931396484, 31.985078811645508], "94": [4.973465919494629, 5.199532508850098, 5.425599098205566, 5.651665687561035, 5.877732276916504, 6.103798866271973, 6.3298659324646, 6.555932521820068, 6.781999111175537, 7.008065700531006, 7.234132289886475, 7.460198879241943, 7.686265468597412, 7.912332057952881, 8.138399124145508, 8.364465713500977, 8.590532302856445, 8.816598892211914, 9.042665481567383, 9.268732070922852, 9.49479866027832, 9.720865249633789, 9.946931838989258, 10.172998428344727, 10.399065017700195, 10.625131607055664, 10.851198196411133, 11.077264785766602, 11.30333137512207, 11.529397964477539, 11.755464553833008, 11.981531143188477, 12.207597732543945, 12.43366527557373, 12.6597318649292, 12.885798454284668, 13.111865043640137, 13.337931632995605, 13.563998222351074, 13.790064811706543, 14.016131401062012, 14.24219799041748, 14.46826457977295, 14.694331169128418, 14.920397758483887, 15.146464347839355, 15.372530937194824, 15.598597526550293, 15.824664115905762, 16.050731658935547, 16.276798248291016, 16.502864837646484, 16.728931427001953, 16.954998016357422, 17.18106460571289, 17.40713119506836, 17.633197784423828, 17.859264373779297, 18.085330963134766, 18.311397552490234, 18.537464141845703, 18.763530731201172, 18.98959732055664, 19.21566390991211, 19.441730499267578, 19.667797088623047, 19.893863677978516, 20.119930267333984, 20.345996856689453, 20.572063446044922, 20.79813003540039, 21.02419662475586, 21.250263214111328, 21.476329803466797, 21.702396392822266, 21.928462982177734, 22.154529571533203, 22.380596160888672, 22.60666275024414, 22.83272933959961, 23.058795928955078, 23.284862518310547, 23.510929107666016, 23.736995697021484, 23.963062286376953, 24.189128875732422, 24.41519546508789, 24.641263961791992, 24.86733055114746, 25.09339714050293, 25.3194637298584, 25.545530319213867, 25.771596908569336, 25.997663497924805, 26.223730087280273, 26.449796676635742, 26.67586326599121, 26.90192985534668, 27.12799644470215, 27.354063034057617, 27.580129623413086, 27.806196212768555, 28.032262802124023, 28.258329391479492, 28.48439598083496, 28.71046257019043, 28.9365291595459, 29.162595748901367, 29.388662338256836, 29.614728927612305, 29.840795516967773, 30.066862106323242, 30.29292869567871, 30.51899528503418, 30.74506187438965, 30.971128463745117, 31.197195053100586, 31.423261642456055, 31.649328231811523, 31.875394821166992], "95": [4.956488132476807, 5.1817827224731445, 5.407077789306641, 5.632372856140137, 5.857667446136475, 6.082962512969971, 6.308257579803467, 6.533552169799805, 6.758847236633301, 6.984142303466797, 7.209436893463135, 7.434731960296631, 7.660027027130127, 7.885321617126465, 8.110616683959961, 8.335911750793457, 8.561206817626953, 8.786500930786133, 9.011795997619629, 9.237091064453125, 9.462386131286621, 9.687681198120117, 9.912976264953613, 10.138270378112793, 10.363565444946289, 10.588860511779785, 10.814155578613281, 11.039450645446777, 11.264745712280273, 11.490039825439453, 11.71533489227295, 11.940629959106445, 12.165925025939941, 12.391220092773438, 12.616515159606934, 12.841809272766113, 13.06710433959961, 13.292399406433105, 13.517694473266602, 13.742989540100098, 13.968284606933594, 14.193578720092773, 14.41887378692627, 14.644168853759766, 14.869463920593262, 15.094758987426758, 15.320054054260254, 15.545348167419434, 15.77064323425293, 15.995938301086426, 16.221233367919922, 16.4465274810791, 16.671823501586914, 16.897117614746094, 17.122413635253906, 17.347707748413086, 17.573001861572266, 17.798297882080078, 18.023591995239258, 18.24888801574707, 18.47418212890625, 18.699478149414062, 18.924772262573242, 19.150066375732422, 19.375362396240234, 19.600656509399414, 19.825952529907227, 20.051246643066406, 20.276540756225586, 20.5018367767334, 20.727130889892578, 20.95242691040039, 21.17772102355957, 21.403017044067383, 21.628311157226562, 21.853605270385742, 22.078901290893555, 22.304195404052734, 22.529491424560547, 22.754785537719727, 22.980079650878906, 23.20537567138672, 23.4306697845459, 23.65596580505371, 23.88125991821289, 24.106555938720703, 24.331850051879883, 24.557144165039062, 24.782440185546875, 25.007734298706055, 25.233030319213867, 25.458324432373047, 25.683618545532227, 25.90891456604004, 26.13420867919922, 26.35950469970703, 26.58479881286621, 26.810094833374023, 27.035388946533203, 27.260683059692383, 27.485979080200195, 27.711273193359375, 27.936569213867188, 28.161863327026367, 28.387157440185547, 28.61245346069336, 28.83774757385254, 29.06304359436035, 29.28833770751953, 29.513633728027344, 29.738927841186523, 29.964221954345703, 30.189517974853516, 30.414812088012695, 30.640108108520508, 30.865402221679688, 31.090696334838867, 31.31599235534668, 31.54128646850586, 31.766582489013672], "96": [4.9396443367004395, 5.164173603057861, 5.388702869415283, 5.613232135772705, 5.837761402130127, 6.062290668487549, 6.286819934844971, 6.511349201202393, 6.7358784675598145, 6.960407733917236, 7.184937000274658, 7.409466743469238, 7.63399600982666, 7.858525276184082, 8.083054542541504, 8.307583808898926, 8.532113075256348, 8.75664234161377, 8.981171607971191, 9.205700874328613, 9.430230140686035, 9.654759407043457, 9.879288673400879, 10.1038179397583, 10.328347206115723, 10.552876472473145, 10.777405738830566, 11.001935005187988, 11.22646427154541, 11.450993537902832, 11.675522804260254, 11.900052070617676, 12.124581336975098, 12.34911060333252, 12.573639869689941, 12.798169136047363, 13.022698402404785, 13.247227668762207, 13.471756935119629, 13.69628620147705, 13.920815467834473, 14.145344734191895, 14.369874000549316, 14.594403266906738, 14.818933486938477, 15.043462753295898, 15.26799201965332, 15.492521286010742, 15.717050552368164, 15.941579818725586, 16.166109085083008, 16.39063835144043, 16.61516761779785, 16.839696884155273, 17.064226150512695, 17.288755416870117, 17.51328468322754, 17.73781394958496, 17.962343215942383, 18.186872482299805, 18.411401748657227, 18.63593101501465, 18.86046028137207, 19.084989547729492, 19.309518814086914, 19.534048080444336, 19.758577346801758, 19.98310661315918, 20.2076358795166, 20.432165145874023, 20.656694412231445, 20.881223678588867, 21.10575294494629, 21.33028221130371, 21.554811477661133, 21.779340744018555, 22.003870010375977, 22.2283992767334, 22.45292854309082, 22.677457809448242, 22.901987075805664, 23.126516342163086, 23.351045608520508, 23.57557487487793, 23.80010414123535, 24.024633407592773, 24.249162673950195, 24.473691940307617, 24.69822120666504, 24.92275047302246, 25.147279739379883, 25.371809005737305, 25.596338272094727, 25.82086753845215, 26.04539680480957, 26.269926071166992, 26.494455337524414, 26.718984603881836, 26.943513870239258, 27.16804313659668, 27.3925724029541, 27.617101669311523, 27.841630935668945, 28.066160202026367, 28.29068946838379, 28.51521873474121, 28.739748001098633, 28.964277267456055, 29.188806533813477, 29.41333770751953, 29.637866973876953, 29.862396240234375, 30.086925506591797, 30.31145477294922, 30.53598403930664, 30.760513305664062, 30.985042572021484, 31.209571838378906, 31.434101104736328, 31.65863037109375], "97": [4.922933578491211, 5.146703243255615, 5.3704729080200195, 5.594242572784424, 5.818012237548828, 6.041782379150391, 6.265552043914795, 6.489321708679199, 6.7130913734436035, 6.936861038208008, 7.160630702972412, 7.384400367736816, 7.608170032501221, 7.831939697265625, 8.055709838867188, 8.279479026794434, 8.503249168395996, 8.727018356323242, 8.950788497924805, 9.17455768585205, 9.398327827453613, 9.62209701538086, 9.845867156982422, 10.069637298583984, 10.29340648651123, 10.517176628112793, 10.740945816040039, 10.964715957641602, 11.188485145568848, 11.41225528717041, 11.636024475097656, 11.859794616699219, 12.083564758300781, 12.307333946228027, 12.53110408782959, 12.754873275756836, 12.978643417358398, 13.202412605285645, 13.426182746887207, 13.649951934814453, 13.873722076416016, 14.097491264343262, 14.321261405944824, 14.545031547546387, 14.768800735473633, 14.992570877075195, 15.216340065002441, 15.440110206604004, 15.66387939453125, 15.887649536132812, 16.111419677734375, 16.335187911987305, 16.558958053588867, 16.78272819519043, 17.006498336791992, 17.230268478393555, 17.454036712646484, 17.677806854248047, 17.90157699584961, 18.125347137451172, 18.3491153717041, 18.572885513305664, 18.796655654907227, 19.02042579650879, 19.24419403076172, 19.46796417236328, 19.691734313964844, 19.915504455566406, 20.13927459716797, 20.3630428314209, 20.58681297302246, 20.810583114624023, 21.034353256225586, 21.258121490478516, 21.481891632080078, 21.70566177368164, 21.929431915283203, 22.153202056884766, 22.376970291137695, 22.600740432739258, 22.82451057434082, 23.048280715942383, 23.272048950195312, 23.495819091796875, 23.719589233398438, 23.943359375, 24.167129516601562, 24.390897750854492, 24.614667892456055, 24.838438034057617, 25.06220817565918, 25.28597640991211, 25.509746551513672, 25.733516693115234, 25.957286834716797, 26.181055068969727, 26.40482521057129, 26.62859535217285, 26.852365493774414, 27.076135635375977, 27.299903869628906, 27.52367401123047, 27.74744415283203, 27.971214294433594, 28.194982528686523, 28.418752670288086, 28.64252281188965, 28.86629295349121, 29.090063095092773, 29.313831329345703, 29.537601470947266, 29.761371612548828, 29.98514175415039, 30.20890998840332, 30.432680130004883, 30.656450271606445, 30.880220413208008, 31.103988647460938, 31.3277587890625, 31.551528930664062], "98": [4.9063544273376465, 5.129370212554932, 5.352386474609375, 5.575402736663818, 5.7984185218811035, 6.021434783935547, 6.24445104598999, 6.467466831207275, 6.690483093261719, 6.913499355316162, 7.136515140533447, 7.359531402587891, 7.582547664642334, 7.805563449859619, 8.028579711914062, 8.251595497131348, 8.47461223602295, 8.697628021240234, 8.92064380645752, 9.143660545349121, 9.366676330566406, 9.589692115783691, 9.812708854675293, 10.035724639892578, 10.258740425109863, 10.481757164001465, 10.70477294921875, 10.927788734436035, 11.150805473327637, 11.373821258544922, 11.596837043762207, 11.819853782653809, 12.042869567871094, 12.265885353088379, 12.48890209197998, 12.711917877197266, 12.93493366241455, 13.157950401306152, 13.380966186523438, 13.603981971740723, 13.826998710632324, 14.05001449584961, 14.273030281066895, 14.496047019958496, 14.719062805175781, 14.942078590393066, 15.165095329284668, 15.388111114501953, 15.611126899719238, 15.83414363861084, 16.057159423828125, 16.280176162719727, 16.503190994262695, 16.726207733154297, 16.9492244720459, 17.172239303588867, 17.39525604248047, 17.61827278137207, 17.84128761291504, 18.06430435180664, 18.287321090698242, 18.51033592224121, 18.733352661132812, 18.956369400024414, 19.179384231567383, 19.402400970458984, 19.625417709350586, 19.848432540893555, 20.071449279785156, 20.294466018676758, 20.517480850219727, 20.740497589111328, 20.96351432800293, 21.1865291595459, 21.4095458984375, 21.6325626373291, 21.85557746887207, 22.078594207763672, 22.301610946655273, 22.524625778198242, 22.747642517089844, 22.970659255981445, 23.193674087524414, 23.416690826416016, 23.639707565307617, 23.862722396850586, 24.085739135742188, 24.30875587463379, 24.531770706176758, 24.75478744506836, 24.97780418395996, 25.20081901550293, 25.42383575439453, 25.646852493286133, 25.8698673248291, 26.092884063720703, 26.315900802612305, 26.538915634155273, 26.761932373046875, 26.984949111938477, 27.207963943481445, 27.430980682373047, 27.65399742126465, 27.877012252807617, 28.10002899169922, 28.32304573059082, 28.54606056213379, 28.76907730102539, 28.992094039916992, 29.21510887145996, 29.438125610351562, 29.661142349243164, 29.884157180786133, 30.107173919677734, 30.330190658569336, 30.553205490112305, 30.776222229003906, 30.999238967895508, 31.222253799438477, 31.445270538330078], "99": [4.889904975891113, 5.112173080444336, 5.334441661834717, 5.556710243225098, 5.77897834777832, 6.001246929168701, 6.223515510559082, 6.445783615112305, 6.6680521965026855, 6.890320301055908, 7.112588882446289, 7.33485746383667, 7.557125568389893, 7.779394149780273, 8.001662254333496, 8.223931312561035, 8.446199417114258, 8.66846752166748, 8.89073657989502, 9.113004684448242, 9.335272789001465, 9.557540893554688, 9.779809951782227, 10.00207805633545, 10.224346160888672, 10.446615219116211, 10.668883323669434, 10.891151428222656, 11.113420486450195, 11.335688591003418, 11.55795669555664, 11.78022575378418, 12.002493858337402, 12.224761962890625, 12.447031021118164, 12.669299125671387, 12.89156723022461, 13.113835334777832, 13.336104393005371, 13.558372497558594, 13.780640602111816, 14.002909660339355, 14.225177764892578, 14.4474458694458, 14.66971492767334, 14.891983032226562, 15.114251136779785, 15.336520195007324, 15.558788299560547, 15.78105640411377, 16.003324508666992, 16.22559356689453, 16.44786262512207, 16.670129776000977, 16.892398834228516, 17.114667892456055, 17.33693504333496, 17.5592041015625, 17.78147315979004, 18.003740310668945, 18.226009368896484, 18.448278427124023, 18.67054557800293, 18.89281463623047, 19.115081787109375, 19.337350845336914, 19.559619903564453, 19.78188705444336, 20.0041561126709, 20.226425170898438, 20.448692321777344, 20.670961380004883, 20.893230438232422, 21.115497589111328, 21.337766647338867, 21.560035705566406, 21.782302856445312, 22.00457191467285, 22.22684097290039, 22.449108123779297, 22.671377182006836, 22.893646240234375, 23.11591339111328, 23.33818244934082, 23.56045150756836, 23.782718658447266, 24.004987716674805, 24.227256774902344, 24.44952392578125, 24.67179298400879, 24.894062042236328, 25.116329193115234, 25.338598251342773, 25.560867309570312, 25.78313446044922, 26.005403518676758, 26.227670669555664, 26.449939727783203, 26.672208786010742, 26.89447593688965, 27.116744995117188, 27.339014053344727, 27.561281204223633, 27.783550262451172, 28.00581932067871, 28.228086471557617, 28.450355529785156, 28.672624588012695, 28.8948917388916, 29.11716079711914, 29.33942985534668, 29.561697006225586, 29.783966064453125, 30.006235122680664, 30.22850227355957, 30.45077133178711, 30.67304039001465, 30.895307540893555, 31.117576599121094, 31.339845657348633], "100": [4.873583793640137, 5.0951104164123535, 5.31663703918457, 5.538163661956787, 5.759690284729004, 5.981216907501221, 6.202743053436279, 6.424269676208496, 6.645796298980713, 6.86732292175293, 7.0888495445251465, 7.310376167297363, 7.53190279006958, 7.753428936004639, 7.9749555587768555, 8.19648265838623, 8.418008804321289, 8.639534950256348, 8.861062049865723, 9.082588195800781, 9.304115295410156, 9.525641441345215, 9.747167587280273, 9.968694686889648, 10.190220832824707, 10.411747932434082, 10.63327407836914, 10.854801177978516, 11.076327323913574, 11.297853469848633, 11.519380569458008, 11.740906715393066, 11.962433815002441, 12.1839599609375, 12.405486106872559, 12.627013206481934, 12.848539352416992, 13.070066452026367, 13.291592597961426, 13.5131196975708, 13.73464584350586, 13.956171989440918, 14.177699089050293, 14.399225234985352, 14.620752334594727, 14.842278480529785, 15.06380558013916, 15.285331726074219, 15.506857872009277, 15.728384971618652, 15.949911117553711, 16.171438217163086, 16.39296531677246, 16.614490509033203, 16.836017608642578, 17.057544708251953, 17.279069900512695, 17.50059700012207, 17.722124099731445, 17.943649291992188, 18.165176391601562, 18.386703491210938, 18.608230590820312, 18.829755783081055, 19.05128288269043, 19.272809982299805, 19.494335174560547, 19.715862274169922, 19.937389373779297, 20.158916473388672, 20.380441665649414, 20.60196876525879, 20.823495864868164, 21.045021057128906, 21.26654815673828, 21.488075256347656, 21.70960235595703, 21.931127548217773, 22.15265464782715, 22.374181747436523, 22.595706939697266, 22.81723403930664, 23.038761138916016, 23.26028823852539, 23.481813430786133, 23.703340530395508, 23.924867630004883, 24.146392822265625, 24.367919921875, 24.589447021484375, 24.810972213745117, 25.032499313354492, 25.254026412963867, 25.475553512573242, 25.697078704833984, 25.91860580444336, 26.140132904052734, 26.361658096313477, 26.58318519592285, 26.804712295532227, 27.0262393951416, 27.247764587402344, 27.46929168701172, 27.690818786621094, 27.912343978881836, 28.13387107849121, 28.355398178100586, 28.57692527770996, 28.798450469970703, 29.019977569580078, 29.241504669189453, 29.463029861450195, 29.68455696105957, 29.906084060668945, 30.12761116027832, 30.349136352539062, 30.570663452148438, 30.792190551757812, 31.013715744018555, 31.23524284362793], "101": [4.857390403747559, 5.07818078994751, 5.298971176147461, 5.519761562347412, 5.740551948547363, 5.961342811584473, 6.182133197784424, 6.402923583984375, 6.623713970184326, 6.844504356384277, 7.0652947425842285, 7.286085605621338, 7.506875991821289, 7.72766637802124, 7.948456764221191, 8.1692476272583, 8.390037536621094, 8.610828399658203, 8.831618309020996, 9.052409172058105, 9.273200035095215, 9.493989944458008, 9.714780807495117, 9.93557071685791, 10.15636157989502, 10.377151489257812, 10.597942352294922, 10.818733215332031, 11.039523124694824, 11.260313987731934, 11.481103897094727, 11.701894760131836, 11.922685623168945, 12.143475532531738, 12.364266395568848, 12.58505630493164, 12.80584716796875, 13.026637077331543, 13.247427940368652, 13.468218803405762, 13.689008712768555, 13.909799575805664, 14.130589485168457, 14.351380348205566, 14.572171211242676, 14.792961120605469, 15.013751983642578, 15.234541893005371, 15.45533275604248, 15.67612361907959, 15.896913528442383, 16.117704391479492, 16.3384952545166, 16.559284210205078, 16.780075073242188, 17.000865936279297, 17.221656799316406, 17.442447662353516, 17.663236618041992, 17.8840274810791, 18.10481834411621, 18.32560920715332, 18.54640007019043, 18.767189025878906, 18.987979888916016, 19.208770751953125, 19.429561614990234, 19.650352478027344, 19.87114143371582, 20.09193229675293, 20.31272315979004, 20.53351402282715, 20.754302978515625, 20.975093841552734, 21.195884704589844, 21.416675567626953, 21.637466430664062, 21.85825538635254, 22.07904624938965, 22.299837112426758, 22.520627975463867, 22.741418838500977, 22.962207794189453, 23.182998657226562, 23.403789520263672, 23.62458038330078, 23.84537124633789, 24.066160202026367, 24.286951065063477, 24.507741928100586, 24.728532791137695, 24.949323654174805, 25.17011260986328, 25.39090347290039, 25.6116943359375, 25.83248519897461, 26.053274154663086, 26.274065017700195, 26.494855880737305, 26.715646743774414, 26.936437606811523, 27.1572265625, 27.37801742553711, 27.59880828857422, 27.819599151611328, 28.040390014648438, 28.261178970336914, 28.481969833374023, 28.702760696411133, 28.923551559448242, 29.14434242248535, 29.365131378173828, 29.585922241210938, 29.806713104248047, 30.027503967285156, 30.248294830322266, 30.469083786010742, 30.68987464904785, 30.91066551208496, 31.13145637512207], "102": [4.841322422027588, 5.061382293701172, 5.281442642211914, 5.501502513885498, 5.72156286239624, 5.941622734069824, 6.161683082580566, 6.38174295425415, 6.601803302764893, 6.821863174438477, 7.041923522949219, 7.261983394622803, 7.482043266296387, 7.702103614807129, 7.922163486480713, 8.142223358154297, 8.362283706665039, 8.582344055175781, 8.802404403686523, 9.02246379852295, 9.242524147033691, 9.462584495544434, 9.682644844055176, 9.902704238891602, 10.122764587402344, 10.342824935913086, 10.562885284423828, 10.782944679260254, 11.003005027770996, 11.223065376281738, 11.44312572479248, 11.663185119628906, 11.883245468139648, 12.10330581665039, 12.323366165161133, 12.543425559997559, 12.7634859085083, 12.983546257019043, 13.203606605529785, 13.423666000366211, 13.643726348876953, 13.863786697387695, 14.083847045898438, 14.303906440734863, 14.523966789245605, 14.744027137756348, 14.964086532592773, 15.184146881103516, 15.404207229614258, 15.624267578125, 15.844326972961426, 16.064388275146484, 16.284446716308594, 16.504507064819336, 16.724567413330078, 16.94462776184082, 17.164688110351562, 17.384748458862305, 17.604808807373047, 17.82486915588379, 18.0449275970459, 18.26498794555664, 18.485048294067383, 18.705108642578125, 18.925168991088867, 19.14522933959961, 19.36528968811035, 19.585350036621094, 19.805408477783203, 20.025468826293945, 20.245529174804688, 20.46558952331543, 20.685649871826172, 20.905710220336914, 21.125770568847656, 21.3458309173584, 21.565889358520508, 21.78594970703125, 22.006010055541992, 22.226070404052734, 22.446130752563477, 22.66619110107422, 22.88625144958496, 23.10630989074707, 23.326370239257812, 23.546430587768555, 23.766490936279297, 23.98655128479004, 24.20661163330078, 24.426671981811523, 24.646732330322266, 24.866790771484375, 25.086851119995117, 25.30691146850586, 25.5269718170166, 25.747032165527344, 25.967092514038086, 26.187152862548828, 26.40721321105957, 26.62727165222168, 26.847332000732422, 27.067392349243164, 27.287452697753906, 27.50751304626465, 27.72757339477539, 27.947633743286133, 28.167694091796875, 28.387752532958984, 28.607812881469727, 28.82787322998047, 29.04793357849121, 29.267993927001953, 29.488054275512695, 29.708114624023438, 29.928173065185547, 30.14823341369629, 30.36829376220703, 30.588354110717773, 30.808414459228516, 31.028474807739258], "103": [4.82537841796875, 5.044713973999023, 5.264049530029297, 5.483384609222412, 5.7027201652526855, 5.922055721282959, 6.141390800476074, 6.360726356506348, 6.580061912536621, 6.799396991729736, 7.01873254776001, 7.238068103790283, 7.457403182983398, 7.676738739013672, 7.896074295043945, 8.115409851074219, 8.334744453430176, 8.55408000946045, 8.773415565490723, 8.992751121520996, 9.21208667755127, 9.431422233581543, 9.6507568359375, 9.870092391967773, 10.089427947998047, 10.30876350402832, 10.528099060058594, 10.747434616088867, 10.966769218444824, 11.186104774475098, 11.405440330505371, 11.624775886535645, 11.844111442565918, 12.063446998596191, 12.282781600952148, 12.502117156982422, 12.721452713012695, 12.940788269042969, 13.160123825073242, 13.3794584274292, 13.598793983459473, 13.818129539489746, 14.03746509552002, 14.256800651550293, 14.476136207580566, 14.695470809936523, 14.914806365966797, 15.13414192199707, 15.353477478027344, 15.572813034057617, 15.79214859008789, 16.011484146118164, 16.230819702148438, 16.45015525817871, 16.66948890686035, 16.888824462890625, 17.1081600189209, 17.327495574951172, 17.546831130981445, 17.76616668701172, 17.985502243041992, 18.204837799072266, 18.42417335510254, 18.643508911132812, 18.862844467163086, 19.08218002319336, 19.301513671875, 19.520849227905273, 19.740184783935547, 19.95952033996582, 20.178855895996094, 20.398191452026367, 20.61752700805664, 20.836862564086914, 21.056198120117188, 21.27553367614746, 21.494869232177734, 21.714202880859375, 21.93353843688965, 22.152873992919922, 22.372209548950195, 22.59154510498047, 22.810880661010742, 23.030216217041016, 23.24955177307129, 23.468887329101562, 23.688222885131836, 23.90755844116211, 24.126893997192383, 24.346227645874023, 24.565563201904297, 24.78489875793457, 25.004234313964844, 25.223569869995117, 25.44290542602539, 25.662240982055664, 25.881576538085938, 26.10091209411621, 26.320247650146484, 26.539583206176758, 26.7589168548584, 26.978252410888672, 27.197587966918945, 27.41692352294922, 27.636259078979492, 27.855594635009766, 28.07493019104004, 28.294265747070312, 28.513601303100586, 28.73293685913086, 28.952272415161133, 29.171607971191406, 29.390941619873047, 29.61027717590332, 29.829612731933594, 30.048948287963867, 30.26828384399414, 30.487619400024414, 30.706954956054688, 30.92629051208496], "104": [4.809557914733887, 5.02817440032959, 5.246790409088135, 5.465406894683838, 5.684022903442383, 5.902639389038086, 6.121255397796631, 6.339871883392334, 6.558488368988037, 6.777104377746582, 6.995720863342285, 7.21433687210083, 7.432953357696533, 7.651569366455078, 7.870185852050781, 8.088802337646484, 8.307418823242188, 8.526034355163574, 8.744650840759277, 8.96326732635498, 9.181883811950684, 9.40049934387207, 9.619115829467773, 9.837732315063477, 10.05634880065918, 10.274965286254883, 10.49358081817627, 10.712197303771973, 10.930813789367676, 11.149430274963379, 11.368045806884766, 11.586662292480469, 11.805278778076172, 12.023895263671875, 12.242510795593262, 12.461127281188965, 12.679743766784668, 12.898360252380371, 13.116976737976074, 13.335592269897461, 13.554208755493164, 13.772825241088867, 13.99144172668457, 14.210057258605957, 14.42867374420166, 14.647290229797363, 14.865906715393066, 15.08452320098877, 15.303138732910156, 15.52175521850586, 15.740371704101562, 15.958988189697266, 16.17760467529297, 16.396221160888672, 16.614837646484375, 16.833452224731445, 17.05206871032715, 17.27068519592285, 17.489301681518555, 17.707918167114258, 17.92653465270996, 18.145151138305664, 18.363767623901367, 18.58238410949707, 18.80099868774414, 19.019615173339844, 19.238231658935547, 19.45684814453125, 19.675464630126953, 19.894081115722656, 20.11269760131836, 20.331314086914062, 20.549930572509766, 20.768545150756836, 20.98716163635254, 21.205778121948242, 21.424394607543945, 21.64301109313965, 21.86162757873535, 22.080244064331055, 22.298860549926758, 22.517475128173828, 22.73609161376953, 22.954708099365234, 23.173324584960938, 23.39194107055664, 23.610557556152344, 23.829174041748047, 24.04779052734375, 24.266407012939453, 24.485021591186523, 24.703638076782227, 24.92225456237793, 25.140871047973633, 25.359487533569336, 25.57810401916504, 25.796720504760742, 26.015336990356445, 26.23395347595215, 26.45256805419922, 26.671184539794922, 26.889801025390625, 27.108417510986328, 27.32703399658203, 27.545650482177734, 27.764266967773438, 27.98288345336914, 28.201499938964844, 28.420114517211914, 28.638731002807617, 28.85734748840332, 29.075963973999023, 29.294580459594727, 29.51319694519043, 29.731813430786133, 29.950429916381836, 30.16904640197754, 30.38766098022461, 30.606277465820312, 30.824893951416016], "105": [4.793859004974365, 5.011761665344238, 5.229664325714111, 5.447566986083984, 5.665469646453857, 5.8833723068237305, 6.1012749671936035, 6.319177627563477, 6.537080764770508, 6.754983425140381, 6.972886085510254, 7.190788745880127, 7.40869140625, 7.626594066619873, 7.844496726989746, 8.062398910522461, 8.280302047729492, 8.498205184936523, 8.716107368469238, 8.93401050567627, 9.151912689208984, 9.369815826416016, 9.58771800994873, 9.805621147155762, 10.023523330688477, 10.241426467895508, 10.459328651428223, 10.677231788635254, 10.895133972167969, 11.113037109375, 11.330939292907715, 11.548842430114746, 11.766744613647461, 11.984647750854492, 12.202549934387207, 12.420453071594238, 12.638355255126953, 12.856258392333984, 13.074161529541016, 13.29206371307373, 13.509966850280762, 13.727869033813477, 13.945772171020508, 14.163674354553223, 14.381577491760254, 14.599479675292969, 14.8173828125, 15.035284996032715, 15.253188133239746, 15.471090316772461, 15.688993453979492, 15.906895637512207, 16.124797821044922, 16.342700958251953, 16.560604095458984, 16.778507232666016, 16.996410369873047, 17.214311599731445, 17.432214736938477, 17.650117874145508, 17.86802101135254, 18.085922241210938, 18.30382537841797, 18.521728515625, 18.73963165283203, 18.95753288269043, 19.17543601989746, 19.393339157104492, 19.611242294311523, 19.829143524169922, 20.047046661376953, 20.264949798583984, 20.482852935791016, 20.700754165649414, 20.918657302856445, 21.136560440063477, 21.354463577270508, 21.57236671447754, 21.790267944335938, 22.00817108154297, 22.22607421875, 22.44397735595703, 22.66187858581543, 22.87978172302246, 23.097684860229492, 23.315587997436523, 23.533489227294922, 23.751392364501953, 23.969295501708984, 24.187198638916016, 24.405099868774414, 24.623003005981445, 24.840906143188477, 25.058809280395508, 25.276710510253906, 25.494613647460938, 25.71251678466797, 25.930419921875, 26.14832305908203, 26.36622428894043, 26.58412742614746, 26.802030563354492, 27.019933700561523, 27.237834930419922, 27.455738067626953, 27.673641204833984, 27.891544342041016, 28.109445571899414, 28.327348709106445, 28.545251846313477, 28.763154983520508, 28.981056213378906, 29.198959350585938, 29.41686248779297, 29.634765625, 29.85266876220703, 30.07056999206543, 30.28847312927246, 30.506376266479492, 30.724279403686523], "106": [4.778280735015869, 4.9954752922058105, 5.212669849395752, 5.429864406585693, 5.647058963775635, 5.864253520965576, 6.081448078155518, 6.298642635345459, 6.5158371925354, 6.733031749725342, 6.950226306915283, 7.167420864105225, 7.384615421295166, 7.601809978485107, 7.819004535675049, 8.036198616027832, 8.253393173217773, 8.470588684082031, 8.687783241271973, 8.904977798461914, 9.122172355651855, 9.339366912841797, 9.556561470031738, 9.77375602722168, 9.990950584411621, 10.208145141601562, 10.425339698791504, 10.642534255981445, 10.859728813171387, 11.076923370361328, 11.29411792755127, 11.511312484741211, 11.728507041931152, 11.945701599121094, 12.162896156311035, 12.380090713500977, 12.597285270690918, 12.81447982788086, 13.0316743850708, 13.248868942260742, 13.466063499450684, 13.683258056640625, 13.900452613830566, 14.117647171020508, 14.33484172821045, 14.55203628540039, 14.769230842590332, 14.986425399780273, 15.203619956970215, 15.420814514160156, 15.638009071350098, 15.855203628540039, 16.072397232055664, 16.289592742919922, 16.506786346435547, 16.723981857299805, 16.941177368164062, 17.158370971679688, 17.375566482543945, 17.59276008605957, 17.809955596923828, 18.027149200439453, 18.24434471130371, 18.461538314819336, 18.678733825683594, 18.89592742919922, 19.113122940063477, 19.3303165435791, 19.54751205444336, 19.764705657958984, 19.981901168823242, 20.199094772338867, 20.416290283203125, 20.63348388671875, 20.850679397583008, 21.067873001098633, 21.28506851196289, 21.502262115478516, 21.719457626342773, 21.9366512298584, 22.153846740722656, 22.37104034423828, 22.58823585510254, 22.805429458618164, 23.022624969482422, 23.239818572998047, 23.457014083862305, 23.67420768737793, 23.891403198242188, 24.108596801757812, 24.32579231262207, 24.542985916137695, 24.760181427001953, 24.977375030517578, 25.194570541381836, 25.41176414489746, 25.62895965576172, 25.846153259277344, 26.0633487701416, 26.280542373657227, 26.497737884521484, 26.71493148803711, 26.932126998901367, 27.149320602416992, 27.36651611328125, 27.583709716796875, 27.800905227661133, 28.018098831176758, 28.235294342041016, 28.45248794555664, 28.6696834564209, 28.886877059936523, 29.10407257080078, 29.321266174316406, 29.538461685180664, 29.75565528869629, 29.972850799560547, 30.190044403076172, 30.40723991394043, 30.624433517456055], "107": [4.762821197509766, 4.979312896728516, 5.195804595947266, 5.412296772003174, 5.628788471221924, 5.845280647277832, 6.061772346496582, 6.278264045715332, 6.49475622177124, 6.71124792098999, 6.92773962020874, 7.144231796264648, 7.360723495483398, 7.577215194702148, 7.793707370758057, 8.010199546813965, 8.226691246032715, 8.443182945251465, 8.659674644470215, 8.876166343688965, 9.092658042907715, 9.309150695800781, 9.525642395019531, 9.742134094238281, 9.958625793457031, 10.175117492675781, 10.391609191894531, 10.608101844787598, 10.824593544006348, 11.041085243225098, 11.257576942443848, 11.474068641662598, 11.690561294555664, 11.907052993774414, 12.123544692993164, 12.340036392211914, 12.556528091430664, 12.773019790649414, 12.98951244354248, 13.20600414276123, 13.42249584197998, 13.63898754119873, 13.85547924041748, 14.07197093963623, 14.288463592529297, 14.504955291748047, 14.721446990966797, 14.937938690185547, 15.154430389404297, 15.370923042297363, 15.587414741516113, 15.803906440734863, 16.02039909362793, 16.23689079284668, 16.45338249206543, 16.66987419128418, 16.88636589050293, 17.10285758972168, 17.31934928894043, 17.53584098815918, 17.75233268737793, 17.96882438659668, 18.18531608581543, 18.401809692382812, 18.618301391601562, 18.834793090820312, 19.051284790039062, 19.267776489257812, 19.484268188476562, 19.700759887695312, 19.917251586914062, 20.133743286132812, 20.350234985351562, 20.566726684570312, 20.783218383789062, 20.999711990356445, 21.216203689575195, 21.432695388793945, 21.649187088012695, 21.865678787231445, 22.082170486450195, 22.298662185668945, 22.515153884887695, 22.731645584106445, 22.948137283325195, 23.164628982543945, 23.381122589111328, 23.597614288330078, 23.814105987548828, 24.030597686767578, 24.247089385986328, 24.463581085205078, 24.680072784423828, 24.896564483642578, 25.113056182861328, 25.329547882080078, 25.546039581298828, 25.76253318786621, 25.97902488708496, 26.19551658630371, 26.41200828552246, 26.62849998474121, 26.84499168395996, 27.06148338317871, 27.27797508239746, 27.49446678161621, 27.71095848083496, 27.92745018005371, 28.14394187927246, 28.360435485839844, 28.576927185058594, 28.793418884277344, 29.009910583496094, 29.226402282714844, 29.442893981933594, 29.659385681152344, 29.875877380371094, 30.092369079589844, 30.308860778808594, 30.525352478027344], "108": [4.747479438781738, 4.963274002075195, 5.179068565368652, 5.394863128662109, 5.610657691955566, 5.826452255249023, 6.0422468185424805, 6.258040904998779, 6.473835468292236, 6.689630031585693, 6.90542459487915, 7.121219158172607, 7.3370137214660645, 7.5528082847595215, 7.7686028480529785, 7.9843974113464355, 8.200191497802734, 8.415986061096191, 8.631780624389648, 8.847575187683105, 9.063369750976562, 9.27916431427002, 9.494958877563477, 9.710753440856934, 9.92654800415039, 10.142342567443848, 10.358137130737305, 10.573931694030762, 10.789726257324219, 11.005520820617676, 11.221315383911133, 11.43710994720459, 11.652904510498047, 11.868699073791504, 12.084493637084961, 12.300288200378418, 12.516081809997559, 12.731876373291016, 12.947670936584473, 13.16346549987793, 13.379260063171387, 13.595054626464844, 13.8108491897583, 14.026643753051758, 14.242438316345215, 14.458232879638672, 14.674027442932129, 14.889822006225586, 15.105616569519043, 15.3214111328125, 15.537205696105957, 15.753000259399414, 15.968794822692871, 16.184589385986328, 16.40038299560547, 16.616178512573242, 16.831972122192383, 17.047767639160156, 17.263561248779297, 17.47935676574707, 17.69515037536621, 17.910945892333984, 18.126739501953125, 18.3425350189209, 18.55832862854004, 18.774124145507812, 18.989917755126953, 19.205713272094727, 19.421506881713867, 19.63730239868164, 19.85309600830078, 20.068889617919922, 20.284685134887695, 20.500478744506836, 20.71627426147461, 20.93206787109375, 21.147863388061523, 21.363656997680664, 21.579452514648438, 21.795246124267578, 22.01104164123535, 22.226835250854492, 22.442630767822266, 22.658424377441406, 22.87421989440918, 23.09001350402832, 23.305809020996094, 23.521602630615234, 23.737398147583008, 23.95319175720215, 24.168987274169922, 24.384780883789062, 24.600576400756836, 24.816370010375977, 25.032163619995117, 25.24795913696289, 25.46375274658203, 25.679548263549805, 25.895341873168945, 26.11113739013672, 26.32693099975586, 26.542726516723633, 26.758520126342773, 26.974315643310547, 27.190109252929688, 27.40590476989746, 27.6216983795166, 27.837493896484375, 28.053287506103516, 28.26908302307129, 28.48487663269043, 28.700672149658203, 28.916465759277344, 29.132261276245117, 29.348054885864258, 29.56385040283203, 29.779644012451172, 29.995437622070312, 30.211233139038086, 30.427026748657227], "109": [4.732254505157471, 4.947356700897217, 5.162459373474121, 5.377562046051025, 5.5926642417907715, 5.807766914367676, 6.022869110107422, 6.237971782684326, 6.4530744552612305, 6.668176651000977, 6.883279323577881, 7.098381519317627, 7.313484191894531, 7.5285868644714355, 7.743689060211182, 7.958791732788086, 8.173893928527832, 8.388996124267578, 8.60409927368164, 8.819201469421387, 9.034303665161133, 9.249406814575195, 9.464509010314941, 9.679611206054688, 9.894713401794434, 10.109816551208496, 10.324918746948242, 10.540020942687988, 10.75512409210205, 10.970226287841797, 11.185328483581543, 11.400431632995605, 11.615533828735352, 11.830636024475098, 12.045738220214844, 12.260841369628906, 12.475943565368652, 12.691045761108398, 12.906148910522461, 13.121251106262207, 13.336353302001953, 13.5514554977417, 13.766558647155762, 13.981660842895508, 14.196763038635254, 14.411866188049316, 14.626968383789062, 14.842070579528809, 15.057173728942871, 15.272275924682617, 15.487378120422363, 15.70248031616211, 15.917583465576172, 16.1326847076416, 16.347787857055664, 16.562891006469727, 16.777992248535156, 16.99309539794922, 17.20819854736328, 17.42329978942871, 17.638402938842773, 17.853506088256836, 18.068607330322266, 18.283710479736328, 18.49881362915039, 18.71391487121582, 18.929018020629883, 19.144121170043945, 19.359222412109375, 19.574325561523438, 19.789426803588867, 20.00452995300293, 20.219633102416992, 20.434734344482422, 20.649837493896484, 20.864940643310547, 21.080041885375977, 21.29514503479004, 21.5102481842041, 21.72534942626953, 21.940452575683594, 22.155555725097656, 22.370656967163086, 22.58576011657715, 22.80086326599121, 23.01596450805664, 23.231067657470703, 23.446168899536133, 23.661272048950195, 23.876375198364258, 24.091476440429688, 24.30657958984375, 24.521682739257812, 24.736783981323242, 24.951887130737305, 25.166990280151367, 25.382091522216797, 25.59719467163086, 25.812297821044922, 26.02739906311035, 26.242502212524414, 26.457605361938477, 26.672706604003906, 26.88780975341797, 27.1029109954834, 27.31801414489746, 27.533117294311523, 27.748218536376953, 27.963321685791016, 28.178424835205078, 28.393526077270508, 28.60862922668457, 28.823732376098633, 29.038833618164062, 29.253936767578125, 29.469039916992188, 29.684141159057617, 29.89924430847168, 30.114347457885742, 30.329448699951172], "110": [4.717144966125488, 4.931560516357422, 5.1459760665893555, 5.360391616821289, 5.574807643890381, 5.7892231941223145, 6.003638744354248, 6.218054294586182, 6.432470321655273, 6.646885871887207, 6.861301422119141, 7.075716972351074, 7.290132999420166, 7.5045485496521, 7.718964099884033, 7.933379650115967, 8.147795677185059, 8.362211227416992, 8.576626777648926, 8.79104232788086, 9.005457878112793, 9.219873428344727, 9.434289932250977, 9.64870548248291, 9.863121032714844, 10.077536582946777, 10.291952133178711, 10.506367683410645, 10.720783233642578, 10.935198783874512, 11.149615287780762, 11.364030838012695, 11.578446388244629, 11.792861938476562, 12.007277488708496, 12.22169303894043, 12.436108589172363, 12.650524139404297, 12.864940643310547, 13.07935619354248, 13.293771743774414, 13.508187294006348, 13.722602844238281, 13.937018394470215, 14.151433944702148, 14.365850448608398, 14.580265998840332, 14.794681549072266, 15.0090970993042, 15.223512649536133, 15.437928199768066, 15.65234375, 15.866759300231934, 16.081174850463867, 16.295591354370117, 16.510005950927734, 16.724422454833984, 16.938838958740234, 17.15325355529785, 17.3676700592041, 17.58208465576172, 17.79650115966797, 18.010915756225586, 18.225332260131836, 18.439746856689453, 18.654163360595703, 18.868579864501953, 19.08299446105957, 19.29741096496582, 19.511825561523438, 19.726242065429688, 19.940656661987305, 20.155073165893555, 20.369489669799805, 20.583904266357422, 20.798320770263672, 21.01273536682129, 21.22715187072754, 21.441566467285156, 21.655982971191406, 21.870397567749023, 22.084814071655273, 22.299230575561523, 22.51364517211914, 22.72806167602539, 22.942476272583008, 23.156892776489258, 23.371307373046875, 23.585723876953125, 23.800140380859375, 24.014554977416992, 24.228971481323242, 24.44338607788086, 24.65780258178711, 24.872217178344727, 25.086633682250977, 25.301048278808594, 25.515464782714844, 25.729881286621094, 25.94429588317871, 26.15871238708496, 26.373126983642578, 26.587543487548828, 26.801958084106445, 27.016374588012695, 27.230791091918945, 27.445205688476562, 27.659622192382812, 27.87403678894043, 28.08845329284668, 28.302867889404297, 28.517284393310547, 28.731700897216797, 28.946115493774414, 29.160531997680664, 29.37494659423828, 29.58936309814453, 29.80377769470215, 30.0181941986084, 30.232608795166016], "111": [4.702149391174316, 4.9158830642700195, 5.129617214202881, 5.343351364135742, 5.5570855140686035, 5.770819664001465, 5.984553337097168, 6.198287487030029, 6.412021636962891, 6.625755786895752, 6.839489936828613, 7.053223609924316, 7.266957759857178, 7.480691909790039, 7.6944260597229, 7.908160209655762, 8.121893882751465, 8.335628509521484, 8.549362182617188, 8.76309585571289, 8.97683048248291, 9.190564155578613, 9.404298782348633, 9.618032455444336, 9.831766128540039, 10.045500755310059, 10.259234428405762, 10.472969055175781, 10.686702728271484, 10.900436401367188, 11.114171028137207, 11.32790470123291, 11.54163932800293, 11.755373001098633, 11.969106674194336, 12.182841300964355, 12.396574974060059, 12.610309600830078, 12.824043273925781, 13.037776947021484, 13.251511573791504, 13.465245246887207, 13.678979873657227, 13.89271354675293, 14.106447219848633, 14.320181846618652, 14.533915519714355, 14.747650146484375, 14.961383819580078, 15.175117492675781, 15.3888521194458, 15.602585792541504, 15.816320419311523, 16.030054092407227, 16.24378776550293, 16.457521438598633, 16.67125701904297, 16.884990692138672, 17.098724365234375, 17.312458038330078, 17.52619171142578, 17.739927291870117, 17.95366096496582, 18.167394638061523, 18.381128311157227, 18.59486198425293, 18.808597564697266, 19.02233123779297, 19.236064910888672, 19.449798583984375, 19.663532257080078, 19.877267837524414, 20.091001510620117, 20.30473518371582, 20.518468856811523, 20.732202529907227, 20.945938110351562, 21.159671783447266, 21.37340545654297, 21.587139129638672, 21.800872802734375, 22.01460838317871, 22.228342056274414, 22.442075729370117, 22.65580940246582, 22.869543075561523, 23.08327865600586, 23.297012329101562, 23.510746002197266, 23.72447967529297, 23.938213348388672, 24.151948928833008, 24.36568260192871, 24.579416275024414, 24.793149948120117, 25.00688362121582, 25.220619201660156, 25.43435287475586, 25.648086547851562, 25.861820220947266, 26.07555389404297, 26.289289474487305, 26.503023147583008, 26.71675682067871, 26.930490493774414, 27.144224166870117, 27.357959747314453, 27.571693420410156, 27.78542709350586, 27.999160766601562, 28.212894439697266, 28.4266300201416, 28.640363693237305, 28.854097366333008, 29.06783103942871, 29.281564712524414, 29.49530029296875, 29.709033966064453, 29.922767639160156, 30.13650131225586], "112": [4.687266826629639, 4.90032434463501, 5.113381862640381, 5.326439380645752, 5.539496898651123, 5.752554416656494, 5.965611934661865, 6.178669452667236, 6.391726970672607, 6.604784965515137, 6.817842483520508, 7.030900001525879, 7.24395751953125, 7.457015037536621, 7.670072555541992, 7.883130073547363, 8.096187591552734, 8.309245109558105, 8.522302627563477, 8.735360145568848, 8.948417663574219, 9.16147518157959, 9.374533653259277, 9.587591171264648, 9.80064868927002, 10.01370620727539, 10.226763725280762, 10.439821243286133, 10.652878761291504, 10.865936279296875, 11.078993797302246, 11.292051315307617, 11.505108833312988, 11.71816635131836, 11.93122386932373, 12.144281387329102, 12.357338905334473, 12.570396423339844, 12.783453941345215, 12.996511459350586, 13.209569931030273, 13.422627449035645, 13.635684967041016, 13.848742485046387, 14.061800003051758, 14.274857521057129, 14.4879150390625, 14.700972557067871, 14.914030075073242, 15.127087593078613, 15.340145111083984, 15.553202629089355, 15.766260147094727, 15.979317665100098, 16.19237518310547, 16.405433654785156, 16.61849021911621, 16.8315486907959, 17.044605255126953, 17.25766372680664, 17.470720291137695, 17.683778762817383, 17.896835327148438, 18.109893798828125, 18.32295036315918, 18.536008834838867, 18.749067306518555, 18.96212387084961, 19.175182342529297, 19.38823890686035, 19.60129737854004, 19.814353942871094, 20.02741241455078, 20.240468978881836, 20.453527450561523, 20.666584014892578, 20.879642486572266, 21.09269905090332, 21.305757522583008, 21.518814086914062, 21.73187255859375, 21.944929122924805, 22.157987594604492, 22.371044158935547, 22.584102630615234, 22.797161102294922, 23.010217666625977, 23.223276138305664, 23.43633270263672, 23.649391174316406, 23.86244773864746, 24.07550621032715, 24.288562774658203, 24.50162124633789, 24.714677810668945, 24.927736282348633, 25.140792846679688, 25.353851318359375, 25.56690788269043, 25.779966354370117, 25.993022918701172, 26.20608139038086, 26.419139862060547, 26.6321964263916, 26.84525489807129, 27.058311462402344, 27.27136993408203, 27.484426498413086, 27.697484970092773, 27.910541534423828, 28.123600006103516, 28.33665657043457, 28.549715042114258, 28.762771606445312, 28.975830078125, 29.188886642456055, 29.401945114135742, 29.615001678466797, 29.828060150146484, 30.041118621826172], "113": [4.6724958419799805, 4.884881973266602, 5.097268104553223, 5.309654235839844, 5.522040367126465, 5.734426498413086, 5.946812629699707, 6.159198760986328, 6.371584892272949, 6.58397102355957, 6.79635763168335, 7.008743762969971, 7.221129894256592, 7.433516025543213, 7.645902156829834, 7.858288288116455, 8.070673942565918, 8.283061027526855, 8.495447158813477, 8.707833290100098, 8.920219421386719, 9.13260555267334, 9.344991683959961, 9.557377815246582, 9.769763946533203, 9.982150077819824, 10.194536209106445, 10.406922340393066, 10.619308471679688, 10.831694602966309, 11.04408073425293, 11.25646686553955, 11.468852996826172, 11.681239128112793, 11.893625259399414, 12.106011390686035, 12.318397521972656, 12.530783653259277, 12.743169784545898, 12.95555591583252, 13.16794204711914, 13.380328178405762, 13.5927152633667, 13.80510139465332, 14.017487525939941, 14.229873657226562, 14.442259788513184, 14.654645919799805, 14.867032051086426, 15.079418182373047, 15.291804313659668, 15.504190444946289, 15.71657657623291, 15.928962707519531, 16.141347885131836, 16.353734970092773, 16.56612205505371, 16.778507232666016, 16.990894317626953, 17.203279495239258, 17.415666580200195, 17.6280517578125, 17.840438842773438, 18.052824020385742, 18.26521110534668, 18.477596282958984, 18.689983367919922, 18.902368545532227, 19.114755630493164, 19.32714080810547, 19.539527893066406, 19.75191307067871, 19.96430015563965, 20.176685333251953, 20.38907241821289, 20.601457595825195, 20.813844680786133, 21.026229858398438, 21.238616943359375, 21.45100212097168, 21.663389205932617, 21.875776290893555, 22.08816146850586, 22.300548553466797, 22.5129337310791, 22.72532081604004, 22.937705993652344, 23.15009307861328, 23.362478256225586, 23.574865341186523, 23.787250518798828, 23.999637603759766, 24.21202278137207, 24.424409866333008, 24.636795043945312, 24.84918212890625, 25.061567306518555, 25.273954391479492, 25.486339569091797, 25.698726654052734, 25.91111183166504, 26.123498916625977, 26.33588409423828, 26.54827117919922, 26.760656356811523, 26.97304344177246, 27.1854305267334, 27.397815704345703, 27.61020278930664, 27.822587966918945, 28.034975051879883, 28.247360229492188, 28.459747314453125, 28.67213249206543, 28.884519577026367, 29.096904754638672, 29.30929183959961, 29.521677017211914, 29.73406410217285, 29.946449279785156], "114": [4.657835483551025, 4.8695549964904785, 5.08127498626709, 5.292994976043701, 5.504714488983154, 5.716434478759766, 5.928153991699219, 6.13987398147583, 6.351593971252441, 6.5633134841918945, 6.775033473968506, 6.986752986907959, 7.19847297668457, 7.410192489624023, 7.621912479400635, 7.833632469177246, 8.0453519821167, 8.257071495056152, 8.468791961669922, 8.680511474609375, 8.892230987548828, 9.103951454162598, 9.31567096710205, 9.527390480041504, 9.739109992980957, 9.950830459594727, 10.16254997253418, 10.374269485473633, 10.585989952087402, 10.797709465026855, 11.009428977966309, 11.221148490905762, 11.432868957519531, 11.644588470458984, 11.856307983398438, 12.068028450012207, 12.27974796295166, 12.491467475891113, 12.703187942504883, 12.914907455444336, 13.126626968383789, 13.338346481323242, 13.550066947937012, 13.761786460876465, 13.973505973815918, 14.185226440429688, 14.39694595336914, 14.608665466308594, 14.820384979248047, 15.032105445861816, 15.24382495880127, 15.455544471740723, 15.667264938354492, 15.878984451293945, 16.0907039642334, 16.30242347717285, 16.514142990112305, 16.72586441040039, 16.937583923339844, 17.149303436279297, 17.36102294921875, 17.572742462158203, 17.784461975097656, 17.99618148803711, 18.207902908325195, 18.41962242126465, 18.6313419342041, 18.843061447143555, 19.054780960083008, 19.26650047302246, 19.478219985961914, 19.68994140625, 19.901660919189453, 20.113380432128906, 20.32509994506836, 20.536819458007812, 20.748538970947266, 20.96025848388672, 21.171979904174805, 21.383699417114258, 21.59541893005371, 21.807138442993164, 22.018857955932617, 22.23057746887207, 22.442296981811523, 22.65401840209961, 22.865737915039062, 23.077457427978516, 23.28917694091797, 23.500896453857422, 23.712615966796875, 23.92433738708496, 24.136056900024414, 24.347776412963867, 24.55949592590332, 24.771215438842773, 24.982934951782227, 25.19465446472168, 25.406375885009766, 25.61809539794922, 25.829814910888672, 26.041534423828125, 26.253253936767578, 26.46497344970703, 26.676692962646484, 26.88841438293457, 27.100133895874023, 27.311853408813477, 27.52357292175293, 27.735292434692383, 27.947011947631836, 28.15873146057129, 28.370452880859375, 28.582172393798828, 28.79389190673828, 29.005611419677734, 29.217330932617188, 29.42905044555664, 29.640769958496094, 29.85249137878418], "115": [4.643284320831299, 4.854342937469482, 5.065401554107666, 5.276459693908691, 5.487518310546875, 5.6985764503479, 5.909635066986084, 6.120693206787109, 6.331751823425293, 6.542809963226318, 6.753868579864502, 6.964926719665527, 7.175985336303711, 7.387043476104736, 7.59810209274292, 7.809160232543945, 8.020218849182129, 8.231277465820312, 8.44233512878418, 8.653393745422363, 8.864452362060547, 9.07551097869873, 9.286568641662598, 9.497627258300781, 9.708685874938965, 9.919744491577148, 10.130803108215332, 10.3418607711792, 10.552919387817383, 10.763978004455566, 10.97503662109375, 11.186094284057617, 11.3971529006958, 11.608211517333984, 11.819270133972168, 12.030327796936035, 12.241386413574219, 12.452445030212402, 12.663503646850586, 12.874561309814453, 13.085619926452637, 13.29667854309082, 13.507737159729004, 13.718794822692871, 13.929853439331055, 14.140912055969238, 14.351970672607422, 14.563029289245605, 14.774086952209473, 14.985145568847656, 15.19620418548584, 15.407262802124023, 15.61832046508789, 15.829379081726074, 16.040437698364258, 16.251495361328125, 16.462554931640625, 16.673612594604492, 16.88467025756836, 17.09572982788086, 17.306787490844727, 17.517847061157227, 17.728904724121094, 17.93996238708496, 18.15102195739746, 18.362079620361328, 18.573137283325195, 18.784196853637695, 18.995254516601562, 19.206314086914062, 19.41737174987793, 19.628429412841797, 19.839488983154297, 20.050546646118164, 20.261606216430664, 20.47266387939453, 20.6837215423584, 20.8947811126709, 21.105838775634766, 21.316896438598633, 21.527956008911133, 21.739013671875, 21.9500732421875, 22.161130905151367, 22.372188568115234, 22.583248138427734, 22.7943058013916, 23.00536346435547, 23.21642303466797, 23.427480697631836, 23.638540267944336, 23.849597930908203, 24.06065559387207, 24.27171516418457, 24.482772827148438, 24.693832397460938, 24.904890060424805, 25.115947723388672, 25.327007293701172, 25.53806495666504, 25.749122619628906, 25.960182189941406, 26.171239852905273, 26.382299423217773, 26.59335708618164, 26.804414749145508, 27.015474319458008, 27.226531982421875, 27.437589645385742, 27.648649215698242, 27.85970687866211, 28.07076644897461, 28.281824111938477, 28.492881774902344, 28.703941345214844, 28.91499900817871, 29.12605857849121, 29.337116241455078, 29.548173904418945, 29.759233474731445], "116": [4.628841876983643, 4.8392438888549805, 5.049645900726318, 5.260047912597656, 5.470449447631836, 5.680851459503174, 5.891253471374512, 6.10165548324585, 6.3120574951171875, 6.522459030151367, 6.732861042022705, 6.943263053894043, 7.153665065765381, 7.3640666007995605, 7.574468612670898, 7.784870624542236, 7.995272636413574, 8.205674171447754, 8.41607666015625, 8.62647819519043, 8.83687973022461, 9.047282218933105, 9.257683753967285, 9.468086242675781, 9.678487777709961, 9.88888931274414, 10.099291801452637, 10.309693336486816, 10.520095825195312, 10.730497360229492, 10.940898895263672, 11.151301383972168, 11.361702919006348, 11.572105407714844, 11.782506942749023, 11.992908477783203, 12.2033109664917, 12.413712501525879, 12.624114990234375, 12.834516525268555, 13.044918060302734, 13.25532054901123, 13.46572208404541, 13.67612361907959, 13.886526107788086, 14.096927642822266, 14.307330131530762, 14.517731666564941, 14.728133201599121, 14.938535690307617, 15.148937225341797, 15.359339714050293, 15.569741249084473, 15.780142784118652, 15.990545272827148, 16.200946807861328, 16.411348342895508, 16.621749877929688, 16.8321533203125, 17.04255485534668, 17.25295639038086, 17.46335792541504, 17.67375946044922, 17.88416290283203, 18.09456443786621, 18.30496597290039, 18.51536750793457, 18.72576904296875, 18.936172485351562, 19.146574020385742, 19.356975555419922, 19.5673770904541, 19.77777862548828, 19.988182067871094, 20.198583602905273, 20.408985137939453, 20.619386672973633, 20.829788208007812, 21.040191650390625, 21.250593185424805, 21.460994720458984, 21.671396255493164, 21.881797790527344, 22.092201232910156, 22.302602767944336, 22.513004302978516, 22.723405838012695, 22.933807373046875, 23.144210815429688, 23.354612350463867, 23.565013885498047, 23.775415420532227, 23.985816955566406, 24.19622039794922, 24.4066219329834, 24.617023468017578, 24.827425003051758, 25.037826538085938, 25.24822998046875, 25.45863151550293, 25.66903305053711, 25.87943458557129, 26.08983612060547, 26.30023956298828, 26.51064109802246, 26.72104263305664, 26.93144416809082, 27.141845703125, 27.35224723815918, 27.562650680541992, 27.773052215576172, 27.98345375061035, 28.19385528564453, 28.40425682067871, 28.614660263061523, 28.825061798095703, 29.035463333129883, 29.245864868164062, 29.456266403198242, 29.666669845581055], "117": [4.614506721496582, 4.824256896972656, 5.0340070724487305, 5.243757724761963, 5.453507900238037, 5.663258075714111, 5.8730082511901855, 6.082758903503418, 6.292509078979492, 6.502259254455566, 6.712009429931641, 6.921760082244873, 7.131510257720947, 7.3412604331970215, 7.551010608673096, 7.760761260986328, 7.970511436462402, 8.180261611938477, 8.39001178741455, 8.599761962890625, 8.809513092041016, 9.01926326751709, 9.229013442993164, 9.438763618469238, 9.648513793945312, 9.858263969421387, 10.068014144897461, 10.277764320373535, 10.487515449523926, 10.697265625, 10.907015800476074, 11.116765975952148, 11.326516151428223, 11.536266326904297, 11.746016502380371, 11.955767631530762, 12.165517807006836, 12.37526798248291, 12.585018157958984, 12.794768333435059, 13.004518508911133, 13.214268684387207, 13.424018859863281, 13.633769989013672, 13.843520164489746, 14.05327033996582, 14.263020515441895, 14.472770690917969, 14.682520866394043, 14.892271041870117, 15.102021217346191, 15.311772346496582, 15.521522521972656, 15.73127269744873, 15.941022872924805, 16.150774002075195, 16.360523223876953, 16.570274353027344, 16.7800235748291, 16.989774703979492, 17.19952392578125, 17.40927505493164, 17.61902618408203, 17.82877540588379, 18.03852653503418, 18.248275756835938, 18.458026885986328, 18.667776107788086, 18.877527236938477, 19.087276458740234, 19.297027587890625, 19.506778717041016, 19.716527938842773, 19.926279067993164, 20.136028289794922, 20.345779418945312, 20.55552864074707, 20.76527976989746, 20.97503089904785, 21.18478012084961, 21.39453125, 21.604280471801758, 21.81403160095215, 22.023780822753906, 22.233531951904297, 22.443283081054688, 22.653032302856445, 22.862783432006836, 23.072532653808594, 23.282283782958984, 23.492033004760742, 23.701784133911133, 23.911535263061523, 24.12128448486328, 24.331035614013672, 24.54078483581543, 24.75053596496582, 24.960285186767578, 25.17003631591797, 25.379785537719727, 25.589536666870117, 25.799287796020508, 26.009037017822266, 26.218788146972656, 26.428537368774414, 26.638288497924805, 26.848037719726562, 27.057788848876953, 27.267539978027344, 27.4772891998291, 27.687040328979492, 27.89678955078125, 28.10654067993164, 28.3162899017334, 28.52604103088379, 28.73579216003418, 28.945541381835938, 29.155292510986328, 29.365041732788086, 29.574792861938477], "118": [4.600277423858643, 4.809381008148193, 5.018484592437744, 5.227587699890137, 5.4366912841796875, 5.645794868469238, 5.854898452758789, 6.06400203704834, 6.273105621337891, 6.482209205627441, 6.691312313079834, 6.900415897369385, 7.1095194816589355, 7.318623065948486, 7.527726650238037, 7.736830234527588, 7.9459333419799805, 8.155036926269531, 8.364140510559082, 8.573244094848633, 8.782347679138184, 8.991451263427734, 9.200554847717285, 9.409658432006836, 9.618762016296387, 9.827865600585938, 10.036969184875488, 10.246071815490723, 10.455175399780273, 10.664278984069824, 10.873382568359375, 11.082486152648926, 11.291589736938477, 11.500693321228027, 11.709796905517578, 11.918900489807129, 12.12800407409668, 12.33710765838623, 12.546211242675781, 12.755314826965332, 12.964418411254883, 13.173521041870117, 13.382624626159668, 13.591728210449219, 13.80083179473877, 14.00993537902832, 14.219038963317871, 14.428142547607422, 14.637246131896973, 14.846349716186523, 15.055453300476074, 15.264556884765625, 15.473660469055176, 15.682764053344727, 15.891866683959961, 16.100971221923828, 16.310073852539062, 16.51917839050293, 16.728281021118164, 16.93738555908203, 17.146488189697266, 17.3555908203125, 17.564695358276367, 17.7737979888916, 17.98290252685547, 18.192005157470703, 18.40110969543457, 18.610212326049805, 18.819316864013672, 19.028419494628906, 19.237524032592773, 19.446626663208008, 19.655731201171875, 19.86483383178711, 20.073938369750977, 20.28304100036621, 20.492143630981445, 20.701248168945312, 20.910350799560547, 21.119455337524414, 21.32855796813965, 21.537662506103516, 21.74676513671875, 21.955869674682617, 22.16497230529785, 22.37407684326172, 22.583179473876953, 22.79228401184082, 23.001386642456055, 23.21048927307129, 23.419593811035156, 23.62869644165039, 23.837800979614258, 24.046903610229492, 24.25600814819336, 24.465110778808594, 24.67421531677246, 24.883317947387695, 25.092422485351562, 25.301525115966797, 25.510629653930664, 25.7197322845459, 25.928836822509766, 26.137939453125, 26.347042083740234, 26.5561466217041, 26.765249252319336, 26.974353790283203, 27.183456420898438, 27.392560958862305, 27.60166358947754, 27.810768127441406, 28.01987075805664, 28.228975296020508, 28.438077926635742, 28.64718246459961, 28.856285095214844, 29.065387725830078, 29.274492263793945, 29.48359489440918], "119": [4.586153030395508, 4.794614315032959, 5.003076076507568, 5.2115373611450195, 5.419999122619629, 5.62846040725708, 5.8369221687316895, 6.045383453369141, 6.25384521484375, 6.462306499481201, 6.6707682609558105, 6.879229545593262, 7.087690830230713, 7.296152591705322, 7.504613876342773, 7.713075637817383, 7.921536922454834, 8.129998207092285, 8.338459968566895, 8.546921730041504, 8.755383491516113, 8.963844299316406, 9.172306060791016, 9.380767822265625, 9.589228630065918, 9.797690391540527, 10.006152153015137, 10.214613914489746, 10.423074722290039, 10.631536483764648, 10.839998245239258, 11.048460006713867, 11.25692081451416, 11.46538257598877, 11.673844337463379, 11.882305145263672, 12.090766906738281, 12.29922866821289, 12.5076904296875, 12.716151237487793, 12.924612998962402, 13.133074760437012, 13.341536521911621, 13.549997329711914, 13.758459091186523, 13.966920852661133, 14.175381660461426, 14.383843421936035, 14.592305183410645, 14.800766944885254, 15.009227752685547, 15.217689514160156, 15.426151275634766, 15.634613037109375, 15.843073844909668, 16.051536560058594, 16.25999641418457, 16.46845817565918, 16.67691993713379, 16.8853816986084, 17.093843460083008, 17.302305221557617, 17.510766983032227, 17.719226837158203, 17.927688598632812, 18.136150360107422, 18.34461212158203, 18.55307388305664, 18.76153564453125, 18.96999740600586, 19.178457260131836, 19.386919021606445, 19.595380783081055, 19.803842544555664, 20.012304306030273, 20.220766067504883, 20.429227828979492, 20.6376895904541, 20.846149444580078, 21.054611206054688, 21.263072967529297, 21.471534729003906, 21.679996490478516, 21.888458251953125, 22.096920013427734, 22.30537986755371, 22.51384162902832, 22.72230339050293, 22.93076515197754, 23.13922691345215, 23.347688674926758, 23.556150436401367, 23.764610290527344, 23.973072052001953, 24.181533813476562, 24.389995574951172, 24.59845733642578, 24.80691909790039, 25.015380859375, 25.22384262084961, 25.432302474975586, 25.640764236450195, 25.849225997924805, 26.057687759399414, 26.266149520874023, 26.474611282348633, 26.683073043823242, 26.89153289794922, 27.099994659423828, 27.308456420898438, 27.516918182373047, 27.725379943847656, 27.933841705322266, 28.142303466796875, 28.35076332092285, 28.55922508239746, 28.76768684387207, 28.97614860534668, 29.18461036682129, 29.3930721282959], "120": [4.572132587432861, 4.779956817626953, 4.987781047821045, 5.195605278015137, 5.4034295082092285, 5.61125373840332, 5.819077968597412, 6.026902198791504, 6.234726428985596, 6.4425506591796875, 6.650374889373779, 6.858199119567871, 7.066023349761963, 7.273847579956055, 7.4816718101501465, 7.689496040344238, 7.89732027053833, 8.105144500732422, 8.312968254089355, 8.520792961120605, 8.728616714477539, 8.936441421508789, 9.144265174865723, 9.352089881896973, 9.559913635253906, 9.767738342285156, 9.97556209564209, 10.18338680267334, 10.391210556030273, 10.599035263061523, 10.806859016418457, 11.01468276977539, 11.22250747680664, 11.430331230163574, 11.638155937194824, 11.845979690551758, 12.053804397583008, 12.261628150939941, 12.469452857971191, 12.677276611328125, 12.885101318359375, 13.092925071716309, 13.300749778747559, 13.508573532104492, 13.716398239135742, 13.924221992492676, 14.132046699523926, 14.33987045288086, 14.54769515991211, 14.755518913269043, 14.963343620300293, 15.171167373657227, 15.378992080688477, 15.58681583404541, 15.79464054107666, 16.002464294433594, 16.210289001464844, 16.41811180114746, 16.62593650817871, 16.83376121520996, 17.04158592224121, 17.249408721923828, 17.457233428955078, 17.665058135986328, 17.872882843017578, 18.080705642700195, 18.288530349731445, 18.496355056762695, 18.704179763793945, 18.912002563476562, 19.119827270507812, 19.327651977539062, 19.535476684570312, 19.74329948425293, 19.95112419128418, 20.15894889831543, 20.36677360534668, 20.574596405029297, 20.782421112060547, 20.990245819091797, 21.198070526123047, 21.405893325805664, 21.613718032836914, 21.821542739868164, 22.02936553955078, 22.23719024658203, 22.44501495361328, 22.65283966064453, 22.86066246032715, 23.0684871673584, 23.27631187438965, 23.4841365814209, 23.691959381103516, 23.899784088134766, 24.107608795166016, 24.315433502197266, 24.523256301879883, 24.731081008911133, 24.938905715942383, 25.146730422973633, 25.35455322265625, 25.5623779296875, 25.77020263671875, 25.97802734375, 26.185850143432617, 26.393674850463867, 26.601499557495117, 26.809324264526367, 27.017147064208984, 27.224971771240234, 27.432796478271484, 27.6406192779541, 27.84844398498535, 28.0562686920166, 28.26409339904785, 28.47191619873047, 28.67974090576172, 28.88756561279297, 29.09539031982422, 29.303213119506836], "121": [4.558215141296387, 4.765406608581543, 4.972598552703857, 5.179790019989014, 5.38698148727417, 5.594172954559326, 5.801364898681641, 6.008556365966797, 6.215747833251953, 6.422939777374268, 6.630131244659424, 6.83732271194458, 7.044514179229736, 7.251706123352051, 7.458897590637207, 7.666089057922363, 7.8732805252075195, 8.080471992492676, 8.287663459777832, 8.494855880737305, 8.702047348022461, 8.909238815307617, 9.116430282592773, 9.32362174987793, 9.530813217163086, 9.738004684448242, 9.945197105407715, 10.152388572692871, 10.359580039978027, 10.566771507263184, 10.77396297454834, 10.981154441833496, 11.188345909118652, 11.395538330078125, 11.602729797363281, 11.809921264648438, 12.017112731933594, 12.22430419921875, 12.431495666503906, 12.638687133789062, 12.845879554748535, 13.053071022033691, 13.260262489318848, 13.467453956604004, 13.67464542388916, 13.881836891174316, 14.089028358459473, 14.296219825744629, 14.503412246704102, 14.710603713989258, 14.917795181274414, 15.12498664855957, 15.332178115844727, 15.539369583129883, 15.746561050415039, 15.953753471374512, 16.16094398498535, 16.368135452270508, 16.575326919555664, 16.782520294189453, 16.98971176147461, 17.196903228759766, 17.404094696044922, 17.611286163330078, 17.818477630615234, 18.02566909790039, 18.232860565185547, 18.440052032470703, 18.64724349975586, 18.854434967041016, 19.061626434326172, 19.268817901611328, 19.476009368896484, 19.683202743530273, 19.89039421081543, 20.097585678100586, 20.304777145385742, 20.5119686126709, 20.719160079956055, 20.92635154724121, 21.133543014526367, 21.340734481811523, 21.54792594909668, 21.755117416381836, 21.962308883666992, 22.16950035095215, 22.376691818237305, 22.58388328552246, 22.79107666015625, 22.998268127441406, 23.205459594726562, 23.41265106201172, 23.619842529296875, 23.82703399658203, 24.034225463867188, 24.241416931152344, 24.4486083984375, 24.655799865722656, 24.862991333007812, 25.07018280029297, 25.277374267578125, 25.48456573486328, 25.69175910949707, 25.898950576782227, 26.106142044067383, 26.31333351135254, 26.520524978637695, 26.72771644592285, 26.934907913208008, 27.142099380493164, 27.34929084777832, 27.556482315063477, 27.763673782348633, 27.97086524963379, 28.178056716918945, 28.3852481842041, 28.592439651489258, 28.799633026123047, 29.006824493408203, 29.21401596069336], "122": [4.544399261474609, 4.75096321105957, 4.957526683807373, 5.164090156555176, 5.370654106140137, 5.5772175788879395, 5.783781051635742, 5.990345001220703, 6.196908473968506, 6.403471946716309, 6.610035419464111, 6.816599369049072, 7.023162841796875, 7.229726314544678, 7.436290264129639, 7.642853736877441, 7.849417209625244, 8.055980682373047, 8.262544631958008, 8.469108581542969, 8.675671577453613, 8.882235527038574, 9.088798522949219, 9.29536247253418, 9.50192642211914, 9.708489418029785, 9.915053367614746, 10.121617317199707, 10.328180313110352, 10.534744262695312, 10.741308212280273, 10.947871208190918, 11.154435157775879, 11.36099910736084, 11.567562103271484, 11.774126052856445, 11.980690002441406, 12.18725299835205, 12.393816947937012, 12.600379943847656, 12.806943893432617, 13.013507843017578, 13.220070838928223, 13.426634788513184, 13.633198738098145, 13.839761734008789, 14.04632568359375, 14.252889633178711, 14.459452629089355, 14.666016578674316, 14.872580528259277, 15.079143524169922, 15.285707473754883, 15.492271423339844, 15.698834419250488, 15.90539836883545, 16.111961364746094, 16.318525314331055, 16.525089263916016, 16.731653213500977, 16.938217163085938, 17.144779205322266, 17.351343154907227, 17.557907104492188, 17.76447105407715, 17.97103500366211, 18.177597045898438, 18.3841609954834, 18.59072494506836, 18.79728889465332, 19.00385284423828, 19.210416793823242, 19.41697883605957, 19.62354278564453, 19.830106735229492, 20.036670684814453, 20.243234634399414, 20.449798583984375, 20.656360626220703, 20.862924575805664, 21.069488525390625, 21.276052474975586, 21.482616424560547, 21.689178466796875, 21.895742416381836, 22.102306365966797, 22.308870315551758, 22.51543426513672, 22.72199821472168, 22.928560256958008, 23.13512420654297, 23.34168815612793, 23.54825210571289, 23.75481605529785, 23.961380004882812, 24.16794204711914, 24.3745059967041, 24.581069946289062, 24.787633895874023, 24.994197845458984, 25.200759887695312, 25.407323837280273, 25.613887786865234, 25.820451736450195, 26.027015686035156, 26.233579635620117, 26.440141677856445, 26.646705627441406, 26.853269577026367, 27.059833526611328, 27.26639747619629, 27.47296142578125, 27.679523468017578, 27.88608741760254, 28.0926513671875, 28.29921531677246, 28.505779266357422, 28.71234130859375, 28.91890525817871, 29.125469207763672], "123": [4.530684471130371, 4.736624717712402, 4.942564964294434, 5.148505210876465, 5.354445457458496, 5.560385704040527, 5.766325950622559, 5.97226619720459, 6.178206443786621, 6.384146690368652, 6.590086460113525, 6.796026706695557, 7.001966953277588, 7.207907199859619, 7.41384744644165, 7.619787693023682, 7.825727939605713, 8.031667709350586, 8.237607955932617, 8.443548202514648, 8.64948844909668, 8.855428695678711, 9.061368942260742, 9.267309188842773, 9.473249435424805, 9.679189682006836, 9.885129928588867, 10.091070175170898, 10.29701042175293, 10.502950668334961, 10.708890914916992, 10.914831161499023, 11.120771408081055, 11.326711654663086, 11.532651901245117, 11.738592147827148, 11.94453239440918, 12.150472640991211, 12.356412887573242, 12.562353134155273, 12.768293380737305, 12.974233627319336, 13.18017292022705, 13.386113166809082, 13.592053413391113, 13.797993659973145, 14.003933906555176, 14.209874153137207, 14.415814399719238, 14.62175464630127, 14.8276948928833, 15.033635139465332, 15.239575386047363, 15.445515632629395, 15.651455879211426, 15.857396125793457, 16.063335418701172, 16.269275665283203, 16.475215911865234, 16.681156158447266, 16.887096405029297, 17.093036651611328, 17.29897689819336, 17.50491714477539, 17.710857391357422, 17.916797637939453, 18.122737884521484, 18.328678131103516, 18.534618377685547, 18.740558624267578, 18.94649887084961, 19.15243911743164, 19.358379364013672, 19.564319610595703, 19.770259857177734, 19.976200103759766, 20.182140350341797, 20.388080596923828, 20.59402084350586, 20.79996109008789, 21.005901336669922, 21.211841583251953, 21.417781829833984, 21.623722076416016, 21.829662322998047, 22.035602569580078, 22.24154281616211, 22.44748306274414, 22.653423309326172, 22.859363555908203, 23.065303802490234, 23.271244049072266, 23.477184295654297, 23.683124542236328, 23.88906478881836, 24.09500503540039, 24.300945281982422, 24.506885528564453, 24.712825775146484, 24.918766021728516, 25.124706268310547, 25.330646514892578, 25.53658676147461, 25.74252700805664, 25.948467254638672, 26.15440559387207, 26.3603458404541, 26.566286087036133, 26.772226333618164, 26.978166580200195, 27.184106826782227, 27.390047073364258, 27.59598731994629, 27.80192756652832, 28.00786781311035, 28.213808059692383, 28.419748306274414, 28.625688552856445, 28.831628799438477, 29.037569046020508], "124": [4.517069339752197, 4.722390651702881, 4.9277119636535645, 5.133033752441406, 5.33835506439209, 5.543676376342773, 5.748997688293457, 5.954319000244141, 6.159640312194824, 6.364961624145508, 6.570282936096191, 6.775604248046875, 6.980925559997559, 7.186246871948242, 7.391568183898926, 7.596889495849609, 7.802210807800293, 8.007532119750977, 8.21285343170166, 8.418174743652344, 8.623496055603027, 8.828817367553711, 9.034138679504395, 9.239459991455078, 9.444781303405762, 9.650102615356445, 9.855423927307129, 10.060745239257812, 10.266067504882812, 10.471388816833496, 10.67671012878418, 10.882031440734863, 11.087352752685547, 11.29267406463623, 11.497995376586914, 11.703316688537598, 11.908638000488281, 12.113959312438965, 12.319280624389648, 12.524601936340332, 12.729923248291016, 12.9352445602417, 13.140565872192383, 13.345887184143066, 13.55120849609375, 13.756529808044434, 13.961851119995117, 14.1671724319458, 14.372493743896484, 14.577815055847168, 14.783136367797852, 14.988457679748535, 15.193778991699219, 15.399100303649902, 15.604421615600586, 15.80974292755127, 16.015064239501953, 16.220386505126953, 16.42570686340332, 16.63102912902832, 16.836349487304688, 17.041671752929688, 17.246992111206055, 17.452314376831055, 17.657634735107422, 17.862957000732422, 18.06827735900879, 18.27359962463379, 18.478919982910156, 18.684242248535156, 18.889562606811523, 19.094884872436523, 19.30020523071289, 19.50552749633789, 19.710847854614258, 19.916170120239258, 20.121490478515625, 20.326812744140625, 20.532135009765625, 20.737455368041992, 20.942777633666992, 21.14809799194336, 21.35342025756836, 21.558740615844727, 21.764062881469727, 21.969383239746094, 22.174705505371094, 22.38002586364746, 22.58534812927246, 22.790668487548828, 22.995990753173828, 23.201311111450195, 23.406633377075195, 23.611953735351562, 23.817276000976562, 24.02259635925293, 24.22791862487793, 24.433238983154297, 24.638561248779297, 24.843881607055664, 25.049203872680664, 25.25452423095703, 25.45984649658203, 25.6651668548584, 25.8704891204834, 26.075809478759766, 26.281131744384766, 26.486452102661133, 26.691774368286133, 26.8970947265625, 27.1024169921875, 27.3077392578125, 27.513059616088867, 27.718381881713867, 27.923702239990234, 28.129024505615234, 28.3343448638916, 28.5396671295166, 28.74498748779297, 28.95030975341797], "125": [4.50355339050293, 4.7082600593566895, 4.912967205047607, 5.117673873901367, 5.322381019592285, 5.527088165283203, 5.731794834136963, 5.936501979827881, 6.141209125518799, 6.345915794372559, 6.550622940063477, 6.755329608917236, 6.960036754608154, 7.164743900299072, 7.369450569152832, 7.57415771484375, 7.77886438369751, 7.983571529388428, 8.188278198242188, 8.392985343933105, 8.597692489624023, 8.802399635314941, 9.00710678100586, 9.211812973022461, 9.416520118713379, 9.621227264404297, 9.825934410095215, 10.030641555786133, 10.235347747802734, 10.440054893493652, 10.64476203918457, 10.849469184875488, 11.054176330566406, 11.258882522583008, 11.463589668273926, 11.668296813964844, 11.873003959655762, 12.07771110534668, 12.282418251037598, 12.4871244430542, 12.691831588745117, 12.896538734436035, 13.101245880126953, 13.305953025817871, 13.510659217834473, 13.71536636352539, 13.920073509216309, 14.124780654907227, 14.329487800598145, 14.534193992614746, 14.738901138305664, 14.943608283996582, 15.1483154296875, 15.353022575378418, 15.55772876739502, 15.762435913085938, 15.967143058776855, 16.171850204467773, 16.376556396484375, 16.58126449584961, 16.78597068786621, 16.990678787231445, 17.195384979248047, 17.40009117126465, 17.604799270629883, 17.809505462646484, 18.01421356201172, 18.21891975402832, 18.423625946044922, 18.628334045410156, 18.833040237426758, 19.037748336791992, 19.242454528808594, 19.447160720825195, 19.65186882019043, 19.85657501220703, 20.061283111572266, 20.265989303588867, 20.47069549560547, 20.675403594970703, 20.880109786987305, 21.08481788635254, 21.28952407836914, 21.494230270385742, 21.698938369750977, 21.903644561767578, 22.108352661132812, 22.313058853149414, 22.517765045166016, 22.72247314453125, 22.92717933654785, 23.131887435913086, 23.336593627929688, 23.54129981994629, 23.746007919311523, 23.950714111328125, 24.15542221069336, 24.36012840270996, 24.564836502075195, 24.769542694091797, 24.9742488861084, 25.178956985473633, 25.383663177490234, 25.58837127685547, 25.79307746887207, 25.997783660888672, 26.202491760253906, 26.407197952270508, 26.611906051635742, 26.816612243652344, 27.021318435668945, 27.22602653503418, 27.43073272705078, 27.635440826416016, 27.840147018432617, 28.04485321044922, 28.249561309814453, 28.454267501831055, 28.65897560119629, 28.86368179321289], "126": [4.4901347160339355, 4.6942315101623535, 4.89832878112793, 5.102425575256348, 5.306522846221924, 5.510619640350342, 5.714716911315918, 5.918813705444336, 6.122910976409912, 6.32700777053833, 6.531105041503906, 6.735201835632324, 6.9392991065979, 7.143395900726318, 7.3474931716918945, 7.5515899658203125, 7.755687236785889, 7.959784030914307, 8.163881301879883, 8.3679780960083, 8.572074890136719, 8.776172637939453, 8.980269432067871, 9.184366226196289, 9.388463020324707, 9.592560768127441, 9.79665756225586, 10.000754356384277, 10.204851150512695, 10.40894889831543, 10.613045692443848, 10.817142486572266, 11.021239280700684, 11.225337028503418, 11.429433822631836, 11.633530616760254, 11.837627410888672, 12.041725158691406, 12.245821952819824, 12.449918746948242, 12.65401554107666, 12.858113288879395, 13.062210083007812, 13.26630687713623, 13.470403671264648, 13.674501419067383, 13.8785982131958, 14.082695007324219, 14.286791801452637, 14.490889549255371, 14.694986343383789, 14.899083137512207, 15.103179931640625, 15.30727767944336, 15.511374473571777, 15.715471267700195, 15.919568061828613, 16.12366485595703, 16.327762603759766, 16.5318603515625, 16.7359561920166, 16.940053939819336, 17.144149780273438, 17.348247528076172, 17.552345275878906, 17.756441116333008, 17.960538864135742, 18.164636611938477, 18.368732452392578, 18.572830200195312, 18.776926040649414, 18.98102378845215, 19.185121536254883, 19.389217376708984, 19.59331512451172, 19.797412872314453, 20.001508712768555, 20.20560646057129, 20.40970230102539, 20.613800048828125, 20.81789779663086, 21.02199363708496, 21.226091384887695, 21.43018913269043, 21.63428497314453, 21.838382720947266, 22.042478561401367, 22.2465763092041, 22.450674057006836, 22.654769897460938, 22.858867645263672, 23.062963485717773, 23.267061233520508, 23.471158981323242, 23.675254821777344, 23.879352569580078, 24.083450317382812, 24.287546157836914, 24.49164390563965, 24.69573974609375, 24.899837493896484, 25.10393524169922, 25.30803108215332, 25.512128829956055, 25.71622657775879, 25.92032241821289, 26.124420166015625, 26.328516006469727, 26.53261375427246, 26.736711502075195, 26.940807342529297, 27.14490509033203, 27.349002838134766, 27.553098678588867, 27.7571964263916, 27.961292266845703, 28.165390014648438, 28.369487762451172, 28.573583602905273, 28.777681350708008], "127": [4.476812839508057, 4.680304527282715, 4.883795738220215, 5.087287425994873, 5.290779113769531, 5.494270324707031, 5.6977620124816895, 5.901253700256348, 6.104744911193848, 6.308236598968506, 6.511727809906006, 6.715219497680664, 6.918711185455322, 7.122202396392822, 7.3256940841674805, 7.5291852951049805, 7.732676982879639, 7.936168670654297, 8.139659881591797, 8.343151092529297, 8.546643257141113, 8.750134468078613, 8.953625679016113, 9.15711784362793, 9.36060905456543, 9.56410026550293, 9.76759147644043, 9.971083641052246, 10.174574851989746, 10.378066062927246, 10.581558227539062, 10.785049438476562, 10.988540649414062, 11.192032814025879, 11.395524024963379, 11.599015235900879, 11.802507400512695, 12.005998611450195, 12.209489822387695, 12.412981033325195, 12.616473197937012, 12.819964408874512, 13.023455619812012, 13.226947784423828, 13.430438995361328, 13.633930206298828, 13.837422370910645, 14.040913581848145, 14.244404792785645, 14.447896003723145, 14.651388168334961, 14.854879379272461, 15.058370590209961, 15.261862754821777, 15.465353965759277, 15.668845176696777, 15.872337341308594, 16.075828552246094, 16.279319763183594, 16.482810974121094, 16.686302185058594, 16.889795303344727, 17.093286514282227, 17.296777725219727, 17.500268936157227, 17.703760147094727, 17.907251358032227, 18.110742568969727, 18.31423568725586, 18.51772689819336, 18.72121810913086, 18.92470932006836, 19.12820053100586, 19.33169174194336, 19.53518295288086, 19.738676071166992, 19.942167282104492, 20.145658493041992, 20.349149703979492, 20.552640914916992, 20.756132125854492, 20.959625244140625, 21.163116455078125, 21.366607666015625, 21.570098876953125, 21.773590087890625, 21.977081298828125, 22.180572509765625, 22.384065628051758, 22.587556838989258, 22.791048049926758, 22.994539260864258, 23.198030471801758, 23.401521682739258, 23.60501480102539, 23.80850601196289, 24.01199722290039, 24.21548843383789, 24.41897964477539, 24.62247085571289, 24.82596206665039, 25.029455184936523, 25.232946395874023, 25.436437606811523, 25.639928817749023, 25.843420028686523, 26.046911239624023, 26.250402450561523, 26.453895568847656, 26.657386779785156, 26.860877990722656, 27.064369201660156, 27.267860412597656, 27.471351623535156, 27.67484474182129, 27.87833595275879, 28.08182716369629, 28.28531837463379, 28.48880958557129, 28.69230079650879], "128": [4.463587284088135, 4.666477680206299, 4.869367599487305, 5.072257995605469, 5.275148391723633, 5.478038787841797, 5.680929183959961, 5.883819580078125, 6.086709499359131, 6.289599895477295, 6.492490291595459, 6.695380687713623, 6.898271083831787, 7.101161479949951, 7.304051876068115, 7.506941795349121, 7.709832191467285, 7.912722587585449, 8.115612983703613, 8.318503379821777, 8.521393775939941, 8.724284172058105, 8.92717456817627, 9.130064964294434, 9.332955360412598, 9.535844802856445, 9.73873519897461, 9.941625595092773, 10.144515991210938, 10.347406387329102, 10.550296783447266, 10.75318717956543, 10.956077575683594, 11.158967971801758, 11.361858367919922, 11.564748764038086, 11.76763916015625, 11.970529556274414, 12.173418998718262, 12.376309394836426, 12.57919979095459, 12.782090187072754, 12.984980583190918, 13.187870979309082, 13.390761375427246, 13.59365177154541, 13.796542167663574, 13.999432563781738, 14.202322959899902, 14.405213356018066, 14.60810375213623, 14.810994148254395, 15.013883590698242, 15.216773986816406, 15.41966438293457, 15.622554779052734, 15.825445175170898, 16.028335571289062, 16.231225967407227, 16.43411636352539, 16.637006759643555, 16.83989715576172, 17.042787551879883, 17.245677947998047, 17.44856834411621, 17.651458740234375, 17.85434913635254, 18.057239532470703, 18.260129928588867, 18.46302032470703, 18.665910720825195, 18.86880111694336, 19.07168960571289, 19.274580001831055, 19.47747039794922, 19.680360794067383, 19.883251190185547, 20.08614158630371, 20.289031982421875, 20.49192237854004, 20.694812774658203, 20.897703170776367, 21.10059356689453, 21.303483963012695, 21.50637435913086, 21.709264755249023, 21.912155151367188, 22.11504554748535, 22.317935943603516, 22.52082633972168, 22.723716735839844, 22.926607131958008, 23.129497528076172, 23.332387924194336, 23.5352783203125, 23.738168716430664, 23.941059112548828, 24.143949508666992, 24.346837997436523, 24.549728393554688, 24.75261878967285, 24.955509185791016, 25.15839958190918, 25.361289978027344, 25.564180374145508, 25.767070770263672, 25.969961166381836, 26.1728515625, 26.375741958618164, 26.578632354736328, 26.781522750854492, 26.984413146972656, 27.18730354309082, 27.390193939208984, 27.59308433532715, 27.795974731445312, 27.998865127563477, 28.20175552368164, 28.404645919799805, 28.60753631591797], "129": [4.450456142425537, 4.652749538421631, 4.855042934417725, 5.057336807250977, 5.25963020324707, 5.461923599243164, 5.664216995239258, 5.866510391235352, 6.068803787231445, 6.271097183227539, 6.473391056060791, 6.675684452056885, 6.8779778480529785, 7.080271244049072, 7.282564640045166, 7.48485803604126, 7.6871514320373535, 7.8894453048706055, 8.0917387008667, 8.294032096862793, 8.496325492858887, 8.69861888885498, 8.900912284851074, 9.103205680847168, 9.305499076843262, 9.507792472839355, 9.71008586883545, 9.91238021850586, 10.114673614501953, 10.316967010498047, 10.51926040649414, 10.721553802490234, 10.923847198486328, 11.126140594482422, 11.328433990478516, 11.53072738647461, 11.733020782470703, 11.935314178466797, 12.13760757446289, 12.339900970458984, 12.542194366455078, 12.744488716125488, 12.946782112121582, 13.149075508117676, 13.35136890411377, 13.553662300109863, 13.755955696105957, 13.95824909210205, 14.160542488098145, 14.362835884094238, 14.565129280090332, 14.767422676086426, 14.96971607208252, 15.172009468078613, 15.374302864074707, 15.576597213745117, 15.778890609741211, 15.981184005737305, 16.1834774017334, 16.385770797729492, 16.588064193725586, 16.79035758972168, 16.992650985717773, 17.194944381713867, 17.39723777770996, 17.599531173706055, 17.80182456970215, 18.004117965698242, 18.206411361694336, 18.40870475769043, 18.610998153686523, 18.813291549682617, 19.01558494567871, 19.217878341674805, 19.4201717376709, 19.622465133666992, 19.82476043701172, 20.027053833007812, 20.229347229003906, 20.431640625, 20.633934020996094, 20.836227416992188, 21.03852081298828, 21.240814208984375, 21.44310760498047, 21.645401000976562, 21.847694396972656, 22.04998779296875, 22.252281188964844, 22.454574584960938, 22.65686798095703, 22.859161376953125, 23.06145477294922, 23.263748168945312, 23.466041564941406, 23.6683349609375, 23.870628356933594, 24.072921752929688, 24.27521514892578, 24.477508544921875, 24.67980194091797, 24.882095336914062, 25.084388732910156, 25.28668212890625, 25.488977432250977, 25.69127082824707, 25.893564224243164, 26.095857620239258, 26.29815101623535, 26.500444412231445, 26.70273780822754, 26.905031204223633, 27.107324600219727, 27.30961799621582, 27.511911392211914, 27.714204788208008, 27.9164981842041, 28.118791580200195, 28.32108497619629, 28.523378372192383], "130": [4.437419414520264, 4.639120101928711, 4.840821266174316, 5.042521953582764, 5.244222640991211, 5.445923805236816, 5.647624492645264, 5.849325656890869, 6.051026344299316, 6.252727031707764, 6.454428195953369, 6.656128883361816, 6.857829570770264, 7.059530735015869, 7.261231422424316, 7.462932586669922, 7.664633274078369, 7.866333961486816, 8.068035125732422, 8.269736289978027, 8.471436500549316, 8.673137664794922, 8.874838829040527, 9.076539039611816, 9.278240203857422, 9.479941368103027, 9.681642532348633, 9.883342742919922, 10.085043907165527, 10.286745071411133, 10.488445281982422, 10.690146446228027, 10.891847610473633, 11.093547821044922, 11.295248985290527, 11.496950149536133, 11.698651313781738, 11.900351524353027, 12.102052688598633, 12.303753852844238, 12.505454063415527, 12.707155227661133, 12.908856391906738, 13.110556602478027, 13.312257766723633, 13.513958930969238, 13.715659141540527, 13.917360305786133, 14.119061470031738, 14.320762634277344, 14.522462844848633, 14.724164009094238, 14.925865173339844, 15.127565383911133, 15.329266548156738, 15.530967712402344, 15.732667922973633, 15.934369087219238, 16.136070251464844, 16.337770462036133, 16.539472579956055, 16.741172790527344, 16.942873001098633, 17.144575119018555, 17.346275329589844, 17.547975540161133, 17.749677658081055, 17.951377868652344, 18.153078079223633, 18.354780197143555, 18.556480407714844, 18.758180618286133, 18.959882736206055, 19.161582946777344, 19.363285064697266, 19.564985275268555, 19.766685485839844, 19.968387603759766, 20.170087814331055, 20.371788024902344, 20.573490142822266, 20.775190353393555, 20.976890563964844, 21.178592681884766, 21.380292892456055, 21.581993103027344, 21.783695220947266, 21.985395431518555, 22.187095642089844, 22.388797760009766, 22.590497970581055, 22.792198181152344, 22.993900299072266, 23.195600509643555, 23.397302627563477, 23.599002838134766, 23.800703048706055, 24.002405166625977, 24.204105377197266, 24.405805587768555, 24.607507705688477, 24.809207916259766, 25.010908126831055, 25.212610244750977, 25.414310455322266, 25.616010665893555, 25.817712783813477, 26.019412994384766, 26.221113204956055, 26.422815322875977, 26.624515533447266, 26.826215744018555, 27.027917861938477, 27.229618072509766, 27.431318283081055, 27.633020401000977, 27.834720611572266, 28.036422729492188, 28.238122940063477, 28.439823150634766], "131": [4.424475193023682, 4.6255879402160645, 4.826700210571289, 5.027812957763672, 5.228925704956055, 5.430037975311279, 5.631150722503662, 5.832262992858887, 6.0333757400512695, 6.234488010406494, 6.435600757598877, 6.636713027954102, 6.837825775146484, 7.038938045501709, 7.240050792694092, 7.441163063049316, 7.642275810241699, 7.843388080596924, 8.044500350952148, 8.245613098144531, 8.446725845336914, 8.647838592529297, 8.848950386047363, 9.050063133239746, 9.251175880432129, 9.452288627624512, 9.653400421142578, 9.854513168334961, 10.055625915527344, 10.256738662719727, 10.45785140991211, 10.658963203430176, 10.860075950622559, 11.061188697814941, 11.262301445007324, 11.46341323852539, 11.664525985717773, 11.865638732910156, 12.066751480102539, 12.267863273620605, 12.468976020812988, 12.670088768005371, 12.871201515197754, 13.07231330871582, 13.273426055908203, 13.474538803100586, 13.675651550292969, 13.876763343811035, 14.077876091003418, 14.2789888381958, 14.480101585388184, 14.68121337890625, 14.882326126098633, 15.083438873291016, 15.284551620483398, 15.485664367675781, 15.686776161193848, 15.88788890838623, 16.089000701904297, 16.29011344909668, 16.491226196289062, 16.692338943481445, 16.893451690673828, 17.09456443786621, 17.295677185058594, 17.496789932250977, 17.697900772094727, 17.89901351928711, 18.100126266479492, 18.301239013671875, 18.502351760864258, 18.70346450805664, 18.904577255249023, 19.105690002441406, 19.306800842285156, 19.50791358947754, 19.709026336669922, 19.910139083862305, 20.111251831054688, 20.31236457824707, 20.513477325439453, 20.714590072631836, 20.91570281982422, 21.11681365966797, 21.31792640686035, 21.519039154052734, 21.720151901245117, 21.9212646484375, 22.122377395629883, 22.323490142822266, 22.52460289001465, 22.7257137298584, 22.92682647705078, 23.127939224243164, 23.329051971435547, 23.53016471862793, 23.731277465820312, 23.932390213012695, 24.133502960205078, 24.334613800048828, 24.53572654724121, 24.736839294433594, 24.937952041625977, 25.13906478881836, 25.340177536010742, 25.541290283203125, 25.742403030395508, 25.94351577758789, 26.14462661743164, 26.345739364624023, 26.546852111816406, 26.74796485900879, 26.949077606201172, 27.150190353393555, 27.351303100585938, 27.55241584777832, 27.75352668762207, 27.954639434814453, 28.155752182006836, 28.35686492919922], "132": [4.411623477935791, 4.612152099609375, 4.812680244445801, 5.013208866119385, 5.2137370109558105, 5.4142656326293945, 5.61479377746582, 5.815321922302246, 6.01585054397583, 6.216378688812256, 6.41690731048584, 6.617435455322266, 6.81796407699585, 7.018492221832275, 7.219020366668701, 7.419548988342285, 7.620077133178711, 7.820605754852295, 8.021134376525879, 8.221662521362305, 8.42219066619873, 8.622718811035156, 8.823246955871582, 9.023776054382324, 9.22430419921875, 9.424832344055176, 9.625360488891602, 9.825888633728027, 10.02641773223877, 10.226945877075195, 10.427474021911621, 10.628002166748047, 10.828531265258789, 11.029059410095215, 11.22958755493164, 11.430115699768066, 11.630643844604492, 11.831172943115234, 12.03170108795166, 12.232229232788086, 12.432757377624512, 12.633285522460938, 12.83381462097168, 13.034342765808105, 13.234870910644531, 13.435399055480957, 13.6359281539917, 13.836456298828125, 14.03698444366455, 14.237512588500977, 14.438040733337402, 14.638569831848145, 14.83909797668457, 15.039626121520996, 15.240154266357422, 15.440682411193848, 15.64121150970459, 15.841739654541016, 16.042268753051758, 16.242795944213867, 16.44332504272461, 16.64385223388672, 16.84438133239746, 17.044910430908203, 17.245437622070312, 17.445966720581055, 17.646493911743164, 17.847023010253906, 18.04755210876465, 18.248079299926758, 18.4486083984375, 18.64913558959961, 18.84966468811035, 19.050193786621094, 19.250720977783203, 19.451250076293945, 19.651777267456055, 19.852306365966797, 20.05283546447754, 20.25336265563965, 20.45389175415039, 20.654420852661133, 20.854948043823242, 21.055477142333984, 21.256004333496094, 21.456533432006836, 21.657062530517578, 21.857589721679688, 22.05811882019043, 22.25864601135254, 22.45917510986328, 22.659704208374023, 22.860231399536133, 23.060760498046875, 23.261287689208984, 23.461816787719727, 23.66234588623047, 23.862873077392578, 24.06340217590332, 24.26392936706543, 24.464458465576172, 24.664987564086914, 24.865514755249023, 25.066043853759766, 25.266571044921875, 25.467100143432617, 25.66762924194336, 25.86815643310547, 26.06868553161621, 26.26921272277832, 26.469741821289062, 26.670270919799805, 26.870798110961914, 27.071327209472656, 27.2718563079834, 27.472383499145508, 27.67291259765625, 27.87343978881836, 28.0739688873291, 28.274497985839844], "133": [4.398863315582275, 4.598811626434326, 4.798759937286377, 4.998708248138428, 5.1986565589904785, 5.398604869842529, 5.59855318069458, 5.798501491546631, 5.998449802398682, 6.198398113250732, 6.398346424102783, 6.598294734954834, 6.798243045806885, 6.9981913566589355, 7.198139667510986, 7.398087978363037, 7.598036289215088, 7.797984600067139, 7.9979329109191895, 8.197881698608398, 8.39783000946045, 8.5977783203125, 8.79772663116455, 8.997674942016602, 9.197623252868652, 9.397571563720703, 9.597519874572754, 9.797468185424805, 9.997416496276855, 10.197364807128906, 10.397313117980957, 10.597261428833008, 10.797209739685059, 10.99715805053711, 11.19710636138916, 11.397054672241211, 11.597002983093262, 11.796951293945312, 11.996899604797363, 12.196847915649414, 12.396796226501465, 12.596744537353516, 12.796692848205566, 12.996641159057617, 13.196589469909668, 13.396537780761719, 13.59648609161377, 13.79643440246582, 13.996382713317871, 14.196331024169922, 14.396279335021973, 14.596227645874023, 14.796175956726074, 14.996124267578125, 15.196072578430176, 15.396020889282227, 15.595969200134277, 15.795917510986328, 15.995865821838379, 16.19581413269043, 16.395763397216797, 16.59571075439453, 16.7956600189209, 16.995607376098633, 17.195556640625, 17.395503997802734, 17.5954532623291, 17.795400619506836, 17.995349884033203, 18.195297241210938, 18.395246505737305, 18.59519386291504, 18.795143127441406, 18.99509048461914, 19.195039749145508, 19.394987106323242, 19.59493637084961, 19.794883728027344, 19.99483299255371, 20.194780349731445, 20.394729614257812, 20.594676971435547, 20.794626235961914, 20.99457359313965, 21.194522857666016, 21.39447021484375, 21.594419479370117, 21.79436683654785, 21.99431610107422, 22.194263458251953, 22.39421272277832, 22.594160079956055, 22.794109344482422, 22.994056701660156, 23.194005966186523, 23.393953323364258, 23.593902587890625, 23.79384994506836, 23.993799209594727, 24.19374656677246, 24.393695831298828, 24.593645095825195, 24.79359245300293, 24.993541717529297, 25.19348907470703, 25.3934383392334, 25.593385696411133, 25.7933349609375, 25.993282318115234, 26.1932315826416, 26.393178939819336, 26.593128204345703, 26.793075561523438, 26.993024826049805, 27.19297218322754, 27.392921447753906, 27.59286880493164, 27.792818069458008, 27.992765426635742, 28.19271469116211], "134": [4.38619327545166, 4.585565567016602, 4.784937858581543, 4.984310150146484, 5.183682918548584, 5.383055210113525, 5.582427501678467, 5.781799793243408, 5.981172561645508, 6.180544853210449, 6.379917144775391, 6.579289436340332, 6.778662204742432, 6.978034496307373, 7.1774067878723145, 7.376779079437256, 7.5761518478393555, 7.775524139404297, 7.974896430969238, 8.17426872253418, 8.373641014099121, 8.573013305664062, 8.77238655090332, 8.971758842468262, 9.171131134033203, 9.370503425598145, 9.569875717163086, 9.769248008728027, 9.968620300292969, 10.16799259185791, 10.367365837097168, 10.56673812866211, 10.76611042022705, 10.965482711791992, 11.164855003356934, 11.364227294921875, 11.563599586486816, 11.762971878051758, 11.962345123291016, 12.161717414855957, 12.361089706420898, 12.56046199798584, 12.759834289550781, 12.959206581115723, 13.158578872680664, 13.357951164245605, 13.557324409484863, 13.756696701049805, 13.956068992614746, 14.155441284179688, 14.354813575744629, 14.55418586730957, 14.753558158874512, 14.952930450439453, 15.152303695678711, 15.351675987243652, 15.551048278808594, 15.750420570373535, 15.949792861938477, 16.149166107177734, 16.34853744506836, 16.547910690307617, 16.747282028198242, 16.9466552734375, 17.146026611328125, 17.345399856567383, 17.54477310180664, 17.744144439697266, 17.943517684936523, 18.14288902282715, 18.342262268066406, 18.54163360595703, 18.74100685119629, 18.940378189086914, 19.139751434326172, 19.33912467956543, 19.538496017456055, 19.737869262695312, 19.937240600585938, 20.136613845825195, 20.33598518371582, 20.535358428955078, 20.734731674194336, 20.93410301208496, 21.13347625732422, 21.332847595214844, 21.5322208404541, 21.731592178344727, 21.930965423583984, 22.130338668823242, 22.329710006713867, 22.529083251953125, 22.72845458984375, 22.927827835083008, 23.127199172973633, 23.32657241821289, 23.525943756103516, 23.725317001342773, 23.92469024658203, 24.124061584472656, 24.323434829711914, 24.52280616760254, 24.722179412841797, 24.921550750732422, 25.12092399597168, 25.320297241210938, 25.519668579101562, 25.71904182434082, 25.918413162231445, 26.117786407470703, 26.317157745361328, 26.516530990600586, 26.71590232849121, 26.91527557373047, 27.114648818969727, 27.31402015686035, 27.51339340209961, 27.712764739990234, 27.912137985229492, 28.111509323120117], "135": [4.373612403869629, 4.572412967681885, 4.771213531494141, 4.9700140953063965, 5.168814659118652, 5.367615222930908, 5.566415786743164, 5.76521635055542, 5.964016914367676, 6.162817478179932, 6.3616180419921875, 6.560418605804443, 6.759219169616699, 6.958019733428955, 7.156820297241211, 7.355620861053467, 7.554421424865723, 7.7532219886779785, 7.952022552490234, 8.150823593139648, 8.349623680114746, 8.54842472076416, 8.747224807739258, 8.946025848388672, 9.14482593536377, 9.343626976013184, 9.542427062988281, 9.741228103637695, 9.940028190612793, 10.138829231262207, 10.337629318237305, 10.536430358886719, 10.735230445861816, 10.93403148651123, 11.132831573486328, 11.331632614135742, 11.53043270111084, 11.729233741760254, 11.928033828735352, 12.126834869384766, 12.325634956359863, 12.524435997009277, 12.723236083984375, 12.922037124633789, 13.120837211608887, 13.3196382522583, 13.518438339233398, 13.717239379882812, 13.91603946685791, 14.114840507507324, 14.313640594482422, 14.512441635131836, 14.711241722106934, 14.910042762756348, 15.108842849731445, 15.30764389038086, 15.506443977355957, 15.705245018005371, 15.904045104980469, 16.102846145629883, 16.301647186279297, 16.500446319580078, 16.699247360229492, 16.898048400878906, 17.09684944152832, 17.2956485748291, 17.494449615478516, 17.69325065612793, 17.892051696777344, 18.090850830078125, 18.28965187072754, 18.488452911376953, 18.687253952026367, 18.88605308532715, 19.084854125976562, 19.283655166625977, 19.48245620727539, 19.681255340576172, 19.880056381225586, 20.078857421875, 20.277658462524414, 20.476457595825195, 20.67525863647461, 20.874059677124023, 21.072860717773438, 21.27165985107422, 21.470460891723633, 21.669261932373047, 21.86806297302246, 22.066862106323242, 22.265663146972656, 22.46446418762207, 22.663265228271484, 22.862064361572266, 23.06086540222168, 23.259666442871094, 23.458467483520508, 23.65726661682129, 23.856067657470703, 24.054868698120117, 24.25366973876953, 24.452468872070312, 24.651269912719727, 24.85007095336914, 25.048871994018555, 25.247671127319336, 25.44647216796875, 25.645273208618164, 25.844074249267578, 26.04287338256836, 26.241674423217773, 26.440475463867188, 26.6392765045166, 26.838075637817383, 27.036876678466797, 27.23567771911621, 27.434478759765625, 27.633277893066406, 27.83207893371582, 28.030879974365234], "136": [4.361120223999023, 4.559353351593018, 4.7575860023498535, 4.9558186531066895, 5.154051303863525, 5.352283954620361, 5.5505170822143555, 5.748749732971191, 5.946982383728027, 6.145215034484863, 6.343447685241699, 6.541680812835693, 6.739913463592529, 6.938146114349365, 7.136378765106201, 7.334611415863037, 7.532844543457031, 7.731077194213867, 7.929309844970703, 8.127542495727539, 8.325775146484375, 8.524007797241211, 8.722240447998047, 8.9204740524292, 9.118706703186035, 9.316939353942871, 9.515172004699707, 9.713404655456543, 9.911637306213379, 10.109869956970215, 10.30810260772705, 10.506335258483887, 10.704567909240723, 10.902801513671875, 11.101034164428711, 11.299266815185547, 11.497499465942383, 11.695732116699219, 11.893964767456055, 12.09219741821289, 12.290430068969727, 12.488662719726562, 12.686895370483398, 12.88512897491455, 13.083361625671387, 13.281594276428223, 13.479826927185059, 13.678059577941895, 13.87629222869873, 14.074524879455566, 14.272757530212402, 14.470990180969238, 14.669222831726074, 14.867456436157227, 15.065689086914062, 15.263921737670898, 15.462154388427734, 15.66038703918457, 15.858619689941406, 16.056852340698242, 16.255084991455078, 16.453317642211914, 16.65155029296875, 16.849782943725586, 17.048015594482422, 17.246248245239258, 17.444480895996094, 17.64271354675293, 17.8409481048584, 18.039180755615234, 18.23741340637207, 18.435646057128906, 18.633878707885742, 18.832111358642578, 19.030344009399414, 19.22857666015625, 19.426809310913086, 19.625041961669922, 19.823274612426758, 20.021507263183594, 20.21973991394043, 20.417972564697266, 20.6162052154541, 20.814437866210938, 21.012670516967773, 21.21090316772461, 21.409135818481445, 21.60736846923828, 21.80560302734375, 22.003835678100586, 22.202068328857422, 22.400300979614258, 22.598533630371094, 22.79676628112793, 22.994998931884766, 23.1932315826416, 23.391464233398438, 23.589696884155273, 23.78792953491211, 23.986162185668945, 24.18439483642578, 24.382627487182617, 24.580860137939453, 24.77909278869629, 24.977325439453125, 25.17555809020996, 25.373790740966797, 25.572023391723633, 25.7702579498291, 25.968490600585938, 26.166723251342773, 26.36495590209961, 26.563188552856445, 26.76142120361328, 26.959653854370117, 27.157886505126953, 27.35611915588379, 27.554351806640625, 27.75258445739746, 27.950817108154297], "137": [4.3487162590026855, 4.546385288238525, 4.744053840637207, 4.941722869873047, 5.139391899108887, 5.337060928344727, 5.534729480743408, 5.732398509979248, 5.930067539215088, 6.127736568450928, 6.325405120849609, 6.523074150085449, 6.720743179321289, 6.918412208557129, 7.116081237792969, 7.31374979019165, 7.51141881942749, 7.70908784866333, 7.90675687789917, 8.104425430297852, 8.302094459533691, 8.499763488769531, 8.697432518005371, 8.895101547241211, 9.09277057647705, 9.290438652038574, 9.488107681274414, 9.685776710510254, 9.883445739746094, 10.081114768981934, 10.278783798217773, 10.476452827453613, 10.674121856689453, 10.871790885925293, 11.069458961486816, 11.267127990722656, 11.464797019958496, 11.662466049194336, 11.860135078430176, 12.057804107666016, 12.255473136901855, 12.453142166137695, 12.650810241699219, 12.848479270935059, 13.046148300170898, 13.243817329406738, 13.441486358642578, 13.639155387878418, 13.836824417114258, 14.034493446350098, 14.232162475585938, 14.429830551147461, 14.6274995803833, 14.82516860961914, 15.02283763885498, 15.22050666809082, 15.41817569732666, 15.6158447265625, 15.81351375579834, 16.01118278503418, 16.208850860595703, 16.40652084350586, 16.604188919067383, 16.80185890197754, 16.999526977539062, 17.197195053100586, 17.394865036010742, 17.592533111572266, 17.790203094482422, 17.987871170043945, 18.1855411529541, 18.383209228515625, 18.58087730407715, 18.778547286987305, 18.976215362548828, 19.173885345458984, 19.371553421020508, 19.569223403930664, 19.766891479492188, 19.964561462402344, 20.162229537963867, 20.35989761352539, 20.557567596435547, 20.75523567199707, 20.952905654907227, 21.15057373046875, 21.348243713378906, 21.54591178894043, 21.743581771850586, 21.94124984741211, 22.138917922973633, 22.33658790588379, 22.534255981445312, 22.73192596435547, 22.929594039916992, 23.12726402282715, 23.324932098388672, 23.522602081298828, 23.72027015686035, 23.917938232421875, 24.11560821533203, 24.313276290893555, 24.51094627380371, 24.708614349365234, 24.90628433227539, 25.103952407836914, 25.301620483398438, 25.499290466308594, 25.696958541870117, 25.894628524780273, 26.092296600341797, 26.289966583251953, 26.487634658813477, 26.685304641723633, 26.882972717285156, 27.08064079284668, 27.278310775756836, 27.47597885131836, 27.673648834228516, 27.87131690979004], "138": [4.336399078369141, 4.533507823944092, 4.730617046356201, 4.927725791931152, 5.124835014343262, 5.321944236755371, 5.519052982330322, 5.716162204742432, 5.913270950317383, 6.110380172729492, 6.307489395141602, 6.504598140716553, 6.701707363128662, 6.8988165855407715, 7.095925331115723, 7.293034553527832, 7.490143299102783, 7.687252521514893, 7.884361743927002, 8.081470489501953, 8.278579711914062, 8.475688934326172, 8.672798156738281, 8.869906425476074, 9.067015647888184, 9.264124870300293, 9.461234092712402, 9.658343315124512, 9.855451583862305, 10.052560806274414, 10.249670028686523, 10.446779251098633, 10.643888473510742, 10.840996742248535, 11.038105964660645, 11.235215187072754, 11.432324409484863, 11.629433631896973, 11.826541900634766, 12.023651123046875, 12.220760345458984, 12.417869567871094, 12.614978790283203, 12.812088012695312, 13.009196281433105, 13.206305503845215, 13.403414726257324, 13.600523948669434, 13.797633171081543, 13.994741439819336, 14.191850662231445, 14.388959884643555, 14.586069107055664, 14.783178329467773, 14.980286598205566, 15.177395820617676, 15.374505043029785, 15.571614265441895, 15.768723487854004, 15.965831756591797, 16.162940979003906, 16.360050201416016, 16.557159423828125, 16.754268646240234, 16.951377868652344, 17.148487091064453, 17.345596313476562, 17.54270362854004, 17.73981285095215, 17.936922073364258, 18.134031295776367, 18.331140518188477, 18.528249740600586, 18.725358963012695, 18.922468185424805, 19.119577407836914, 19.316686630249023, 19.513795852661133, 19.71090316772461, 19.90801239013672, 20.105121612548828, 20.302230834960938, 20.499340057373047, 20.696449279785156, 20.893558502197266, 21.090667724609375, 21.287776947021484, 21.484886169433594, 21.68199348449707, 21.87910270690918, 22.07621192932129, 22.2733211517334, 22.470430374145508, 22.667539596557617, 22.864648818969727, 23.061758041381836, 23.258867263793945, 23.455976486206055, 23.65308380126953, 23.85019302368164, 24.04730224609375, 24.24441146850586, 24.44152069091797, 24.638629913330078, 24.835739135742188, 25.032848358154297, 25.229957580566406, 25.427066802978516, 25.624176025390625, 25.8212833404541, 26.01839256286621, 26.21550178527832, 26.41261100769043, 26.60972023010254, 26.80682945251465, 27.003938674926758, 27.201047897338867, 27.398157119750977, 27.595266342163086, 27.792373657226562], "139": [4.324167728424072, 4.520720958709717, 4.717273712158203, 4.913826942443848, 5.110380172729492, 5.3069329261779785, 5.503486156463623, 5.700039386749268, 5.896592140197754, 6.093145370483398, 6.289698600769043, 6.486251354217529, 6.682804584503174, 6.879357814788818, 7.075910568237305, 7.272463798522949, 7.469017028808594, 7.66556978225708, 7.862123012542725, 8.058675765991211, 8.255228996276855, 8.4517822265625, 8.648335456848145, 8.844888687133789, 9.041441917419434, 9.237994194030762, 9.434547424316406, 9.63110065460205, 9.827653884887695, 10.02420711517334, 10.220760345458984, 10.417312622070312, 10.613865852355957, 10.810419082641602, 11.006972312927246, 11.20352554321289, 11.400078773498535, 11.596631050109863, 11.793184280395508, 11.989737510681152, 12.186290740966797, 12.382843971252441, 12.579397201538086, 12.775949478149414, 12.972502708435059, 13.169055938720703, 13.365609169006348, 13.562162399291992, 13.758715629577637, 13.955267906188965, 14.15182113647461, 14.348374366760254, 14.544927597045898, 14.741480827331543, 14.938034057617188, 15.134587287902832, 15.33113956451416, 15.527692794799805, 15.72424602508545, 15.920799255371094, 16.117351531982422, 16.313905715942383, 16.51045799255371, 16.707012176513672, 16.903564453125, 17.100116729736328, 17.29667091369629, 17.493223190307617, 17.689777374267578, 17.886329650878906, 18.082883834838867, 18.279436111450195, 18.475988388061523, 18.672542572021484, 18.869094848632812, 19.065649032592773, 19.2622013092041, 19.45875358581543, 19.65530776977539, 19.85186004638672, 20.04841423034668, 20.244966506958008, 20.44152069091797, 20.638072967529297, 20.834625244140625, 21.031179428100586, 21.227731704711914, 21.424285888671875, 21.620838165283203, 21.81739044189453, 22.013944625854492, 22.21049690246582, 22.40705108642578, 22.60360336303711, 22.80015754699707, 22.9967098236084, 23.193262100219727, 23.389816284179688, 23.586368560791016, 23.782922744750977, 23.979475021362305, 24.176029205322266, 24.372581481933594, 24.569133758544922, 24.765687942504883, 24.96224021911621, 25.158794403076172, 25.3553466796875, 25.551898956298828, 25.74845314025879, 25.945005416870117, 26.141559600830078, 26.338111877441406, 26.534666061401367, 26.731218338012695, 26.927770614624023, 27.124324798583984, 27.320877075195312, 27.517431259155273, 27.7139835357666], "140": [4.312021732330322, 4.508022785186768, 4.704023838043213, 4.900024890899658, 5.096025466918945, 5.292026519775391, 5.488027572631836, 5.684028625488281, 5.880029678344727, 6.076030731201172, 6.272031784057617, 6.4680328369140625, 6.66403341293335, 6.860034465789795, 7.05603551864624, 7.2520365715026855, 7.448037624359131, 7.644038677215576, 7.8400397300720215, 8.036040306091309, 8.232041358947754, 8.4280424118042, 8.624043464660645, 8.82004451751709, 9.016045570373535, 9.21204662322998, 9.408047676086426, 9.604048728942871, 9.800049781799316, 9.996050834655762, 10.19205093383789, 10.388051986694336, 10.584053039550781, 10.780054092407227, 10.976055145263672, 11.172056198120117, 11.368057250976562, 11.564058303833008, 11.760059356689453, 11.956060409545898, 12.152061462402344, 12.348062515258789, 12.544063568115234, 12.74006462097168, 12.936065673828125, 13.132065773010254, 13.3280668258667, 13.524067878723145, 13.72006893157959, 13.916069984436035, 14.11207103729248, 14.308072090148926, 14.504073143005371, 14.700074195861816, 14.896075248718262, 15.092076301574707, 15.288077354431152, 15.484078407287598, 15.680079460144043, 15.876079559326172, 16.072080612182617, 16.268081665039062, 16.464082717895508, 16.660083770751953, 16.8560848236084, 17.052085876464844, 17.24808692932129, 17.444087982177734, 17.64008903503418, 17.836090087890625, 18.03209114074707, 18.228092193603516, 18.42409324645996, 18.620094299316406, 18.81609535217285, 19.012096405029297, 19.208097457885742, 19.404098510742188, 19.600099563598633, 19.796100616455078, 19.992101669311523, 20.188100814819336, 20.38410186767578, 20.580102920532227, 20.776103973388672, 20.972105026245117, 21.168106079101562, 21.364107131958008, 21.560108184814453, 21.7561092376709, 21.952110290527344, 22.14811134338379, 22.344112396240234, 22.54011344909668, 22.736114501953125, 22.93211555480957, 23.128116607666016, 23.32411766052246, 23.520118713378906, 23.71611976623535, 23.912120819091797, 24.108121871948242, 24.304122924804688, 24.500123977661133, 24.696125030517578, 24.892126083374023, 25.08812713623047, 25.284128189086914, 25.48012924194336, 25.676130294799805, 25.87213134765625, 26.068130493164062, 26.264131546020508, 26.460132598876953, 26.6561336517334, 26.852134704589844, 27.04813575744629, 27.244136810302734, 27.44013786315918, 27.636138916015625], "141": [4.299960136413574, 4.495412826538086, 4.690865993499756, 4.886318683624268, 5.081771373748779, 5.277224063873291, 5.472676753997803, 5.6681294441223145, 5.863582134246826, 6.059034824371338, 6.25448751449585, 6.449940204620361, 6.645393371582031, 6.840846061706543, 7.036298751831055, 7.231751441955566, 7.427204132080078, 7.62265682220459, 7.818109512329102, 8.013562202453613, 8.209014892578125, 8.404467582702637, 8.599920272827148, 8.79537296295166, 8.990825653076172, 9.186278343200684, 9.381731986999512, 9.577184677124023, 9.772637367248535, 9.968090057373047, 10.163542747497559, 10.35899543762207, 10.554448127746582, 10.749900817871094, 10.945353507995605, 11.140806198120117, 11.336258888244629, 11.53171157836914, 11.727164268493652, 11.922616958618164, 12.118069648742676, 12.313522338867188, 12.5089750289917, 12.704427719116211, 12.899880409240723, 13.09533405303955, 13.290786743164062, 13.486239433288574, 13.681692123413086, 13.877144813537598, 14.07259750366211, 14.268050193786621, 14.463502883911133, 14.658955574035645, 14.854408264160156, 15.049860954284668, 15.24531364440918, 15.440766334533691, 15.636219024658203, 15.831671714782715, 16.027124404907227, 16.222578048706055, 16.41802978515625, 16.613483428955078, 16.808935165405273, 17.0043888092041, 17.199840545654297, 17.395294189453125, 17.59074592590332, 17.78619956970215, 17.981651306152344, 18.177104949951172, 18.372556686401367, 18.568010330200195, 18.763463973999023, 18.95891571044922, 19.154369354248047, 19.349821090698242, 19.54527473449707, 19.740726470947266, 19.936180114746094, 20.13163185119629, 20.327085494995117, 20.522537231445312, 20.71799087524414, 20.913442611694336, 21.108896255493164, 21.30434799194336, 21.499801635742188, 21.695253372192383, 21.89070701599121, 22.086158752441406, 22.281612396240234, 22.477066040039062, 22.672517776489258, 22.867971420288086, 23.06342315673828, 23.25887680053711, 23.454328536987305, 23.649782180786133, 23.845233917236328, 24.040687561035156, 24.23613929748535, 24.43159294128418, 24.627044677734375, 24.822498321533203, 25.0179500579834, 25.213403701782227, 25.408855438232422, 25.60430908203125, 25.799760818481445, 25.995214462280273, 26.1906681060791, 26.386119842529297, 26.581573486328125, 26.77702522277832, 26.97247886657715, 27.167930603027344, 27.363384246826172, 27.558835983276367], "142": [4.28798246383667, 4.482890605926514, 4.677799224853516, 4.872707366943359, 5.067615509033203, 5.262524127960205, 5.457432270050049, 5.652340412139893, 5.8472490310668945, 6.042157173156738, 6.237065315246582, 6.431973934173584, 6.626882076263428, 6.8217902183532715, 7.016698837280273, 7.211606979370117, 7.406515121459961, 7.601423740386963, 7.796331882476807, 7.99124002456665, 8.186148643493652, 8.381056785583496, 8.57596492767334, 8.770873069763184, 8.965781211853027, 9.160690307617188, 9.355598449707031, 9.550506591796875, 9.745414733886719, 9.940322875976562, 10.135231018066406, 10.330140113830566, 10.52504825592041, 10.719956398010254, 10.914864540100098, 11.109772682189941, 11.304680824279785, 11.499588966369629, 11.694498062133789, 11.889406204223633, 12.084314346313477, 12.27922248840332, 12.474130630493164, 12.669038772583008, 12.863947868347168, 13.058856010437012, 13.253764152526855, 13.4486722946167, 13.643580436706543, 13.838488578796387, 14.033397674560547, 14.22830581665039, 14.423213958740234, 14.618122100830078, 14.813030242919922, 15.007938385009766, 15.202847480773926, 15.39775562286377, 15.592663764953613, 15.787571907043457, 15.9824800491333, 16.17738914489746, 16.372297286987305, 16.56720542907715, 16.762113571166992, 16.957021713256836, 17.15192985534668, 17.346837997436523, 17.541746139526367, 17.73665428161621, 17.931562423706055, 18.1264705657959, 18.321380615234375, 18.51628875732422, 18.711196899414062, 18.906105041503906, 19.10101318359375, 19.295921325683594, 19.490829467773438, 19.68573760986328, 19.880645751953125, 20.07555389404297, 20.270462036132812, 20.465370178222656, 20.660280227661133, 20.855188369750977, 21.05009651184082, 21.245004653930664, 21.439912796020508, 21.63482093811035, 21.829729080200195, 22.02463722229004, 22.219545364379883, 22.414453506469727, 22.60936164855957, 22.804269790649414, 22.999177932739258, 23.194087982177734, 23.388996124267578, 23.583904266357422, 23.778812408447266, 23.97372055053711, 24.168628692626953, 24.363536834716797, 24.55844497680664, 24.753353118896484, 24.948261260986328, 25.143169403076172, 25.338077545166016, 25.532987594604492, 25.727895736694336, 25.92280387878418, 26.117712020874023, 26.312620162963867, 26.50752830505371, 26.702436447143555, 26.8973445892334, 27.092252731323242, 27.287160873413086, 27.48206901550293], "143": [4.276087760925293, 4.470455169677734, 4.664823055267334, 4.859190464019775, 5.053557872772217, 5.247925758361816, 5.442293167114258, 5.636661052703857, 5.831028461456299, 6.025396347045898, 6.21976375579834, 6.4141316413879395, 6.608499050140381, 6.802866458892822, 6.997234344482422, 7.191601753234863, 7.385969638824463, 7.580337047576904, 7.774704933166504, 7.969072341918945, 8.163439750671387, 8.357807159423828, 8.552175521850586, 8.746542930603027, 8.940910339355469, 9.13527774810791, 9.329646110534668, 9.52401351928711, 9.71838092803955, 9.912748336791992, 10.107115745544434, 10.301484107971191, 10.495851516723633, 10.690218925476074, 10.884586334228516, 11.078954696655273, 11.273322105407715, 11.467689514160156, 11.662056922912598, 11.856424331665039, 12.050792694091797, 12.245160102844238, 12.43952751159668, 12.633894920349121, 12.828263282775879, 13.02263069152832, 13.216998100280762, 13.411365509033203, 13.605732917785645, 13.800101280212402, 13.994468688964844, 14.188836097717285, 14.383203506469727, 14.577571868896484, 14.771939277648926, 14.966306686401367, 15.160674095153809, 15.35504150390625, 15.549409866333008, 15.74377727508545, 15.93814468383789, 16.13251304626465, 16.326879501342773, 16.52124786376953, 16.715614318847656, 16.909982681274414, 17.104351043701172, 17.298717498779297, 17.493085861206055, 17.687454223632812, 17.881820678710938, 18.076189041137695, 18.27055549621582, 18.464923858642578, 18.659292221069336, 18.85365867614746, 19.04802703857422, 19.242393493652344, 19.4367618560791, 19.63113021850586, 19.825496673583984, 20.019865036010742, 20.214231491088867, 20.408599853515625, 20.602968215942383, 20.797334671020508, 20.991703033447266, 21.18606948852539, 21.38043785095215, 21.574806213378906, 21.76917266845703, 21.96354103088379, 22.157909393310547, 22.352275848388672, 22.54664421081543, 22.741010665893555, 22.935379028320312, 23.12974739074707, 23.324113845825195, 23.518482208251953, 23.712848663330078, 23.907217025756836, 24.101585388183594, 24.29595184326172, 24.490320205688477, 24.6846866607666, 24.87905502319336, 25.073423385620117, 25.267789840698242, 25.462158203125, 25.656526565551758, 25.850893020629883, 26.04526138305664, 26.239627838134766, 26.433996200561523, 26.62836456298828, 26.822731018066406, 27.017099380493164, 27.21146583557129, 27.405834197998047], "144": [4.264274597167969, 4.458105564117432, 4.651936054229736, 4.845767021179199, 5.039597511291504, 5.233428001403809, 5.4272589683532715, 5.621089458465576, 5.814920425415039, 6.008750915527344, 6.202581405639648, 6.396412372589111, 6.590242862701416, 6.784073352813721, 6.977904319763184, 7.171734809875488, 7.365565776824951, 7.559396266937256, 7.7532267570495605, 7.947057723999023, 8.140888214111328, 8.334718704223633, 8.528549194335938, 8.722380638122559, 8.916211128234863, 9.110041618347168, 9.303872108459473, 9.497702598571777, 9.691534042358398, 9.885364532470703, 10.079195022583008, 10.273025512695312, 10.466856002807617, 10.660687446594238, 10.854517936706543, 11.048348426818848, 11.242178916931152, 11.436009407043457, 11.629840850830078, 11.823671340942383, 12.017501831054688, 12.211332321166992, 12.405162811279297, 12.598994255065918, 12.792824745178223, 12.986655235290527, 13.180485725402832, 13.374316215515137, 13.568146705627441, 13.761978149414062, 13.955808639526367, 14.149639129638672, 14.343469619750977, 14.537300109863281, 14.731131553649902, 14.924962043762207, 15.118792533874512, 15.312623023986816, 15.506453514099121, 15.700284957885742, 15.894115447998047, 16.08794593811035, 16.281776428222656, 16.47560691833496, 16.669437408447266, 16.86326789855957, 17.057098388671875, 17.250930786132812, 17.444761276245117, 17.638591766357422, 17.832422256469727, 18.02625274658203, 18.220083236694336, 18.41391372680664, 18.607744216918945, 18.80157470703125, 18.995405197143555, 19.189237594604492, 19.383068084716797, 19.5768985748291, 19.770729064941406, 19.96455955505371, 20.158390045166016, 20.35222053527832, 20.546051025390625, 20.73988151550293, 20.933712005615234, 21.12754249572754, 21.321374893188477, 21.51520538330078, 21.709035873413086, 21.90286636352539, 22.096696853637695, 22.29052734375, 22.484357833862305, 22.67818832397461, 22.872018814086914, 23.06584930419922, 23.259681701660156, 23.45351219177246, 23.647342681884766, 23.84117317199707, 24.035003662109375, 24.22883415222168, 24.422664642333984, 24.61649513244629, 24.810325622558594, 25.0041561126709, 25.197988510131836, 25.39181900024414, 25.585649490356445, 25.77947998046875, 25.973310470581055, 26.16714096069336, 26.360971450805664, 26.55480194091797, 26.748632431030273, 26.942462921142578, 27.136293411254883, 27.33012580871582], "145": [4.2525434494018555, 4.445840835571289, 4.639138221740723, 4.832435607910156, 5.02573299407959, 5.219030380249023, 5.412327766418457, 5.605625152587891, 5.798923015594482, 5.992220401763916, 6.18551778793335, 6.378815174102783, 6.572112560272217, 6.76540994644165, 6.958707332611084, 7.152004718780518, 7.345302104949951, 7.538599491119385, 7.731896877288818, 7.925194263458252, 8.118492126464844, 8.311789512634277, 8.505086898803711, 8.698384284973145, 8.891681671142578, 9.084979057312012, 9.278276443481445, 9.471573829650879, 9.664871215820312, 9.858168601989746, 10.05146598815918, 10.244763374328613, 10.438060760498047, 10.63135814666748, 10.824655532836914, 11.017952919006348, 11.211250305175781, 11.404547691345215, 11.597846031188965, 11.791143417358398, 11.984440803527832, 12.177738189697266, 12.3710355758667, 12.564332962036133, 12.757630348205566, 12.950927734375, 13.144225120544434, 13.337522506713867, 13.5308198928833, 13.724117279052734, 13.917414665222168, 14.110712051391602, 14.304009437561035, 14.497306823730469, 14.690604209899902, 14.883901596069336, 15.07719898223877, 15.270496368408203, 15.463793754577637, 15.65709114074707, 15.850388526916504, 16.043685913085938, 16.236984252929688, 16.430280685424805, 16.623579025268555, 16.816875457763672, 17.010173797607422, 17.20347023010254, 17.39676856994629, 17.590065002441406, 17.783363342285156, 17.976659774780273, 18.169958114624023, 18.36325454711914, 18.55655288696289, 18.74985122680664, 18.943147659301758, 19.136445999145508, 19.329742431640625, 19.523040771484375, 19.716337203979492, 19.909635543823242, 20.10293197631836, 20.29623031616211, 20.489526748657227, 20.682825088500977, 20.876121520996094, 21.069419860839844, 21.26271629333496, 21.45601463317871, 21.649311065673828, 21.842609405517578, 22.035905838012695, 22.229204177856445, 22.422500610351562, 22.615798950195312, 22.80909538269043, 23.00239372253418, 23.19569206237793, 23.388988494873047, 23.582286834716797, 23.775583267211914, 23.968881607055664, 24.16217803955078, 24.35547637939453, 24.54877281188965, 24.7420711517334, 24.935367584228516, 25.128665924072266, 25.321962356567383, 25.515260696411133, 25.70855712890625, 25.90185546875, 26.095151901245117, 26.288450241088867, 26.481746673583984, 26.675045013427734, 26.86834144592285, 27.0616397857666, 27.25493621826172], "146": [4.24089241027832, 4.433660507202148, 4.626428127288818, 4.8191962242126465, 5.011963844299316, 5.2047319412231445, 5.3974995613098145, 5.590267181396484, 5.7830352783203125, 5.975802898406982, 6.1685709953308105, 6.3613386154174805, 6.554106712341309, 6.7468743324279785, 6.939642429351807, 7.132410049438477, 7.325178146362305, 7.517945766448975, 7.710713863372803, 7.903481483459473, 8.0962495803833, 8.289016723632812, 8.48178482055664, 8.674552917480469, 8.867321014404297, 9.060088157653809, 9.252856254577637, 9.445624351501465, 9.638392448425293, 9.831159591674805, 10.023927688598633, 10.216695785522461, 10.409463882446289, 10.6022310256958, 10.794999122619629, 10.987767219543457, 11.180534362792969, 11.373302459716797, 11.566070556640625, 11.758838653564453, 11.951605796813965, 12.144373893737793, 12.337141990661621, 12.52991008758545, 12.722677230834961, 12.915445327758789, 13.108213424682617, 13.300980567932129, 13.493748664855957, 13.686516761779785, 13.879284858703613, 14.072052001953125, 14.264820098876953, 14.457588195800781, 14.65035629272461, 14.843123435974121, 15.03589153289795, 15.228659629821777, 15.421427726745605, 15.614194869995117, 15.806962966918945, 15.999731063842773, 16.1924991607666, 16.38526725769043, 16.578033447265625, 16.770801544189453, 16.96356964111328, 17.15633773803711, 17.349105834960938, 17.541873931884766, 17.734642028808594, 17.927410125732422, 18.120176315307617, 18.312944412231445, 18.505712509155273, 18.6984806060791, 18.89124870300293, 19.084016799926758, 19.276784896850586, 19.46955108642578, 19.66231918334961, 19.855087280273438, 20.047855377197266, 20.240623474121094, 20.433391571044922, 20.62615966796875, 20.818927764892578, 21.011693954467773, 21.2044620513916, 21.39723014831543, 21.589998245239258, 21.782766342163086, 21.975534439086914, 22.168302536010742, 22.361068725585938, 22.553836822509766, 22.746604919433594, 22.939373016357422, 23.13214111328125, 23.324909210205078, 23.517677307128906, 23.710445404052734, 23.90321159362793, 24.095979690551758, 24.288747787475586, 24.481515884399414, 24.674283981323242, 24.86705207824707, 25.0598201751709, 25.252586364746094, 25.445354461669922, 25.63812255859375, 25.830890655517578, 26.023658752441406, 26.216426849365234, 26.409194946289062, 26.601961135864258, 26.794729232788086, 26.987497329711914, 27.180265426635742], "147": [4.229321479797363, 4.421563148498535, 4.613805294036865, 4.806046962738037, 4.998289108276367, 5.190530776977539, 5.382772922515869, 5.575014591217041, 5.767256736755371, 5.959498405456543, 6.151740550994873, 6.343982219696045, 6.536223888397217, 6.728466033935547, 6.920707702636719, 7.112949848175049, 7.305191516876221, 7.497433662414551, 7.689675331115723, 7.881917476654053, 8.074159622192383, 8.266401290893555, 8.458642959594727, 8.650884628295898, 8.84312629699707, 9.035368919372559, 9.22761058807373, 9.419852256774902, 9.612093925476074, 9.804336547851562, 9.996578216552734, 10.188819885253906, 10.381061553955078, 10.57330322265625, 10.765545845031738, 10.95778751373291, 11.150029182434082, 11.342270851135254, 11.534513473510742, 11.726755142211914, 11.918996810913086, 12.111238479614258, 12.303481101989746, 12.495722770690918, 12.68796443939209, 12.880206108093262, 13.072447776794434, 13.264690399169922, 13.456932067871094, 13.649173736572266, 13.841415405273438, 14.033658027648926, 14.225899696350098, 14.41814136505127, 14.610383033752441, 14.802624702453613, 14.994867324829102, 15.187108993530273, 15.379350662231445, 15.571592330932617, 15.763834953308105, 15.956076622009277, 16.148319244384766, 16.340560913085938, 16.53280258178711, 16.72504425048828, 16.917285919189453, 17.109527587890625, 17.301769256591797, 17.49401092529297, 17.68625259399414, 17.878496170043945, 18.070737838745117, 18.26297950744629, 18.45522117614746, 18.647462844848633, 18.839704513549805, 19.031946182250977, 19.22418785095215, 19.41642951965332, 19.608673095703125, 19.800914764404297, 19.99315643310547, 20.18539810180664, 20.377639770507812, 20.569881439208984, 20.762123107910156, 20.954364776611328, 21.1466064453125, 21.338850021362305, 21.531091690063477, 21.72333335876465, 21.91557502746582, 22.107816696166992, 22.300058364868164, 22.492300033569336, 22.684541702270508, 22.87678337097168, 23.069026947021484, 23.261268615722656, 23.453510284423828, 23.645751953125, 23.837993621826172, 24.030235290527344, 24.222476959228516, 24.414718627929688, 24.606962203979492, 24.799203872680664, 24.991445541381836, 25.183687210083008, 25.37592887878418, 25.56817054748535, 25.760412216186523, 25.952653884887695, 26.144895553588867, 26.337139129638672, 26.529380798339844, 26.721622467041016, 26.913864135742188, 27.10610580444336], "148": [4.217829704284668, 4.409549236297607, 4.601268768310547, 4.792988300323486, 4.984707832336426, 5.176427364349365, 5.368146896362305, 5.559866428375244, 5.751585483551025, 5.943305015563965, 6.135024547576904, 6.326744079589844, 6.518463611602783, 6.710183143615723, 6.901902675628662, 7.093622207641602, 7.285341739654541, 7.4770612716674805, 7.66878080368042, 7.860500335693359, 8.052220344543457, 8.243939399719238, 8.435659408569336, 8.627378463745117, 8.819098472595215, 9.010817527770996, 9.202537536621094, 9.394256591796875, 9.585976600646973, 9.777695655822754, 9.969415664672852, 10.161134719848633, 10.35285472869873, 10.544573783874512, 10.73629379272461, 10.92801284790039, 11.119732856750488, 11.31145191192627, 11.50317096710205, 11.694890975952148, 11.88661003112793, 12.078330039978027, 12.270049095153809, 12.461769104003906, 12.653488159179688, 12.845208168029785, 13.036927223205566, 13.228647232055664, 13.420366287231445, 13.612086296081543, 13.803805351257324, 13.995525360107422, 14.187244415283203, 14.3789644241333, 14.570683479309082, 14.76240348815918, 14.954122543334961, 15.145842552185059, 15.33756160736084, 15.529281616210938, 15.721000671386719, 15.912720680236816, 16.104440689086914, 16.296159744262695, 16.487878799438477, 16.679597854614258, 16.871318817138672, 17.063037872314453, 17.254756927490234, 17.446475982666016, 17.63819694519043, 17.82991600036621, 18.021635055541992, 18.213354110717773, 18.405075073242188, 18.59679412841797, 18.78851318359375, 18.98023223876953, 19.171953201293945, 19.363672256469727, 19.555391311645508, 19.74711036682129, 19.938831329345703, 20.130550384521484, 20.322269439697266, 20.513988494873047, 20.70570945739746, 20.897428512573242, 21.089147567749023, 21.280866622924805, 21.47258758544922, 21.664306640625, 21.85602569580078, 22.047744750976562, 22.239465713500977, 22.431184768676758, 22.62290382385254, 22.81462287902832, 23.0063419342041, 23.198062896728516, 23.389781951904297, 23.581501007080078, 23.77322006225586, 23.964941024780273, 24.156660079956055, 24.348379135131836, 24.540098190307617, 24.73181915283203, 24.923538208007812, 25.115257263183594, 25.306976318359375, 25.49869728088379, 25.69041633605957, 25.88213539123535, 26.073854446411133, 26.265575408935547, 26.457294464111328, 26.64901351928711, 26.84073257446289, 27.032453536987305], "149": [4.206416130065918, 4.397616863250732, 4.588817596435547, 4.780018329620361, 4.971219062805176, 5.16241979598999, 5.3536200523376465, 5.544820785522461, 5.736021518707275, 5.92722225189209, 6.118422985076904, 6.309623718261719, 6.500824451446533, 6.692025184631348, 6.883225917816162, 7.074426651000977, 7.265627384185791, 7.4568281173706055, 7.64802885055542, 7.839229583740234, 8.030430793762207, 8.221631050109863, 8.412832260131836, 8.604032516479492, 8.795233726501465, 8.986433982849121, 9.177635192871094, 9.36883544921875, 9.560036659240723, 9.751236915588379, 9.942438125610352, 10.133638381958008, 10.32483959197998, 10.516039848327637, 10.707240104675293, 10.898441314697266, 11.089641571044922, 11.280842781066895, 11.47204303741455, 11.663244247436523, 11.85444450378418, 12.045645713806152, 12.236845970153809, 12.428047180175781, 12.619247436523438, 12.81044864654541, 13.001648902893066, 13.192850112915039, 13.384050369262695, 13.575251579284668, 13.766451835632324, 13.957653045654297, 14.148853302001953, 14.340054512023926, 14.531254768371582, 14.722455978393555, 14.913656234741211, 15.104857444763184, 15.29605770111084, 15.487258911132812, 15.678459167480469, 15.869660377502441, 16.060861587524414, 16.25206184387207, 16.443262100219727, 16.634462356567383, 16.825664520263672, 17.016864776611328, 17.208065032958984, 17.39926528930664, 17.59046745300293, 17.781667709350586, 17.972867965698242, 18.1640682220459, 18.355270385742188, 18.546470642089844, 18.7376708984375, 18.928871154785156, 19.120073318481445, 19.3112735748291, 19.502473831176758, 19.693674087524414, 19.884876251220703, 20.07607650756836, 20.267276763916016, 20.458477020263672, 20.64967918395996, 20.840879440307617, 21.032079696655273, 21.22327995300293, 21.414480209350586, 21.605682373046875, 21.79688262939453, 21.988082885742188, 22.179283142089844, 22.370485305786133, 22.56168556213379, 22.752885818481445, 22.9440860748291, 23.13528823852539, 23.326488494873047, 23.517688751220703, 23.70888900756836, 23.90009117126465, 24.091291427612305, 24.28249168395996, 24.473691940307617, 24.664894104003906, 24.856094360351562, 25.04729461669922, 25.238494873046875, 25.429697036743164, 25.62089729309082, 25.812097549438477, 26.003297805786133, 26.194499969482422, 26.385700225830078, 26.576900482177734, 26.76810073852539, 26.95930290222168], "150": [4.195079803466797, 4.385765552520752, 4.576450824737549, 4.767136573791504, 4.957821846008301, 5.148507118225098, 5.339192867279053, 5.52987813949585, 5.7205634117126465, 5.911249160766602, 6.101934432983398, 6.2926201820373535, 6.48330545425415, 6.673990726470947, 6.864676475524902, 7.055361747741699, 7.246047496795654, 7.436732769012451, 7.627418041229248, 7.818103790283203, 8.0087890625, 8.199474334716797, 8.390159606933594, 8.580845832824707, 8.771531105041504, 8.9622163772583, 9.152901649475098, 9.343586921691895, 9.534273147583008, 9.724958419799805, 9.915643692016602, 10.106328964233398, 10.297014236450195, 10.487700462341309, 10.678385734558105, 10.869071006774902, 11.0597562789917, 11.250441551208496, 11.441126823425293, 11.631813049316406, 11.822498321533203, 12.01318359375, 12.203868865966797, 12.394554138183594, 12.585240364074707, 12.775925636291504, 12.9666109085083, 13.157296180725098, 13.347981452941895, 13.538667678833008, 13.729352951049805, 13.920038223266602, 14.110723495483398, 14.301408767700195, 14.492094993591309, 14.682780265808105, 14.873465538024902, 15.0641508102417, 15.254836082458496, 15.445521354675293, 15.636207580566406, 15.826892852783203, 16.017578125, 16.208263397216797, 16.398948669433594, 16.58963394165039, 16.780319213867188, 16.971006393432617, 17.161691665649414, 17.35237693786621, 17.543062210083008, 17.733747482299805, 17.9244327545166, 18.1151180267334, 18.305803298950195, 18.496488571166992, 18.68717384338379, 18.877859115600586, 19.068546295166016, 19.259231567382812, 19.44991683959961, 19.640602111816406, 19.831287384033203, 20.02197265625, 20.212657928466797, 20.403343200683594, 20.59402847290039, 20.784713745117188, 20.975400924682617, 21.166086196899414, 21.35677146911621, 21.547456741333008, 21.738142013549805, 21.9288272857666, 22.1195125579834, 22.310197830200195, 22.500883102416992, 22.69156837463379, 22.882253646850586, 23.072940826416016, 23.263626098632812, 23.45431137084961, 23.644996643066406, 23.835681915283203, 24.0263671875, 24.217052459716797, 24.407737731933594, 24.59842300415039, 24.789108276367188, 24.979795455932617, 25.170480728149414, 25.36116600036621, 25.551851272583008, 25.742536544799805, 25.9332218170166, 26.1239070892334, 26.314592361450195, 26.505277633666992, 26.69596290588379, 26.886648178100586], "151": [4.183821201324463, 4.373994827270508, 4.564168453216553, 4.754342079162598, 4.944515705108643, 5.1346893310546875, 5.324862957000732, 5.515036582946777, 5.705210208892822, 5.895384311676025, 6.08555793762207, 6.275731563568115, 6.46590518951416, 6.656078815460205, 6.84625244140625, 7.036426067352295, 7.22659969329834, 7.416773796081543, 7.606947422027588, 7.797121047973633, 7.987294673919678, 8.177468299865723, 8.367642402648926, 8.557815551757812, 8.747989654541016, 8.938162803649902, 9.128336906433105, 9.318510055541992, 9.508684158325195, 9.698857307434082, 9.889031410217285, 10.079205513000488, 10.269378662109375, 10.459552764892578, 10.649725914001465, 10.839900016784668, 11.030073165893555, 11.220247268676758, 11.410420417785645, 11.600594520568848, 11.79076862335205, 11.980941772460938, 12.17111587524414, 12.361289024353027, 12.55146312713623, 12.741636276245117, 12.93181037902832, 13.121983528137207, 13.31215763092041, 13.502331733703613, 13.6925048828125, 13.882678985595703, 14.07285213470459, 14.263026237487793, 14.45319938659668, 14.643373489379883, 14.833547592163086, 15.023720741271973, 15.213894844055176, 15.404067993164062, 15.594242095947266, 15.784415245056152, 15.974589347839355, 16.164762496948242, 16.354936599731445, 16.54511070251465, 16.73528480529785, 16.925457000732422, 17.115631103515625, 17.305805206298828, 17.49597930908203, 17.6861515045166, 17.876325607299805, 18.066499710083008, 18.25667381286621, 18.446847915649414, 18.637020111083984, 18.827194213867188, 19.01736831665039, 19.207542419433594, 19.397714614868164, 19.587888717651367, 19.77806282043457, 19.968236923217773, 20.158411026000977, 20.348583221435547, 20.53875732421875, 20.728931427001953, 20.919105529785156, 21.109277725219727, 21.29945182800293, 21.489625930786133, 21.679800033569336, 21.86997413635254, 22.06014633178711, 22.250320434570312, 22.440494537353516, 22.63066864013672, 22.82084083557129, 23.011014938354492, 23.201189041137695, 23.3913631439209, 23.5815372467041, 23.771709442138672, 23.961883544921875, 24.152057647705078, 24.34223175048828, 24.53240394592285, 24.722578048706055, 24.912752151489258, 25.10292625427246, 25.293100357055664, 25.483272552490234, 25.673446655273438, 25.86362075805664, 26.053794860839844, 26.243967056274414, 26.434141159057617, 26.62431526184082, 26.814489364624023], "152": [4.172638416290283, 4.362303733825684, 4.551969051361084, 4.741634368896484, 4.931299686431885, 5.120965003967285, 5.3106303215026855, 5.500295639038086, 5.689960956573486, 5.879626750946045, 6.069292068481445, 6.258957386016846, 6.448622703552246, 6.6382880210876465, 6.827953338623047, 7.017618656158447, 7.207283973693848, 7.396949291229248, 7.586615085601807, 7.776280403137207, 7.965945720672607, 8.155611038208008, 8.345276832580566, 8.534941673278809, 8.724607467651367, 8.91427230834961, 9.103938102722168, 9.29360294342041, 9.483268737792969, 9.672933578491211, 9.86259937286377, 10.052265167236328, 10.24193000793457, 10.431595802307129, 10.621260643005371, 10.81092643737793, 11.000591278076172, 11.19025707244873, 11.379921913146973, 11.569587707519531, 11.75925350189209, 11.948918342590332, 12.13858413696289, 12.328248977661133, 12.517914772033691, 12.707579612731934, 12.897245407104492, 13.086910247802734, 13.276576042175293, 13.466241836547852, 13.655906677246094, 13.845572471618652, 14.035237312316895, 14.224903106689453, 14.414567947387695, 14.604233741760254, 14.793898582458496, 14.983564376831055, 15.173230171203613, 15.362895011901855, 15.552560806274414, 15.742225646972656, 15.931891441345215, 16.121557235717773, 16.311222076416016, 16.500886917114258, 16.690553665161133, 16.880218505859375, 17.069883346557617, 17.25954818725586, 17.449214935302734, 17.638879776000977, 17.82854461669922, 18.01820945739746, 18.207876205444336, 18.397541046142578, 18.58720588684082, 18.776872634887695, 18.966537475585938, 19.15620231628418, 19.345867156982422, 19.535533905029297, 19.72519874572754, 19.91486358642578, 20.104530334472656, 20.2941951751709, 20.48386001586914, 20.673524856567383, 20.863191604614258, 21.0528564453125, 21.242521286010742, 21.432188034057617, 21.62185287475586, 21.8115177154541, 22.001182556152344, 22.19084930419922, 22.38051414489746, 22.570178985595703, 22.759843826293945, 22.94951057434082, 23.139175415039062, 23.328840255737305, 23.51850700378418, 23.708171844482422, 23.897836685180664, 24.087501525878906, 24.27716827392578, 24.466833114624023, 24.656497955322266, 24.84616470336914, 25.035829544067383, 25.225494384765625, 25.415159225463867, 25.604825973510742, 25.794490814208984, 25.984155654907227, 26.17382049560547, 26.363487243652344, 26.553152084350586, 26.742816925048828], "153": [4.1615309715271, 4.350691318511963, 4.539852142333984, 4.729012489318848, 4.918172836303711, 5.107333183288574, 5.296494007110596, 5.485654354095459, 5.674814701080322, 5.863975524902344, 6.053135871887207, 6.24229621887207, 6.431457042694092, 6.620617389678955, 6.809777736663818, 6.99893856048584, 7.188098907470703, 7.377259254455566, 7.566420078277588, 7.755580425262451, 7.9447407722473145, 8.133901596069336, 8.3230619430542, 8.512222290039062, 8.701382637023926, 8.890542984008789, 9.079704284667969, 9.268864631652832, 9.458024978637695, 9.647185325622559, 9.836345672607422, 10.025506019592285, 10.214666366577148, 10.403827667236328, 10.592988014221191, 10.782148361206055, 10.971308708190918, 11.160469055175781, 11.349629402160645, 11.538790702819824, 11.727951049804688, 11.91711139678955, 12.106271743774414, 12.295432090759277, 12.48459243774414, 12.67375373840332, 12.862914085388184, 13.052074432373047, 13.24123477935791, 13.430395126342773, 13.619555473327637, 13.8087158203125, 13.99787712097168, 14.187037467956543, 14.376197814941406, 14.56535816192627, 14.754518508911133, 14.943678855895996, 15.132840156555176, 15.322000503540039, 15.511160850524902, 15.700321197509766, 15.889481544494629, 16.078641891479492, 16.267803192138672, 16.45696258544922, 16.6461238861084, 16.835285186767578, 17.024444580078125, 17.213605880737305, 17.40276527404785, 17.59192657470703, 17.781085968017578, 17.970247268676758, 18.159408569335938, 18.348567962646484, 18.537729263305664, 18.72688865661621, 18.91604995727539, 19.105209350585938, 19.294370651245117, 19.483531951904297, 19.672691345214844, 19.861852645874023, 20.05101203918457, 20.24017333984375, 20.429332733154297, 20.618494033813477, 20.807655334472656, 20.996814727783203, 21.185976028442383, 21.37513542175293, 21.56429672241211, 21.75345802307129, 21.942617416381836, 22.131778717041016, 22.320938110351562, 22.510099411010742, 22.69925880432129, 22.88842010498047, 23.07758140563965, 23.266740798950195, 23.455902099609375, 23.645061492919922, 23.8342227935791, 24.02338218688965, 24.212543487548828, 24.401704788208008, 24.590864181518555, 24.780025482177734, 24.96918487548828, 25.15834617614746, 25.34750747680664, 25.536666870117188, 25.725828170776367, 25.914987564086914, 26.104148864746094, 26.29330825805664, 26.48246955871582, 26.671630859375], "154": [4.150498390197754, 4.339157581329346, 4.5278167724609375, 4.716475486755371, 4.905134677886963, 5.093793869018555, 5.282452583312988, 5.47111177444458, 5.659770488739014, 5.8484296798706055, 6.037088871002197, 6.225747585296631, 6.414406776428223, 6.6030659675598145, 6.791724681854248, 6.98038387298584, 7.169043064117432, 7.357701778411865, 7.546360969543457, 7.735020160675049, 7.923678874969482, 8.112338066101074, 8.300996780395508, 8.489656448364258, 8.678315162658691, 8.866973876953125, 9.055633544921875, 9.244292259216309, 9.432950973510742, 9.621610641479492, 9.810269355773926, 9.99892807006836, 10.18758773803711, 10.376246452331543, 10.564905166625977, 10.75356388092041, 10.94222354888916, 11.130882263183594, 11.319540977478027, 11.508200645446777, 11.696859359741211, 11.885518074035645, 12.074177742004395, 12.262836456298828, 12.451495170593262, 12.640154838562012, 12.828813552856445, 13.017472267150879, 13.206131935119629, 13.394790649414062, 13.583449363708496, 13.772109031677246, 13.96076774597168, 14.149426460266113, 14.338086128234863, 14.526744842529297, 14.71540355682373, 14.90406322479248, 15.092721939086914, 15.281380653381348, 15.470040321350098, 15.658699035644531, 15.847357749938965, 16.0360164642334, 16.22467613220215, 16.4133358001709, 16.601993560791016, 16.790653228759766, 16.979312896728516, 17.167970657348633, 17.356630325317383, 17.545289993286133, 17.73394775390625, 17.922607421875, 18.11126708984375, 18.299924850463867, 18.488584518432617, 18.677244186401367, 18.865901947021484, 19.054561614990234, 19.243221282958984, 19.4318790435791, 19.62053871154785, 19.8091983795166, 19.99785614013672, 20.18651580810547, 20.37517547607422, 20.563833236694336, 20.752492904663086, 20.941152572631836, 21.129810333251953, 21.318470001220703, 21.50712776184082, 21.69578742980957, 21.88444709777832, 22.073104858398438, 22.261764526367188, 22.450424194335938, 22.639081954956055, 22.827741622924805, 23.016401290893555, 23.205059051513672, 23.393718719482422, 23.582378387451172, 23.77103614807129, 23.95969581604004, 24.14835548400879, 24.337013244628906, 24.525672912597656, 24.714332580566406, 24.902990341186523, 25.091650009155273, 25.280309677124023, 25.46896743774414, 25.65762710571289, 25.84628677368164, 26.034944534301758, 26.223604202270508, 26.412263870239258, 26.600921630859375], "155": [4.139540195465088, 4.327701091766357, 4.515861988067627, 4.7040228843688965, 4.892183780670166, 5.0803446769714355, 5.268505573272705, 5.456666946411133, 5.644827842712402, 5.832988739013672, 6.021149635314941, 6.209310531616211, 6.3974714279174805, 6.58563232421875, 6.7737932205200195, 6.961954116821289, 7.150115013122559, 7.338275909423828, 7.526436805725098, 7.714597702026367, 7.902758598327637, 8.090919494628906, 8.279080390930176, 8.467241287231445, 8.655402183532715, 8.843563079833984, 9.031723976135254, 9.219884872436523, 9.408045768737793, 9.596206665039062, 9.784367561340332, 9.972528457641602, 10.160689353942871, 10.34885025024414, 10.53701114654541, 10.72517204284668, 10.913333892822266, 11.101494789123535, 11.289655685424805, 11.477816581726074, 11.665977478027344, 11.854138374328613, 12.042299270629883, 12.230460166931152, 12.418621063232422, 12.606781959533691, 12.794942855834961, 12.98310375213623, 13.1712646484375, 13.35942554473877, 13.547586441040039, 13.735747337341309, 13.923908233642578, 14.112069129943848, 14.300230026245117, 14.488390922546387, 14.676551818847656, 14.864712715148926, 15.052873611450195, 15.241034507751465, 15.429195404052734, 15.617356300354004, 15.805517196655273, 15.993678092956543, 16.181838989257812, 16.3700008392334, 16.55816078186035, 16.746322631835938, 16.93448257446289, 17.122644424438477, 17.31080436706543, 17.498966217041016, 17.68712615966797, 17.875288009643555, 18.063447952270508, 18.251609802246094, 18.439769744873047, 18.627931594848633, 18.816091537475586, 19.004253387451172, 19.192413330078125, 19.38057518005371, 19.568735122680664, 19.75689697265625, 19.945056915283203, 20.13321876525879, 20.321378707885742, 20.509540557861328, 20.69770050048828, 20.885862350463867, 21.07402229309082, 21.262184143066406, 21.45034408569336, 21.638505935668945, 21.82666778564453, 22.014827728271484, 22.20298957824707, 22.391149520874023, 22.57931137084961, 22.767471313476562, 22.95563316345215, 23.1437931060791, 23.331954956054688, 23.52011489868164, 23.708276748657227, 23.89643669128418, 24.084598541259766, 24.27275848388672, 24.460920333862305, 24.649080276489258, 24.837242126464844, 25.025402069091797, 25.213563919067383, 25.401723861694336, 25.589885711669922, 25.778045654296875, 25.96620750427246, 26.154367446899414, 26.342529296875, 26.530689239501953], "156": [4.128655433654785, 4.316321849822998, 4.503987789154053, 4.691654205322266, 4.87932014465332, 5.066986083984375, 5.254652500152588, 5.442318439483643, 5.6299848556518555, 5.81765079498291, 6.005317211151123, 6.192983150482178, 6.380649566650391, 6.568315505981445, 6.755981922149658, 6.943647861480713, 7.131314277648926, 7.3189802169799805, 7.506646633148193, 7.694312572479248, 7.881978511810303, 8.069644927978516, 8.25731086730957, 8.444976806640625, 8.632643699645996, 8.82030963897705, 9.007975578308105, 9.19564151763916, 9.383308410644531, 9.570974349975586, 9.75864028930664, 9.946306228637695, 10.13397216796875, 10.321639060974121, 10.509305000305176, 10.69697093963623, 10.884636878967285, 11.072303771972656, 11.259969711303711, 11.447635650634766, 11.63530158996582, 11.822968482971191, 12.010634422302246, 12.1983003616333, 12.385966300964355, 12.57363224029541, 12.761299133300781, 12.948965072631836, 13.13663101196289, 13.324296951293945, 13.511963844299316, 13.699629783630371, 13.887295722961426, 14.07496166229248, 14.262628555297852, 14.450294494628906, 14.637960433959961, 14.825626373291016, 15.013293266296387, 15.200959205627441, 15.388625144958496, 15.57629108428955, 15.763957023620605, 15.951623916625977, 16.13928985595703, 16.326955795288086, 16.51462173461914, 16.702287673950195, 16.88995361328125, 17.077621459960938, 17.265287399291992, 17.452953338623047, 17.6406192779541, 17.828285217285156, 18.01595115661621, 18.203617095947266, 18.39128303527832, 18.578948974609375, 18.766616821289062, 18.954282760620117, 19.141948699951172, 19.329614639282227, 19.51728057861328, 19.704946517944336, 19.89261245727539, 20.080278396606445, 20.2679443359375, 20.455612182617188, 20.643278121948242, 20.830944061279297, 21.01861000061035, 21.206275939941406, 21.39394187927246, 21.581607818603516, 21.76927375793457, 21.956941604614258, 22.144607543945312, 22.332273483276367, 22.519939422607422, 22.707605361938477, 22.89527130126953, 23.082937240600586, 23.27060317993164, 23.458269119262695, 23.645936965942383, 23.833602905273438, 24.021268844604492, 24.208934783935547, 24.3966007232666, 24.584266662597656, 24.77193260192871, 24.959598541259766, 25.14726448059082, 25.334932327270508, 25.522598266601562, 25.710264205932617, 25.897930145263672, 26.085596084594727, 26.27326202392578, 26.460927963256836], "157": [4.1178436279296875, 4.305018424987793, 4.492193222045898, 4.679367542266846, 4.866542339324951, 5.053717136383057, 5.240891933441162, 5.428066730499268, 5.615241050720215, 5.80241584777832, 5.989590644836426, 6.176765441894531, 6.363940238952637, 6.551115036010742, 6.7382893562316895, 6.925464153289795, 7.1126389503479, 7.299813747406006, 7.486988544464111, 7.674162864685059, 7.861337661743164, 8.04851245880127, 8.235687255859375, 8.42286205291748, 8.610036849975586, 8.797211647033691, 8.984386444091797, 9.171560287475586, 9.358735084533691, 9.545909881591797, 9.733084678649902, 9.920259475708008, 10.107434272766113, 10.294609069824219, 10.481783866882324, 10.66895866394043, 10.856133460998535, 11.04330825805664, 11.23048210144043, 11.417656898498535, 11.60483169555664, 11.792006492614746, 11.979181289672852, 12.166356086730957, 12.353530883789062, 12.540705680847168, 12.727880477905273, 12.915055274963379, 13.102230072021484, 13.289403915405273, 13.476578712463379, 13.663753509521484, 13.85092830657959, 14.038103103637695, 14.2252779006958, 14.412452697753906, 14.599627494812012, 14.786802291870117, 14.973977088928223, 15.161151885986328, 15.348325729370117, 15.535500526428223, 15.722675323486328, 15.909850120544434, 16.09702491760254, 16.284198760986328, 16.47137451171875, 16.65854835510254, 16.84572410583496, 17.03289794921875, 17.220073699951172, 17.40724754333496, 17.594423294067383, 17.781597137451172, 17.968772888183594, 18.155946731567383, 18.343120574951172, 18.530296325683594, 18.717470169067383, 18.904645919799805, 19.091819763183594, 19.278995513916016, 19.466169357299805, 19.653345108032227, 19.840518951416016, 20.027694702148438, 20.214868545532227, 20.402042388916016, 20.589218139648438, 20.776391983032227, 20.96356773376465, 21.150741577148438, 21.33791732788086, 21.52509117126465, 21.71226692199707, 21.89944076538086, 22.08661651611328, 22.27379035949707, 22.46096420288086, 22.64813995361328, 22.83531379699707, 23.022489547729492, 23.20966339111328, 23.396839141845703, 23.584012985229492, 23.771188735961914, 23.958362579345703, 24.145538330078125, 24.332712173461914, 24.519886016845703, 24.707061767578125, 24.894235610961914, 25.081411361694336, 25.268585205078125, 25.455760955810547, 25.642934799194336, 25.830110549926758, 26.017284393310547, 26.20446014404297, 26.391633987426758], "158": [4.1071038246154785, 4.293790340423584, 4.4804768562316895, 4.667163372039795, 4.8538498878479, 5.040536403656006, 5.227222919464111, 5.413909435272217, 5.6005964279174805, 5.787282943725586, 5.973969459533691, 6.160655975341797, 6.347342491149902, 6.534029006958008, 6.720715522766113, 6.907402038574219, 7.094088554382324, 7.28077507019043, 7.467461585998535, 7.654148101806641, 7.840834617614746, 8.027521133422852, 8.214207649230957, 8.400894165039062, 8.587580680847168, 8.774267196655273, 8.960953712463379, 9.147640228271484, 9.33432674407959, 9.521013259887695, 9.7076997756958, 9.894386291503906, 10.081072807312012, 10.267759323120117, 10.454445838928223, 10.641132354736328, 10.827818870544434, 11.014505386352539, 11.201192855834961, 11.387879371643066, 11.574565887451172, 11.761252403259277, 11.947938919067383, 12.134625434875488, 12.321311950683594, 12.5079984664917, 12.694684982299805, 12.88137149810791, 13.068058013916016, 13.254744529724121, 13.441431045532227, 13.628117561340332, 13.814804077148438, 14.001490592956543, 14.188177108764648, 14.374863624572754, 14.56155014038086, 14.748236656188965, 14.93492317199707, 15.121609687805176, 15.308296203613281, 15.494982719421387, 15.681669235229492, 15.868355751037598, 16.055042266845703, 16.241729736328125, 16.428415298461914, 16.615102767944336, 16.801788330078125, 16.988475799560547, 17.175161361694336, 17.361848831176758, 17.548534393310547, 17.73522186279297, 17.921907424926758, 18.10859489440918, 18.29528045654297, 18.48196792602539, 18.66865348815918, 18.8553409576416, 19.04202651977539, 19.228713989257812, 19.4153995513916, 19.602087020874023, 19.788772583007812, 19.975460052490234, 20.162145614624023, 20.348833084106445, 20.535518646240234, 20.722206115722656, 20.908891677856445, 21.095579147338867, 21.282264709472656, 21.468952178955078, 21.655637741088867, 21.84232521057129, 22.029010772705078, 22.2156982421875, 22.402385711669922, 22.58907127380371, 22.775758743286133, 22.962444305419922, 23.149131774902344, 23.335817337036133, 23.522504806518555, 23.709190368652344, 23.895877838134766, 24.082563400268555, 24.269250869750977, 24.455936431884766, 24.642623901367188, 24.829309463500977, 25.0159969329834, 25.202682495117188, 25.38936996459961, 25.5760555267334, 25.76274299621582, 25.94942855834961, 26.13611602783203, 26.32280158996582], "159": [4.096435546875, 4.282637119293213, 4.468838691711426, 4.655040740966797, 4.84124231338501, 5.027443885803223, 5.2136454582214355, 5.399847030639648, 5.586048603057861, 5.772250175476074, 5.958451747894287, 6.1446533203125, 6.330855369567871, 6.517056941986084, 6.703258514404297, 6.88946008682251, 7.075661659240723, 7.2618632316589355, 7.448064804077148, 7.634266376495361, 7.820467948913574, 8.006669998168945, 8.19287109375, 8.379073143005371, 8.565274238586426, 8.751476287841797, 8.937677383422852, 9.123879432678223, 9.310081481933594, 9.496282577514648, 9.68248462677002, 9.868685722351074, 10.054887771606445, 10.2410888671875, 10.427290916442871, 10.613492012023926, 10.799694061279297, 10.985896110534668, 11.172097206115723, 11.358299255371094, 11.544500350952148, 11.73070240020752, 11.916903495788574, 12.103105545043945, 12.289306640625, 12.475508689880371, 12.661710739135742, 12.847911834716797, 13.034113883972168, 13.220314979553223, 13.406517028808594, 13.592718124389648, 13.77892017364502, 13.965121269226074, 14.151323318481445, 14.3375244140625, 14.523726463317871, 14.709928512573242, 14.896129608154297, 15.082331657409668, 15.268532752990723, 15.454734802246094, 15.640935897827148, 15.82713794708252, 16.01333999633789, 16.199541091918945, 16.3857421875, 16.571945190429688, 16.758146286010742, 16.944347381591797, 17.13054847717285, 17.31675148010254, 17.502952575683594, 17.68915367126465, 17.875354766845703, 18.06155776977539, 18.247758865356445, 18.4339599609375, 18.620162963867188, 18.806364059448242, 18.992565155029297, 19.17876625061035, 19.36496925354004, 19.551170349121094, 19.73737144470215, 19.923574447631836, 20.10977554321289, 20.295976638793945, 20.482177734375, 20.668380737304688, 20.854581832885742, 21.040782928466797, 21.22698402404785, 21.41318702697754, 21.599388122558594, 21.78558921813965, 21.971792221069336, 22.15799331665039, 22.344194412231445, 22.5303955078125, 22.716598510742188, 22.902799606323242, 23.089000701904297, 23.27520179748535, 23.46140480041504, 23.647605895996094, 23.83380699157715, 24.020009994506836, 24.20621109008789, 24.392412185668945, 24.57861328125, 24.764816284179688, 24.951017379760742, 25.137218475341797, 25.323421478271484, 25.50962257385254, 25.695823669433594, 25.88202476501465, 26.068227767944336, 26.25442886352539], "160": [4.085838317871094, 4.2715582847595215, 4.457278251647949, 4.642998218536377, 4.828718185424805, 5.014438152313232, 5.20015811920166, 5.385878086090088, 5.571597576141357, 5.757317543029785, 5.943037509918213, 6.128757476806641, 6.314477443695068, 6.500197410583496, 6.685917377471924, 6.871637344360352, 7.057357311248779, 7.243077278137207, 7.428797245025635, 7.6145172119140625, 7.800236701965332, 7.98595666885376, 8.171676635742188, 8.357397079467773, 8.543116569519043, 8.728837013244629, 8.914556503295898, 9.100275993347168, 9.285996437072754, 9.471715927124023, 9.65743637084961, 9.843155860900879, 10.028876304626465, 10.214595794677734, 10.40031623840332, 10.58603572845459, 10.771756172180176, 10.957475662231445, 11.143195152282715, 11.3289155960083, 11.51463508605957, 11.700355529785156, 11.886075019836426, 12.071795463562012, 12.257514953613281, 12.443235397338867, 12.628954887390137, 12.814675331115723, 13.000394821166992, 13.186115264892578, 13.371834754943848, 13.557554244995117, 13.743274688720703, 13.928994178771973, 14.114714622497559, 14.300434112548828, 14.486154556274414, 14.671874046325684, 14.85759449005127, 15.043313980102539, 15.229034423828125, 15.414753913879395, 15.600473403930664, 15.78619384765625, 15.97191333770752, 16.15763282775879, 16.343353271484375, 16.52907371520996, 16.714794158935547, 16.9005126953125, 17.086233139038086, 17.271953582763672, 17.457674026489258, 17.64339256286621, 17.829113006591797, 18.014833450317383, 18.200551986694336, 18.386272430419922, 18.571992874145508, 18.757713317871094, 18.943431854248047, 19.129152297973633, 19.31487274169922, 19.500593185424805, 19.686311721801758, 19.872032165527344, 20.05775260925293, 20.243471145629883, 20.42919158935547, 20.614912033081055, 20.80063247680664, 20.986351013183594, 21.17207145690918, 21.357791900634766, 21.54351234436035, 21.729230880737305, 21.91495132446289, 22.100671768188477, 22.28639030456543, 22.472110748291016, 22.6578311920166, 22.843551635742188, 23.02927017211914, 23.214990615844727, 23.400711059570312, 23.5864315032959, 23.77215003967285, 23.957870483398438, 24.143590927124023, 24.329309463500977, 24.515029907226562, 24.70075035095215, 24.886470794677734, 25.072189331054688, 25.257909774780273, 25.44363021850586, 25.629350662231445, 25.8150691986084, 26.000789642333984, 26.18651008605957], "161": [4.075311183929443, 4.260552883148193, 4.445794105529785, 4.631035804748535, 4.816277027130127, 5.001518726348877, 5.186759948730469, 5.3720011711120605, 5.5572428703308105, 5.742484092712402, 5.927725791931152, 6.112967014312744, 6.298208713531494, 6.483449935913086, 6.668691158294678, 6.853932857513428, 7.0391740798950195, 7.2244157791137695, 7.409657001495361, 7.594898700714111, 7.780139923095703, 7.965381145477295, 8.150622367858887, 8.335864067077637, 8.521105766296387, 8.706347465515137, 8.89158821105957, 9.07682991027832, 9.26207160949707, 9.447312355041504, 9.632554054260254, 9.817795753479004, 10.003037452697754, 10.188278198242188, 10.373519897460938, 10.558761596679688, 10.744002342224121, 10.929244041442871, 11.114485740661621, 11.299727439880371, 11.484968185424805, 11.670209884643555, 11.855451583862305, 12.040692329406738, 12.225934028625488, 12.411175727844238, 12.596417427062988, 12.781658172607422, 12.966899871826172, 13.152141571044922, 13.337382316589355, 13.522624015808105, 13.707865715026855, 13.893107414245605, 14.078348159790039, 14.263589859008789, 14.448831558227539, 14.634072303771973, 14.819314002990723, 15.004555702209473, 15.189797401428223, 15.375038146972656, 15.560279846191406, 15.745521545410156, 15.93076229095459, 16.116004943847656, 16.301244735717773, 16.486486434936523, 16.671728134155273, 16.856969833374023, 17.042211532592773, 17.227453231811523, 17.412694931030273, 17.59793472290039, 17.78317642211914, 17.96841812133789, 18.15365982055664, 18.33890151977539, 18.52414321899414, 18.70938491821289, 18.894624710083008, 19.079866409301758, 19.265108108520508, 19.450349807739258, 19.635591506958008, 19.820833206176758, 20.006074905395508, 20.191314697265625, 20.376556396484375, 20.561798095703125, 20.747039794921875, 20.932281494140625, 21.117523193359375, 21.302764892578125, 21.488004684448242, 21.673246383666992, 21.858488082885742, 22.043729782104492, 22.228971481323242, 22.414213180541992, 22.599454879760742, 22.78469467163086, 22.96993637084961, 23.15517807006836, 23.34041976928711, 23.52566146850586, 23.71090316772461, 23.89614486694336, 24.081384658813477, 24.266626358032227, 24.451868057250977, 24.637109756469727, 24.822351455688477, 25.007593154907227, 25.192834854125977, 25.378074645996094, 25.563316345214844, 25.748558044433594, 25.933799743652344, 26.119041442871094], "162": [4.064854145050049, 4.249619960784912, 4.434386253356934, 4.619152069091797, 4.803918361663818, 4.98868465423584, 5.173450469970703, 5.358216762542725, 5.542982578277588, 5.727748870849609, 5.912514686584473, 6.097280979156494, 6.282047271728516, 6.466813087463379, 6.6515793800354, 6.836345195770264, 7.021111488342285, 7.205877780914307, 7.39064359664917, 7.575409889221191, 7.760175704956055, 7.944941997528076, 8.129708290100098, 8.314474105834961, 8.499239921569824, 8.684006690979004, 8.868772506713867, 9.05353832244873, 9.238304138183594, 9.423070907592773, 9.607836723327637, 9.7926025390625, 9.97736930847168, 10.162135124206543, 10.346900939941406, 10.53166675567627, 10.71643352508545, 10.901199340820312, 11.085965156555176, 11.270731925964355, 11.455497741699219, 11.640263557434082, 11.825029373168945, 12.009796142578125, 12.194561958312988, 12.379327774047852, 12.564094543457031, 12.748860359191895, 12.933626174926758, 13.118391990661621, 13.3031587600708, 13.487924575805664, 13.672690391540527, 13.857457160949707, 14.04222297668457, 14.226988792419434, 14.411755561828613, 14.596521377563477, 14.78128719329834, 14.966053009033203, 15.150819778442383, 15.335585594177246, 15.52035140991211, 15.705118179321289, 15.889883995056152, 16.074649810791016, 16.259416580200195, 16.444181442260742, 16.628948211669922, 16.8137149810791, 16.99847984313965, 17.183246612548828, 17.368013381958008, 17.552778244018555, 17.737545013427734, 17.92230987548828, 18.10707664489746, 18.29184341430664, 18.476608276367188, 18.661375045776367, 18.846141815185547, 19.030906677246094, 19.215673446655273, 19.400440216064453, 19.585205078125, 19.76997184753418, 19.95473861694336, 20.139503479003906, 20.324270248413086, 20.509037017822266, 20.693801879882812, 20.878568649291992, 21.06333351135254, 21.24810028076172, 21.4328670501709, 21.617631912231445, 21.802398681640625, 21.987165451049805, 22.17193031311035, 22.35669708251953, 22.54146385192871, 22.726228713989258, 22.910995483398438, 23.095762252807617, 23.280527114868164, 23.465293884277344, 23.65005874633789, 23.83482551574707, 24.01959228515625, 24.204357147216797, 24.389123916625977, 24.573890686035156, 24.758655548095703, 24.943422317504883, 25.128189086914062, 25.31295394897461, 25.49772071838379, 25.68248748779297, 25.867252349853516, 26.052019119262695], "163": [4.0544657707214355, 4.238759517669678, 4.42305326461792, 4.60734748840332, 4.7916412353515625, 4.975934982299805, 5.160229206085205, 5.344522953033447, 5.5288166999816895, 5.71311092376709, 5.897404670715332, 6.081698417663574, 6.265992164611816, 6.450286388397217, 6.634580135345459, 6.818873882293701, 7.003168106079102, 7.187461853027344, 7.371755599975586, 7.556049823760986, 7.7403435707092285, 7.924637317657471, 8.108931541442871, 8.293225288391113, 8.477519035339355, 8.661812782287598, 8.84610652923584, 9.030401229858398, 9.21469497680664, 9.398988723754883, 9.583282470703125, 9.767576217651367, 9.95186996459961, 10.136163711547852, 10.32045841217041, 10.504752159118652, 10.689045906066895, 10.873339653015137, 11.057633399963379, 11.241927146911621, 11.42622184753418, 11.610515594482422, 11.794809341430664, 11.979103088378906, 12.163396835327148, 12.34769058227539, 12.531984329223633, 12.716279029846191, 12.900572776794434, 13.084866523742676, 13.269160270690918, 13.45345401763916, 13.637747764587402, 13.822042465209961, 14.006336212158203, 14.190629959106445, 14.374923706054688, 14.55921745300293, 14.743511199951172, 14.927804946899414, 15.112099647521973, 15.296393394470215, 15.480687141418457, 15.6649808883667, 15.849274635314941, 16.0335693359375, 16.217863082885742, 16.402156829833984, 16.586450576782227, 16.77074432373047, 16.95503807067871, 17.139331817626953, 17.323625564575195, 17.507919311523438, 17.69221305847168, 17.876506805419922, 18.060802459716797, 18.24509620666504, 18.42938995361328, 18.613683700561523, 18.797977447509766, 18.982271194458008, 19.16656494140625, 19.350858688354492, 19.535152435302734, 19.719446182250977, 19.90373992919922, 20.08803367614746, 20.272327423095703, 20.456623077392578, 20.64091682434082, 20.825210571289062, 21.009504318237305, 21.193798065185547, 21.37809181213379, 21.56238555908203, 21.746679306030273, 21.930973052978516, 22.115266799926758, 22.299560546875, 22.483854293823242, 22.668148040771484, 22.85244369506836, 23.0367374420166, 23.221031188964844, 23.405324935913086, 23.589618682861328, 23.77391242980957, 23.958206176757812, 24.142499923706055, 24.326793670654297, 24.51108741760254, 24.69538116455078, 24.879674911499023, 25.063968658447266, 25.24826431274414, 25.432558059692383, 25.616851806640625, 25.801145553588867, 25.98543930053711], "164": [4.044145584106445, 4.227970600128174, 4.411795616149902, 4.595620155334473, 4.779445171356201, 4.9632697105407715, 5.1470947265625, 5.33091926574707, 5.514744281768799, 5.698568820953369, 5.882393836975098, 6.066218852996826, 6.2500433921813965, 6.433868408203125, 6.617692947387695, 6.801517963409424, 6.985342502593994, 7.169167518615723, 7.352992534637451, 7.5368170738220215, 7.72064208984375, 7.90446662902832, 8.08829116821289, 8.272116661071777, 8.455941200256348, 8.639765739440918, 8.823591232299805, 9.007415771484375, 9.191240310668945, 9.375064849853516, 9.558890342712402, 9.742714881896973, 9.926539421081543, 10.110363960266113, 10.294189453125, 10.47801399230957, 10.66183853149414, 10.845664024353027, 11.029488563537598, 11.213313102722168, 11.397137641906738, 11.580963134765625, 11.764787673950195, 11.948612213134766, 12.132437705993652, 12.316262245178223, 12.500086784362793, 12.683911323547363, 12.86773681640625, 13.05156135559082, 13.23538589477539, 13.419211387634277, 13.603035926818848, 13.786860466003418, 13.970685005187988, 14.154510498046875, 14.338335037231445, 14.522159576416016, 14.705985069274902, 14.889809608459473, 15.073634147644043, 15.257458686828613, 15.4412841796875, 15.62510871887207, 15.80893325805664, 15.992757797241211, 16.17658233642578, 16.360408782958984, 16.544233322143555, 16.728057861328125, 16.911882400512695, 17.095706939697266, 17.279531478881836, 17.463356018066406, 17.64718246459961, 17.83100700378418, 18.01483154296875, 18.19865608215332, 18.38248062133789, 18.56630516052246, 18.75012969970703, 18.9339542388916, 19.117780685424805, 19.301605224609375, 19.485429763793945, 19.669254302978516, 19.853078842163086, 20.036903381347656, 20.220727920532227, 20.40455436706543, 20.58837890625, 20.77220344543457, 20.95602798461914, 21.13985252380371, 21.32367706298828, 21.50750160217285, 21.691328048706055, 21.875152587890625, 22.058977127075195, 22.242801666259766, 22.426626205444336, 22.610450744628906, 22.794275283813477, 22.97810173034668, 23.16192626953125, 23.34575080871582, 23.52957534790039, 23.71339988708496, 23.89722442626953, 24.0810489654541, 24.264875411987305, 24.448699951171875, 24.632524490356445, 24.816349029541016, 25.000173568725586, 25.183998107910156, 25.367822647094727, 25.55164909362793, 25.7354736328125, 25.91929817199707], "165": [4.033893585205078, 4.217252731323242, 4.400611400604248, 4.583970069885254, 4.76732873916626, 4.950687885284424, 5.13404655456543, 5.3174052238464355, 5.500763893127441, 5.6841230392456055, 5.867481708526611, 6.050840377807617, 6.234199523925781, 6.417558193206787, 6.600916862487793, 6.784275531768799, 6.967634677886963, 7.150993347167969, 7.334352016448975, 7.517711162567139, 7.7010698318481445, 7.88442850112915, 8.067787170410156, 8.25114631652832, 8.434505462646484, 8.617863655090332, 8.801222801208496, 8.984580993652344, 9.167940139770508, 9.351299285888672, 9.53465747833252, 9.718016624450684, 9.901375770568848, 10.084733963012695, 10.26809310913086, 10.451452255249023, 10.634810447692871, 10.818169593811035, 11.001527786254883, 11.184886932373047, 11.368246078491211, 11.551604270935059, 11.734963417053223, 11.918322563171387, 12.101680755615234, 12.285039901733398, 12.468399047851562, 12.65175724029541, 12.835116386413574, 13.018475532531738, 13.201833724975586, 13.38519287109375, 13.568551063537598, 13.751910209655762, 13.935269355773926, 14.118627548217773, 14.301986694335938, 14.485345840454102, 14.66870403289795, 14.852063179016113, 15.035422325134277, 15.218780517578125, 15.402139663696289, 15.585498809814453, 15.7688570022583, 15.952216148376465, 16.135574340820312, 16.318933486938477, 16.50229263305664, 16.685651779174805, 16.86901092529297, 17.0523681640625, 17.235727310180664, 17.419086456298828, 17.602445602416992, 17.785804748535156, 17.969161987304688, 18.15252113342285, 18.335880279541016, 18.51923942565918, 18.702598571777344, 18.885957717895508, 19.06931495666504, 19.252674102783203, 19.436033248901367, 19.61939239501953, 19.802751541137695, 19.986108779907227, 20.16946792602539, 20.352827072143555, 20.53618621826172, 20.719545364379883, 20.902904510498047, 21.086261749267578, 21.269620895385742, 21.452980041503906, 21.63633918762207, 21.819698333740234, 22.003055572509766, 22.18641471862793, 22.369773864746094, 22.553133010864258, 22.736492156982422, 22.919851303100586, 23.103208541870117, 23.28656768798828, 23.469926834106445, 23.65328598022461, 23.836645126342773, 24.020004272460938, 24.20336151123047, 24.386720657348633, 24.570079803466797, 24.75343894958496, 24.936798095703125, 25.120155334472656, 25.30351448059082, 25.486873626708984, 25.67023277282715, 25.853591918945312], "166": [4.023708820343018, 4.206604480743408, 4.389500617980957, 4.572396278381348, 4.7552924156188965, 4.938188076019287, 5.121084213256836, 5.303979873657227, 5.486875534057617, 5.669771671295166, 5.852667331695557, 6.0355634689331055, 6.218459129333496, 6.401354789733887, 6.5842509269714355, 6.767146587371826, 6.950042724609375, 7.132938385009766, 7.3158345222473145, 7.498730182647705, 7.681625843048096, 7.8645219802856445, 8.047417640686035, 8.230313301086426, 8.413208961486816, 8.596105575561523, 8.779001235961914, 8.961896896362305, 9.144792556762695, 9.327689170837402, 9.510584831237793, 9.693480491638184, 9.876376152038574, 10.059271812438965, 10.242168426513672, 10.425064086914062, 10.607959747314453, 10.790855407714844, 10.973751068115234, 11.156647682189941, 11.339543342590332, 11.522439002990723, 11.705334663391113, 11.888230323791504, 12.071126937866211, 12.254022598266602, 12.436918258666992, 12.619813919067383, 12.802709579467773, 12.98560619354248, 13.168501853942871, 13.351397514343262, 13.534293174743652, 13.717188835144043, 13.90008544921875, 14.08298110961914, 14.265876770019531, 14.448772430419922, 14.631669044494629, 14.81456470489502, 14.99746036529541, 15.1803560256958, 15.363251686096191, 15.546148300170898, 15.729043960571289, 15.91193962097168, 16.09483528137207, 16.27773094177246, 16.46062660217285, 16.643522262573242, 16.826417922973633, 17.009315490722656, 17.192211151123047, 17.375106811523438, 17.558002471923828, 17.74089813232422, 17.92379379272461, 18.106689453125, 18.28958511352539, 18.47248077392578, 18.655378341674805, 18.838274002075195, 19.021169662475586, 19.204065322875977, 19.386960983276367, 19.569856643676758, 19.75275230407715, 19.93564796447754, 20.11854362487793, 20.30143928527832, 20.484336853027344, 20.667232513427734, 20.850128173828125, 21.033023834228516, 21.215919494628906, 21.398815155029297, 21.581710815429688, 21.764606475830078, 21.94750213623047, 22.13039779663086, 22.313295364379883, 22.496191024780273, 22.679086685180664, 22.861982345581055, 23.044878005981445, 23.227773666381836, 23.410669326782227, 23.593564987182617, 23.776460647583008, 23.95935821533203, 24.142253875732422, 24.325149536132812, 24.508045196533203, 24.690940856933594, 24.873836517333984, 25.056732177734375, 25.239627838134766, 25.422523498535156, 25.605419158935547, 25.78831672668457]}


# boundaries for study area, used in regridding
study_area = {
    "min_lat": 54.125,
    "max_lat": 68.875,
    "min_lon": 8.375,
    "max_lon": 24.125
}

# cells for areas of interest based on TUW_GEO reshuffle
swe_shuffle_cells = [1397, 1398, 1399, 1433, 1434, 1435, 1470, 1471]
den_shuffle_cells = [1360, 1361, 1396, 1397, 1433]
nordic_shuffle_cells = [1326, 1360, 1361, 1362, 1396, 1397, 1398, 1399, 1433, 1434, 1435, 1436, 1469, 1470, 1471, 1472,
                        1506, 1507, 1508, 1542, 1543, 1544]

