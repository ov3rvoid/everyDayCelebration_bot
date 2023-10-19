from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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


def without_rus_words(word):
    can_be = string.ascii_letters + string.digits + string.punctuation + ' '
    fl = 0
    for symb in word:
        if symb == '-':
            fl = 1
        elif fl:
            if symb == ' ':
                break
            else:
                fl = 0
        elif symb not in can_be:
            return False
    return True


def formatting_all_celebrates(allCelebrates, final_formatting=1):
    filteredCelebrates = list()
    forbidden_symbols = string.ascii_letters + string.digits + '!#%&()*/;<=>@[]^_`{|}~'

    for celebrate in allCelebrates:
        celebrate = celebrate.strip('• ')
        final_text = ''
        if without_rus_words(celebrate):
            final_text = celebrate
        else:
            for symb in celebrate:
                if symb not in forbidden_symbols:
                    final_text += symb
        for _ in range(4): final_text = final_text.replace('  ', ' ')
        filteredCelebrates.append(final_text.strip(string.punctuation))
    output_celebrates = ''
    if final_formatting:
        for i in range(len(filteredCelebrates)):
            output_celebrates += str(i + 1) + '. ' + filteredCelebrates[i] + smiles[randint(1, len(smiles) - 1)] +'\n' + '\n'
        output_celebrates = output_celebrates[:-2]
    else:
        output_celebrates = filteredCelebrates
    return output_celebrates
            

def activate_browser_url(url):
    options = Options()
    options.add_argument("--disable-infobars") 
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    return browser


def list_of_all_Celebrates(brsr):
    elems = brsr.find_elements(By.CLASS_NAME,  'main' )
    allCelebrates = list()
    for el in elems:
        allCelebrates.append(el.text)
    return allCelebrates



month = months[int(date_list[1]) - 1]
day = date_list[0]

url = r'https://kakoysegodnyaprazdnik.ru/baza/' + month + '/' + day
browser = activate_browser_url(url)
allCelebrates = list_of_all_Celebrates(browser)
#   time.sleep(3)   #  if u meet the capcha or another test in browser

output_celebrates = formatting_all_celebrates(allCelebrates)