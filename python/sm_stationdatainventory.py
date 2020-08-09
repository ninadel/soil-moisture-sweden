"""
Author: Nina del Rosario
Date: 8/4/2020
Script for counting inventory for evaluation data
Status: In progress
"""
from datetime import datetime
import os
import sm_tools as tools
import sm_config as config
import sm_evaluation as evaluation
import xarray as xr
import pandas as pd
import warnings
from multiprocessing import Pool

output_root = "../test_output_data/inventory_data"
if not os.path.exists(output_root):
    os.makedirs(output_root)

evaluation_datasets = ['SMAP L4', 'ASCAT 12.5 TS', 'SMAP L3 Enhanced', 'GLDAS', 'ERA5 0-1', 'ERA5 0-25', 'Sentinel-1',
                       'SMOS-BEC', 'SMOS-IC', 'SMAP L3', 'CCI Combined', 'CCI Passive', 'CCI Active']


icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
evaluation_stations = icos_readers + ismn_readers

def get_station_inventory(dataset_name, start_date, end_date, station):
    def get_inventory_dict(filter, df):
        inventory_dict = {'dataset': dataset_name, 'network': station.network, 'station': station.station,
                          'lat': station.latitude, 'lon': station.longitude, 'filter': filter}
        timefilter_counts = tools.split_by_timeframe(df, years=(2015, 2018), months=False,
                                                     ignore=[(2015, "winter", None), (2015, None, 1),
                                                             (2015, None, 2), (2015, None, 3)])[1]
        inventory_dict.update(timefilter_counts)
        return inventory_dict
    lon = station.longitude
    lat = station.latitude
    f = config.dict_native_files[dataset_name]
    ds = xr.open_dataset(f)
    sm_field = config.dict_product_fields[dataset_name]['sm_field']
    sm = ds[sm_field]
    if dataset_name == "ASCAT 12.5 TS":
        row = tools.find_nearest(config.dict_h115_coords['lat'], lat)[0]
        col = tools.find_nearest(config.dict_h115_coords[str(row)], lon)[0]
        df = sm.sel(time=slice(start_date, end_date), row=row, col=col).to_pandas().dropna()
        inventory_dict = get_inventory_dict('DropNA', df)
        inventory_cols = list(inventory_dict.keys())
        inventory_df = pd.DataFrame(columns=inventory_cols)
        inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        # valid values 0-100
        df = df[(df >= 0) & (df <= 100)]
        inventory_dict = get_inventory_dict('sm_0-100', df)
        inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        # noise filters
        noise = ds['sm_noise']
        df = noise.sel(time=slice(start_date, end_date), row=row, col=col).to_pandas().dropna()
        noise_filter = df[df < 50]
        inventory_dict = get_inventory_dict('noise_below50', noise_filter)
        inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        noise_filter = df[df < 20]
        inventory_dict = get_inventory_dict('noise_below20', noise_filter)
        inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        noise_filter = df[df < 10]
        inventory_dict = get_inventory_dict('noise_below10', noise_filter)
        inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        noise_filter = df[df < 5]
        inventory_dict = get_inventory_dict('noise_below05', noise_filter)
        inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        # conf_flag filters
        conf_flag = ds['conf_flag']
        df = conf_flag.sel(time=slice(start_date, end_date), row=row, col=col).to_pandas().dropna()
        conf_values = df.unique()
        for value in conf_values:
            conf_filter = df[df == value]
            inventory_dict = get_inventory_dict('confflag_{}'.format(value), conf_filter)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        # corr_flag filters
        corr_flag = ds['corr_flag']
        df = corr_flag.sel(time=slice(start_date, end_date), row=row, col=col).to_pandas().dropna()
        corr_values = df.unique()
        for value in corr_values:
            corr_filter = df[df == value]
            inventory_dict = get_inventory_dict('corrflag_{}'.format(value), corr_filter)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        # proc_flag filters
        proc_flag = ds['proc_flag']
        df = proc_flag.sel(time=slice(start_date, end_date), row=row, col=col).to_pandas().dropna()
        proc_values = df.unique()
        for value in proc_values:
            proc_filter = df[df == value]
            inventory_dict = get_inventory_dict('procflag_{}'.format(value), proc_filter)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        # ssf filters
        ssf = ds['ssf']
        df = ssf.sel(time=slice(start_date, end_date), row=row, col=col).to_pandas().dropna()
        ssf_values = df.unique()
        for value in ssf_values:
            ssf_filter = df[df == value]
            inventory_dict = get_inventory_dict('ssf_{}'.format(value), ssf_filter)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        return inventory_df
    else:
        df = sm.sel(time=slice(start_date, end_date), lat=lat, lon=lon).to_pandas().dropna()
        inventory_dict = get_inventory_dict('DropNA', df)
        inventory_cols = list(inventory_dict.keys())
        inventory_df = pd.DataFrame(columns=inventory_cols)
        inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        if dataset_name == 'CCI Active' or dataset_name == 'CCI Passive' or dataset_name == 'CCI Combined':
            flag = ds['flag']
            df = flag.sel(time=slice(start_date, end_date), lat=lat, lon=lon).to_pandas().dropna()
            flag_values = df.unique()
            for value in flag_values:
                flag_filter = df[df == value]
                inventory_dict = get_inventory_dict('flag_{}'.format(value), flag_filter)
                inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
            df = ds['sm_uncertainty']
            sm_uncertainty_filter = df[df < 50]
            inventory_dict = get_inventory_dict('sm_uncertainty_below50', sm_uncertainty_filter)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
            sm_uncertainty_filter = df[df < 20]
            inventory_dict = get_inventory_dict('sm_uncertainty_below20', sm_uncertainty_filter)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
            sm_uncertainty_filter = df[df < 10]
            inventory_dict = get_inventory_dict('sm_uncertainty_below10', sm_uncertainty_filter)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
            sm_uncertainty_filter = df[df < 5]
            inventory_dict = get_inventory_dict('sm_uncertainty_below10', sm_uncertainty_filter)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        if dataset_name == 'CCI Active':
            # valid values 0-100
            df = sm[sm >= 0 & sm <= 100]
            inventory_dict = get_inventory_dict('sm_0-100', df)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        elif dataset_name == 'CCI Passive':
            # valid values 0-1
            df = sm[sm >= 0 & sm <= 1]
            inventory_dict = get_inventory_dict('sm_0-1', df)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        elif dataset_name == 'CCI Combined':
            # valid values 0-1
            df = sm[sm >= 0 & sm <= 1]
            inventory_dict = get_inventory_dict('sm_0-1', df)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        elif dataset_name == 'ERA 0-1':
            # valid values 0-1
            df = sm[sm >= 0 & sm <= 1]
            inventory_dict = get_inventory_dict('sm_0-1', df)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        elif dataset_name == 'ERA 0-25':
            # valid values 0-1
            df = sm[sm >= 0 & sm <= 1]
            inventory_dict = get_inventory_dict('sm_0-1', df)
            inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        # elif dataset_name == 'GLDAS':
        #     pass
        elif dataset_name == 'SMAP L3' or dataset_name == 'SMAP L3 Enhanced':
            # retrieval_qual_flag
            df = ds['retrieval_qual_flag']
            retrieval_flag_values = df.unique()
            for value in retrieval_flag_values:
                retrieval_flag_filter = df[df == value]
                inventory_dict = get_inventory_dict('retrieval_qual_flag_{}'.format(value), retrieval_flag_filter)
                inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
            # surface_flag
            df = ds['surface_flag']
            surface_flag_values = df.unique()
            for value in surface_flag_values:
                surface_flag_filter = df[df == value]
                inventory_dict = get_inventory_dict('surface_flag_{}'.format(value), surface_flag_filter)
                inventory_df = inventory_df.append(inventory_dict, ignore_index=True)
        elif dataset_name == 'SMAP L4':
            pass
        elif dataset_name == 'Sentinel-1':
            pass
        elif dataset_name == 'SMOS-BEC':
            pass
        elif dataset_name == 'SMOS-IC':
            pass
        return inventory_df

