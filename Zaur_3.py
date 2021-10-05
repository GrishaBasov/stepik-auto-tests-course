#1 . Зайти на сайт и авторизоваться, как в кейсе 1
#2 . Раскрыть подменю “Services” СЛЕВА
#3 . assert, что в ниспадающем списке есть элементы с текстом “Dates”, “Search”, “User Table” и т.д.
#4 . Закрыть подменю “Services”
#5 . assert, что пункт подменю с текстом “Support” не виден

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = "https://jdi-testing.github.io/jdi-light/index.html"
browser = webdriver.Chrome()

try: 
    
    browser.get(link)

    button = browser.find_element_by_css_selector(".dropdown.uui-profile-menu")
    button.click()

    name = browser.find_element_by_css_selector("#name.uui-form-element")
    name.send_keys("Roman")

    password = browser.find_element_by_css_selector("#password.uui-form-element")
    password.send_keys("Jdi1234")

    login = browser.find_element_by_css_selector("#login-button")
    login.click()

    services_btn = browser.find_element_by_css_selector("a.dropdown-toggle")
    services_btn.click()

    for element in service_dropdown_elements:
        assert EC.visibility_of_element_located((By.XPATH, element))

    
    

finally:
    time.sleep(5)
    browser.quit()