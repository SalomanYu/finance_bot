import requests
from bs4 import BeautifulSoup
import json


def parse_vacance(url, name_vacance):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    try: 
        levels_vacance = soup.find('div', class_='category').text
        levels_vacance = ';'.join(levels_vacance.split('•'))
        
        tags = soup.find('div', class_='tags').text
        tags = ';'.join(tags.split('•'))

        indystry = tags.split(';')[-1]
        specialization = ';'.join(tags.split(';')[:-1])

        experience = soup.find('span', class_='jobformat').text.split('\n')[1].replace('Опыт работы', '')
        salary = soup.find('span', class_='salary').text

        result = {
            'Наименование вакансии': name_vacance,
            'Ссылка': url,
            'Уровень должности': levels_vacance,
            'Отрасль применения': indystry,
            'Специализация': specialization, 
            'Опыт работы': experience,
            'Зарплата': salary
        }
        print('Записан ', name_vacance)
        return result

    except AttributeError:
        print(url)
        quit()

   
    

def parser_vacance_list(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    page_result = []

    vacance_list = soup.find_all('li', class_='collection-item avatar')
    for item in vacance_list:
        name_vacance = item.find('p', class_='truncate vacancy-name')
        link_vacance = 'https://geekjob.ru' + name_vacance.a['href']
        page_result.append(parse_vacance(link_vacance, name_vacance.text))

    return page_result

def main():
    req = requests.get('https://geekjob.ru/vacancies/')
    soup = BeautifulSoup(req.text, 'lxml')
    count_pages = int(soup.find('section', id='paginator').small.text.split()[1])
    
    parser_result = []
    
    for page_num in range(1, count_pages+1):
        print(f'Осталось парсить {count_pages-page_num} страниц.')
        parser_result += parser_vacance_list(url=f'https://geekjob.ru/vacancies/{page_num}')

    with open('parser_result.json', 'w') as file:
            json.dump(parser_result, file, ensure_ascii=False, indent=2)

main()
# parse_vacance('https://geekjob.ru/vacancy/61ffac30425d5b0dca0a4065', 'heelo')
# parser_vacance_list('https://geekjob.ru/vacancies/')
