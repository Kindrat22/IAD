import pandas as pd
from datetime import datetime
import Kindrat1


def time_parser(time):
    return datetime.strptime(time, '%I:%M %p').strftime('%H:%M')


def date_parser(date):
    return datetime.strptime(date, '%d.%b').strftime('%d-%m-2019')


def parser(data):
    for row in range(len(data)):
        data["Time"][row] = time_parser(data["Time"][row])
        data["day/month"][row] = date_parser(data["day/month"][row])
        data["Humidity"][row] = int(data["Humidity"][row].replace('%', ''))
        data["Wind Speed"][row] = int(data["Wind Speed"][row].replace(' mph', ''))
        data["Wind Gust"][row] = int(data["Wind Gust"][row].replace(' mph', ''))
    return data


pd.set_option('display.max_columns', 15)
df = parser(pd.read_csv("DATABASE.csv", delimiter=";"))
print("Write names of graphs you want to show:")
names_list = str(input()).split(', ')
print("Write names of graphs you want to plot by")
by_set = str(input())
Kindrat1.build_schedule(df, names_list, by_set)


