# 패키지지
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # 키보드 입력
from selenium.webdriver.common.by import By         # 태그 조회 방식 지정 (요소 선택)
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlretrieve

# -----------------------------------------------------
######### 1 MySQL에서 table정보 가져오기
# -----------------------------------------------------

import mysql.connector
import requests
from bs4 import BeautifulSoup

# MySQL 연결 설정
connection = mysql.connector.connect(
    host='localhost',
    user='squirrel',
    password='squirrel',
    database='car_info_db'
)
cursor = connection.cursor()


keyword = f'{car_name} 정보'
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}'


cursor.execute("SELECT id, name, url FROM car_info_table")
cars = cursor.fetchall()

print('첫번째 결과 : SQL 불러온 테이블 출력 가져오기')
print(cars)
print("-"*50)

# -----------------------------------------------------
######### 2 URL 이동후 웹 스크래핑
# -----------------------------------------------------

driver = webdriver.Chrome()

for car in cars:
    url = car[2]
    driver.get(url)
    time.sleep(1)
    # URL주소로 이동
    
    '''
    driver = webdriver.Chrome()
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=36347970&qvt=0&query=2025%20%EB%A9%94%EB%A5%B4%EC%84%B8%EB%8D%B0%EC%8A%A4-%EB%B2%A4%EC%B8%A0%20GLE%20%EC%BF%A0%ED%8E%98'
    driver.get(url)
    time.sleep(2)
    '''
    # 기본 정보 탭으로 이동
    # 버튼 이동
    x_path = '//*[@id="main_pack"]/div[3]/div[1]/div/div[3]/div/div/ul/li[3]/a/span[2]'
    btn = driver.find_element(By.XPATH, f"{x_path}")
    btn.click()
    time.sleep(1)


    # 차량 데이터 수집
    car_data = []
    car_area_elems = driver.find_elements(By.CSS_SELECTOR, ".cm_info_box")

    for car_area_elem in car_area_elems:
        soup = BeautifulSoup(car_area_elem.get_attribute("outerHTML"), "html.parser")
        
        car_info_dict = {}

        for dt, dd in zip(soup.find_all("dt"), soup.find_all("dd")):
            label = dt.text.strip()
            value = dd.text.strip()
            car_info_dict[label] = value

        car_data.append(car_info_dict)

driver.quit()  # WebDriver 종료

# -----------------------------------------------------
########## 3 테이블 병합
# -----------------------------------------------------




# -----------------------------------------------------
########## 4 MySQL로 저장
# -----------------------------------------------------

import mysql.connector
import requests
from bs4 import BeautifulSoup

# 1. MySQL 연결 설정
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

cursor = connection.cursor()



#-------------------------------



# 테이블 수정

cursor.execute(
"""ALTER TABLE car_info_table
ADD COLUMN price VARCHAR(255),
ADD COLUMN fuel VARCHAR(255),
ADD COLUMN mileage VARCHAR(255),
ADD COLUMN power VARCHAR(255),
ADD COLUMN torque VARCHAR(255),
ADD COLUMN displacement VARCHAR(255),
ADD COLUMN engine VARCHAR(255),
ADD COLUMN drive VARCHAR(255),
ADD COLUMN transmission VARCHAR(255),
ADD COLUMN length VARCHAR(255),
ADD COLUMN height VARCHAR(255),
ADD COLUMN width VARCHAR(255),
ADD COLUMN wheelbase VARCHAR(255);"""
)

# 가격, 연료, 연비, 출력, 토크, 배기, 엔진, 구동, 변속, 전장, 전고, 전폭, 축거거

# SQL 쿼리 작성 (각 차종에 대해 삽입)
insert_query = """
    INSERT INTO car_info_table (
        name, url, price, fuel, mileage, power, torque, displacement, engine, 
        drive, transmission, length, height, width, wheelbase
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# 반복문을 통해 데이터를 삽입
for car in data:            # data는 크롤링한 데이터
    cursor.execute(insert_query, car)

# 변경 사항을 데이터베이스에 커밋
connection.commit()
