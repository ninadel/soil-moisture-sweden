import pandas as pd
import os
import numpy as np

def write_grid_ascii_raster(metric_file):
    def get_quarter_grid_coord_index(lat, lon):
        lon0 = 11.375
        lat0 = 55.375
        lats = [lat0 + (0.25 * i) for i in range(0, nrows)]
        lats.sort(reverse=True)
        lons = [lon0 + (0.25 * i) for i in range(0, ncols)]
        lati = lats.index(lat)
        loni = lons.index(lon)
        index = (lati * ncols) + loni
        return index
    def start_ascii_file():
        out_f = os.path.join(output_folder, "grideval_{}_{}_{}_{}.asc".format(dataset, timefilter, anomaly_str, metric))
        asciif = open(out_f,"w")
        asciif.write("ncols {}\n".format(ncols))
        asciif.write("nrows {}\n".format(nrows))
        asciif.write("xllcorner     {}\n".format(xllcorner))
        asciif.write("yllcorner     {}\n".format(yllcorner))
        asciif.write("cellsize      {}\n".format(cellsize))
        asciif.write("NODATA_value  {}\n".format(NODATA_value))
        return asciif
    def get_dataset_name(filename):
        split_filename = filename.split(" ")
        ei = split_filename.index("ERA5")
        dataset_name = " ".join(split_filename[0:ei])
        return dataset_name
    ncols = 52
    nrows = 55
    output_root = r"../test_output_data/grid_rasters"
    filename = os.path.split(metric_file)[1]
    split_filename = filename.split(" ")
    dataset = get_dataset_name(filename)
    timefilter = split_filename[-2]
    anomaly_str = filename.split(" ")[-3]
    output_folder = os.path.join(output_root, dataset)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 11.375, 52 columns
    # 55.125, 55 rows
    xllcorner = 11.25
    yllcorner = 55.25
    cellsize = 0.25
    NODATA_value = -9999
    metrics = ["pearson_r", "bias", "ubrmsd"]
    mf = pd.read_csv(metric_file)
    for metric in metrics:
        df = mf.copy()
        asciif = start_ascii_file()
        values = [NODATA_value] * (nrows * ncols)
        if metric == "pearson_r":
            df = df[df["pearson_r_p-value"] < 0.05]
        else:
            df[metric].replace('', np.nan, inplace=True)
            df = df[['lat', 'lon', metric]]
            df = df.dropna()
        for index, row in df.iterrows():
            lat = row['lat']
            lon = row['lon']
            value = row[metric]
            gridi = get_quarter_grid_coord_index(lat=lat, lon=lon)
            values[gridi] = value
        for value in values:
            asciif.write("{} ".format(value))
        asciif.close()


in_dir = r"..\input_data\grid_evaluation_data\all_metrics"
files = [os.path.join(in_dir, filename) for filename in os.listdir(in_dir)]
for file in files:
    write_grid_ascii_raster(file)