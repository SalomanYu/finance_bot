import json
from selenium import webdriver
from selenium.webdriver.common.by import By

def parse_vacance_requirements(vacance_url, browser):
    
    browser.get(vacance_url)

    browser.implicitly_wait(20)
    requirements = browser.find_element(By.XPATH, "//div[@class='e8mowj42 css-10mimit ecmo2q0']")

    return requirements.text

def create_common_requirements_data():
    with open('result_parse.json', 'r') as file:
        content = json.load(file)
    
    result_data = []
    browser = webdriver.Chrome()
    for vacance, vacance_url in content.items():
        try:
            requirements_vacance = parse_vacance_requirements(vacance_url, browser)
            result_data.append({
                'Вакансия': vacance,
                'Ссылка': vacance_url,
                'Требования': requirements_vacance
            })
        except BaseException:
            print(vacance_url)

    browser.quit()
    with open('requirements.json', 'w') as file:
        json.dump(result_data, file, ensure_ascii=False, indent=2)
    

create_common_requirements_data()