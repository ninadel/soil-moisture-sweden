# from numpy import cov
import os
import pandas
import geopandas
from shapely.geometry import Point
import sys
import matplotlib
# from pytesmo.time_series.anomaly import calc_anomaly
# from pytesmo.time_series.anomaly import calc_anomaly
sys.path.append('../python')
sys.path.append('../../icos_data')
sys.path.append('../../ismn_data\HOBE_Data_2015-2018')
import sm_config as config
import sm_tools as tools
import sm_triplecollocation

def get_filenames(path_to_dir, suffix=".csv"):
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

def get_basemap(f, color="white", edgecolor="silver", figsize=(9,6)):
    base = geopandas.read_file(f)
    plot = base.plot(color=color, edgecolor=edgecolor, figsize=figsize)
    return plot

# grid evaluation metrics
def grid_metrics_output(grid_metrics_dir, output_dir, base_shp, include_months=False, metric="pearson_r", cutoff=100,
                        map_legend=True, round=True):
    m_dir = os.path.join(output_dir, "metrics", metric)
    if not os.path.exists(m_dir):
        os.makedirs(m_dir)
    base = get_basemap(base_shp)
#     sweden = geopandas.read_file(r"../basemap/SWE_adm0.shp")
    # sweden_shape.boundary.plot()
#     sweden = sweden_shape.plot(color='white', edgecolor='silver')
#     base = sweden.plot(color='white', edgecolor='silver', figsize=(9,6))
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    grid_metrics_csvs = get_filenames(grid_metrics_dir)
    for fn in grid_metrics_csvs:
        pn = fn.replace(" metrics.csv", "")
        pn_dir = os.path.join(output_dir, "products", pn)
        if not os.path.exists(pn_dir):
            os.makedirs(pn_dir)
        f = os.path.join(grid_metrics_dir, fn)
        df = pandas.read_csv(f)
        df = df[['lon', 'lat', 'anomaly', 'timefilter', metric, 'pearson_sig']]
        # filter out insignificant and non-anomaly rows
        df_sub = df[(df.pearson_sig) & (df.anomaly == True)]
        # filter df_sub by timefilter values
        tfs = [tf for tf in df.timefilter.unique() if tf != "all"]
        if not include_months:
            tfs = [tf for tf in tfs if "M" not in tf]
        for timefilter in tfs:
#             matplotlib.pyplot.clf()
#         if timefilter == "No-Timefilter":
            tf_dir = os.path.join(output_dir, "timefilters", timefilter)
            if not os.path.exists(tf_dir):
                os.makedirs(tf_dir)
            df_tf = df_sub[df.timefilter == timefilter]
            # create and output map
            gm_geo = [Point(xy) for xy in zip(df_tf.iloc[:, 0], df_tf.iloc[:, 1])]
            gm_gdf = geopandas.GeoDataFrame(df_tf, geometry=gm_geo)
#             print(gdf)
            # suppressing legend for now because otherwise it is outputting multiple legends
#             gm_gdf.plot(column=metric)
#             gm_gdf.plot(ax=base, column=metric, figsize=(6,6))
            if map_legend:
                gm_gdf.plot(ax=base, column=metric, legend=True, legend_kwds={'label': "{}".format(metric)}, figsize=(9,6))
                map_legend = False
            else:
                gm_gdf.plot(ax=base, column=metric, figsize=(9,6))
            matplotlib.pyplot.suptitle("{} x ERA5 ({}: {})".format(pn, timefilter, metric))
            # save one copy of figure in timeframe subdirectory
            matplotlib.pyplot.savefig(os.path.join(tf_dir, "{} {} {}.jpg".format(pn, timefilter, metric)))
            # save one copy of figure in product name subdirectory
            matplotlib.pyplot.savefig(os.path.join(pn_dir, "{} {} {}.jpg".format(pn, timefilter, metric)))
            # save one copy of figure in metric subdirectory
            matplotlib.pyplot.savefig(os.path.join(m_dir, "{} {} {}.jpg".format(pn, timefilter, metric)))
