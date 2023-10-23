# Python
# Author : wsyzbsj@gmail.com
# Date : 22 Oct. 2023

import netCDF4
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置


# Read nc File
NcFile = netCDF4.Dataset('/home/yzbsj/mega/mega/ERA5/2023/Oct/01-Global/adaptor.mars.internal-1697354388.8651552-541-7-d82c1dec-98a1-4a42-be3d-6340efa3cbd7.nc','r')
Latitude = NcFile.variables['latitude'][:].data
Longitude = NcFile.variables['longitude'][:].data
Time = NcFile.variables['time'][:].data
Level = NcFile.variables['level'][:].data


# Variable ( time, level, latitude, longitude )
Geopotential_Height = NcFile.variables['z'][:].data
Relative_Humidity = NcFile.variables['r'][:].data
Humidity_Ratio = NcFile.variables['q'][:].data
Air_Temperature = NcFile.variables['t'][:].data


# Draw plots
plt.figure(figsize = (30,20),dpi=600)
m = Basemap(projection='lcc',lat_0=45,lon_0=150,llcrnrlon=120,llcrnrlat=25,urcrnrlon=180,urcrnrlat=65,resolution='f')
m.drawcoastlines(linewidth=1.0, linestyle='solid', color='grey')
m.fillcontinents()

lons, lats = np.meshgrid(Longitude, Latitude)
xi, yi = m(lons, lats)
m.contourf(xi,yi,Air_Temperature[1,7,:,:])
parallels = np.arange(0.,91.,5.)
m.drawparallels(parallels,labels=[1,1,0,0],fontsize=20)
meridians = np.arange(0.,181,5.)
m.drawmeridians(meridians,labels=[0,0,1,1],fontsize=20)
plt.savefig('1.png')

