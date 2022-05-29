import json
import xlsxwriter

data = json.load(open('parser_result.json', 'r'))

workbook = xlsxwriter.Workbook('excel_result.xlsx')
sheet = workbook.add_worksheet('Вакансии')



sheet.write(0, 0, 'ID')
sheet.write(0, 1, 'Наименование профессии')
sheet.write(0, 2, 'Уровень должности')
sheet.write(0, 3, 'Специализация')
sheet.write(0, 4, 'Отрасль и сфера применения')
sheet.write(0, 5, 'Опыт работы')
sheet.write(0, 6, 'Зарплата')


row_count = 1
for vacance in data:
    sheet.write(row_count, 0, row_count)
    sheet.write(row_count, 1, vacance['Наименование вакансии'])
    sheet.write(row_count, 2, vacance['Уровень должности'])
    sheet.write(row_count, 3, vacance['Специализация'])
    sheet.write(row_count, 4, vacance['Отрасль применения'])
    sheet.write(row_count, 5, vacance['Опыт работы'])
    sheet.write(row_count, 6, vacance['Зарплата'])

    row_count += 1

workbook.close()



