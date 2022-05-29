from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException

from bs4 import BeautifulSoup
from time import sleep
import json


def save(page_source, driver):
    page_source = driver.page_source
    file = open('desc.html', 'w')
    file.write(page_source)
    file.close()


def add_to_json(data):
    with open('JSON.json', 'a') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def parse_descriptions(url):
    file = open('desc.html', 'r')
    soup = BeautifulSoup(file, 'lxml')

    descriptions = soup.find_all('div', class_='styled__Answer-eTxGpd ZiJo')
    result_data = []
    for desc in descriptions:
        try:
            p_tag = f'<p>{desc.find("div", class_="Text_root__3j40U Text_weight-normal__2T_yh Text_lineHeight-l__2v_gr Text_fontStyle-normal__264_c styled__Description-gqzIas boCOdH FontSize_fontSize-20__1rxeY FontSize_fontSize-l-20__30M0U FontSize_fontSize-s-16__1Hj7U Color_color-mineShaft__2PSyK").text}</p>'
        except BaseException:
            p_tag = ''
        ul_tag = []
        for item in desc.find_all('li'):
            ul_tag.append(f'<li>{item.text}</li>')
        result_data.append(f'{p_tag} {" ".join(ul_tag)};')
    return result_data

    # add_to_json({
    #     'Ссылка': url,
    #     'Описания': result_data
    # })


def get_course_program(url):
    options = Options()

    # options.add_argument("--headless") # ФОНОВЫЙ РЕЖИМ
    driver = webdriver.Chrome(options=options)
    driver.get(url.replace('/api', ''))
    driver.implicitly_wait(10)

    course_program_titles = ' ; '.join([item.text for item in driver.find_elements(
        By.XPATH, '//div[@class="Text_root__3j40U Text_weight-normal__2T_yh Text_lineHeight-l__2v_gr Text_fontStyle-normal__264_c styled__Title-jpEqXL dNzVOg FontSize_fontSize-28__C5IlD FontSize_fontSize-l-28__1ho_8 FontSize_fontSize-m-24__cSDz7 FontSize_fontSize-xs-20__rruhO Color_color-inherit__27FNT"]')])
    try:
        buttons_program_descriptions = [item.click() for item in driver.find_elements(
            By.XPATH, "//li[@class='styled__Toggler-jiJmVh gawdid']")]
    except ElementClickInterceptedException:
        pass

    # course_program_descriptions = driver.find_element(By.XPATH, '//div[@class="styled__Toggler-jiJmVh gawdid"]').click()
    save(driver.page_source, driver)
    driver.close()
    driver.quit()

    parse_descriptions(url.replace('/api', ''))


def main():
    file = open('foxford_source.html', 'r')
    soup = BeautifulSoup(file, 'lxml')
    all_courses = soup.find_all(
        'div', class_='styled__Root-jXqSpG daGTGj styled__CourseCard-buiJLf kNLeaB')

    # button = soup.find('button', class_='Button_root__2dkqG Button_basic__2xk6W Button_rounded__2JE2g Button_size-m__Xl-Qj Button_theme-default__1H8st Button_height-52__kpeu- styled__CatalogCardControl-cUquhe jbaHfF Display_display-inline-block__d_JhC FontSize_fontSize-m__3Cy9B PadMarg_padding-left-32__1R_1k PadMarg_padding-right-32__1Lgqk PadMarg_padding-left-m-24__1xsRC PadMarg_padding-right-m-24__2DpRX PadMarg_padding-left-s-20__vlhp3 PadMarg_padding-right-s-20__wxl6R')

    result_data = []
    count = 2
    for course in range(5):
        more_info_url = "https://foxford.ru/api" + \
            all_courses[course].parent['href']
        get_course_program(more_info_url)


main()
