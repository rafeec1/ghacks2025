import numpy as np
import matplotlib.pyplot as plt

# location "C:\Users\Owner\Desktop\Gesture Recognition\ghacks2025\data1.csv"
# file = open("C:\\Users\\Owner\\Desktop\\Gesture Recognition\\ghacks2025\\data1.csv", "r")
# print(file.read())

arr = np.loadtxt("C:\\Users\\Owner\\Desktop\\Gesture Recognition\\ghacks2025\\data1.csv",
                 delimiter=",")
print(arr)

axis = plt.axes(projection='3d')


#x = 
#y =
#z =

#axis.scatter(x, y, z)
#axis.set_title("3D plot of land")
#axis.set_xlabel("x-coordinate")
#axis.set_ylabel("y-coordinate")
#axis.set_zlabel("z-coordinate")

