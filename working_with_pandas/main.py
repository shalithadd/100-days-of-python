import pandas

# data = pandas.read_csv('weather_data.csv')
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(data.temp.max())
# print(data['temp'].max())
#
# # Get data in columns
# print(data.condition)

# Get data in row
# # print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# f_temp = (monday.temp * 1.8) + 32
# print(monday.temp)
# print(f_temp)

# Create datafram from scratch
# data_dict = {'Students': ['Dinu', 'Shalu', 'Maalu'],
#              'Grades': [75, 65, 72],
#              }
# my_data = pandas.DataFrame(data_dict)
# print(my_data)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Colour': ['Gray', 'Red', 'Black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}
squirrel_fur_data = pandas.DataFrame(data_dict)
squirrel_fur_data.to_csv('squirrel_fur_data')
