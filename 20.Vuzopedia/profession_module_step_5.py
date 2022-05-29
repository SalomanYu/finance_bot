import json
import re
from vuzopedia_step_1 import get_soup, save_json, write_error_to_json

class Profession:
    def __init__(self):
        pass
    
    def parse_page(self, proffesions_url):
        self.profile_url = proffesions_url
        soup = get_soup(self.profile_url)
        
        professions = soup.find_all('div', class_='col-lg-3 col-md-4 col-xs-12 col-sm-4')
        for prof in professions:
            self.profession_name = prof.find('div', class_='profItemTitle').text
            self.proffesion_url = "https://vuzopedia.ru" + prof.find('a')['href']
            proff_soup = get_soup(self.proffesion_url)
            self.proffesion_descr = proff_soup.find('div', class_='mainWrap').p.text
            self.img = re.findall('https.*?\)', str(proff_soup.find('div', class_='mainBlock')['style']))[0].replace(')', '')

            self.add_to_json()

    def add_to_json(self):
        global ID
        result = {
            'ID': ID,
            'Название профессии': self.profession_name,
            'Картинка': self.img,
            'Описание': self.proffesion_descr,
            'Ссылка': self.proffesion_url,
            'Связь с профилем': self.profile_url
        }
        ID += 1
        save_json('profession', result)
        print(self.profession_name)

if __name__ == "__main__":
    ID = 1
    prof = Profession()
    
    profiles = json.load(open('JSON/profile.json'))
    for profile in profiles:
        prof.parse_page(profile['Ссылка']+ '/prof')
        # break