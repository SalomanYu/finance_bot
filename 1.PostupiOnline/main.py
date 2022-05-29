from bs4 import BeautifulSoup
import requests
import openpyxl
import sys, csv


class PostupiOnlineParser:
	def __init__(self, outputFile):
		# self.book = openpyxl.Workbook() # создаем Таблицу xlsx
		# self.main_page = self.book.active # открываем первую и главую страницу таблицы
		self.fileName = outputFile
		self.row = 2

		# инициализируем колонки
		# self.main_page['A1'] = 'Код направления'
		# self.main_page['B1'] = 'Наименование направления'
		# self.main_page['C1'] = 'Описание направления '
		# self.main_page['D1'] = 'Уровень подготовки'
		# self.main_page['E1'] = 'Ссылка на страницу с направлением'
		# self.main_page['F1'] = 'Предметы'
		# self.main_page['G1'] = 'Наименование ВУЗа'
		# self.main_page['H1'] = 'Логотип ВУЗа'
		# self.main_page['I1'] = 'Тип обучения'
		# self.main_page['J1'] = 'Город'
		self.headers = {
			'accept': '*/*',
			'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
			}

		with open('cvsData.csv', 'w') as file:
			writer = csv.writer(file)

			writer.writerow(
				(
					'Код направления',
					'Наименование направления',
					'Описание направления',
					'Уровень подготовки',
					'Ссылка на страницу с направлением',
					'Предметы',
					'Наименование ВУЗа',
					'Логотип ВУЗа',
					'Тип обучения',
					'Город',
				)
			)



	# Функция запуска парсера
	def run(self):
		main_urls = ('https://postupi.online/specialnosti/bakalavr/', 'https://postupi.online/specialnosti/specialist/', 'https://postupi.online/specialnosti/magistratura/') # специальности по которым будет вестись поиск

		count = 1 # счетчик страниц направлений
		
		"""
	 Берем каждый элемент из наших специальностей и начинаем собирать информацию по их страницам, если страницы с номером count не существует(то есть, страницы данной специальности закончились),
	 мы выходим из цикла while и берем следующий элемент в main_urls
		"""
		
		for target in main_urls:
			count = 1
			print('Пошла ', target)
			while True:
				url = target + f'?page_num={count}'
				current_page = self.getDirection(url)
				if current_page == []:
					break
				else:
					print('Открылась страница', url)
					self.getDirection(url) 
					count +=1



	# Функция для сбора всех направлений на конкретной странице 
	def getDirection(self, url):
		soup = self.callUrl(url)

		specializations = {
			'bakalavr': 'Бакалавриат',
			'specialist': 'Специалитет',
			'magistratura': 'Магистратура'
		}
		current_specialization = specializations[url.split('/')[-2]] # специализация, по которой идет поиск 
		directionsList = soup.find_all('li', class_='list') # вся информация о направлениях на конкретной странице (наименование, ссылка и код)


		for direction in directionsList:
			title = direction.find('h2', class_='list__h') # наименование направления
			link = title.a['href'] # ссылка направления
			code = direction.find('p', class_='list__pre').a.text # код направления
		

			self.DirectionInformation(title=title.text, url=link, code=code, specialization=current_specialization) # передаем полученную информацию следующей функции.


	# Данная функция будет получать ссылку на определенное направление и собирать информацию об этом направлении (Описание и Варианты обучения)
	def DirectionInformation(self, url, title, code, specialization):
		soup = self.callUrl(url)
		exams = []

		# В направлениях магистратуры не указаны предметы ЕГЭ, поэтому чтобы не было ошибок, написал такую проверку
		try:
			subjects = soup.find_all('div', class_='score-box__inner')[1].find_all('div', class_='score-box__item')
			for item in subjects:
				exams.append(item.find('p').text.replace(u'\xa0', u' ')) # replace() удаляет возникающий \xa0 вместо пробела
		except Exception as error:
			pass

		description = soup.find('div', class_='descr-max').text
		variants_links = soup.find_all('a','btn-violet-nd btn-violet-nd_light')
		for variant in variants_links:
			self.VariantsDirection(url=variant['href'], title=title, code=code, description=description, direction_link=url, specialization=specialization, subjects=exams) # передаем полученную информацию следующей функции.


	def VariantsDirection(self, url, title, code, description, direction_link, specialization, subjects):
		counter = 1

		"""
		Цикл While я использовал для просмотра всех страниц вариантов обучения. 
		По сути цикл проверяет есть ли страница со следующим номером или нет, если ее нет, То мы выходим из цикла и переходим к другому профилю обучени
		"""

		while True:
			url = url.split('varianti')[0] + '/varianti' + f'/?page_num={counter}' # таким образом я сделал удобный url адрес страницы (Раньше он был таким: https://postupi.online/specialnost/01.05.01/varianti/?fcost=2&fexams[0]=10&fexams[1]=1&fexams[2]=6)
			soup = self.callUrl(url)

			list_variants = soup.find('ul', 'list-unstyled list-wrap') # список вариантов обучения на определенной странице
			children = list_variants.findChildren('li')
			if children == []:
				break
			else:

				for item in children:
					if item.find('h2') != None: # обходим один неприятный li класс, который содержит стили css, а не информацию о профиле
						
						# Собираем окончательную информацию (наименование, город, лого и тип обучения ВУЗа)
						universityName = item.find('h2').text 
						city = item.find('p', class_='list-var__pre list-var__rt').span.text  
						logo = item.find('img', class_='list-var__logo')['src']
						study_type = item.find('div', class_='list-var__params').span.span.text
						
						if study_type != 'Бюджет' and study_type != 'Платно': # встречаются исключения, у которых не указан тип обучения
							study_type = '___'

						# Записываем в таблицу окончательные данные. Одна строка- один вариант обучения
						# self.main_page[self.row][0].value = code
						# self.main_page[self.row][1].value = title
						# self.main_page[self.row][2].value = description
						# self.main_page[self.row][3].value = specialization
						# self.main_page[self.row][4].value = direction_link
						# self.main_page[self.row][5].value = '; '.join(subjects)
						# self.main_page[self.row][6].value = universityName
						# self.main_page[self.row][7].value = logo
						# self.main_page[self.row][8].value = study_type
						# self.main_page[self.row][9].value = city

						subjects_for_exams = '; '.join(subjects),
						with open('cvsData.csv', 'a') as file:
							writer = csv.writer(file)
							writer.writerow(
									(
									code,
									title,
									description,
									specialization,
									direction_link,
									subjects_for_exams,
									universityName,
									logo,
									study_type,
									city,
										)
								)

						self.row +=1
						print('Запись номер ', self.row-1, specialization) #принт для получения информации о состоянии парсера
				# self.book.save(self.fileName + '.xlsx') # Сохраняем таблицу
				# self.book.close() # Закрываем таблицу

				counter +=1 # открываем следующую страницу с вариантами обучения 

	# Промежуточная функция, для получения доступа к странице
	def callUrl(self, url):
		try:
			request = requests.get(url, 'lxml')
			soup = BeautifulSoup(request.text, 'lxml')
			return soup
			
		except Exception:
			print('[Ошибка!] Не удалось подключиться к сайту. Проверьте интернет-соединение')
			sys.exit()


app = PostupiOnlineParser('DataBase')
app.run()