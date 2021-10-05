#1 . Зайти на https://jdi-testing.github.io/jdi-light/index.html
#2 . Авторизоваться через иконку в правом-верхнем углу (
#username: Roman
#pass: Jdi1234)
#3 . assert, что в правом-верхнем углу есть текст “Roman Iovlev”


from selenium import webdriver
import time

try: 
    link = "https://jdi-testing.github.io/jdi-light/index.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".dropdown-toggle")
    button.click()

finally:
    browser.quit