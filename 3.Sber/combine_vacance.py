import json
import spacy


def save_in_json(data, namefile):
    with open(f"{namefile}.json", 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print('Файл успешно сохранен: ', namefile)


def get_any_titles_vacance():
    file = open('requirements.json', 'r')
    data = json.load(file)
    all_titles = []
    for vacance in data:
        all_titles.append(vacance['Вакансия'])

    return all_titles


def create_vacancies_group_with_nlp():
    nlp = spacy.load('ru_core_news_lg')
    text = get_any_titles_vacance()
    vacancies_that_are_already_in_group = []
    vacancies_in_subgroup = []
    data = []

    for item in range((len(text)-1)): # len(text)-1
        if text[item] not in vacancies_that_are_already_in_group:
            first = text[item]
            doc1 = nlp(first)
            item_data = []

            for item2 in range(item+1, len(text)):
                second = text[item2]
                doc2 = nlp(second)
                similary = doc1.similarity(doc2)
                if similary * 100 >= 80 and vacancies_in_subgroup != []:
                    for subgroup_elem in vacancies_in_subgroup:
                        sub_doc = nlp(subgroup_elem)
                        sub_similary = doc2.similarity(sub_doc)
                        if sub_similary * 100 >= 80:
                            item_data.append({
                                'second': second,
                                'similary': similary * 100
                            })
                            vacancies_in_subgroup.append(second)
                            vacancies_that_are_already_in_group.append(second)
                            break
                elif similary * 100 >= 80 and vacancies_in_subgroup == []:
                        item_data.append({
                            'second': second,
                            'similary': similary * 100
                        })
                        vacancies_in_subgroup.append(second)
                        vacancies_that_are_already_in_group.append(second)
            vacancies_in_subgroup.clear()

            if item_data != []:
                result = item_data[::]
                print(result, item)
                data.append({
                    'id': item, # first Было раньше
                    'name': first,
                    'items': result
                })
                item_data.clear()
    return data


def combining_vacancies():
    requirements_data = json.load(open('sorted_requirements.json', 'r'))
    # vacancies_group = create_vacancies_group_with_nlp()
    # save_in_json(vacancies_group, 'group_vacancies')
    vacancies_group = json.load(open('groups_vacancies.json', 'r'))
    result_data = []

    for vacance in vacancies_group:
        group_data = []
        for item in requirements_data:
            if vacance['name'] == item['Вакансия']:
                group_data += item['Требования']

            for sub_vacance in vacance['items']:
                if sub_vacance['second'] == item['Вакансия']:
                    # group_data.append(item['Требования'])
                    group_data += item['Требования'] 

        result_data.append({
            'Группа': vacance['name'],
            'Общие требования': group_data,
        })
    return result_data
# nlp_data = create_vacancies_group_with_nlp()
req_in_group = combining_vacancies()
save_in_json(req_in_group, 'req_in_group')
# save_in_json(nlp_data, 'groups_vacanciesNEWMETHOD')