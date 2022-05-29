import re
import json

def filter_requirement(text):
    """
    Метод чистит требования от стоп-слов
    """
    lock_symbols = ('Требования к образованию и опыту работы:', 'Требования', "**Технические компетенции:**", 'Эта работа тебе подойдет, если:',
                    "**Личностные качества:**", '**Будет здорово, если вы:**',  '**Ты нам подходишь, если у тебя есть**',
                    '**Ты подходишь нам, если**:', '**Ты подходишь нам, если ты:**', '**Вы нам подходите, если:**',
                    '**Ты подходишь нам, если ты:**', 'Ты подходишь нам, если ты:', 'Ты подходишь нам, если:', "**Тебе точно у нас понравится, если ты:**",
                    "**Мы ожидаем, что Вы:**", "**Будет преимуществом опыт работы с:**", 'Тебе точно у нас понравится, если ты:', 'Будет здорово, если Вы:',
                    ',Будет плюсом:', 'Инструментарий:', 'как весомое преимущество', 'Ты нам подходишь', 'Плюсом будет:', 'Мы рассмотрим кандидатов, у которых есть:',
                    '·               ','·      ', '\n\n', '\n*', "\n", 'и пр.', '(', ')', '*', '\-', ',∙ ', ',· ', '·    ', '·  ', ',:', '• ')
    for item in lock_symbols:
        if  item == "**Личностные качества:**" or item == '\n\n' or item == '\n*':
            text = text.replace(item, ',')
        else:
            text = text.replace(item, '')

    text = re.split('\. |, |;', text)
    result_data = []
    for item in text:
        if item != '' and item != ',':
            result_data.append(item.strip())
    

    return result_data


def sort_requirements():
    file = open('requirements.json', 'r')
    all_vacancies_requirements = json.load(file)
    data = []

    for vacance in all_vacancies_requirements:
        filtered_req = filter_requirement(vacance['Требования'])
        vacance_title = vacance['Вакансия']
        vacance_url = vacance['Ссылка']

        data.append({
            'Вакансия': vacance_title,
            'Ссылка': vacance_url,
            'Требования': filtered_req
        })
    with open('sorted_requirements.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

sort_requirements()
