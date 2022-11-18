import pandas

# color_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color = color_data["Primary Fur Color"]
#
# gray_color = color_data[fur_color == "Gray"]
# gray_list = gray_color["Primary Fur Color"].to_list()
# gray_count = len(gray_list)
#
# red_color = color_data[fur_color == "Cinnamon"]
# red_list = red_color["Primary Fur Color"].to_list()
# red_count = len(red_list)
#
# black_color = color_data[fur_color == "Black"]
# black_list = black_color["Primary Fur Color"].to_list()
# black_count = len(black_list)
#
# color_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [gray_count, red_count, black_count]
# }
# new_color_csv = pandas.DataFrame(color_dict)
# print(new_color_csv)
# new_color_csv.to_csv("Color_count.csv")
# Above also work like Angela

# By Angela

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_sq_count, red_sq_count, black_sq_count]
}
new_color_csv = pandas.DataFrame(color_dict)
print(new_color_csv)
new_color_csv.to_csv("Color_count_by_Angela.csv")

Result :
  Fur Color  Count
0      Gray   2473
1       Red    392
2     Black    103