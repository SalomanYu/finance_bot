import json

with open('result.json', 'r') as file:
    json_data = json.load(file)


def get_any_title():
    title_list = []
    requirements_list = []

    for item in json_data:
        title_list.append(item['title'])
        requirements_list.append(item['requirements'])

    return title_list


