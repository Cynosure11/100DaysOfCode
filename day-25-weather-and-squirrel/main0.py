import pandas

# Read more docs about Pandas library
data = pandas.read_csv("/day-25-weather-and-squirrel/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

# This example to find average temperature
# average = sum(temp_list) / len(temp_list)
# print(average)

print(data["temp"].mean())

print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

# Challenge: Print the row of data which had the highest temp
print(data[data.temp == data.temp.max()])

# Challenge: Show temp on Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp *9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

