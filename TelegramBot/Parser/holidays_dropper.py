import pandas as pd
import datetime
import parsing 

path_to_data = 'TelegramBot/Data/AllHolidays.csv'
date_list = parsing.date_list

data = pd.read_csv(path_to_data)
day_name = '{0:0>2}'.format(str(date_list[0]))
month_name = '{0:0>2}'.format( str( parsing.months.index(date_list[1]) + 1 ) )
date_name = f'{day_name}/{month_name}'
holidays = data[date_name]
output_celebrates = parsing.formatting_all_celebrates(holidays)
print(holidays)