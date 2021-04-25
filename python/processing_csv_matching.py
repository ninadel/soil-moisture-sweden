import csv
import os
import pandas
import datetime
import sm_config as config
import sm_tools as tools
from multiprocessing import Pool


def export_loc_dict(loc_dict, export_file, orient="index"):
    # df_loc_inventory = pandas.DataFrame.from_dict(loc_inventory, orient="rows")
    df = pandas.DataFrame.from_dict(loc_dict, orient=orient)
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
            loc_data.dropna(inplace=True)
            loc_index = loc_data.index
            lines = len(loc_index)
            # loc_file = open(loc_filename)
            # reader = csv.reader(loc_file)
            # lines = len(list(reader))
            loc_inventory[loc][dataset] = lines
    return loc_inventory


def filter_loc_inventory(loc_inventory_dict, cutoff=100):
# function that filters a location inventory dictionary based on all datasets having a count above the cutoff
    filtered_loc_list = []
    datasets = []
    for loc, loc_dict in loc_inventory_dict.items():
        low_row_count = 1000000000
        for dataset, count in loc_dict.items():
            if count < low_row_count:
                low_row_count = count
        if low_row_count >= cutoff + 1:
            filtered_loc_list.append(loc)
    return filtered_loc_list


def filter_temporal_match(temp_match_dict):
    datasets = temp_match_dict['datasets']
    loc = temp_match_dict['loc']
    output_root = temp_match_dict['output_root']
    ignore_datasets = temp_match_dict['ignore_datasets']
    start_date = temp_match_dict['start_date']
    end_date = temp_match_dict['end_date']
    daily_row_cutoff = temp_match_dict['daily_row_cutoff']
    # list which stores dates between start date and end date
    all_dates = []
    # list which stores dates where all datasets have records
    loc_date_list = []
    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        # print(start_date)
        all_dates.append(start_date)
        start_date += delta
        # dictionary to track records matching filtering criteria, stores
        date_data_dict = {}
    # Loop 1 - cycle through datasets in that location
    dataset_len = len(datasets)
    dataset_counter = 0
    for dataset in datasets:
        dataset_counter += 1
        print("dataset {} of {}".format(dataset_counter, dataset_len))
        # if dataset in ignore list, skip
        if dataset in ignore_datasets:
            print("break")
            break
        csv_quarter_dir = config.dict_product_inputs[dataset]['csv_quarters']
        loc_filename = "{}_{}.csv".format(dataset, loc)
        loc_file = os.path.join(csv_quarter_dir, loc_filename)
        loc_data = tools.csv_to_pdseries(loc_file)
        loc_data.dropna(inplace=True)
        # Loop 2 - cycle through dates between start and end date
        for match_date in all_dates:
            date_id = (match_date.year, match_date.month, match_date.day)
            if date_id not in date_data_dict.keys():
                date_data_dict[date_id] = {}
            date_data = tools.timefilter_data(loc_data, year_filter=match_date.year,  month_filter=match_date.month,
                                              day_filter=match_date.day)
            date_data_dict[date_id][dataset] = {
                'rows': date_data.shape[0],
                'data': date_data
            }
    # Loop 1 - cycle through dates for loc
    for match_date, data_dict in date_data_dict.items():
        min_rows = 1000000000
        # Loop 3 - cycle through datasets for date
        for dataset, count_dict in data_dict.items():
            if count_dict['rows'] < min_rows:
                min_rows = count_dict['rows']
        if min_rows > daily_row_cutoff:
            loc_date_list.append(date_id)
            if output_root is not None:
                # Loop 2 - cycle through datasets for date
                for dataset, count_dict in data_dict.items():
                    output_subdir = os.path.join(output_root, dataset)
                    if not os.path.exists(output_subdir):
                        os.makedirs(output_subdir)
                    # generate output csv file name
                    output_csv_filename = "{}_{}.csv".format(dataset, loc)
                    output_csv_file = os.path.join(output_subdir, output_csv_filename)
                    if not os.path.exists(output_csv_file):
                        count_dict['data'].to_csv(output_csv_file)
                    else:
                        count_dict['data'].to_csv(output_csv_file, mode='a', header=False)
    return loc_date_list


