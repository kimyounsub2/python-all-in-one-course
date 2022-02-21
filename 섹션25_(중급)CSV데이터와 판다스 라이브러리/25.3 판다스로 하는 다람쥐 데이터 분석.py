import pandas

#2018_Central_Park_Squirrel_Census_-_Squirrel_Data엑셀시트에 있는 primary fur color열을 분리하자
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


data_dict ={
    "Fur Color": ["grey", "red", "black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data = pandas.DataFrame(data_dict)

data.to_csv("squirrel_count.csv")