#             gm_gdf.plot(ax=base, column=metric, legend=None, legend_kwds={'label': " R (p < 0.05)"}, figsize=(6,6))
#             matplotlib.pyplot.clf()
#             matplotlib.axes.Axes.get_legend().remove()

def tc_metrics_output(csv, output_dir, base_shp, metric="r", cutoff=100, map_legend=True, round=True):
    base = get_basemap(base_shp)
#     sweden = geopandas.read_file(r"../basemap/SWE_adm0.shp")
    # sweden_shape.boundary.plot()
#     sweden = sweden_shape.plot(color='white', edgecolor='silver')
#     base = sweden.plot(color='white', edgecolor='silver', figsize=(9,6))
    df = pandas.read_csv(csv)
    df = df[df.n >= cutoff]
    df = df[['lon', 'lat', 'prod_name', 'triplet', metric]]
    # print(df)
#     print(df.shape)
    df.dropna(inplace=True)
#     print(df.shape)
    triplets = df.triplet.unique()
#     print(triplets)
#     print(df.prod_name)
#     print(pns)
#     map_legend = True
    for t in triplets:
        # ('SMAP L3 Enhanced', 'ERA5 0-1', 'ASCAT 12.5 TS')
        t_str = t.replace("('", "").replace("')", "").replace("', '", "_")
        df_t = df[df.triplet == t]
#         print(df_t.head())
        pns = df_t.prod_name.unique()
        for pn in pns:
            output_subdir = os.path.join(output_dir, t_str)
#             print(output_subdir)
            if not os.path.exists(output_subdir):
                os.makedirs(output_subdir)
            df_p = df_t[df_t.prod_name == pn]
            df_p = df_p[~df_p[metric].str.contains('i')]
            df_p[metric] = df_p[metric].astype(float)
            df_p = round_dataframe(df_p, metric)
            # create and output map
#             print("df p")
#             print(df_p.shape)
#             print(df_p.head())
#             print(df_p.iloc[:, lon])
#             print(df_p.iloc[:, lat])
            tc_geo = [Point(xy) for xy in zip(df_p.iloc[:, 0], df_p.iloc[:, 1])]
#             print(len(geometry))
#             print(geometry)
            tc_gdf = geopandas.GeoDataFrame(df_p, geometry=tc_geo)
#             print(gdf)
            # suppressing legend for now because otherwise it is outputting multiple legends
#             print(df_p.r)
#             tc_gdf.plot(column=metric)
#             tc_gdf.plot(ax=base, column=metric, figsize=(6,6))
#             tc_gdf.plot(ax=base, column=metric, figsize=(6,6))
            if map_legend:
                print("map_legend ", map_legend)
                tc_gdf.plot(ax=base, column=metric, legend=True, legend_kwds={'label': "{}".format(metric)}, figsize=(9,6))
                # tc_gdf.plot(ax=base, column=metric, legend=True, figsize=(9,6))
                map_legend = False
            else:
                print("map_legend ", map_legend)
                tc_gdf.plot(ax=base, column=metric, figsize=(9,6))
                # tc_gdf.plot(ax=base, column=metric, legend=True, figsize=(9, 6))
            # legend_kwds is not working here
            # tc_gdf.plot(ax=base, column=metric, legend=True, legend_kwds={'label': "R"}, figsize=(9,6))
            matplotlib.pyplot.suptitle("{} ({})".format(pn, metric))
            # save figure in subdirectory
            matplotlib.pyplot.savefig(os.path.join(output_subdir, "{} {}.jpg".format(pn, metric)))

def tc_matlab2pandas(in_csv, dict):
    df = pandas.read_csv(in_csv)
    new_df = pandas.DataFrame(
        columns=['location', 'lat', 'lon', 'location_veg_class', 'prod_name', 'triplet',
                 'anomaly', 'n', 'err_std', 'r'])
    for index, row in df.iterrows():
        location = str(row['location'])
        lat = dict[location]['latitude']
        lon = dict[location]['longitude']
        location_veg_class = dict[location]['veg_class_name']
        prod_name = row['prod_name']
        triplet = row['triplet']
        anomaly = row['anomaly']
        n = row['n']
        err_std = row['err_std']
        r = row['r']
        new_df = new_df.append(
            {'location': location, 'lat': lat, 'lon': lon, 'location_veg_class': location_veg_class,
             'prod_name': prod_name, 'triplet': triplet, 'anomaly': anomaly, 'n': n, 'err_std': err_std,
             'r': r}, ignore_index=True)
    return new_df

