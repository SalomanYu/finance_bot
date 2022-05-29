import xlrd
from cleaning import remove_stop_words




def get_skills_from_excel(path: str) -> dict:
    """Returned {'id': 'name'} dictionary"""
    book = xlrd.open_workbook(path) # Открываем таблицу
    sheet = book.sheet_by_index(0) # Читаем первую страницу таблицы
    tableTitles = sheet.row_values(0) # Сохраняем все заголовки колонок, чтобы по ним определить номер необходимых колонок
    for titleIndex in range(sheet.ncols): 
        if tableTitles[titleIndex] == 'id': # Если колонка называется id, то запоминаем номер колонки
            id_col = titleIndex
        elif tableTitles[titleIndex] == 'name':
            name_col = titleIndex
    
    # Создаем два генератора, содержащих все айдишники и все наименования соответственно. 
    # Передаем эти генераторы в функцию, создающую словарь из двух списков
    return dict(zip((int(ID) for ID in sheet.col_values(id_col)[1:]), (NAME for NAME in sheet.col_values(name_col)[1:])))

if __name__ == "__main__":
    excel_data = get_skills_from_excel('/home/saloman/Documents/Edwica(Work)/Other/21. Check Repeat Skills/Data/course_skill.xlsx')
    remove_stop_words(excel_data)
    