import json, csv

file = open('sorted_vacance2.json')
data = json.load(file)

with open('NEW_RESULT.csv', 'w') as f:
		writer = csv.writer(f)	
		writer.writerow(
			(
				'Название группы',
				'Содержимое группы'
			)
		)


counter = 0
for group in data:
	title = group['group']
	items = []
	for item in group['items']:
		items.append(item['second'])

	with open('NEW_RESULT.csv', 'a') as f:
		writer = csv.writer(f)		
		writer.writerow(
			(
				title,
				'||| '.join(items)

			)
		)
	counter += 1
	print(f'Добавлена запись [{counter}]')