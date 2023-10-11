from bs4 import BeautifulSoup
import requests

url = 'https://kakoysegodnyaprazdnik.ru/'
page = requests.get(url)

filteredCelebrates = []
allCelebrates = []
soup = BeautifulSoup(page.text, "html.parser")
allCelebrates = soup.findAll('div', class_ = 'other')
for celebrates in allCelebrates:
    if celebrates.find('span', class_='super'):
        print(celebrates.text)
