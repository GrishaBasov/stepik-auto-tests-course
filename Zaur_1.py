#1 . Зайти на https://jdi-testing.github.io/jdi-light/index.html
#2 . Авторизоваться через иконку в правом-верхнем углу (
#username: Roman
#pass: Jdi1234
#3 . assert, что в правом-верхнем углу есть текст “Roman Iovlev”


from selenium import webdriver
import time

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

    user_name = browser.find_element_by_css_selector("#user-name")
    assert "ROMAN IOVLEV" == user_name.text

finally:
    time.sleep(5)
    browser.quit()
