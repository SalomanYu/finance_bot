import json
from vuzopedia_step_1 import write_error_to_json, get_soup,save_json
import re

class Specialization:
    def __init__(self, vuz_url):
        self.vuz_url = vuz_url
        self.page = 1

    def run(self):
        self.spec_url = self.vuz_url + '/spec'
        soup = get_soup(self.vuz_url)
        spec_in_page = soup.find_all('div', class_='itemSpecAllinfo')
        while spec_in_page:
            print(self.page, self.spec_url + f'?page={self.page}')
            spec_in_page = self.parse_page(self.spec_url + f'?page={self.page}')
            self.page += 1
    
    def parse_page(self, url):
        soup = get_soup(url)
        all_specs = soup.find_all('div', class_='col-md-12 shadowForItem')
        for spec in all_specs:
            try:
                self.spec_name = spec.find('div', class_='itemSpecAllinfo').a.text
            except:
                write_error_to_json(tag='Specialization', error='Нет наименования', link=url)
                self.spec_name = ''
            try:
                self.qualification = spec.find('div', class_='itemSpecAllinfo').find_all('div')[1].text.strip().split('|')[0]
            except:
                write_error_to_json(tag='Specialization', error='Нет квалификации', link=url)
                self.qualification = ''
            try:
                self.img = re.findall('https.*?\)', str(spec.find('div', class_='itemSpecAlltitle')['style']))[0].replace(')', '')
            except:
                write_error_to_json(tag='Specialization', error='Нет картинки', link=url)
                self.img = ''
            try:
                self.profile_urls = "https://vuzopedia.ru" + spec.find('a', class_='linknap')['href']
            except:                
                write_error_to_json(tag='Specialization', error='Нет профилей', link=url)
                self.profile_urls = ''

            self.add_to_json()
        return all_specs

    def add_to_json(self):
        global ID
        print(self.spec_name)
        result = {
            'ID': ID,
            'Название специальности': self.spec_name,
            'Картинка': self.img,
            'Квалификация': self.qualification,
            'Связь с Профилем': self.profile_urls,
            'Связь с ВУЗОМ': self.vuz_url
        }
        ID += 1
        save_json(filename='specialization2', data=result)

# For test
if __name__ == "__main__":
    ID = 1
    vuzes_data = json.load(open('JSON/vuz.json'))
    for vuz in vuzes_data:
        spec = Specialization(vuz_url=vuz['Ссылка'])
        spec.run()
        # break
        