from bs4 import BeautifulSoup
import requests
import sys
import csv
import time
import threading


class PostupiOnlineParser:
	def __init__(self):
		self.row = 2

		self.headers = {
			'accept': '*/*',
			'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
			}

		with open('bakalavriatData.csv', 'w') as file:
			writer = csv.writer(file)

			writer.writerow((
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
		main_urls = ('https://postupi.online/specialnosti/bakalavr/', ) # специальности по которым будет вестись поиск

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
				soup = self.callUrl(url)

				specializations = {
					'bakalavr': 'Бакалавриат',
					'specialist': 'Специалитет',
					'magistratura': 'Магистратура'
				}
				current_specialization = specializations[url.split('/')[-2]] # специализация, по которой идет поиск 
				directionsList = soup.find_all('li', class_='list') # вся информация о направлениях на конкретной странице (наименование, ссылка и код)

				if directionsList == []:
					print('ПАРСИНГ ЗАКОНЧИЛСЯ ', self.row)
					break
				else:
					print('Открылась страница', url)
					for direction in directionsList:
						title = direction.find('h2', class_='list__h') # наименование направления
						link = title.a['href'] # ссылка направления
						code = direction.find('p', class_='list__pre').a.text # код направления
						
						self.DirectionInformation(title=title.text, url=link, code=code, specialization=current_specialization) # передаем полученную информацию следующей функции.


				# current_page = self.getDirection(url)
				# if current_page == []:
				# 	break
				# else:
				# self.getDirection(url) 
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

		if directionsList == []:
			return

		for direction in directionsList:
			title = direction.find('h2', class_='list__h') # наименование направления
			link = title.a['href'] # ссылка направления
			code = direction.find('p', class_='list__pre').a.text # код направления
		
		# print(directionsList)
			# self.DirectionInformation(title=title.text, url=link, code=code, specialization=current_specialization) # передаем полученную информацию следующей функции.



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
			thread = threading.Thread(target=self.VariantsDirection, args=(variant['href'],title,code,description, url, specialization, exams,))
			thread.start()
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


						# if specialization != 'magistratura':
						# 	pass
						# 	# subjects_for_exams = ['; '.join(subjects)]data.
						# 	# print(subjects_for_exams)
						# else:
						# 	subjects_for_exams = '___'

						with open('bakalavriatData.csv', 'a') as file:
							writer = csv.writer(file)
							writer.writerow(
									(
									code,
									title,
									description,
									specialization,
									direction_link,
									', '.join(subjects),
									universityName,
									logo,
									study_type,
									city,
										)
								)

						print('Запись номер ', self.row-1, specialization) #принт для получения информации о состоянии парсера
						self.row +=1


				counter +=1 # открываем следующую страницу с вариантами обучения 

	# Промежуточная функция, для получения доступа к странице
	def callUrl(self, url, retry=10):
		try:
			request = requests.get(url, 'lxml')
			soup = BeautifulSoup(request.text, 'lxml')
			return soup
			
		except Exception as ex:
			time.sleep(4)
			if retry:
				return self.callUrl(url, retry=(retry-1))
			else:
				raise
			

app = PostupiOnlineParser()
app.run()
# app.getDirection('https://postupi.online/specialnosti/magistratura/?page_num=51')