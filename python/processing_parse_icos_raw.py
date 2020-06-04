"""
Author: Nina del Rosario, nina.del@gmail.com
Date: 5/31/2020
Script to parse raw ICOS data to a time series more similar to ISMN format
Times shifted from CET to UTC
Exports soil moisture values & QC flags, soil temperature values & QC flags
"""

import os
import pandas
import datetime

# input data
input_folder = r"C:\git\nordic-insitu-sm-data\ICOS_raw-data\nor_reformatted"
output_folder = r"C:\git\soil-moisture-sweden\icos_data"

import_fields = ['date', 'time', 'SWC_1_1_1', 'qc_SWC_1_1_1', 'TS_1_1_1', 'qc_TS_1_1_1']
target_fields = ['datetime_utc', 'icos_ssm', 'qc_ssm', 'icos_ts', 'qc_ts']

raw_file_dict = {}

# read files
file_list = os.listdir(input_folder)
for file in file_list:
    # split filenames to get codes
    file_parts = file.split('_')
    # if file name startes with 'SE-' and file ext is either txt or csv, add to dictionary
    if file_parts[0][0:3] == 'SE-' and ((file_parts[-1][-3:] == 'txt') or (file_parts[-1][-3:] == 'csv')):
        station_code = file_parts[0]
        file_year = file_parts[2]
        if station_code not in raw_file_dict.keys():
            raw_file_dict[station_code] = {}
        if file_year not in raw_file_dict[station_code].keys():
            raw_file_dict[station_code][file_year] = file
        else:
            print('File not added. Entry already in dictionary.')

for station in raw_file_dict:
    # start a dataframe for each code with target fields
    station_df = pandas.DataFrame(columns=target_fields)
    station_df.set_index(target_fields[0])
    file_dict = raw_file_dict[station]
    for year in file_dict:
        file = file_dict[year]
        print(year)
        # open each file as a dataframe, no index, 2 header rows
        file_df = pandas.read_csv(os.path.join(input_folder, file), usecols=import_fields, skiprows=[1])
        rename_dict = {'SWC_1_1_1': "icos_ssm",
                       'qc_SWC_1_1_1': 'qc_ssm',
                       'TS_1_1_1': 'icos_ts',
                       'qc_TS_1_1_1': 'qc_ts'}
        file_df = file_df.rename(columns=rename_dict)
        file_df['datetime_cet'] = file_df['date'] + ' ' + file_df['time']
        # convert cet to utc
        file_df['datetime_cet'] = file_df['datetime_cet'].apply(pandas.to_datetime)
        file_df['datetime_utc'] = file_df['datetime_cet'] - datetime.timedelta(hours=1)
        # convert % to decimals
        file_df['icos_ssm'] = file_df['icos_ssm'] / 100
        temp_df = file_df[['datetime_utc', 'icos_ssm', 'qc_ssm', 'icos_ts', 'qc_ts']]
        station_df = pandas.concat([station_df, temp_df])
    station_df = station_df.set_index('datetime_utc')
    print(station, station_df.shape)
    filename = '{}.csv'.format(station)
    station_df.to_csv(os.path.join(output_folder, filename), sep=",")
