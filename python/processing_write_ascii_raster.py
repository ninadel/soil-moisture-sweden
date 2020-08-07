import os
output_root = r"../test_output_folder"
ncols = 52
nrows = 55
# 11.375, 52 columns
# 55.125, 55 rows
ncols = 52
nrows = 55
xllcorner = 11.25
yllcorner = 55.25
cellsize = 0.25
NODATA_value = -9999


def get_coord_index(lat, lon):
    lon0 = 11.375
    lat0 = 55.375
    lats = [lat0 + (0.25 * i) for i in range(0, nrows)]
    lats.sort(reverse=True)
    lons = [lon0 + (0.25 * i) for i in range(0, ncols)]
    lati = lats.index(lat)
    loni = lons.index(lon)
    index = (lati * ncols) + loni
    return index

# ascii_dict = {}
# counter = 0
# for lat in lats:
#     for lon in lons:
#         ascii_dict[(lat,lon)] = counter
#         counter += 1
#
# print(ascii_dict)
# print(len(ascii_dict.keys()))

# ncols         52
# nrows         55
# xllcorner     11.25
# yllcorner     55.25
# cellsize      0.25
# NODATA_value  -9999

# values = [-9999] * nrows * ncols
# print(len(values))
# print(get_coord_index(55.375, 11.375))
# print(get_coord_index(68.875, 11.375))
# print(get_coord_index(68.625, 11.375))
# print(get_coord_index(68.625, 11.625))

dataset_name = "GLDAS"
metrics = ["pearson_r",	"pearson_r_p-value", "bias", "rmsd", "ubrmsd"]
in_file = r"\\DESKTOP-J6H9VE7\SM_Data_ReadOnly\grid_evaluation_data\GLDAS ERA5 0-1 absolute\GLDAS ERA5 0-1 absolute all metrics.csv"


out_filename = ""
f = (os.path.join(output_root, "{}_{}.asc".format(dataset_name, metric)))
asciif=open(f,"w")
asciif.write("ncols {}\n".format(ncols))
asciif.write("nrows {}\n".format(nrows))
asciif.write("xllcorner     {}\n".format(xllcorner))
asciif.write("yllcorner     {}\n".format(yllcorner))
asciif.write("cellsize      {}\n".format(cellsize))
asciif.write("NODATA_value  {}\n".format(NODATA_value))
# for i in list, write "value " (without linebreak)
# test by overlaying with arcmap generated file
# for each metrics file
    # open table
    # get evaluation dataset name
    # get timefilter
    # filter table to significnt values
    # for each metric column
        # write data
        # save to asc file: e.g. dataset_{pearsonr/bias/ubRMSE}_timeframe.asc
