# from bs4 import BeautifulSoup
# import requests
import string 
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

newdate = datetime.now()
newdate = newdate.strftime("%d.%m.%Y")
date_list = newdate.split('.')

months = [
    'yanvar',
    'fevral',
    'mart',
    'aprel',
    'may',
    'iyun',
    'iyul',
    'avgust',
    'sentyabr',
    'oktyabr',
    'noyabr',
    'decabr'
]

month = months[int(date_list[1]) - 1]
day = date_list[0]

url = r'https://kakoysegodnyaprazdnik.ru/baza/' + month + '/' + day

options = Options()
options.add_argument("--disable-infobars") 
browser = webdriver.Chrome(options=options)
browser.get(url)

elems  =  browser.find_elements(By.CLASS_NAME,  'listing_wr' )
time.sleep(4)

# page = requests.get(url)
# print(url)
# print(page)
# print(page.text)
# page.encoding = 'utf-8'

filteredCelebrates = []
allCelebrates = []
# print(date_list)
# soup = BeautifulSoup(page.text, "html.parser")
# allCelebrates = soup.findAll('div', class_ = 'main')
print(allCelebrates)

forbidden_symbols = string.ascii_letters + string.digits + '()'

for celebrates in allCelebrates:
    if celebrates.find('span', class_='other'):
        celebrates_of_day = celebrates.text
        final_text = ''
        mb_its_abb = 0
        for symb in celebrates_of_day:
            if mb_its_abb == 1 and symb.isupper():
                final_text = final_text[:-1]
                break
            else:
                mb_its_abb = 0
            if symb.isupper():
                mb_its_abb = 1
            if symb not in forbidden_symbols:
                final_text += symb
        final_text = final_text.replace('лет', '')
        final_text = final_text.replace('года', '')
        filteredCelebrates.append(final_text.strip())

print(filteredCelebrates[:10])
