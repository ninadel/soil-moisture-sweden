import datetime
import os
import pandas
import sm_config as config
import sm_tools as tools

write_ts_to_file = True
product = "SMOS BEC"
input_dir = config.dict_product_inputs[product]['raw_dir']
output_dir = config.dict_product_inputs[product]['ts_dir']
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
file_list = os.listdir(input_dir)
file_list.sort()
export_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

sm_key = config.dict_product_fields[product]['sm_field']
hours_shift = config.dict_product_inputs[product]['hours_shift']

ref_locations = {}
icos_stations = config.dict_icos
hobe_stations = config.dict_hobe
ref_locations.update(config.dict_icos)
ref_locations.update(config.dict_hobe)

# dict to store station ts dataframes
station_ts = {}
# dict used for get_values function
locations = {}
for location, metadata in ref_locations.items():
    if "network" in metadata.keys():
        filename = "{}_{}.csv".format(metadata["network"], metadata["station"].replace(".", "-"))
    else:
        filename = "quarterdeg_{}.csv".format(location)
    station_ts[location] = {}
    station_ts[location]["filename"] = filename
    station_ts[location]["data"] = pandas.DataFrame(columns=['timestamp', 'sm'])
    locations[location] = {}
    locations[location]['lon'] = metadata['longitude']
    locations[location]['lat'] = metadata['latitude']

# extract data for locations from images
for file in file_list:
    image = tools.get_img_reader(product, os.path.join(input_dir, file))
    timestamp = image.timestamp
    print(timestamp)
    data_dict = image.get_values(locations)
    for key, value in data_dict.items():
        if key == "metadata":
            metadata = value
            sm_fill_value = metadata[sm_key]['_FillValue']
        else:
            location = key
            data = value['data']
            sm_value = data[sm_key]
            # only add valid values (invalid values were set to fill value by image reader class)
            if sm_value != sm_fill_value:
                loc_df = station_ts[location]['data']
                # if timestamp defaults to midnight, shift time to UTC of local overpass time
                obs_timestamp = timestamp + datetime.timedelta(hours=hours_shift)
                obs_df = pandas.DataFrame([[obs_timestamp, sm_value]], columns=['timestamp', 'sm'])
                station_ts[location]['data'] = pandas.concat([loc_df, obs_df])

for location, metadata in station_ts.items():
    filename = metadata['filename']
    df = metadata['data']
    df.set_index('timestamp', drop=True)
    tools.write_log(os.path.join(output_dir, "results_log_{}.txt".format(export_timestamp)),
                    "{}: {} rows".format(filename, df.shape[0]))
    if write_ts_to_file:
        df.to_csv(os.path.join(output_dir, filename), index=False)