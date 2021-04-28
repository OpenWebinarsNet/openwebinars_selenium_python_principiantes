import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class prueba_selenium(unittest.TestCase):
    
    def setUp(self):        
        print("Me ejecuto antes de cada test")
        self.driver = webdriver.Chrome()
        
    def test_a(self):        
        print("Me ejecuto en test_a")
        
        #GOOGLE
        self.driver.get("https://www.google.com")
        time.sleep(2)
        #aceptamos cookies
        self.driver.find_element(By.XPATH, "//div[text()='Acepto']/ancestor::button").click()
        time.sleep(2)
        
        #buscamos texto wikipedia                
        search_bar = self.driver.find_element(By.NAME, "q")
        time.sleep(2)
        search_bar.send_keys("wikipedia")
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)
        
        #BUSQUEDA DE GOOGLE
        self.driver.find_element(By.XPATH, "(//div[@id='search']/descendant::div[@class='g'])[1]/descendant::a[1]").click()
        
        #WIKIPEDIA
        title = self.driver.title
        
        self.assertEqual("Wikipedia, la enciclopedia libre", title)
       
        
    def tearDown(self):
        print("Me ejecuto después de cada test")
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main()
