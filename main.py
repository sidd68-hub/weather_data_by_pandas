import pandas

# data = pandas.read_csv("weather_data.csv")


# # data_dic = data.to_dict()



# # temp_list = data['temp'].to_list()


# # average = data['temp'].mean()
# # print(average)

# # largest_number = data['temp'].max()
# # print(f"Largest: {largest_number}")

# # average = data['temp'].max()
# # print(data[data.temp == data.temp.max()])

# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp_F = monday_temp * 9/5 +32
# # print(monday_temp_F)


# data_dic = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }

# data = pandas.DataFrame(data_dic)
# print(data)


data = pandas.read_csv("squirrel_data.csv")

data_dic = data.to_dict()
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])


data_dic = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray,black,cinnamon]
}

df = pandas.DataFrame(data_dic)
df.to_csv('squirrel_count.csv')