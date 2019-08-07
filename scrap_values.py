from bs4 import BeautifulSoup as bs
from requests import get
import itertools


headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

base_url = "https://casa.sapo.pt/en_gb/buy-apartments/most-recent/district.santarem/"


response = get(base_url, headers=headers).text
with open('html.txt', 'w', encoding="utf-8") as html_file:
    html_file.write(response)
with open('html.txt', 'r') as html_file:
    html_soup = bs(html_file, 'html.parser')



title_list, location_list, price_list, condition_list, net_area_list, floor_area_list = [], [], [], [], [], []
house_container = html_soup.find_all('div', class_="searchResultProperty")


for house in house_container:       #Loop for scrapper
    title = house.find_all('p', class_="searchPropertyTitle HasFeatures")
    titleandinfo = str(title[0].find_all('span')[0]).strip("span<>/").strip().split(", ")
    title_list.append(titleandinfo[0])
    location_list.append(titleandinfo[1])

    try:
        price = house.find_all('span')[3]
    except:
        price = house.find_all('span')[2]
    price = int(str(price).strip("b'span<>/").split()[0].replace(",", ""))
    price_list.append(price)

    searchPropertyInfo = house.find_all('div', class_= "searchPropertyInfo")
    condition = searchPropertyInfo[0].find_all('div')[0].find_all('p')[1].text.strip("p<>/")
    net_area = searchPropertyInfo[0].find_all('div')[1].find_all('p')[1].text.strip("p<>/m²")
    floor_area = searchPropertyInfo[0].find_all('div')[2].find_all('p')[1].text.strip("p<>/m²")
    condition_list.append(condition)
    net_area_list.append(net_area)
    floor_area_list.append(floor_area)


print(len(title_list), len(location_list), len(price_list), len(condition_list), len(net_area_list), len(floor_area_list), sep="\n")



















"""
'for i in range(len(house_container)):

#first = house_container[1]
#print(first.find_all('span')[2].text.encode("utf-8"))
    try:
        price = house_container[i].find_all('span')[3].text.encode("utf-8")#[2:9]#.replace(",", "")
    except:
        price = house_container[i].find_all('span')[2].text.encode("utf-8")#[2:9]#.replace(",", "")
    price = int(str(price).strip("b'").split()[0].replace(",", ""))
    print(price)'
#print(type(price))
"""
