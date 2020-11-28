from bs4 import BeautifulSoup
from urllib.request import urlopen as ur
from requests import get
import json
import re

# zapisuje adres url do zmiennej i pobieram tresc strony
url = 'https://nabory.kprm.gov.pl/wyniki-naborow?AdResult%5BpagesCnt%5D=10&AdResult%5BisAdvancedMode%5D=&AdResult%5Bsort%5D=1&AdResult%5Bid%5D=&AdResult%5Bid_institution%5D=&AdResult%5Bid_institution_position%5D=&search-button='
page = get(url)
bs = BeautifulSoup(page.content, 'html.parser')

for element in bs.find_all('li', class_= 'row'):
    # pobieram podstawowe dane o kazdym naborze ze strony glownej
    job_id = element.find('span', class_='id').get_text()
    job_title = element.find('strong', class_='title').get_text()
    institution = element.select('div > b')[0].get_text(strip=True)
    city = element.select('div > b')[1].get_text(strip=True)
    date = element.select('div > b')[2].get_text(strip=True)

    # pobieram odnosnik ze strony glownej do podstrony kazdego wyniku
    link = element.find('a', class_='single').get('href')
    url2 = "https://nabory.kprm.gov.pl" + link
    bs2 = BeautifulSoup(get(url2).content, 'html.parser')
    result = bs2.find('div', class_='row job-res').get_text()
    # wyswietlenie wszystkich pobranych danych
    print(job_id, job_title, institution, city, date, re.sub(r'(\s+|\n)', ' ', result))








    




