"""
В этом модуле мы будем проставлять связи между:
1 Вуз - специализация
2 Вуз - профиль
3 Специализация - Вуз
4 Специализация - профиль
5 Профиль - Вуз
6 Профиль - Специализация
"""


import json
from vuzopedia_step_1 import save_json


def Vuz_connect_with_spec_and_profile():
    """
    Данный метод реализует связи между вузом и специализацией, плюс вузом и профилем
    """
    vuz_data = json.load(open('JSON/vuz.json')) # Подключаем спарсенную информацию о вузах
    spec_data = json.load(open('JSON/updated_specializations.json')) # Подключаем спарсенную информацию о специализациях
    profile_data = json.load(open('JSON/updated_profiles.json')) # Подключаем спарсенную информацию о профилях

    for vuz in vuz_data: # Запускаем цикл по каждому вузу. Итерация происходит по списку словарей
        vuz_url = vuz['Ссылка']
        # vuz_url = vuz['Ссылка'] + '/spec' # Нам нужна чистая ссылка на вуз
        # print(vuz['Связь со специальностью'])
        for spec in spec_data: # Запускаем цикл по каждой специальности. Инерация происходит по списку словарей
            spec_urls = spec['Связь с ВУЗОМ'] # Ссылка, которая указывает, что данная специальность принадлежит конкретному вузу
            if type(spec_urls) == list: # Если специализация принадлежит сразу нескольким вузам
                for replace_url in spec_urls: # Итерация по ссылке каждого вуза
                    if replace_url == vuz_url: # Если ссылки совпадают, с итерируемым вузом, то 
                        print(vuz_url)
                        try: # Пробуем добавить в список связей айди вуза
                            vuz['Связь со специальностью'].append(spec['ID'])
                        except: # Если такой список еще не составлен, то добавляем туда первый айди специализации
                            vuz['Связь со специальностью'] = [spec['ID']]
                        #  Отзеркаливание
                        try: # Пробудем добавить в список связей айди специализации
                            spec['Связь с ВУЗОМ (IDS)'].append(vuz['ID'])
                        except: # Если такой список еще не составлен, то добавляем туда первый айди Вуза
                            spec['Связь с ВУЗОМ (IDS)'] = [vuz['ID']]

            elif vuz_url == spec_urls: # Если у специализации только одна ссылка, то проверяем совпадает ли она с итерируемым вузом и копируем try-case выше
                try:
                    vuz['Связь со специальностью'].append(spec['ID'])
                except:
                    vuz['Связь со специальностью'] = [spec['ID']]
                try:
                    spec['Связь с ВУЗОМ (IDS)'].append(vuz['ID'])
                except:
                    spec['Связь с ВУЗОМ (IDS)'] = [vuz['ID']]

        for profile in profile_data: # Запускаем цикл по профилям. Интерация происходит по списку словарей
            profile_urls = profile['Связь со Специализацией'] # Ссылка на специализацию
            # Дальше прописывается аналогия вышеописанно
            if type(profile_urls) == list:
                for replace_url in profile_urls:
                    if vuz['Ссылка'] in replace_url:
                        try:
                            vuz['Связь с профилем'].append(profile['ID'])
                        except:
                            vuz['Связь с профилем'] = [profile['ID']]
                        try:
                            profile['Связь с ВУЗОМ (IDS)'].append(vuz['ID'])
                        except:
                            profile['Связь с ВУЗОМ (IDS)'] = [vuz['ID']]

            elif vuz['Ссылка'] in profile_urls: # Будет истинно если vuz=https://vuzopedia.ru/vuz/1297, а profile_urls=https://vuzopedia.ru/vuz/1297/napr/2
                try:
                    vuz['Связь с профилем'].append(profile['ID'])
                except:
                    vuz['Связь с профилем'] = [profile['ID']]
                try:
                    profile['Связь с ВУЗОМ (IDS)'].append(vuz['ID'])
                except:
                    profile['Связь с ВУЗОМ (IDS)'] = [vuz['ID']]

    # Сохраняем измененные словари  
    save_json('final_vuz', vuz_data)
    save_json('final_spec', spec_data)
    save_json('final_profile', profile_data)


def spec_connect_with_vuz_and_profile():
    spec_data = json.load(open('JSON/final_spec.json'))
    profile_data = json.load(open('JSON/final_profile.json'))
    for profile in profile_data:
        if type(profile['Связь со Специализацией']) == list:
            for prof in profile['Связь со Специализацией']:    
                prof_url = prof.split('/napr')[0]
                for spec in spec_data:
                    spec_urls = spec['Связь с ВУЗОМ']
                    if type(spec_urls) == list:
                        for url in spec_urls:
                            if url == prof_url:
                                try:
                                    spec['Связь с профилем (IDS)'].append(profile['ID'])
                                except:
                                    spec['Связь с профилем (IDS)'] = [profile['ID']]
                                try:
                                    profile['Связь со специализацией (IDS)'].append(spec['ID'])
                                except:
                                    profile['Связь со специализацией (IDS)'] = [spec['ID']]
                    elif spec_urls == prof_url:
                        try:
                            spec['Связь с профилем (IDS)'].append(profile['ID'])
                        except:
                            spec['Связь с профилем (IDS)'] = [profile['ID']]
                        try:
                            profile['Связь со специализацией (IDS)'].append(spec['ID'])
                        except:
                            profile['Связь со специализацией (IDS)'] = [spec['ID']]
        else:
            prof_url = profile['Связь со Специализацией'].split('/napr')[0]
            for spec in spec_data:
                spec_urls = spec['Связь с ВУЗОМ']
                if type(spec_urls) == list:
                    for url in spec_urls:
                        if url == prof_url:
                            try:
                                print('yo')
                                spec['Связь с профилем (IDS)'].append(profile['ID'])
                            except:
                                spec['Связь с профилем (IDS)'] = [profile['ID']]
                            try:
                                profile['Связь со специализацией (IDS)'].append(spec['ID'])
                            except:
                                profile['Связь со специализацией (IDS)'] = [spec['ID']]
                elif spec_urls == prof_url:
                    try:
                        spec['Связь с профилем (IDS)'].append(profile['ID'])
                    except:
                        spec['Связь с профилем (IDS)'] = [profile['ID']]
                    try:
                        profile['Связь со специализацией (IDS)'].append(spec['ID'])
                    except:
                        profile['Связь со специализацией (IDS)'] = [spec['ID']]

    save_json('final_spec2', spec_data)
    save_json('final_profile2', profile_data)

def profile_connect_with_profession():
    profile_data = json.load(open('JSON/final_profile2.json'))
    prof_data = json.load(open('JSON/updated_professions.json'))
    for profile in profile_data:
        profile_url = profile['Ссылка']
        for prof in prof_data:
            prof_url = prof['Связь с профилем']
            if type(prof_url) == list:
                for url in prof_url:
                    if profile_url == url.split('/prof')[0]:
                        try:
                            print(profile_url)
                            profile['Связь с профессией (IDS)'].append(prof['ID'])
                        except:
                            profile['Связь с профессией (IDS)'] = [prof['ID']]
            elif prof_url.split('/prof')[0] == prof:
                try:
                    print(profile_url)
                    profile['Связь с профессией (IDS)'].append(prof['ID'])
                except:
                    profile['Связь с профессией (IDS)'] = [prof['ID']]

    save_json('final_profile3', profile_data)

if __name__ == "__main__":
    # Vuz_connect_with_spec_and_profile()
    # spec_connect_with_vuz_and_profile()
    profile_connect_with_profession()