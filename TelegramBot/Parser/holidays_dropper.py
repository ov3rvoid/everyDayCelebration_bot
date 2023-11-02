import pandas as pd
import parsing as prs

path_to_data = 'TelegramBot/Data/AllHolidays.csv'
date_list = prs.date_list


data = pd.read_csv(path_to_data, sep=';')
date_name = f'{date_list[0]}/{date_list[1]}'
holidays = data[date_name]
holidays = holidays[holidays.notnull()]
output_celebrates = prs.formatting_all_celebrates(holidays)