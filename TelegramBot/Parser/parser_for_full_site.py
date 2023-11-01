import parsing
import time
from selenium.webdriver.common.by import By
from random import randint
import pandas as pd
import json
import re


url_of_json_date = 'TelegramBot/Parser/dates.json'
main_url = 'https://kakoysegodnyaprazdnik.ru/'
path_for_csv_file = 'TelegramBot/Data/AllHolidays.csv'

class LazyDecoder(json.JSONDecoder):
    def decode(self, s, **kwargs):
        regex_replacements = [
            (re.compile(r'([^\\])\\([^\\])'), r'\1\\\\\2'),
            (re.compile(r',(\s*])'), r'\1'),
        ]
        for regex, replacement in regex_replacements:
            s = regex.sub(replacement, s)
        return super().decode(s, **kwargs)

def filling_the_dict(dict, mx_num):
    final_dict = {}
    for key in dict:
        lst = dict[key]
        lst.extend((mx_num - len(lst)) * [''])
        final_dict[key] = lst
    return final_dict

def mx_len_in_list_dict(dict):
    mx_num = 0
    for key in dict:
        mx_num = max(mx_num, len(dict[key]))
    return mx_num

def generate_nums_days(months):
    nums_days = {}
    for i, month in enumerate(months):
        if i % 2 == 0:
            nums_days[month] = 31
        elif i == 1:
            nums_days[month] = 29
        else:
            nums_days[month] = 30
    return nums_days

def join_new_data(dict_of_celebrates_in_csv, is_here):
    final_dict_of_celebrates_in_csv = {}
    max_numbers_of_celebrates = mx_len_in_list_dict(dict_of_celebrates_in_csv)
    final_dict_of_celebrates_in_csv = filling_the_dict(dict_of_celebrates_in_csv, max_numbers_of_celebrates)
    csv_file = pd.DataFrame(final_dict_of_celebrates_in_csv)
    csv_file.index = range(1, max_numbers_of_celebrates + 1)
    if is_here == 0:
        csv_file.to_csv(path_for_csv_file, sep=';')
    else:
        final_csv_file = pd.read_csv(path_for_csv_file)
        final_csv_file.join(csv_file)
        final_csv_file.to_csv(path_for_csv_file, sep=';')

def update_json_file(day, month):
    with open(url_of_json_date, 'w', encoding='UTF-8') as file_out:
        global last_date
        last_date = [day, month]
        new_file = {
            'last_date': last_date,
            'is_here': 1
        }
        json.dump(new_file, file_out, ensure_ascii=False, indent=2)
    
# with open(url_of_json_date, 'w', encoding='UTF-8') as file_out:
#     data = {}
#     data['last_date'] = [29, 'oktyabr']
#     data['is_here'] = 0
#     json.dump(data, file_out, ensure_ascii=False, indent=2)
# exit()

with open(url_of_json_date, encoding='UTF-8') as file_in:
    data = json.load(file_in, cls=LazyDecoder)
    last_date = data['last_date']
    day = last_date[0]
    month = last_date[1]
    is_here = data['is_here']

months = parsing.months
nums_days = generate_nums_days(months)
fl = 0
browser = parsing.activate_browser_url()
browser.get(f'{main_url}/baza/{last_date[1]}/{last_date[0]}')
time.sleep(4)
dict_of_celebrates_in_csv = {}
while( not(month == months[-1] and last_date[0] == nums_days[month] + 1) ):
    for day in range(last_date[0], nums_days[month] + 1):
        button = browser.find_element(By.XPATH, f"//a[@href='/baza/{month}/{day}']")
        button.click()
        final_text = parsing.list_of_all_Celebrates(browser)
        day_name = '{0:0>2}'.format(str(day))
        month_name = '{0:0>2}'.format( str( parsing.months.index(month) + 1 ) )
        date_name = f'{day_name}/{month_name}'
        print(date_name)
        if len(final_text) != 0:
            dict_of_celebrates_in_csv[date_name] = final_text
        else:
            print('WTF BRO ITS NOT WORKING GO FUCK YOURSELF')
            if not([day, month] == last_date):
                join_new_data(dict_of_celebrates_in_csv, is_here)
                is_here += 1
                last_date = [day, month]
                dict_of_celebrates_in_csv.clear()
            fl = 1
            break
    else:
        join_new_data(dict_of_celebrates_in_csv, is_here)
        is_here += 1
        dict_of_celebrates_in_csv.clear()
        if month != months[-1]:
            month = months[months.index(month) + 1]
            day = 1
            last_date = [day, month]
        else:
            last_date[0] = nums_days[month] + 1
    update_json_file(*last_date)
    if fl: break

browser.quit()
