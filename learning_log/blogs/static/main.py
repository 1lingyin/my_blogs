import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from  matplotlib.pyplot import savefig


m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100)
m.drawcountries(linewidth=2)
m.readshapefile('shape_flie/gadm36_CHN_1', 'states', drawbounds=True)

savefig('image_1.png',dpi=1000)
