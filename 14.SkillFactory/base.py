import xlsxwriter

def create_table(filename):
    workbook = xlsxwriter.Workbook(f"{filename}")
    sheet = workbook.add_worksheet()

    sheet.write(0, 0, 'Организатор курса')
    sheet.write(0, 1, 'Название курса')
    sheet.write(0, 2, 'Популярные')
    sheet.write(0, 3, 'Рекомендуемые')
    sheet.write(0, 4, 'Описание курса')
    sheet.write(0, 5, 'Выбор категории')
    sheet.write(0, 6, 'Язык программирования')
    sheet.write(0, 7, 'Выбор подкатегории')
    sheet.write(0, 8, 'Класс')
    sheet.write(0, 9, 'Предмет')
    sheet.write(0, 10, 'Уровень')
    sheet.write(0, 11, 'Баллы')
    sheet.write(0, 12, 'Сертификат')
    sheet.write(0, 13, 'Формат')
    sheet.write(0, 14, 'Тип')
    sheet.write(0, 15, 'Язык')
    sheet.write(0, 16, 'Продолжительность в неделях')
    sheet.write(0, 17, 'Ссылка на страницу')
    sheet.write(0, 18, 'Вариант для парсинга')
    sheet.write(0, 19, 'Дата начала')
    sheet.write(0, 20, 'Удостоверение о повышении клалификации')
    sheet.write(0, 21, 'Сертификат о прохождении курса')
    sheet.write(0, 22, 'Диплом об окончании')
    sheet.write(0, 23, 'Практико-ориентированность')
    sheet.write(0, 24, 'Наставник')
    sheet.write(0, 25, 'Помощь в трудоустройстве')
    sheet.write(0, 26, 'Наработка портфолио')
    sheet.write(0, 27, 'Рассрочка')
    sheet.write(0, 28, 'Налоговый вычет')
    sheet.write(0, 29, 'Обложка курса')
    sheet.write(0, 30, 'Картинка курса')
    sheet.write(0, 31, 'Приветственное видео')
    sheet.write(0, 32, 'Старая цена')
    sheet.write(0, 33, 'Цена')
    sheet.write(0, 34, 'Срок рассрочки в месяцах')
    sheet.write(0, 35, 'Платеж по рассрочке в рублях')
    sheet.write(0, 36, 'Навыки')
    sheet.write(0, 37, 'Программное обеспечение')
    sheet.write(0, 38, 'Модульный курс')
    sheet.write(0, 39, 'Программа курса')
    sheet.write(0, 40, 'Фото преподавателя')
    sheet.write(0, 41, 'ФИО преподавателя')
    sheet.write(0, 42, 'О преподавателе')
    sheet.write(0, 43, 'Описание преподавателя')
    sheet.write(0, 44, 'Для кого курс')
    sheet.write(0, 45, 'Преимущества')
    sheet.write(0, 46, 'Партнеры')
    sheet.write(0, 47, 'Лого партнеров')
    sheet.write(0, 48, 'Требуемые знания')

    workbook.close()