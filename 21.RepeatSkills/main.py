import json
import xlrd
import sys
from langdetect import detect, LangDetectException
import ru_core_news_md
import en_core_web_md

import translators


def read_data(path:str) -> dict:
    """Returned {'id': 'name'} dictionary"""
    book = xlrd.open_workbook(path) # Открываем таблицу
    sheet = book.sheet_by_index(0) # Читаем первую страницу таблицы
    tableTitles = sheet.row_values(0) # Сохраняем все заголовки колонок, чтобы по ним определить номер необходимых колонок
    for titleIndex in range(sheet.ncols): 
        if tableTitles[titleIndex] == 'id': # Если колонка называется id, то запоминаем номер колонки
            id_col = titleIndex
        elif tableTitles[titleIndex] == 'name':
            name_col = titleIndex
    
    # Создаем два генератора, содержащих все айдишники и все наименования соответственно. 
    # Передаем эти генераторы в функцию, создающую словарь из двух списков
    return dict(zip((int(ID) for ID in sheet.col_values(id_col)[1:]), (NAME for NAME in sheet.col_values(name_col)[1:])))

def update_skills(skills:dict) -> dict:
    """Returned update skills dict"""
    data = []
    skills = {i: n for i, n in skills.items() if n != '' or ' '} # Составляем словарь, в котором не будет пустых значений 
    for ID, NAME in skills.items():
        info = {'Было': NAME}
        try:
            if detect(NAME) == 'en':
                for word in NAME.split():
                    word_lang = detect(word)
                    if word_lang != 'en':
                        NAME = NAME.replace(word, translators.google(word, from_language=word_lang, to_language='en'))

                # print(f"{NAME} ---> {translators.google(NAME, from_language='en', to_language='ru')}")
                info['EN']= NAME    
                info['RU']= translators.google(NAME, from_language='en', to_language='ru')
                data.append(info)    
        except (LangDetectException, TypeError, IndexError):
            continue
    with open('data.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
            
def nlp_update(skills: dict) -> dict:
    data = []
    skills = {i: n for i, n in skills.items() if n != '' or ' '} # Составляем словарь, в котором не будет пустых значений 
    names = tuple(skills.values())[:100]

    ids = tuple(skills.keys())[:100]
    res = []


    with open('nlp_data.json', 'w') as file:
        json.dump(res, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    nlp_ru = ru_core_news_md.load()
    nlp_en = en_core_web_md.load()
    
    skills = read_data(path='Data/course_skill.xlsx')
    # update_skills(skills)
    nlp_update(skills)
    stopwords = ['имеешь опыт работы в сфере','имеете опыт работы с', 'понимание и опыт работы с', 'имеешь опыт работы с', 'опыт работы с', 'опыт работы со',
                'навыки работы с',  'уверенное знание'  , 'уверенные знания', 'базовые знания' 'отличное знание',  'есть опыт написания', 'опыт разработки',
                'знание принципов', 'понимание принципов', 'понимаете принципы', 'знаете принципы', 'умеете работать', 'умение работать' 'приветствуется',
                 'навык работы с', 'имеете работы с', 'мышление', 'опыт работы/ знание']