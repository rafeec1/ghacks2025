import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

def average(data1):
    """ Function takes in a numpy array of all collected data, and returns the average of every 10 data points to three dedicated lists
        In this case, returns the average value of latitude, longitude, and height from receiver data.
        Parameters:
            data1 (numpy array): 
                an array containing data collected from the Hexagon receiver using "log psrposa ontime 0.2"

        Returns:
            average_latitude (list): 
                list containing averaged latitude data.

            average_longitude (list): 
                list containing averaged longitude data.

            average_height (list): 
                list containing averaged height data.

    """
    latitude_average_num = 0        # initializing average sums to zero
    longitude_average_num = 0
    height_average_num = 0

    average_latitude = []           # lists for averaged data
    average_longitude = []
    average_height = []

    for i in range(0, len(data1)-1, 1):               # looping through every 10 lines from data1               
        for j in range(2):                             
            latitude_average_num += data1[i+j][11]      # adds every consecutive latitude point up til 10
            longitude_average_num += data1[i+j][12]     # same for longitude and height
            height_average_num += data1[i+j][13]
         
        average_latitude.append(latitude_average_num / 1)      # calculating mean latitude and adds it to the average lat list
        average_longitude.append(longitude_average_num / 1)    # same for long and height
        average_height.append(height_average_num / 1)

        latitude_average_num = 0                        # resets sum to find the next mean values 
        longitude_average_num = 0
        height_average_num = 0
    return average_latitude, average_longitude, average_height

def remove_outliers(lat, longg, height):
    """ Takes in averaged data and removes any heights that are obvious outliers (less than 1105 or greater than 1125 m)
        Parameters:
            lat (list): list containing average latitudes
            longg (list): list containing average longitudes
            height (list): list containing average heights
        
        returns:
            lat (list): 
            longg (list):
            height_copy (list):
            same lists but outlier data removed
    """

    adjusted=0                                          # counter
    height_copy = height[:]                             # makes copy of height to remove values from
    for i in range(len(height)):                        # iterates over original height list
        if (height[i] <=0 or height[i]>= 11250000):      # outliers defined here
            height_copy.pop(i-adjusted)                 # pops the outlying point from each data list
            longg.pop(i-adjusted)
            lat.pop(i-adjusted)
            adjusted+=1                                 # counter goes up to account for index change
    
    return lat, longg, height_copy

def plot_data(lat, longg, height):
    """ plots and shows a 3D scatter plot of given spacial data using matplotlib
        Parameters:
            lat (list): list of latitude data
            longg (list): list of longitude data
            height (list): list of height data
        Returns:
            None 
    """
    

    min_lat = min(lat)                      # constants for plotting latitude
    max_lat = max(lat)
    lat_interval = (max_lat - min_lat) / 5
    lat_labels = np.arange(min_lat, max_lat, lat_interval)

    min_longg = min(longg)                  # constants for plotting longitude
    max_longg = max(longg)
    longg_interval = (max_longg - min_longg) / 5
    longg_labels = np.arange(min_longg, max_longg, longg_interval)

    # building the plot
    axis = plt.axes(projection='3d')    
    axis.scatter(lat, longg, height, alpha = 0.5)

    axis.set_title("3D plot of land")
    axis.set_xlabel("latitude", labelpad=20)
    axis.set_xticks(lat_labels)
    axis.set_ylabel("longitude", labelpad=20)
    axis.set_yticks(longg_labels)
    axis.set_zlabel("altitude (m)", labelpad=20)
    # axis.set_zlim(1000, 1150)

    plt.show()

def main(positional_data):
    """ program that plots positional data from a Hexagon GNSS receiver in a graphic.
        Parameters:
            positional_data (string): a csv file with data from a GNSS receiver
        Returns:
            a matplotlib plot
    """
    df = pd.read_csv(positional_data)
    data_array = df.to_numpy()
    lat, longg, height = average(data_array)
    cleaned_lat, cleaned_longg, cleaned_height = remove_outliers(lat, longg, height)
    plot_data(cleaned_lat, cleaned_longg, cleaned_height)

if __name__ == '__main__':
    main("C:\\Users\\Owner\\Desktop\\Gesture Recognition\\ghacks2025\\XYZdata.csv")
