from bs4 import BeautifulSoup
import requests

vacance_dictionary = {}

with open('parse_result.txt', 'r') as file:
    for line in file:
        title = line.split(' - ')[0]
        link = line.split(' - ')[1].strip()
        
        vacance_dictionary[title] = link

#url ="https://www.rabota.ru/vacancy/45176078/?search_id=16392159359930yz579zp4kqh"
#req = requests.get(url)

#soup = BeautifulSoup(req.text, 'lxml')

for vacance in vacance_dictionary:
    url = vacance_dictionary[vacance]
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    
    requirements = soup.find('div', class_='vacancy-card__description').find_all('ul')[2]
    print(requirements, url)
