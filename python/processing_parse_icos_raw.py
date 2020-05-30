import os
import pandas

# input data
input_folder = r"C:\git\nordic-insitu-sm-data\ICOS_raw-data"
# output data
output_folder = r"C:\git\soil-moisture-sweden\test_output_data\test_insitu_processing"

filter_fields = ['date', 'time','SWC_1_1_1', 'qc_SWC_1_1_1', 'TS_1_1_1', 'qc_TS_1_1_1']
target_fields = ['date', 'time','icos_ssm', 'qc_qc', 'icos_ts', 'qc_ts', 'datetime_cet', 'datetime_utc']

raw_file_dict = {}


# read files
file_list = os.listdir(input_folder)
for file in file_list:
    # split filenames to get codes
    file_parts = file.split('_')
    if file_parts[0][0:3] == 'SE-' and file_parts[-1] == 'flag.txt':
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
    file_dict = raw_file_dict[station]
    for year in file_dict:
        file = file_dict[year]
        # open each file as a dataframe, no index, 2 header rows
        file_df = pandas.read_csv(os.path.join(input_folder, file), usecols=filter_fields, skiprows=[1])
        # rename fields
        print(file_df)
        break
    break
# convert sm to decimal
# convert cet to utc

# get station from filename
# get year from filename
# extract relevant fields
# rename relevant fields
# convert cet to utc and make utc index
# append to station dataframe
# when all dataframes are filled, export each to a csv
