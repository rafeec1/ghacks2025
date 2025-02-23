import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd





def average(data1):
    latitude_average_num = 0
    longitude_average_num = 0
    height_average_num = 0

    average_latitude = []
    average_longitude = []
    average_height = []

    for i in range(0, len(data1)-10, 10):
        for j in range(10):
            latitude_average_num += data1[i+j][11]
            longitude_average_num += data1[i+j][12]
            height_average_num += data1[i+j][13]
         
        average_latitude.append(latitude_average_num / 10)
        average_longitude.append(longitude_average_num / 10)
        average_height.append(height_average_num / 10)

        # resets values for average to 0
        latitude_average_num = 0
        longitude_average_num = 0
        height_average_num = 0
    return average_latitude, average_longitude, average_height

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\Gesture Recognition\\ghacks2025\\LatLongHeightdata.csv")
data_array = df.to_numpy()


lat, longg, height = average(data_array)

adjusted=0
height_copy = height[:]
for i in range(len(height)):
    if (height[i] <=1105 or height[i]>= 1125):
        height_copy.pop(i-adjusted)
        longg.pop(i-adjusted)
        lat.pop(i-adjusted)
        adjusted+=1


def plotData():
    
axis = plt.axes(projection='3d')
    
axis.scatter(lat, longg, height_copy, alpha = 0.5)

# constants for plotting latitude
min_lat = min(lat)
max_lat = max(lat)
lat_interval = (max_lat - min_lat) / 5
lat_labels = np.arange(min_lat, max_lat, lat_interval)

# constants for plotting longitude
min_longg = min(longg)
max_longg = max(longg)
longg_interval = (max_longg - min_longg) / 5
longg_labels = np.arange(min_longg, max_longg, longg_interval)

# building the plot
axis.set_title("3D plot of land")

axis.set_xlabel("latitude", labelpad=20)
axis.set_xticks(lat_labels)

axis.set_ylabel("longitude", labelpad=20)
axis.set_yticks(longg_labels)

axis.set_zlabel("altitude (m)", labelpad=20)
axis.set_zlim(1000, 1150)








plt.show()