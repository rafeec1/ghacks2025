import csv

with open('C:\Users\Owner\Desktop\Gesture Recognition\ghacks2025\Console_2025-02-22_12-31-51_data1.csv','r') as file:
    coordinates_array = csv.reader(file)

print(coordinates_array[5][4])