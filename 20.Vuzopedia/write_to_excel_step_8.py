import json
import xlsxwriter

def write_vuz():
    data = json.load(open('JSON/final_vuz.json'))
    book = xlsxwriter.Workbook('RESULT_VUZ.xlsx')
    sheet = book.add_worksheet(name='ВУЗы')
    row_count = 0
    sheet.write(row_count, 0, 'ID')
    sheet.write(row_count, 1, '№')
    sheet.write(row_count, 2, 'Название ВУза')
    sheet.write(row_count, 3, 'Лого')
    sheet.write(row_count, 4, 'Город')
    sheet.write(row_count, 5, 'Наличие общежития')
    sheet.write(row_count, 6, 'Государственный')
    sheet.write(row_count, 7, 'Воен. уч. Центр ')
    sheet.write(row_count, 8, 'Бюджетные места ')
    sheet.write(row_count, 9, 'Лицензия/аккредитация ')
    sheet.write(row_count, 10, 'Минимальный проходной балл на бюджет')
    sheet.write(row_count, 11, 'Количество бюджетных мест по вузу')
    sheet.write(row_count, 12, 'Минимальный проходной балл на платное')
    sheet.write(row_count, 13, 'Количество платных мест по вузу')
    sheet.write(row_count, 14, 'Минимальная стоимость обучения в вузе в год')
    sheet.write(row_count, 15, 'Ссылка')
    sheet.write(row_count, 16, 'Связь со специальностью')
    sheet.write(row_count, 17, 'Связь с профилями')
    row_count += 1

    for vuz in data:
        sheet.write(row_count, 0, vuz['ID'])
        sheet.write(row_count, 1, row_count)
        sheet.write(row_count, 2, vuz['Название ВУза'])
        sheet.write(row_count, 3, vuz['Лого'])
        sheet.write(row_count, 4, vuz['Город'])
        sheet.write(row_count, 5, vuz['Наличие общежития'])
        sheet.write(row_count, 6, vuz['Государственный'])
        sheet.write(row_count, 7, vuz['Воен. уч. Центр'])
        sheet.write(row_count, 8, vuz['Бюджетные места'])
        sheet.write(row_count, 9, vuz['Лицензия/аккредитация'])
        sheet.write(row_count, 10, vuz['Минимальный проходной балл на бюджет'])
        sheet.write(row_count, 11, vuz['Количество бюджетных мест по вузу'])
        sheet.write(row_count, 12, vuz['Минимальный проходной балл на платное'])
        sheet.write(row_count, 13, vuz['Количество платных мест по вузу'])
        sheet.write(row_count, 14, vuz['Минимальная стоимость обучения в вузе в год'])
        sheet.write(row_count, 15, vuz['Ссылка'])
        try:
            sheet.write(row_count, 16, ' | '.join([str(i) for i in vuz['Связь со специальностью']]))
        except:
            sheet.write(row_count, 16, '')
        try:
            sheet.write(row_count, 17, ' | '.join([str(i) for i in vuz['Связь с профилем']]))
        except:
            sheet.write(row_count, 17, '')
        row_count += 1
    book.close()


def write_specializations():
    data = json.load(open('JSON/final_spec2.json'))
    book = xlsxwriter.Workbook('RESULT_SPEC.xlsx')
    sheet = book.add_worksheet(name='Специальности')
    row_count = 0

    sheet.write(row_count, 0, 'ID')
    sheet.write(row_count, 1, '№')
    sheet.write(row_count, 2, 'Название специальности')
    sheet.write(row_count, 3, 'Картинка')
    sheet.write(row_count, 4, 'Квалификация')
    sheet.write(row_count, 5, 'Связь с ВУЗом')
    sheet.write(row_count, 6, 'Связь с профилем')
    row_count += 1

    for spec in data:
        sheet.write(row_count, 0, spec['ID'])
        sheet.write(row_count, 1, row_count)
        sheet.write(row_count, 2, spec['Название специальности'])
        sheet.write(row_count, 3, spec['Картинка'])
        sheet.write(row_count, 4, spec['Квалификация'])
        sheet.write(row_count, 5, ' | '.join([str(i) for i in spec['Связь с ВУЗОМ (IDS)']]))
        try:
            sheet.write(row_count, 6, ' | '.join([str(i) for i in spec['Связь с профилем (IDS)']]))
        except:
            sheet.write(row_count, 6, '')
        row_count += 1
    book.close()

