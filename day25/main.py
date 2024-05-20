# with open("day25\weather_data.csv", mode="r") as weather_file:
#     weather_data = weather_file.readlines()
    
# print(weather_data)
# import csv
# with open("day25\weather_data.csv", mode="r") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperatures = []
#     for row in weather_data:
#         if row[1].isdigit():
#         # if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)
    
# # print(weather_data)

import pandas
# pip install pandas

data = pandas.read_csv("day25\weather_data.csv")

print(data["temp"])

