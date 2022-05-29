import spacy
import json,time

with open('NEW_JSON_REDACT.json', 'r') as file:
    json_data = json.load(file)


def get_any_title():
    title_list = []
    requirements_list = []

    for item in json_data:
        title_list.append(item['title'])
        requirements_list.append(item['requirements'])
    # print(title_list[:3])
    return title_list


nlp = spacy.load('ru_core_news_md')
text = get_any_title()
data = []
vacancies_in_subgroup = []

for item in range(len(text)-1):
    if text[item] not in vacancies_in_subgroup:
        doc1 = nlp(text[item])
        item_data = []

        for item2 in range(item+1, len(text)):
            first = text[item]
            second = text[item2]
            doc2 = nlp(text[item2])
            similary = doc1.similarity(doc2)

            if similary * 100 >= 80:
                item_data.append({
                    'second': second,
                    'similary': similary * 100
                })
                vacancies_in_subgroup.append(second)

        if item_data != []:
            result = item_data[::]
            data.append({
                'group': text[item],
                'items': result
            })
            item_data.clear()
        # print('\n\n')

with open('sorted_vacance2.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print('DONE')