from selenium import webdriver
import time
import unittest



class test(unittest.TestCase):
    def test1(self):
        x = "Congratulations! You have successfully registered!"
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("[class = 'form-control first']")
        input1.send_keys("Grisha")
        input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input") 
        input1.send_keys("Basistov")
        input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input") 
        input1.send_keys("Yo")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(10)

        self.assertEqual(x, "Congratulations! You have successfully registered!", "you should pass")
        browser.quit()

        
    def test2(self):
        x = "Congratulations! You have successfully registered!"
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("[class = 'form-control first']")
        input1.send_keys("Grisha")
        input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input") 
        input1.send_keys("Basistov")
        input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input") 
        input1.send_keys("Yo")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(10)

        self.assertEqual(x, "Congratulations! You have successfully registered!", "Break")
        browser.quit()

        
        
        
if __name__ == "__main__": unittest.main()


