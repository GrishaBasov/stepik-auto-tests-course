from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_css_selector("#num2")
    y = int(y_element.text)
    z = str(x + y)

    select = Select(browser.find_element_by_tag_name("#dropdown"))
    select.select_by_visible_text(z)

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
   

finally:
     
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
