import spacy, json
req = ['Образование высшее техническое;', 'Опыт работы от 3-х лет;', 'Возможно без опыта работы. Решение принимается по результатам собеседования;', 'Высшее (техническое) образование;', '4. Знание типовых конфигураций: Бухгалтерия, Документооорот 1;', 'Опыт разработки SAP ABAP HR / HCM\xa0от\xa03-х лет;', 'Опыт разработки SAP ABAP HR / HCM от 3-х лет;', 'Знание ABAP Web Dynpro, портальных настроек, OO-ABAP, MSS/ESS, SAP Enterprise Portal 7.0 и 7.5;', 'Желательно наличие сертификатов 1С;', 'Знание типовых конфигураций: Бухгалтерия, Документооорот 2.1;', 'Знание разработки, коректировки отчетов и транзакций в системе с учетом требований ( OM, PA, PT, PY, FI-TV );', 'Знание разработки, корректировки отчетов и транзакций в системе с учетом требований ( OM, PA, PT, PY, FI-TV );', 'Опыт разработки межсистемных интерфейсов с использованием IDOC, RFC, ABAP-proxy;', 'Опыт разработки межсистемных интерфейсов с использованием IDOC, RFC, ABAP-proxy;', 'Опыт выгрузки и обработки данных в продуктах Microsoft Office, разработки PDF форм;', 'Опыт выгрузки и обработки данных в продуктах Microsoft Office, разработки PDF форм;', '3. Знание ABAP Web Dynpro, портальных настроек, OO-ABAP, MSS/ESS, SAP Enterprise Portal 0 и 5;', 'Внимательость, ответственность, соблюдение установленных сроков разработок;', 'Внимательность, ответственность, соблюдение установленных сроков разработок;']
nlp = spacy.load('ru_core_news_md')

# new_list = []
# for item in range(len(req)-1):
# 	doc1 = nlp(req[item])
# 	for item2 in range(item+1, len(req)):
# 		doc2 = nlp(req[item2])
# 		similary = doc1.similarity(doc2)
# 		if similary * 100 >= 90:
# 			new_list.append(req[item])

# for item in new_list:
# 	req.remove(item)

# for item in req:print(item)


# Проверяем почему некоторые требования не заполняются на примере "Машиниста бульдозера 6 разряда"


# group = ['Столяр 5 разряда', 'Маляр 4 разряда', 'Электрогазосварщик 5, 6 разряда',
#  'Слесарь КИПиА 5 разряда', 'Электрогазосварщик 5 - 6 разряда Пелымского ЛПУМГ',
#   'Электрогазосварщик 5-6 разряда Сосьвинского ЛПУМГ', 'Электрогазосварщик 5-6 разряда Пунгинского ЛПУМГ',
#    'Электрогазосварщик 5-6 разряда Уральского ЛПУМГ', 'Электрогазосварщик 5, 6 разряда Ивдельского ЛПУМГ',
#     'Машинист бульдозера 6 разряда', 'Водитель вездехода 6 разряда', 'Машинист бульдозера 6 разряда']


group = ['Ведущий инженер отдела планирования и сопровождения проектов', 'Главный специалист отдела планирования \nи сопровождения проектов']


jsonfile = open('../NEW_JSON_REDACT.json')
data = json.load(jsonfile)

group_data = []
for item in group:
	requirements = []
	for vacance in data:
		if item == vacance['title']:
			requirements.append(vacance['requirements'])
	if requirements != []:
		group_data.append({
			'Группа': item,
			'Требования':requirements
			})


print(group_data)

# for group in groups:
# 	group_data = []
# 	for item in group:
# 		requirements = []
# 		for vacance in data:
# 			if vacance['title'] == item:
# 				requirements.append(vacance['requirements'])
# 		if requirements != []:
# 			group_data.append(requirements)
# 	if group_data != []:
# 		common_list = [item for sublist in group_data for sub in sublist for item in sub] # удаляем лишние скобки 
# 		taboo_symbols = ('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '11.', '12.')
# 		result_list = []
# 		for symbol in taboo_symbols:
# 			for item in common_list:
# 				if symbol in item:
# 					result_list.append(item.replace(symbol, '').strip()) # очистили от ненужных символов

# 		# удаляем одинаковые требования
# 		dublicate_list = []
# 		for item in range(len(result_list)-1):
# 			doc1 = nlp(result_list[item])
# 			for item2 in range(item+1, len(result_list)):
# 				doc2 = nlp(result_list[item2])
# 				similary = doc1.similarity(doc2)
# 				if similary * 100 >= 90:
# 					dublicate_list.append(result_list[item]) # наполняем список повторяющиемся элементами

# 		for item in dublicate_list:
# 			if item in result_list:
# 				result_list.remove(item)