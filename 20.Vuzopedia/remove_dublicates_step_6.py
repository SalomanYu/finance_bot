import json
from vuzopedia_step_1 import save_json

def clear_dublicate_specializations():
    ids_for_remove = []
    data = json.load(open('JSON/specialization2.json'))
    for index in range(len(data)-1):
        first_spec = data[index]
        for index2 in range(index+1, len(data)):
            second_spec = data[index2]
            if (first_spec['Название специальности'] == second_spec['Название специальности']):
                if type(first_spec['Связь с ВУЗОМ']) == list:
                    first_spec['Связь с ВУЗОМ'].append(second_spec['Связь с ВУЗОМ'])
                else:
                    first_spec['Связь с ВУЗОМ'] = [first_spec['Связь с ВУЗОМ'], second_spec['Связь с ВУЗОМ']]
                ids_for_remove.append(second_spec['ID'])

    for id in ids_for_remove:
        for spec in data:
            if spec['ID'] == id:
                print('Удален: ', id)
                data.remove(spec)
    save_json('updated_specializations', data)


def clear_dublicate_profiles():
    ids_for_remove = []
    data = json.load(open('JSON/profile.json'))
    for index in range(len(data)-1):
        first_spec = data[index]
        for index2 in range(index+1, len(data)):
            second_spec = data[index2]
            if (first_spec['Название'] == second_spec['Название']):
                if type(first_spec['Связь со Специализацией']) == list:
                    first_spec['Связь со Специализацией'].append(second_spec['Связь со Специализацией'])
                else:
                    first_spec['Связь со Специализацией'] = [first_spec['Связь со Специализацией'], second_spec['Связь со Специализацией']]
                ids_for_remove.append(second_spec['ID'])

    for id in ids_for_remove:
        for spec in data:
            if spec['ID'] == id:
                print('Удален: ', id)
                data.remove(spec)
    save_json('updated_profiles', data)


def clear_dublicate_professions():
    ids_for_remove = []
    data = json.load(open('JSON/profession.json'))
    for index in range(len(data)-1):
        first_spec = data[index]
        for index2 in range(index+1, len(data)):
            second_spec = data[index2]
            if (first_spec['Название профессии'] == second_spec['Название профессии']):
                if type(first_spec['Связь с профилем']) == list:
                    first_spec['Связь с профилем'].append(second_spec['Связь с профилем'])
                else:
                    first_spec['Связь с профилем'] = [first_spec['Связь с профилем'], second_spec['Связь с профилем']]
                ids_for_remove.append(second_spec['ID'])

    for id in ids_for_remove:
        for spec in data:
            if spec['ID'] == id:
                print('Удален: ', id)
                data.remove(spec)
    save_json('updated_professions', data)


if __name__ == "__main__":
    # clear_dublicate_specializations()
    # clear_dublicate_profiles()
    clear_dublicate_professions()
    # pass