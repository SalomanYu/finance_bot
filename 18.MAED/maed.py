from bs4 import BeautifulSoup
import requests 
from lxml import html


path = "//div[@class='r t-rec']//div[@class='t396__artboard rendered']//div[@class='tn-atom']"

req = requests.get('https://sale.maed.ru/new_context')

tree = html.fromstring(req.text)
a = tree.xpath("//div[@class='t849']//ul")
for item in a:
    print(item.text)