def write_profiles():
    print('fd')
    data = json.load(open('JSON/final_profile3.json'))
    book = xlsxwriter.Workbook('RESULT_PROFILES.xlsx')
    sheet = book.add_worksheet(name='Профили')
    row_count = 0
    sheet.write(row_count, 0, 'ID')
    sheet.write(row_count, 1, '№')
    sheet.write(row_count, 2, 'Название Профиля')
    sheet.write(row_count, 3, 'Картинка')
    sheet.write(row_count, 4, 'Квалификация')
    sheet.write(row_count, 5, 'Форма обучения')
    sheet.write(row_count, 6, 'Язык обучения')
    sheet.write(row_count, 7, 'Срок обучения')
    sheet.write(row_count, 8, 'Стоимость обучения в год')
    sheet.write(row_count, 9, 'Ссылка')
    sheet.write(row_count, 10, 'Минимальный проходной балл на бюджет')
    sheet.write(row_count, 11, 'Количество бюджетных мест по вузу')
    sheet.write(row_count, 12, 'Минимальный проходной балл на платное')
    sheet.write(row_count, 13, 'Количество платных мест по вузу')
    
    sheet.write(row_count, 14, 'Связь с ВУЗом')
    sheet.write(row_count, 15, 'Связь со специальностью')
    sheet.write(row_count, 16, 'Связь с профессиями')
    sheet.write(row_count, 17, 'Предмет ЕГЭ для поступления 1')
    sheet.write(row_count, 18, 'Предмет ЕГЭ для поступления 2')
    sheet.write(row_count, 19, 'Предмет ЕГЭ для поступления 3')
    sheet.write(row_count, 20, 'Предмет ЕГЭ для поступления 4')
    sheet.write(row_count, 21, 'Предмет ЕГЭ для поступления 5')
    row_count += 1

    for profile in data:
        sheet.write(row_count, 0, profile['ID'])
        sheet.write(row_count, 1, row_count)
        sheet.write(row_count, 2, profile['Название'])
        sheet.write(row_count, 3, profile['Картинка'])
        sheet.write(row_count, 4, profile['Квалификация'])
        sheet.write(row_count, 5, profile['Форма обучения'])
        sheet.write(row_count, 6, profile['Язык обучения'])
        sheet.write(row_count, 7, profile['Срок обучения'])
        sheet.write(row_count, 8, profile['Стоимость обучения в год'])
        sheet.write(row_count, 9, profile['Ссылка'])
        sheet.write(row_count, 10, profile['Минимальный проходной балл на бюджет'])
        sheet.write(row_count, 11, profile['Количество бюджетных мест по вузу'])
        sheet.write(row_count, 12, profile['Минимальный проходной балл на платное'])
        sheet.write(row_count, 13, profile['Количество платных мест'])
        sheet.write(row_count, 14, ' | '.join([str(i) for i in profile['Связь с ВУЗОМ (IDS)']]))
        sheet.write(row_count, 15, ' | '.join([str(i) for i in profile['Связь со специализацией (IDS)']]))
        try:
            sheet.write(row_count, 16, ' | '.join([str(i) for i in profile['Связь с профессией (IDS)']]))
        except:
            sheet.write(row_count, 16, '')
        col_ege = 0
        for key in profile['ЕГЭ']:
            print(key)
            sheet.write(row_count, col_ege+18, f"{key}:{profile['ЕГЭ'][key]}")
            col_ege += 1

        row_count += 1
    book.close()

def write_professions():
    data = json.load(open('JSON/updated_professions.json'))
    book = xlsxwriter.Workbook('RESULT_PROFESSIONS.xlsx')
    sheet = book.add_worksheet(name='Профессии')
    row_count = 0

    sheet.write(row_count, 0, 'ID')
    sheet.write(row_count, 1, '№')
    sheet.write(row_count, 2, 'Название профессии')
    sheet.write(row_count, 3, 'Картинка')
    sheet.write(row_count, 4, 'Описание')
    sheet.write(row_count, 5, 'Ссылка')
    row_count += 1

    for prof in data:
        sheet.write(row_count, 0, prof['ID'])
        sheet.write(row_count, 1, row_count)
        sheet.write(row_count, 2, prof['Название профессии'])
        sheet.write(row_count, 3, prof['Картинка'])
        sheet.write(row_count, 4, prof['Описание'])
        sheet.write(row_count, 5, prof['Ссылка'])

        row_count += 1
    book.close()

if __name__ == "__main__":
    # write_vuz()
    # write_specializations()
    # write_profiles()
    write_professions()