# STILL DOESNT WORK !!!
# ПОХУЙ BY THE WAY
# REMONT THIS AND USE IF U WANT TO PARS FULL SITE


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import parsing
# import time
# from random import randint
# import pandas as pd

# main_url = 'https://kakoysegodnyaprazdnik.ru' # main page for geys
# url_of_txt_date = './last_date.txt'
# path_for_csv_file = 'TelegramBot/AllCelebratesData/data_of_celebrates.csv'

# def filling_the_dict(dict, mx_num):
#     final_dict = {}
#     for key in dict:
#         lst = dict[key]
#         lst.extend((mx_num - len(lst)) * [''])
#         final_dict[key] = lst
#     return final_dict


# def mx_len_in_list_dict(dict):
#     for key in dict:
#         mx_num = max(mx_num, len(dict[key]))
#     return mx_num


# options = Options()
# options.add_argument("--disable-infobars")
# browser = webdriver.Chrome(options=options)
# browser.get(main_url)
# time.sleep(4)

# dict_of_celebrates_in_csv = {}
# k = 0
# month = parsing.months[0]
# day = 1
# last_date = [day, month]
# for month in pa
# while(not (month == parsing.months[-1] and day == 31)):
#     if parsing.months.index(month) % 2 == 0:
#         nums_days = 31
#     else:
#         if month == parsing.months[1]:
#             nums_days = 29
#         else:
#             nums_days = 30
#     with open(url_of_txt_date, encoding='UTF-8') as file_in:
#         a, b = str(file_in).split('/')
#         last_date = [int(a), b]
#     for day in range(last_date[0], nums_days + 1):
#         new_url = main_url + f'/baza/{month}/{day}'  # url of new day
#         browser.get(new_url)

#         allCelebrates = parsing.list_of_all_Celebrates(browser)
#         final_text = parsing.formatting_all_celebrates(allCelebrates, final_formatting=0)

#         day_name = '{0:0>2}'.format(str(day))
#         month_name = '{0:0>2}'.format( str( parsing.months.index(month) + 1 ) )
#         date_name = f'{day_name}/{month_name}'
#         dict_of_celebrates_in_csv[date_name] = final_text
#         if len(final_text) < 2:
#             print('WTF BRO ITS NOT WORKING GO FUCK YOURSELF')
#             last_date = [day, month]
#             k += 1
#             with open(url_of_txt_date, 'w', encoding='UTF-8') as file_out:
#                 file_out.write(str(day) + '/' + month)
#             final_dict_of_celebrates_in_csv = {}
#             max_numbers_of_celebrates = mx_len_in_list_dict(dict_of_celebrates_in_csv)
#             final_dict_of_celebrates_in_csv = filling_the_dict(dict_of_celebrates_in_csv, max_numbers_of_celebrates)
#             csv_file = pd.DataFrame(final_dict_of_celebrates_in_csv)
#             csv_file.index = range(1, max_numbers_of_celebrates + 1)
#             if k == 1:
#                 csv_file.to_csv(path_for_csv_file, sep=';')
#             else:
#                 final_csv_file = pd.read_csv(path_for_csv_file)
#                 final_csv_file.join(csv_file)
#                 final_csv_file.to_csv(path_for_csv_file, sep=';')
#             dict_of_celebrates_in_csv.clear()
#             print(date_name)
#             break
#     if month != parsing.months[-1] and last_date[1] != month:
#         month = parsing.months[parsing.months.index(month) + 1]

# browser.quit()
