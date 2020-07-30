"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 7/23/2020
Script for downloading ERA5 data
"""

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-land',
    {
        'format': 'netcdf',
        'variable': 'volumetric_soil_water_layer_1',
        'year': [
            '2015', '2016', '2017',
            '2018',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '06:00',
            '09:00',
        ],
        'grid': [0.25, 0.25],
        'area': [
            70.87, 4.87, 54.87,
            31.37,
        ],
    },
    '0-25_ERA5-Land_0600-0900.nc')