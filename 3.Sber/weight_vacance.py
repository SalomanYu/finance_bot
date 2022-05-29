import json

def definer_weight_vacance():
    file_with_level_vacancies = json.load(open('level_vacancies.json', 'r'))
    file_with_vacance_groups = json.load(open('groups_vacancies.json', 'r'))

    data_with_weight_vacancies = []

    for item in file_with_vacance_groups:
        group = []

        for vacance2 in file_with_level_vacancies:
            if item['name'] == vacance2['Вакансия']:
                group.append({
                    'Вакансия': item['name'],
                    'Уровень': vacance2['Уровень']
                })

        for vacance in item['items']:
            for vacance2 in file_with_level_vacancies:
                if vacance['second'] == vacance2['Вакансия']:
                    group.append({
                            'Вакансия': vacance['second'],
                            'Уровень': vacance2['Уровень']
                        })
        data_with_weight_vacancies.append({
            'id': item['id'],
            'Группа': group
        })
    with open('weight_vacancies.json', 'w') as file:
        json.dump(data_with_weight_vacancies, file, ensure_ascii=False, indent=2)

# definer_weight_vacance()


def definer_bigger_vacance_in_group():
    file_data = json.load(open('weight_vacancies.json', 'r'))
    data_with_bigger_vacance = []
    
    for item in file_data:
        max_level = -1
        bigger_vacance = ''
        for vacance in item['Группа']:
            if int(vacance['Уровень']) > max_level:
                max_level = int(vacance['Уровень'])
                bigger_vacance = vacance['Вакансия']

        for vacance in item['Группа']:
            if vacance['Вакансия'] == bigger_vacance:
                vacance['Вес'] = 1
            else:
                vacance['Вес'] = 0

    with open('bigger_vacance.json', 'w') as file:
        json.dump(file_data, file, ensure_ascii=False, indent=2)


        # data_with_bigger_vacance.append({
        #     'id': item['id'],
        #     'Вакансия': bigger_vacance,
        #     'Вес вакансии': 1,
            
        # }) 
    

# definer_bigger_vacance_in_group()

def definer_bigger_vacance_in_level_group():
    file_data = json.load(open('bigger_vacance.json', 'r'))
    data_result = []

    for item in file_data:
        group_data = []
        levels = (0, 1, 2, 3)
        for level in levels:
            group_level = []
            for vacance in item['Группа']:
                if level == vacance['Уровень']:
                    group_level.append(vacance)

            if group_level != []:
                main_vacance_in_level_group = group_level[0]['Вакансия']
            else:
                pass
            for vacance in group_level:
                if len(vacance['Вакансия']) < len(main_vacance_in_level_group):
                    main_vacance_in_level_group = vacance['Вакансия']

            
            # print(main_vacance_in_level_group)
            # for vacance in item['Группа']:
                # if level == vacance['Уровень'] and len(vacance['Вакансия']) < len(main_vacance_in_level_group):
                # if level == vacance['Уровень']:

            #         print('Тут меньше')
            #         main_vacance_in_level_group = vacance['Вакансия']

            for vacance in item['Группа']:
                for level in levels:
                    if level == vacance['Уровень']:
                        if vacance['Вакансия'] == main_vacance_in_level_group:
                            vacance['Вес в уровне'] = 1
   

    
    with open('bigger_in_level2.json', 'w') as file:
        json.dump(file_data, file, ensure_ascii=False, indent=2)
                    

definer_bigger_vacance_in_level_group()