def get_temp_match_dicts(datasets, output_root, ignore_datasets, start_date, end_date, daily_row_cutoff):
    datasets = [dataset for dataset in datasets if dataset not in ignore_datasets]
    loc_inventory = get_loc_inventory(datasets, config.dict_swe_gldas_points)
    export_loc_dict(loc_inventory, os.path.join(output_root, 'loc_inventory_{}.csv'.format(
                        datetime.datetime.now().strftime("%Y%m%d%H%M%S"))))
    filtered_loc_list = filter_loc_inventory(loc_inventory, cutoff=100)
    print("{} datasets".format(len(datasets)))
    print("{} locations".format(len(filtered_loc_list)))
    temp_match_dicts = [{'datasets': datasets, 'loc': loc, 'output_root': output_root,
                         'ignore_datasets': ignore_datasets, 'start_date': start_date, 'end_date': end_date,
                         'daily_row_cutoff': daily_row_cutoff} for loc in filtered_loc_list]
    return temp_match_dicts


if __name__ == '__main__':
    all_grid_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'Sentinel-1', 'SMOS-BEC', 'SMOS-IC',
                         'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']
    start_date = datetime.datetime(2015, 4, 1)
    end_date = datetime.datetime(2018, 12, 31)
    daily_row_cutoff = 0
    # TC 1 - ASCAT
    print("TC 1")
    tc_datasets_1 = ['SMAP L3 Enhanced', 'SMOS-IC', 'ASCAT 12.5 TS', 'ERA5 0-1']
    tc_output_root_1 = r"C:\git\soil-moisture-sweden\analysis_output\tc_temp_match_ASCAT_{}".format(
        datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    os.makedirs(tc_output_root_1)
    tc_temp_match_dicts_1 = get_temp_match_dicts(tc_datasets_1, tc_output_root_1, [], start_date, end_date,
                                                 daily_row_cutoff)
    # GRID 1 - Include ASCAT
    print("GRID 1")
    grid_datasets_1 = all_grid_datasets
    grid_output_root_1 = r"C:\git\soil-moisture-sweden\analysis_output\grid_temp_match_all_{}".format(
        datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    os.makedirs(grid_output_root_1)
    grid_temp_match_dicts_1 = get_temp_match_dicts(grid_datasets_1, grid_output_root_1, [], start_date, end_date,
                                                   daily_row_cutoff)
    # TC 2 - Sentinel-1
    print("TC 2")
    tc_datasets_2 = ['SMAP L3 Enhanced', 'SMOS-IC', 'Sentinel-1', 'ERA5 0-1']
    tc_output_root_2 = r"C:\git\soil-moisture-sweden\analysis_output\tc_temp_match_Sentinel-1_{}".format(
        datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    os.makedirs(tc_output_root_2)
    tc_temp_match_dicts_2 = get_temp_match_dicts(tc_datasets_2, tc_output_root_2, [], start_date, end_date,
                                                 daily_row_cutoff)
    # GRID 2 - Remove ASCAT
    print("GRID 2")
    grid_datasets_2 = [dataset for dataset in all_grid_datasets if dataset != 'ASCAT 12.5 TS']
    grid_output_root_2 = r"C:\git\soil-moisture-sweden\analysis_output\grid_temp_match_NoASCAT_{}".format(
        datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    )
    os.makedirs(grid_output_root_2)
    grid_temp_match_dicts_2 = get_temp_match_dicts(grid_datasets_2, grid_output_root_2, [], start_date, end_date,
                                                   daily_row_cutoff)
    temp_match_dicts = tc_temp_match_dicts_1 + grid_temp_match_dicts_1 + tc_temp_match_dicts_2 + grid_temp_match_dicts_2
    with Pool(5) as p:
        p.map(filter_temporal_match, temp_match_dicts)