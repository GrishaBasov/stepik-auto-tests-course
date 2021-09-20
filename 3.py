from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/find_link_text" 

browser = webdriver.Chrome()
browser.get(link)
link = browser.find_element_by_link_text("224592")
link.click()

input1 = browser.find_element_by_name('first_name')
input1.send_keys("Grisha")
input1 = browser.find_element_by_name('last_name')
input1.send_keys("Basov")
input1 = browser.find_element_by_class_name('form-control.city')
input1.send_keys("Pushkin")
input1 = browser.find_element_by_id('country')
input1.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(30)
browser.quit()
