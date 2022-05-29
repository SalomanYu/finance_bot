from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from time import sleep

def save(page_source, driver):
    page_source = driver.page_source
    file = open('foxford_source.html', 'w')
    file.write(page_source)
    file.close()

driver = webdriver.Chrome()
driver.get('https://foxford.ru/catalog/courses')
driver.implicitly_wait(10)


more_courses_button = driver.find_element(By.XPATH, '//button[@class="Button_root__2dkqG Button_rounded__2JE2g Button_fluid__2X0pg Button_size-m__Xl-Qj Button_theme-default__1H8st Button_height-52__kpeu- Display_display-inline-block__d_JhC FontSize_fontSize-m__3Cy9B PadMarg_padding-left-32__1R_1k PadMarg_padding-right-32__1Lgqk PadMarg_padding-left-m-24__1xsRC PadMarg_padding-right-m-24__2DpRX PadMarg_padding-left-s-20__vlhp3 PadMarg_padding-right-s-20__wxl6R"]')
count = 0

def find(driver):
    global count
    more_courses_button = driver.find_element(By.XPATH, '//button[@class="Button_root__2dkqG Button_rounded__2JE2g Button_fluid__2X0pg Button_size-m__Xl-Qj Button_theme-default__1H8st Button_height-52__kpeu- Display_display-inline-block__d_JhC FontSize_fontSize-m__3Cy9B PadMarg_padding-left-32__1R_1k PadMarg_padding-right-32__1Lgqk PadMarg_padding-left-m-24__1xsRC PadMarg_padding-right-m-24__2DpRX PadMarg_padding-left-s-20__vlhp3 PadMarg_padding-right-s-20__wxl6R"]')
    if more_courses_button:
        count+=1
        print(count)
        more_courses_button.click()
    else:
        return False


# for item in range(70):
try:
    elem = WebDriverWait(driver, 1200).until(find)
    all_courses = driver.find_elements(By.XPATH, "//h3[@class='Text_root__3j40U Text_weight-bold__2PiyR Text_lineHeight-s__Z4XCr Text_fontStyle-normal__264_c FontSize_fontSize-28__C5IlD FontSize_fontSize-m-24__cSDz7 Color_color-mineShaft__2PSyK']")
    print(len(all_courses))
    save(driver.page_source, driver)
except TimeoutException:
    print('Ошибка')
    all_courses = driver.find_elements(By.XPATH, "//h3[@class='Text_root__3j40U Text_weight-bold__2PiyR Text_lineHeight-s__Z4XCr Text_fontStyle-normal__264_c FontSize_fontSize-28__C5IlD FontSize_fontSize-m-24__cSDz7 Color_color-mineShaft__2PSyK']")
    print(len(all_courses))
    save(driver.page_source, driver)
