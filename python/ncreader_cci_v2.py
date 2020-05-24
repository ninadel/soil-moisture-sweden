# function to find index to nearest point
def near(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx

import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from scipy import spatial
from datetime import datetime, timedelta
nc_f = r'C:\git\soil-moisture-sweden\sm_sample_files\NordicESACCICombined2014to2019\ClipESACCICombined2015.nc'
nc_fid = netCDF4.Dataset(nc_f, 'r')
# print(nc_fid.variables)

# Coordinates of the station you want to extract
loni = 19.556539
lati = 64.182029

lat_ = nc_fid.variables['lat'][:]
lon_ = nc_fid.variables['lon'][:]
times = nc_fid.variables['time']
jd = netCDF4.num2date(times[:], times.units)

# find nearest point to desired location
ix = near(lon_, loni)
iy = near(lat_, lati)
# print(ix)
# print(iy)


# get all time records of variable [vname] at indices [iy,ix]
vname = 'sm'
var = nc_fid.variables[vname]
print(var)

h = var[:, iy, ix]

for time in jd:
    print(time)
# print(h)
# print(len(h))

# plt.figure(figsize=(16,4))
# plt.plot_date(jd, h, fmt='-')
# plt.grid()
# plt.ylabel(var.units)
# plt.title('%s at Lon=%.2f, Lat=%.2f' % (vname, lon_[ix], lat_[iy]))