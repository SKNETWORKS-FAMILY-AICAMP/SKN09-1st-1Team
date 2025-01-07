from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver 초기화
driver = webdriver.Chrome()

try:
    # 1. 네이버 접속
    driver.get('https://www.naver.com')
    time.sleep(1)

    # 2. 검색어 입력
    search_box = driver.find_element(By.ID, 'query')
    search_box.send_keys('차량')
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # 3. "조회수순" 버튼 클릭 (없을 수 있으므로 예외 처리)
    try:
        views_btn = driver.find_element(By.XPATH, "//li[@data-value='조회수순|']")
        views_btn.click()
        time.sleep(2)
    except:
        print("'조회수순' 버튼을 찾지 못했습니다. 다음 단계를 진행합니다.")

    

    # 4. 차량 리스트 크롤링
    cars_data = []
    car_items = driver.find_elements(By.CSS_SELECTOR, "div.info_box")

    if not car_items:
        print("차량 리스트 요소(.list_item._list_panel)를 찾지 못했습니다.")
    else:
        
        for item in car_items:
            # (1) 제목, 링크, 이미지
            try:
                title_elem = item.find_element(By.CSS_SELECTOR, "div.info_box")
                title = title_elem.text.strip()
                link = title_elem.get_attribute("href")
            except:
                title = "제목 불러오기 실패"
                link = "링크 불러오기 실패"

            try:
                image_elem = item.find_element(By.CSS_SELECTOR, ".thumb_area")
                image_url = image_elem.get_attribute("src")
            except:
                image_url = "이미지 불러오기 실패"

            # (2) 차량 정보 박스 전체 텍스트
            #    item(한 개 블록) 자체의 텍스트를 추출
            info_text = item.text.strip()

            # (3) 데이터 저장
            cars_data.append({
                "title": title,
                "link": link,
                "image_url": image_url,
                "info_text": info_text
            })

    try:
        views_btn = driver.find_element(By.XPATH, "//li[@data-value='다음|']")
        
        views_btn.click()
        time.sleep(2)
    except:
        print("'조회수순' 버튼을 찾지 못했습니다. 다음 단계를 진행합니다.")



    # 5. 텍스트 파일로 저장
    if cars_data:
        with open("cars_data.txt", "w", encoding="utf-8") as f:
            for idx, car in enumerate(cars_data, start=1):
                f.write(f"[차량 {idx}]\n")
                f.write(f"제목: {car['title']}\n")
                f.write(f"링크: {car['link']}\n")
                f.write(f"이미지 URL: {car['image_url']}\n")
                f.write("차량 정보 박스 텍스트:\n")
                f.write(f"{car['info_text']}\n")
                f.write("=" * 80 + "\n")

        print("차량 정보를 cars_data.txt 파일에 저장했습니다.")
    else:
        print("수집된 차량 정보가 없습니다.")

finally:
    # 6. WebDriver 종료
    driver.quit()
