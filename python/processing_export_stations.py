import sm_tools as tools
import sm_config as config

# Dictionary which turns on/off product analyses
# export_products = ["ASCAT 12.5 TS", "CCI Active", "CCI Passive", "CCI Combined", "ERA5", "GLDAS", "Sentinel-1",
#                    "SMAP L3", "SMAP L3 E", "SMAP L4", "SMOS-IC", "SMOS-BEC"]

# Removing ERA5 and SMAP L3 E
export_products = ["ASCAT 12.5 TS", "CCI Active", "CCI Passive", "CCI Combined", "GLDAS", "Sentinel-1", "SMAP L3",
                   "SMAP L4", "SMOS-IC", "SMOS-BEC"]

reader_dict = {}
for product in export_products:
    product_metadata = config.dict_product_inputs[product]
    reader_dict[product] = tools.get_product_reader(product, product_metadata)

icos_readers = tools.get_icos_readers(config.icos_input_dir)
ismn_readers = tools.get_ismn_readers(config.ismn_input_dir)
# use this as a parameter below if you want to analyze both ICOS and ISMN
reference_list = icos_readers + ismn_readers


def export_station_data(station, product):
    pass