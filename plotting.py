import numpy as np
import matplotlib.pyplot as plt
<<<<<<< HEAD
from matplotlib import style
=======
import pandas as pd
>>>>>>> 0385c521c610988e98277767c45d795c63cb7484

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\Gesture Recognition\\ghacks2025\\data1.csv")
data_array = df.to_numpy()
print(data_array)
print(data_array[5][5])




axis = plt.axes(projection='3d')

x = 
y =
z =

axis.scatter(x, y, z)
axis.set_title("3D plot of land")
axis.set_xlabel(x-coordinate)
axis.set_ylabel(y-coordinate)
axis.set_zlabel(z-coordinate)

plt.show()