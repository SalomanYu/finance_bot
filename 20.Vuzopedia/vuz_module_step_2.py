import re
from vuzopedia_step_1 import write_error_to_json, get_soup, save_json


class Vuz:
    def __init__(self):
        self.page = 1
        self.url = 'https://vuzopedia.ru/vuz'
        self.ID = 1

    def run(self):
        soup = get_soup(self.url)
        univers_in_page = soup.find_all('div', class_='itemVuzTitle')
        while univers_in_page:
            print('new_page',f'https://vuzopedia.ru/vuz?page={self.page}')
            univers_in_page = self.parse_page(f'https://vuzopedia.ru/vuz?page={self.page}')
            self.page += 1
            # break

    def parse_page(self, page_url):
        soup = get_soup(page_url)
        
        all_vuzes = soup.find_all('div', class_='col-md-12 itemVuzPremium')
        if not all_vuzes:
            all_vuzes = soup.find_all('div', class_='col-md-12 itemVuz')
        for vuz in all_vuzes:
            try:
                self.vuz_url = 'https://vuzopedia.ru' + vuz.find('a')['href']
            except:
                write_error_to_json(tag='Vuz', error='Нет ссылки', link=page_url)
                self.vuz_url = ''
            try:
                self.vuz_name = vuz.find('div', class_='itemVuzTitle').text.strip()
            except:
                write_error_to_json(tag='Vuz', error='Нет названия', link=self.vuz_url)
                self.vuz_name = ''
            try:
                self.logo = vuz.find('a').img['data-src']
            except:
                write_error_to_json(tag='Vuz', error='Нет лого', link=self.vuz_url)
                self.logo = ''
            try:
                self.min_price_in_year = re.findall('\d.*? ', vuz.find_all('div', class_='col-md-4 info')[0].find('a', class_='tooltipq').text)[0]
            except IndexError:
                write_error_to_json(tag='Vuz', error='Нет минимальной стоимости в год', link=self.vuz_url)
                self.min_price_in_year = ''
            try:
                self.min_exam_score_budget = re.findall('\d+', vuz.find_all('div', class_='col-md-4 info')[1].find('a', class_='tooltipq').text)[0]
            except:
                write_error_to_json(tag='Vuz', error='Нет минимального балла на бюджет', link=self.vuz_url)
                self.min_exam_score_budget = ''
            try:
                self.min_exam_score_paid = re.findall('\d+', vuz.find_all('div', class_='col-md-4 info')[2].find('a', class_='tooltipq').text)[0]
            except:
                write_error_to_json(tag='Vuz', error='Нет минимального балла на платное', link=self.vuz_url)
                self.min_exam_score_paid = ''

            try:
                self.parse_vuz(self.vuz_url)
            except:
                write_error_to_json(tag='Vuz', error='Нет подробной инфы о вузе', link=self.vuz_url)
        return all_vuzes
    
    def parse_vuz(self, vuz_url):
        print(self.vuz_name)
        soup = get_soup(vuz_url)
        pluses_of_vuz = soup.find('div', class_='vuzOpiton').find_all('i')
        self.has_dormitory = 'Да' if re.findall('".*?"', str(pluses_of_vuz[0]))[0] == '"material-icons vuzok"' else 'Нет' # ОБщага
        self.has_state = 'Да' if re.findall('".*?"', str(pluses_of_vuz[1]))[0] == '"material-icons vuzok"' else 'Нет' # Государственный
        self.has_millary_center = 'Да' if re.findall('".*?"', str(pluses_of_vuz[2]))[0] == '"material-icons vuzok"' else 'Нет' # Военнный центр
        self.has_budget_places = 'Да' if re.findall('".*?"', str(pluses_of_vuz[3]))[0] == '"material-icons vuzok"' else 'Нет' # Есть бюджетные места
        self.has_licence = 'Да' if re.findall('".*?"', str(pluses_of_vuz[4]))[0] == '"material-icons vuzok"' else 'Нет' # Лицензия
        # print(self.has_dormitory, self.has_state, self.has_millary_center, self.has_budget_places, self.has_licence)

        #Доля трудоустроенных - инфа появляется только спустя время, поэтому невозможно достать значение из кода
        #self.percentage_of_employed = soup.find('div', class_='mainWrap').find('div', class_='progress-bar').text
        try:
            self.general_budget_places = re.findall('\d+', soup.find_all('div', class_='col-md-6 col-sm-6 col-xs-6')[0].text)[0]
        except:
            write_error_to_json(tag='Vuz', error='Нет мест на бюджет ', link=vuz_url)
            self.general_budget_places = ''
        try:
            self.general_paid_places = re.findall('\d+', soup.find_all('div', class_='col-md-6 col-sm-6 col-xs-6')[1].text)[0]
        except:
            write_error_to_json(tag='Vuz', error='Нет мест на платное ', link=vuz_url)
            self.general_paid_places = ''
        try:
            self.city = soup.find('div', class_='choosecity').span.text.strip()
        except:
            write_error_to_json(tag='Vuz', error='Нет города', link=self.vuz_url)
            self.city = ''
        
        self.add_to_json()
        
        # SPEC = Specialization(vuz_url=self.vuz_url)
        # SPEC.run()
    
    def add_to_json(self):
        result = {
            'ID': self.ID,
            'Название ВУза': self.vuz_name,
            'Лого': self.logo,
            'Город': self.city,
            'Наличие общежития': self.has_dormitory,
            'Государственный': self.has_state,
            'Воен. уч. Центр': self.has_millary_center,
            'Бюджетные места': self.has_budget_places,
            'Лицензия/аккредитация': self.has_licence,
            'Минимальный проходной балл на бюджет': self.min_exam_score_budget,
            'Количество бюджетных мест по вузу': self.general_budget_places,
            'Минимальный проходной балл на платное': self.min_exam_score_paid,
            'Количество платных мест по вузу': self.general_paid_places,
            'Минимальная стоимость обучения в вузе в год': self.min_price_in_year,
            'Ссылка': self.vuz_url
        }
        save_json(filename='vuz', data=result)
        self.ID += 1



# For test
if __name__ == "__main__":
    parser = Vuz()
    parser.run()
    # parser.parse_vuz('https://vuzopedia.ru/vuz/5322')
    # parser.parse_vuz('https://vuzopedia.ru/vuz/3952')
    # parser.parse_vuz('https://vuzopedia.ru/vuz/3953')