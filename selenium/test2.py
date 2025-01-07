from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd
import time

company_name = '밴츠'
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=차량'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

view_btn = driver.find_element(By.CSS_SELECTOR, "li[data-value='조회수순|'] a[href='#'] span.menu")  # class가 tablist인 div 찾기
view_btn.click()
time.sleep(1)
cars_info = driver.find_elements(By.CSS_SELECTOR, "div[class='info_box']")
# print(len(cars_info))

page_num_elem = driver.find_element(By.CSS_SELECTOR, 'span._total')
print(page_num_elem.text)

# car_name_list = []
# for car_info in cars_info:
#     car_name = car_info.find_element(By.CSS_SELECTOR, 'a._text')
#     # car_payment = car_info.find_element(By.CSS_SELECTOR, 'span.info_txt')
#     if car_name.text.strip():
#         print(car_name.text)
#         car_name_list.append(car_name.text)
        

        

        
# print(car_name_list)

# 4. 종료
time.sleep(1)
driver.quit()

