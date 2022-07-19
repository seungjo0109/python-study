import csv
from numpy import average
import pandas

# with open("./data/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# with open("./data/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     print(data)
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)

data = pandas.read_csv("./data/weather_data.csv")
# print(data)
# print(data.temp)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# temp_average = data["temp"].mean()
# temp_max = data["temp"].max()
# print(temp_list)
# print(average(temp_list))   # sum(temp_list) / len(temp_list)
# print(temp_average)
# print(temp_max)

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in rows
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp_F = monday.temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Jane", "Mike", "David"],
    "scores": [80, 90, 100]
}

student_data = pandas.DataFrame(data_dict)
print(student_data)
student_data.to_csv("./data/student_data.csv")