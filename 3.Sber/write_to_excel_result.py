import json
import xlsxwriter


data = json.load(open('bigger_in_level2.json', 'r'))

workbook = xlsxwriter.Workbook('excel_result2.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Соответствия')
worksheet.write(0, 1, 'Вес профессии в соответствии')
worksheet.write(0, 2, 'Уровень должности')
worksheet.write(0, 3, 'Вес профессии в уровне')
worksheet.write(0, 4, 'Наименование професии и различные написания')

vacance_amount = 0
for item in data: vacance_amount +=  len(item['Группа']) # Нужно для цикла 

row_count = 1
for item in data:
    for vacance in item['Группа']:
        try:
            weight_in_level = vacance['Вес в уровне']
        except KeyError:
            weight_in_level = 0
        worksheet.write(row_count, 0, item['id'])
        worksheet.write(row_count, 1, vacance['Вес'])
        worksheet.write(row_count, 2, vacance['Уровень'])
        worksheet.write(row_count, 3, weight_in_level)
        worksheet.write(row_count, 4, vacance['Вакансия'])

        row_count += 1




# my_list = [1,2,3,4]

# for row_num, data in enumerate(my_list):
#     worksheet.write(row_num, 0, data)

workbook.close()