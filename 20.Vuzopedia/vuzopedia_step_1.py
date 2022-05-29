import json
from bs4 import BeautifulSoup
import requests

def save_json(filename, data):
    try:  
        file_json = json.load(open(f'JSON/{filename}.json'))
        file_json.append(data)
        with open(f'JSON/{filename}.json', 'w') as file:
            json.dump(file_json, file, ensure_ascii=False, indent=2)
    except Exception as err:
        with open(f'JSON/{filename}.json', 'w') as file:
            file.write(json.dumps([data], indent=2, ensure_ascii=False))
        

def get_soup(url):
    try:
        headers = {'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
        req = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        return soup

    except requests.exceptions.ConnectionError as err:
        print(f'Ошибка подключения к {url}. Проверьте ваше интернет-соединение')

def write_error_to_json(tag, error, link):
    data = {
        'Type': tag,
        'Error': error,
        'Url': link
    }
    with open('errors.json', 'a') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    pass
