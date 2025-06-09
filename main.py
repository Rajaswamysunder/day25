# with open("weather_data .csv") as read_file :
#     data = read_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data .csv") as data_file :
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data .csv")
# print((type(data)))
#
# data_dist = data.to_dict()
# print(data_dist)
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].max())
# print(data["temp"])

max_temp = data["temp"].max()
print(data[data.temp == data.temp.max()])