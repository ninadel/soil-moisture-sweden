"""
Author: Nina del Rosario
Date: 7/18/2020
Script for exporting station ts
Done:
"ASCAT 12.5 TS", "GLDAS", "Sentinel-1", "SMAP L3", "SMAP L4", "SMOS-BEC"

Need to do:
"CCI Active", "CCI Passive", "CCI Combined", "SMOS-IC"

For ERA5, SMPL3E, see processing_export_stations_xarray.py
"""
import os
import sm_tools as tools
import sm_config as config

output_root = r"C:\git\soil-moisture-sweden\test_output_data\station_csv"
log_file = os.path.join(output_root, "log_file.csv")

# Dictionary which turns on/off product analyses
# export_products = ["ASCAT 12.5 TS", "CCI Active", "CCI Passive", "CCI Combined", "ERA5", "GLDAS", "Sentinel-1",
#                    "SMAP L3", "SMAP L3 E", "SMAP L4", "SMOS-IC", "SMOS-BEC"]

# Removing ERA5 and SMAP L3 E
# export_products = ["ASCAT 12.5 TS", "CCI Active", "CCI Passive", "CCI Combined", "GLDAS", "Sentinel-1", "SMAP L3",
#                    "SMAP L4", "SMOS-IC", "SMOS-BEC"]
# export_products = ["Sentinel-1"]

icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
# use this as a parameter below if you want to analyze both ICOS and ISMN
station_list = icos_readers + ismn_readers

for product in export_products:
    product_metadata = config.dict_product_inputs[product]
    reader = tools.get_product_reader(product, product_metadata)
    output_dir = os.path.join(output_root, product)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for station in station_list:
        station_name = station.station
        print(station_name)
        # def get_product_data(lon, lat, product, reader, anomaly=False, station=None, filter_prod=True, sm_only=True):
        product_data = tools.get_product_data(lon=station.longitude, lat=station.latitude, station=station,
                                              product=product, reader=reader, filter_prod=False, sm_only=False)
        tools.write_log(log_file, "{}, {}, {}".format(product, station_name, product_data.shape))
        # def get_station_ts_filename(station_object=None, station_name=None, network_name=None):
        ts_filename = tools.get_station_ts_filename(station)
        ts_file = os.path.join(output_dir, ts_filename)
        product_data.to_csv(ts_file)
        # try:
        #     product_data = tools.get_product_data(lon=station.longitude, lat=station.latitude, product=product,
        #                                           reader=reader, filter_prod=False, sm_only=False)
        #     tools.write_log(log_file, "{}, {}, {}".format(product, station_name, product_data.shape))
        #     # def get_station_ts_filename(station_object=None, station_name=None, network_name=None):
        #     ts_filename = tools.get_station_ts_filename(station)
        #     ts_file = os.path.join(output_dir, ts_filename)
        #     product_data.to_csv(ts_file)
        # except:
        #     tools.write_log(log_file, "{}, {}, None".format(product, station_name))