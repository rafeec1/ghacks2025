import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\Gesture Recognition\\ghacks2025\\data1.csv")
data_array = df.to_numpy()
print(data_array)
print(data_array[5][5])

