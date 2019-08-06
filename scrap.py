from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd
import itertools

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

base_url = "https://casa.sapo.pt/en_gb/buy-apartments/most-recent/district.lisboa/?lp=10000"

response = get(base_url, headers=headers).text#.encode("utf-8")
with open('html.txt', 'w', encoding="utf-8") as html_file:
    html_file.write(response)
#print(response.text[:1000].encode("utf-8"))
with open('html.txt', 'r') as html_file:
    html_soup = bs(html_file, 'html.parser')
#print(html_soup)
house_container = html_soup.find_all('div', class_="searchResultProperty")

for i in range(len(house_container)):

#first = house_container[1]
#print(first.find_all('span')[2].text.encode("utf-8"))
    try:
        price = house_container[i].find_all('span')[3].text.encode("utf-8")#[2:9]#.replace(",", "")
    except:
        price = house_container[i].find_all('span')[2].text.encode("utf-8")#[2:9]#.replace(",", "")
    price = int(str(price).strip("b'").split()[0].replace(",", ""))
    print(price)
#print(type(price))
