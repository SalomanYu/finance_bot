import csv, json
import spacy

nlp = spacy.load('ru_core_news_md')


groups = []
subgroups = []

jsonfile = open('NEW_JSON_REDACT.json')
data = json.load(jsonfile)

result_json = []

with open('NEW_RESULT.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		title = row['Название группы']
		items = [item.strip() for item in row['Содержимое группы'].split('|||')] + [title]
		groups.append(items)

# print(groups[29])

for group in groups:
	group_data = []
	for item in group:
		requirements = []
		for vacance in data:
			if vacance['title'] == item:
				requirements.append(vacance['requirements'])
		if requirements != []:
			group_data.append(requirements)
	if group_data != []:
		common_list = [item for sublist in group_data for sub in sublist for item in sub] # удаляем лишние скобки 
		taboo_symbols = ('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '11.', '12.')
		result_list = []
		for symbol in taboo_symbols:
			for item in common_list:
				if symbol in item:
					result_list.append(item.replace(symbol, '').strip()) # очистили от ненужных символов

		# удаляем одинаковые требования
		dublicate_list = []
		for item in range(len(result_list)-1):
			doc1 = nlp(result_list[item])
			for item2 in range(item+1, len(result_list)):
				doc2 = nlp(result_list[item2])
				similary = doc1.similarity(doc2)
				if similary * 100 >= 90:
					dublicate_list.append(result_list[item2]) # наполняем список повторяющиемся элементами Я ПОПРОБОВАЛ ПЕРЕДАВАТЬ ITEM2 вместо ITEM

		# copy_result = result_list[::]
		# for item in dublicate_list:
		# 	if item in result_list:
		# 		result_list.remove(item)

		# if result_list == []:
		# 	result_json.append({
		# 	'Название группы': group[-1],
		# 	'Требования': [
		# 		{'Совместимость больше 90': dublicate_list },
		# 		{'Требования без учета совместимости': copy_result}		
		# 	],
		# 	'Вложеннные вакансии': group[:-1]
		# 	})

		# else:
		result_json.append({
			'Название группы': group[-1],
			'Требования': list(set(result_list)),
			'Вложеннные вакансии': group[:-1]
			})


# print(result_json)
with open('aaaaaaaa.json', 'w') as file:
    json.dump(result_json, file, ensure_ascii=False, indent=2)
		