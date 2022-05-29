import pandas as pd
import json

# Открываем CSV
excel = pd.read_excel('table_level_vacance.xls')
excel.to_csv('table_level_vacance.csv')
file = pd.read_csv('table_level_vacance.csv')

# Сохраняем  названия вакансий в переменную
json_file = open('requirements.json', 'r')
json_data = json.load(json_file)
all_vacances = [item['Вакансия'] for item in json_data]

for vacance in all_vacances:
    for row in file.values:
        for item in range(len(row)):
            if  row[item] in vacance and type(row[item]) != int:
                print(vacance)
