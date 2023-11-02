import pandas as pd
from .parsing import date_list, formatting_all_celebrates


path_to_data = 'Data/AllHolidays.csv'
date_list = date_list


data = pd.read_csv(path_to_data, sep=';')
date_name = f'{date_list[0]}/{date_list[1]}'
holidays = data[date_name]
holidays = holidays[holidays.notnull()]
output_celebrates = formatting_all_celebrates(holidays)