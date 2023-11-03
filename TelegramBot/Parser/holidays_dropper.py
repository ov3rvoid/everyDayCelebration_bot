import pandas as pd
from .parsing import formatting_all_celebrates
from datetime import datetime

path_to_data = 'Data/AllHolidays.csv'

newdate = datetime.now()
newdate = newdate.strftime("%d.%m.%Y")
date_list = newdate.split('.')

data = pd.read_csv(path_to_data, sep=';')
date_name = f'{date_list[0]}/{date_list[1]}'
holidays = data[date_name]
holidays = holidays[holidays.notnull()]
output_celebrates = formatting_all_celebrates(holidays)