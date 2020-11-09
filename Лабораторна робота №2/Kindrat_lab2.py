import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', 50)

def get_sum_data(line, region_names, setting):
    values = []
    values2 = []
    for i in region_names:
        values2.append([i, covid_data.loc[covid_data['registration_area'] == i][line].sum()])
        values.append(covid_data.loc[covid_data['registration_area'] == i][line].sum())

    if setting == 'dict':
        return values2
    else:
        return values

def data_sun(data):
    new_date = {}
    dates = sorted(set(data['zvit_date']))
    for date in dates:
        new_date[date] = data.loc[data['zvit_date'] == date].sum()
    return new_date


def data_visualisation(data, plot_type):
    all_dates = data.keys()
    data_set_names = {'new_susp': 'Нові підозри', 'new_confirm': 'Нові захворювання',
                      'active_confirm': 'Хворих', 'new_death': 'Нові смерті', 'new_recover': 'Одужало'}

    for names in data_set_names:
        data_set = []
        for i in data:
            data_set.append(data.get(i)[names])
        plt.plot(all_dates, data_set, label=data_set_names.get(names))
        if  plot_type.lower() == "multiple":
            plt.xlabel('DATES')
            plt.ylabel('INFO')
            plt.title("COVID-19 IN TERNOPIL")
            plt.legend()
            plt.show()

    if plot_type.lower() != "multiple":
        plt.xlabel('DATES')
        plt.ylabel('INFO')
        plt.title("COVID-19 IN TERNOPIL")
        plt.legend()
        plt.show()


def analisys(data, plot_type):
    region_names = ['Київська', 'Львівська', 'Житомирська', 'Миколаївська', 'Хмельницька', 'Тернопільська', 'Одеська',
                    'Закарпатська', 'Вінницька', 'Чернігівська', 'Волинська', 'Кіровоградська', 'Івано-Франківська',
                    'Чернівецька', 'Донецька']
    for region in region_names:
        data_set = []
        region_data = covid_data.loc[data['registration_area'] == region]
        sorted_region_data = data_sun(region_data)
        all_dates = sorted_region_data.keys()
        for i in sorted_region_data:
            data_set.append(sorted_region_data.get(i)['active_confirm'])
        plt.plot(all_dates, data_set, label=region)
        if  plot_type.lower() == "multiple":
            plt.xlabel('DATES')
            plt.ylabel('INFO')
            plt.title("COVID-19 IN UKRAINE")
            plt.legend()
            plt.show()

    if plot_type.lower() != "multiple":
        plt.xlabel('DATES')
        plt.ylabel('INFO')
        plt.title("COVID-19 IN UKRAINE")
        plt.legend()
        plt.show()

covid_data = pd.read_csv("covid19_by_settlement_dynamics.csv", delimiter=",")
ternopil_data = covid_data.loc[covid_data['registration_area'] == 'Тернопільська']

sorter_by_date_data =  data_sun(ternopil_data)

func_type = input('Input plot type: \nSingle\nMultiple\n')

data_visualisation(sorter_by_date_data, func_type)
analisys(covid_data, func_type)
death_count = get_sum_data('active_confirm', set(covid_data['registration_area']), 'dict')
new_data = pd.DataFrame(death_count, columns=["region_name", "all_confirmed"])
new_data.to_csv('analysis_data.csv', encoding = 'utf-8')

#-------------------
Ukraine = gpd.read_file('ukr_admbnda_adm1_q2_sspe_20171221.shp', encoding = 'utf-8')
Ukraine_data = get_sum_data('active_confirm', Ukraine['ADM1_UA'], 'list')
Ukraine['adm1Clas'] = Ukraine_data
print(Ukraine)

fig, ax = plt.subplots(1, 1)
Ukraine.plot(column = 'adm1Clas',ax=ax, legend=True, cmap='OrRd')
plt.show()