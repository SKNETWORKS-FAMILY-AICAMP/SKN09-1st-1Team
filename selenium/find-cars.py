from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd

class FindCars:
    
    def company_car_find(company_name):
        url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={company_list}+차량'

        driver = webdriver.Chrome()
        driver.get(url)
        cars_info = driver.find_elements(By.CSS_SELECTOR, '.cm_content_wrap')
        
        
        


