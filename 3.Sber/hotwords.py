from collections import Counter
import json
from string import punctuation

import ru_core_news_lg
# import spacy


nlp = ru_core_news_lg.load()

def save_result(data):
    with open('level_vacancies.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def get_hotwords(text):
    global result_data
    levels_dict = { # Стоит ли добавлять сюда: Владелец, Секретаря руководителя относит к 3 категории
        1: ('junior', 'помощник', 'ассистент', 'младший', 'стажёр', 'стажер', 'assistant', 'intern', 'интерн', 'начинать'), # начинающий заменен на начинать с учетом лемматизации
        2: ('middle', 'заместитель', 'старший', 'lead', 'ведущий', 'главный', 'лидер'),
        3: ('senior', 'руководитель', 'head of', 'портфель', 'team lead', 'управлять', 'начальник', 'директор', 'head') # управляющий заменен на управлять с учетом лемматизации
    }

    doc = nlp(text.lower())
    vacance_level = 0
    for token in doc:
        for level in levels_dict:
            if token.lemma_ in levels_dict[level]:
                # print(token.text, '-->', token.lemma_, text, level)
                vacance_level = level

    result_data.append({
        'Вакансия': text,
        'Уровень': vacance_level
    })
    print(result_data)


    
        
result_data = []
all_data = json.load(open('sorted_requirements.json', 'r'))
all_vacancies_title = [vacance['Вакансия'] for vacance in all_data]

for item in range(len(all_vacancies_title)):
    get_hotwords(all_vacancies_title[item])
    break

# save_result(result_data)