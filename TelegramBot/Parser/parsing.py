from bs4 import BeautifulSoup
import requests
import string 
from datetime import datetime

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

url = f'https://kakoysegodnyaprazdnik.ru/'
page = requests.get(url)
print(page)
page.encoding = 'utf-8'


filteredCelebrates = []
allCelebrates = []

soup = BeautifulSoup(page.text, "html.parser")
allCelebrates = soup.findAll('div', class_ = 'event_block')
forbidden_symbols = string.ascii_letters + string.digits + '()'

for celebrates in allCelebrates:
    if celebrates.find('div', class_='event'):
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