def round_dataframe(df, column):
    # mask = (df['Qty'] == 1) & (df['Price'] == 10)
    # df.loc[mask, 'Buy'] = 1
    aboveOne = df[column] > 1
    df.loc[aboveOne, column] = 1
    belowNegOne = df[column] < -1
    df.loc[belowNegOne, column] = -1
    return df

# "C:\git\soil-moisture-sweden\metrics\grid_evaluation\CSV"
grid_metrics_dir = r"../metrics/grid_evaluation/CSV"
grid_map_output_dir = r"../analysis_output/grid_evaluation_maps"
sweden_shp = r"../basemap/SWE_adm0.shp"

# def grid_metrics_output(grid_metrics_dir, output_dir, base_shp, include_months=False, metric="pearson_r", cutoff=100,
#                         map_legend=True, round=True):
# grid_metrics_output(grid_metrics_dir, grid_map_output_dir, sweden_shp, metric="pearson_r")
# grid_metrics_output(grid_metrics_dir, grid_map_output_dir, sweden_shp, metric="bias")
# grid_metrics_output(grid_metrics_dir, grid_map_output_dir, sweden_shp, metric="rmsd")
# grid_metrics_output(grid_metrics_dir, grid_map_output_dir, sweden_shp, metric="ubrmsd")

# tc_matlab_csv = r"C:\git\soil-moisture-sweden\analysis_output\tc_analysis_20210314104637\tc_matlab_results.csv"

# print(dict_swe_gldas_points)
# with open("dict_icos.json", "r") as f:
#     dict_icos = json.load(f)

tc_map_output_dir = r"../analysis_output/tc_evaluation_maps_Sentinel"
os.makedirs(tc_map_output_dir)
input_dir = r"C:\git\soil-moisture-sweden\analysis_output\tc_matched_data_Sentinel_20210425"
pandas_output_dir = r"C:\git\soil-moisture-sweden\analysis_output\tc_matched_data_Sentinel_20210425\pandas"
os.makedirs(pandas_output_dir)

csv_list = ["tc_SMAP L3 Enhanced_Sentinel-1_ERA5 0-1_absolute.csv",
            "tc_SMAP L3 Enhanced_Sentinel-1_ERA5 0-1_anomaly.csv",
            "tc_SMOS-IC_Sentinel-1_ERA5 0-1_absolute.csv",
            "tc_SMOS-IC_Sentinel-1_ERA5 0-1_anomaly.csv"]


for csv in csv_list:
    subdir = csv.replace(".csv", "")
    print(csv)
    file = os.path.join(input_dir, csv)
    tc_matlab_df = tc_matlab2pandas(file, config.dict_swe_gldas_points)
    pandas_csv = os.path.join(pandas_output_dir, csv)
    tc_matlab_df.to_csv(pandas_csv)
    tc_metrics_output(pandas_csv, os.path.join(tc_map_output_dir, subdir), sweden_shp, metric="r", cutoff=100)
    # tc_metrics_output(pandas_csv, tc_map_output_dir, sweden_shp, metric="err_std", cutoff=100)

# tc_matlab_df = tc_matlab2pandas(tc_matlab_csv, config.dict_swe_gldas_points)
# # print(tc_csv)
# tc_matlab_df.to_csv(
#     r"C:\git\soil-moisture-sweden\analysis_output\tc_analysis_20210314104637\tc_matlab_pandas_results.csv", index=False)
# tc_metrics_output(
#     r"C:\git\soil-moisture-sweden\analysis_output\tc_analysis_20210314104637\tc_matlab_pandas_results.csv",
#     tc_map_output_dir, sweden_shp, metric="r", cutoff=100)