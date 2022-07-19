from re import S
import pandas

squirrel_data = pandas.read_csv("./data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data)

grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Grey"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(f"Cinnamon squirrel count: {grey_squirrels_count}")
print(f"Cinnamon squirrel count: {cinnamon_squirrels_count}")
print(f"Black squirrel count: {black_squirrels_count}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("./data/squirrel_count.csv")