def get_dataset_inventory(dataset):
    inventory_df = None
    for station in evaluation_stations:
        station_inventory = get_station_inventory(dataset, start_date=datetime(2015,4,1),
                                                  end_date=datetime(2018, 12, 31, 23, 59, 59), station=station)
        if inventory_df is None:
            inventory_df = station_inventory
        else:
            inventory_df = pd.concat([inventory_df, station_inventory])
    inventory_df.to_csv(os.path.join(output_root, "{} inventory.csv".format(dataset)), index=False)
    return inventory_df


# icos_readers = tools.get_icos_readers(config.icos_input_dir)
# ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
# # use this as a parameter below if you want to analyze both ICOS and ISMN
# reference_list = icos_readers + ismn_readers
#
# analysis_output_root = r"../analysis_output"
# analysis_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# analysis_results_folder = os.path.join(analysis_output_root, "{}_evaluation".format(analysis_timestamp))
# os.mkdir(analysis_results_folder)
# metrics_filename = "evaluation_metrics_{}.csv".format(analysis_timestamp)
# startdate = datetime(2015,4,1)
# enddate = datetime(2018, 12, 31, 23, 59)
#
# results = evaluation.evaluate_shuffle(icos_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=False)
# results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
# results = evaluation.evaluate_shuffle(icos_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=True,
#                               metrics_df=results)
# results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
# results = evaluation.evaluate_shuffle(ismn_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=False,
#                               metrics_df=results)
# results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
# results = evaluation.evaluate_shuffle(ismn_readers, evaluation_dict, output_folder=analysis_results_folder, anomaly=True,
#                               metrics_df=results)
# results.to_csv(os.path.join(analysis_results_folder, metrics_filename))
#
#
# icos_results = evaluation.evaluate_network_product(icos_readers, 'ASCAT 12.5 TS', startdate=datetime, enddate=enddate)

# if __name__ == '__main__':
#     with Pool(5) as p:
#         p.map(export_station_data, evaluation_datasets)

inventory = get_dataset_inventory('ASCAT 12.5 TS')
inventory = get_dataset_inventory('CCI Active')
