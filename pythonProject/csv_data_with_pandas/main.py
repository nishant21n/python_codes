import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

data_list = data["day"].to_list()
print(len(data_list))

temp_list = data["temp"].to_list()
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

panda_avg_temp = data["temp"].mean()
print(panda_avg_temp)

panda_max_temp = data["temp"].max()
print(panda_max_temp)

Get the data in colums
print(data["day"])

print(data.day) # same as above

# how to get data in Row
print(data[data.day == "Monday"])
Result =
      day  temp condition
0  Monday    12     Sunny

print(data[data.temp == data.temp.max()])
print(data[data.temp == 12]) # any day temp or condition can print complete row
sunday = data[data.day == "Sunday"]
sunday_temp = int(sunday.temp)
temp_in_f = (sunday_temp * 1.8) + 32
print(temp_in_f)

# Create a dataframe from scratch
data_dict = {
    "students" : ["Nishant", "Niyanta", "Anjali"],
    "score" : [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")

