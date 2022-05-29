import json
from vuzopedia_step_1 import write_error_to_json, get_soup, save_json
import re

class Profile:
    def __init__(self, url):
        self.url = url
    
    def run(self):
        soup = get_soup(self.url)
        profiles_in_page = soup.find_all('div', class_='itemSpecAll')
        for profile in profiles_in_page:
            try:
                self.profile_url = 'https://vuzopedia.ru' + profile.find('a', class_='spectittle')['href']
            except:
                write_error_to_json(tag='Profile', error='Нет ссылки', link=self.url)
                self.profile_url = ''
            try:
                self.profile_id = self.profile_url.split('/')[-1]
            except:
                write_error_to_json(tag='Profile', error='Нет ID', link=self.url)
                self.profile_id = ''
            try:
                self.profile_name = profile.find('a', class_='spectittle').text
            except:
                write_error_to_json(tag='Profile', error='Нет наименования', link=self.profile_url)
                self.profile_name = ''
            try:
                self.profile_img = re.findall('https.*?\)', profile.find('div', class_='itemSpecAlltitle')['style'])[0].replace(')', '')
            except:
                write_error_to_json(tag='Profile', error='Нет картинки', link=self.profile_url)
                self.profile_img = ''

            self.parse_profile(self.profile_url)
    
    def parse_profile(self, url):
        soup = get_soup(url)
        try:
            short_info = soup.find_all('p', class_='optTitle')
            # self.min_exam_score_budget = short_info[0].text
            self.places_budget = short_info[1].text
            self.places_paid = short_info[2].text
            self.min_price_in_year = short_info[3].text
        except:
            write_error_to_json(tag='Profile', error='Нет инфы мин. баллах и местах', link=url)
            self.min_exam_score_budget = self.min_price_in_year = self.places_budget = self.places_paid = ''
        try:
            self.min_exam_score_paid = re.findall('\d+', soup.find('div', attrs={'id':'filial'}).find_all('div', class_='cpPara')[1].text)[1]
            print(self.min_exam_score_paid.strip())
        except:
            write_error_to_json(tag='Profile', error='Нет мин баллов для платного', link=self.profile_url)
            self.min_exam_score_paid = ''
        try:
            self.min_exam_score_budget = re.findall('\d+', soup.find('div', attrs={'id': 'fak'}).find_all('div', class_='cpPara')[1].text)[1]
        except:
            write_error_to_json(tag='Profile', error='Нет мин баллов для бюджета', link=self.profile_url)
            self.min_exam_score_budget = ''
        try:
            self.facultet = soup.find_all('a', class_='linknap')[1]
        except:
            write_error_to_json(tag='Profile', error='Нет факультета', link=self.url)
            self.facultet = ''
        
        detalied_info = soup.find('div', class_='podrInfo').find_all('div')
        try:
            # Регулярка для "Квалификация:  Бакалавриат;"
            self.qualification = re.findall(':.*?;', detalied_info[2].text)[0].replace(';', '').replace(':', '').strip()
        except:
            write_error_to_json(tag='Profile', error='Нет квалификации', link=self.url)
            self.qualification = ''
        try:
            self.format = re.findall(':.*?;', detalied_info[3].text)[0].replace(';', '').replace(':', '').strip()
        except:
            write_error_to_json(tag='Profile', error='Нет формата обучения', link=self.url)
            self.format = ''
        try:
            self.language = re.findall(':.*?;', detalied_info[4].text)[0].replace(';', '').replace(':', '').strip()
        except:
            write_error_to_json(tag='Profile', error='Нет языка', link=self.url)
            self.language = ''
        try:
            self.duration = re.findall(':.*?;', detalied_info[6].text)[0].replace(';', '').replace(':', '').strip()
        except:
            write_error_to_json(tag='Profile', error='Нет продолжительности', link=self.url)
            self.duration = ''
        
        self.ege_objects = {}
        for ege in soup.find('div', class_='col-md-3 col-sm-6 varEgeProg').find_all('div', class_='cpPara'):
            if ege.text:
                subject = ege.text.split('-')[0]
                score = ege.text.split('-')[1]
                self.ege_objects[subject] = score
        self.add_to_json()

    def add_to_json(self):
        global ID
        result = {
            'ID': ID,
            'Название': self.profile_name,
            'Ссылка': self.profile_url,
            'Картинка': self.profile_img,
            'Квалификация': self.qualification,
            'Форма обучения': self.format,
            'Язык обучения': self.language,
            'Срок обучения': self.duration,
            'Стоимость обучения в год': self.min_price_in_year,
            'Минимальный проходной балл на бюджет': self.min_exam_score_budget,
            'Количество бюджетных мест по вузу': self.places_budget,
            'Минимальный проходной балл на платное': self.min_exam_score_paid,
            'Количество платных мест': self.places_paid,
            'ЕГЭ': self.ege_objects,
            'Связь со Специализацией': self.url
        }
        save_json(filename='profile', data=result)
        print(self.profile_name)
        ID += 1

if __name__ == "__main__":
    ID = 1
    specializations = json.load(open('JSON/specialization2.json'))
    for spec in range(5656, len(specializations)):
        print('\nСпециализация №', specializations[spec]['ID'], '\n')
        try:
            profile = Profile(specializations[spec]['Связь с Профилем'])
            profile.run()
        except:
            print(f'Не получилось спарсить ({specializations[spec]["Связь с Профилем"]})')
        # break
    # profile.parse_profile('https://vuzopedia.ru/vuz/405/programs/bakispec/766')