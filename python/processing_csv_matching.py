import csv
import os
import pandas
import datetime
import sm_config as config
import sm_tools as tools

def export_loc_dict(loc_dict, export_file):
    # df_loc_inventory = pandas.DataFrame.from_dict(loc_inventory, orient="rows")
    df = pandas.DataFrame.from_dict(loc_dict, orient="index")
    df.to_csv(export_file)


def get_loc_inventory(datasets, loc_dict):
# function that generates a loc inventory dictionary which contains the number of records in the corresponding csv file
# location matching
    # start with an empty dictionary for copying locations?
    loc_inventory = {}
    # start with a list of datasets to match
    # for each location
    for loc, dict in loc_dict.items():
        loc_inventory[loc] = {}
        for dataset in datasets:
            csv_quarter_dir = config.dict_product_inputs[dataset]['csv_quarters']
            loc_filename = os.path.join(csv_quarter_dir, "{}_{}.csv".format(dataset, loc))
            loc_data = tools.csv_to_pdseries(loc_filename)
            loc_data.dropna()
            loc_index = loc_data.index
            lines = len(loc_index)
            # loc_file = open(loc_filename)
            # reader = csv.reader(loc_file)
            # lines = len(list(reader))
            loc_inventory[loc][dataset] = lines
        # employees = pd.DataFrame(
        #     data={'Name': ['John Doe', 'William Spark'],
        #           'Occupation': ['Chemist', 'Statistician'],
        #           'Date Of Join': ['2018-01-25', '2018-01-26'],
        #           'Age': [23, 24]},
        #     index=['Emp001', 'Emp002'],
        #     columns=['Name', 'Occupation', 'Date Of Join', 'Age'])
        # empty_df = pandas.DataFrame([[network_name, station_name, product_str, timeframe, anomaly, n, None, None,
        #                               None, None, None]], columns=config.metrics_df_columns)
        # metrics_merge.to_csv(os.path.join(evaluation_dict['output_root'], "{} metrics.csv".format(evaluation_dataset_name)), index=False)
    return loc_inventory
# add dictionary key for counting dataset records
        # check that a file exists for that location for each dataset

def filter_loc_inventory(loc_inventory_dict, cutoff=100):
# function that filters a location inventory dictionary based on all datasets having a count above the cutoff
    filtered_loc_inventory = {}
    for loc, loc_dict in loc_inventory_dict.items():
        low_row_count = 1000000000
        for dataset, count in loc_dict.items():
            if count < low_row_count:
                low_row_count = count
        if low_row_count >= cutoff + 1:
            filtered_loc_inventory[loc] = low_row_count
    return filtered_loc_inventory
# for dataset in triplet:
#     csv_quarter_dir = config.dict_product_inputs[dataset]['csv_quarters']
#     loc_filename = os.path.join(csv_quarter_dir, "{}_{}.csv".format(dataset, loc))

    # if false, add 0 to dictionary
        # if true, count number of rows and add to dictionary
    # this will return a dictonary which can be checked later for further processing


def filter_temporal_match(loc_inventory_dict, ignore_datasets = [], start_date=datetime.datetime(2015, 4, 1),
                          end_date=datetime.datetime(2018, 12, 31), cutoff=10, output_root=None):
    # list which stores dates between start date and end date
    all_dates = []
    # list which stores dates where all datasets have records
    loc_date_dict = {}
    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        # print(start_date)
        all_dates.append(start_date)
        start_date += delta
    # Loop 1 - cycle through locations in inventory
    for loc, dataset_dict in loc_inventory_dict.items():
        # dictionary to track records matching filtering criteria, stores
        date_data_dict = {}
        # Loop 2 - cycle through datasets in that location
        for dataset, count in dataset_dict.items():
            # if dataset in ignore list, skip
            if dataset in ignore_datasets:
                break
            csv_quarter_dir = config.dict_product_inputs[dataset]['csv_quarters']
            loc_filename = "{}_{}.csv".format(dataset, loc)
            loc_file = os.path.join(csv_quarter_dir, loc_file)
            loc_data = tools.csv_to_pdseries(loc_filename)
            loc_data.dropna()
            # Loop 3 - cycle through dates between start and end date
            for match_date in all_dates:
                date_id = (match_date.year, match_date.month, match_date.day)
                if match_date not in date_data_dict.keys():
                    date_data_dict[date_id] = {}
                date_data = tools.timefilter_data(loc_data, year_filter=match_date.year,  month_filter=match_date.month,
                                                  day_filter=match_date.day)
                date_data_dict[date_id][dataset] = {
                    'rows': date_data.shape[0],
                    'data': date_data
                }
        # Loop 2 - cycle through dates for loc
        for match_date, data_dict in date_data_dict.items():
            min_rows = 1000000000
            # Loop 3 - cycle through datasets for date
            for dataset, count_dict in data_dict.items():
                if count_dict['rows'] < min_rows:
                    min_rows = count_dict['rows']
            if min_rows > cutoff:
                if loc not in loc_date_dict.keys():
                    loc_date_dict[loc] = []
                loc_date_dict[loc].append(date_id)
                if output_root is not None:
                    for dataset, count_dict in data_dict.items():
                        pass
    return loc_date_dict

# temporal matching
    # version 1 - match everything including ascat
    # version 2 - match everything but leave out ascat
    # option 1 - use pytesmo - https://github.com/TUW-GEO/pytesmo/blob/master/src/pytesmo/temporal_matching.py
    # option 2 - for each date in series from start to end date,
        # check that records are available in all datasets on this date
        # if true
            # option 1 - write dataset rows to df
            # option 2 - write date to df
        # else go to next date
    # export dfs to csv

evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC', 'SMOS-IC',
                       'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']
dataset_list_1 = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC', 'SMOS-IC',
                       'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']
dataset_list_2 = ['SMAP L4', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC', 'SMOS-IC', 'SMAP L3',
                  'CCI Combined', 'CCI Passive', 'CCI Active']

# test statements
# print(evaluation_datasets[0:1])
# loc_inventory = get_loc_inventory(evaluation_datasets[0:2], config.dict_swe_gldas_points)
# print(loc_inventory)
# df_loc_inventory = pandas.DataFrame.from_dict(loc_inventory, orient="index")
# loc_inventory_file = r"C:\git\soil-moisture-sweden\analysis_output\test_loc_inventory.csv"
# export_loc_dict(loc_inventory, loc_inventory_file)
# print(df_loc_inventory)
# filtered_loc_inventory = filter_loc_inventory(loc_inventory, cutoff=300)
# filter_loc_inventory_file = r"C:\git\soil-moisture-sweden\analysis_output\test_filter_loc_inventory.csv"
# print(filtered_loc_inventory)
# print("loc_inventory len", len(loc_inventory))
# print("filtered_loc_inventory len", len(filtered_loc_inventory))
# 'start_date': datetime(2015, 4, 1),
# 'end_date': datetime(2018, 12, 31, 23, 59),
# tools.timefilter_data(df, year_filter=None, season_filter=None, month_filter=None, day_filter=None:

filter_temporal_match(0,0)