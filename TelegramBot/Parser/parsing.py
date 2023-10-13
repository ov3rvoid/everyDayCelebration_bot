from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import string 
import time
from random import randint

smiles = ['🥳', '🥹', '😉', '💩', '🧐', '😎', '😶‍🌫️', '👻', '🤡', '🤯', '🎉', '🕊️', '🙀', '👽', '🤠', '🦋']

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

elems  =  browser.find_elements(By.CLASS_NAME,  'main' )
allCelebrates = list()
for el in elems:
    allCelebrates.append(el.text)
time.sleep(1)

filteredCelebrates = list()

forbidden_symbols = string.ascii_letters + string.digits + '!#%&()*/;<=>@[\]^_`{|}~'

for celebrate in allCelebrates:
    final_text = ''
    # mb_its_abb = 0
    for symb in celebrate:
        # if mb_its_abb == 1 and symb.isupper():
        #     final_text = final_text[:-1]
        #     break
        # else:
        #     mb_its_abb = 0
        # if symb.isupper():
        #     mb_its_abb = 1
        if symb not in forbidden_symbols:
            final_text += symb
    for _ in range(4): final_text = final_text.replace('  ', ' ')
    filteredCelebrates.append(final_text.strip('• ' + string.punctuation))

output_celebrates = ''

for i in range(len(filteredCelebrates)):
    output_celebrates += str(i + 1) + '. ' + filteredCelebrates[i] + smiles[randint(1, len(smiles) - 1)] +'\n' + '\n'

output_celebrates = output_celebrates[:-2]
