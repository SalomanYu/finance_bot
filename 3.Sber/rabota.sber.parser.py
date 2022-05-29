from os import sync
from selenium import webdriver
from selenium.webdriver.common.by import By
import json, time


def parse_page(url, browser):
    global data

    browser.get(url)
    browser.implicitly_wait(20)
    # vacancies = browser.find_elements(By.XPATH, "//div[@class='e14jyz651 css-kqyu1g e1j1p76k0']")
    titles_parser = browser.find_elements(By.XPATH, "//p[@class='css-1o2zq96 e1j1p76k4']")
    links_parser = browser.find_elements(By.XPATH, "//div[@class='css-1b6n4o1 e1j1p76k1']/a")
    
    for item in range(len(titles_parser)):
        data[titles_parser[item].text] = links_parser[item].get_attribute('href')


def save_result():
    global data
    with open('result_parse.json', 'a') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)    

def main_proccess(page_count=71):
    browser = webdriver.Chrome()
    for page_num in range(page_count):
        request_url = f'https://rabota.sber.ru/search?page={page_num}'
        try:
            parse_page(request_url, browser)
            time.sleep(0.5)
            print('Закончили парсить страницу № ', page_num)
        except BaseException:
            print(request_url)
            save_result()
    browser.quit()
    save_result()

data = {}

main_proccess()


