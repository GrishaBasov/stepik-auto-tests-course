from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)")
    input1.send_keys("Grisha")
    input1 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)") 
    input1.send_keys("Basistov")
    input1 = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)") 
    input1.send_keys("Yo")
    
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(30)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

