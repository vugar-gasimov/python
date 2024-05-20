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

# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# temp_json = data["temp"].to_json()
# print(temp_json)
# amount_of_numbers = len(temp_list)
# all_numbers = sum(temp_list)
# # average_number = round(all_numbers / amount_of_numbers, 2)
# # average_number = round(all_numbers / amount_of_numbers)
# average_number = f"{all_numbers / amount_of_numbers:.2f}"
# print(average_number)

# # Or ===================
# # for number in temp_list:
# #     all_numbers += number
# Or ===================
# average = round(sum(temp_list) / len(temp_list), 2) 
# print(average)
# Or ===================
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
# print(data["temp"].sum())

# print(data["condition"])
# # Or
# print(data.condition)

# Get data in row
# print(data.loc[data["temp"].idxmax()])
# print(data[data.day == "Monday"])
# print(data[data.temp == 24])
# max_idx = data.temp.idxmax()
# print(data[data.index == max_idx])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# monday_temp_celsius = monday.temp
# monday_fahrenheit = (monday_temp_celsius * 9 / 5) + 32
# print(monday_fahrenheit)

# Create a data frame from scratch
data_dict = { 
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.scv")