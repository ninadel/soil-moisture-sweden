import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from scipy import spatial
from datetime import datetime, timedelta
nc_f = r'C:\git\soil-moisture-sweden\sm_sample_files\NordicESACCICombined2014to2019\ClipESACCICombined2015.nc'
nc_fid = netCDF4.Dataset(nc_f, 'r')
nc_fid.variables
# Coordinates of the station you want to extract [lon, lat]
stat = [19.556539, 64.182029]
lat_ = nc_fid.variables['lat'][:]
lon_ = nc_fid.variables['lon'][:]

# lon_lat_array = []
#
# for lon in lon_:
#     for lat in lat_:
#         lon_lat_array.append([lon, lat])

# test = zip(lon_.ravel(), lat_.ravel())
# print(tuple(test))
# print(test.shape)
# print('lon_.ravel().shape')
# print(lon_.ravel().shape)
# print('lon_.shape')
# print(lon_.shape)
# print('lat_.ravel().shape')
# print(lat_.ravel().shape)
# print('lat_.shape')
# print(lat_.shape)
# test = np.array(zip(lon_.ravel(), lat_.ravel()))
# # tree = spatial.KDTree(zip(lon_.ravel(), lat_.ravel()))
# # tree = spatial.KDTree(zip(lon_, lat_))
#

# lon_lat_array = np.array(lon_lat_array)
# print(lon_lat_array.shape)

# tree = spatial.KDTree(np.array(lon_lat_array))
tree = spatial.KDTree(zip(lon_.ravel(), lat_.ravel()))

# tree = spatial.KDTree(np.array(zip(lon_.ravel(), lat_.ravel())))
[d,ID] = tree.query(stat)

# Extraction of cci sm 2015 to 2018
datahub = []
for ii in np.arange(2015,2018):
    nc_f = r'C:\git\soil-moisture-sweden\sm_sample_files\NordicESACCICombined2014to2019\ClipESACCICombined' + str(ii) + '.nc'
    nc_fid = netCDF4.Dataset(nc_f, 'r')
    sm = nc_fid.variables['sm'][ID]
    # np.concatenate does not preserve masking of MaskedArray inputs, here np.ma.concatenate is used
    datahub = np.ma.concatenate((datahub, sm), axis=0)

DD = np.arange(datetime(2015,4,1), datetime(2018,12,31), timedelta(days=1)).astype(datetime)
plt.plot(DD,datahub)
plt.ylabel('sm')
plt.title('cci sm lon;lat='+str(stat[0])+';'+str(stat[1]))
plt.show()




