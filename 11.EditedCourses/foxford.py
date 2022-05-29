from unicodedata import name
import pandas as pd
import re
import json
from base import create_table
import openpyxl

class Foxford:
    def __init__(self, excelfilename, outputfilename):
        self.input_excel = excelfilename
        self.outputfilename = outputfilename
        self.row_count = 2

        create_table(self.outputfilename)
        self.connect_to_table()

    def run(self):
        for course_index in range(len(self.all_descriptions)):
            # print(self.all_names[course_index])
            # print(self.clear_tags(self.all_descriptions[course_index]))
            self.course_index = course_index
            self.add_course_to_result_table()
            # break
            print(self.all_names[self.course_index], self.row_count)
        print('ВСЁ')
    
    def add_course_to_result_table(self):
        workbook_writer = openpyxl.load_workbook(self.outputfilename)
        sheet_writer = workbook_writer.worksheets[0]
        sheet_writer.cell(self.row_count, 43).value = self.clear_tags(self.all_descriptions[self.course_index]) 

        self.row_count += 1
        workbook_writer.save(self.outputfilename)

    def connect_to_table(self):
        workbook = pd.ExcelFile(self.input_excel)
        sheet = workbook.parse(0)

        self.all_descriptions = list(sheet['О преподавателе'])        
        self.all_names = list(sheet['Название курса'])        

    def clear_tags(self, data):
        without_span = re.sub("<span.*?\>", ' ', str(data)).replace('</span>', ' ')
        without_headers = re.sub("</h\d>", "<br/>", re.sub('<h\d>', '', without_span))
        without_lists = without_headers.replace('<li>', '').replace('</li>', '').replace('<ul>', '').replace('</ul>', '').replace('<p>', '').replace('</p>', '')
        result = re.sub('<strong>|</strong>|<b>|</b>', '', without_lists)
        
        if result.lower() == 'NaT' or 'nan':
            return ''
        return result




bot = Foxford('Non-edited files/Foxford(19.5.2022).xlsx', 'Results/Foxford(19.5.2022).xlsx')
bot.run()
# bot.merge_course_headers_with_contents()
