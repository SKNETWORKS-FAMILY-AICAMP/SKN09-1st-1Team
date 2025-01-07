from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver 초기화
driver = webdriver.Chrome()

try:
    # 1. 네이버 접속
    driver.get("https://www.naver.com")
    time.sleep(1)

    # 2. 검색어 입력
    search_box = driver.find_element(By.ID, "query")
    search_box.send_keys("차량")
    search_box.send_keys(Keys.RETURN)
    time.sleep(0.5)

    # 3. "조회수순" 버튼 클릭 (없을 수 있으므로 예외 처리)
    try:
        views_btn = driver.find_element(By.XPATH, "//li[@data-value='조회수순|']")
        views_btn.click()
        time.sleep(0.5)
    except:
        print("'조회수순' 버튼을 찾지 못했습니다. 다음 단계를 진행합니다.")

    ## 이재혁 작업
    page_num_elem = driver.find_element(By.CSS_SELECTOR, "span._total")
    page_num = int(page_num_elem.text)
    next_btn = driver.find_element(
        By.XPATH, '//*[@id="main_pack"]/div[5]/div[2]/div[1]/div/div[4]/div/a[2]'
    )
    count = 0
    ##

    time.sleep(0.5)

    # 4. 차량 리스트 크롤링
    cars_data = []
    car_items = driver.find_elements(By.CSS_SELECTOR, "div.info_box")

    
    for i in range(1, page_num + 1):
        car_items = driver.find_elements(By.CSS_SELECTOR, "div.info_box")
        for item in car_items:
            try:
                title_elem = item.find_element(By.CSS_SELECTOR, "div.info_box")
                if title_elem.text.strip():
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
            cars_data.append(
                {
                    "title": title,
                    "link": link,
                    "image_url": image_url,
                    "info_text": info_text,
                }
            )
                ##
        count += 1
        time.sleep(0.3)
        if count == 52:
            break
        else:
            next_btn.click()



    # 5. 텍스트 파일로 저장
    if cars_data:
        filtered_cars_data = [car for car in cars_data if car['info_text'] and car['info_text'].strip()]
        with open("cars_data.txt", "w", encoding="utf-8") as f:
            for idx, car in enumerate(filtered_cars_data, start=1):
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
    print(len(filtered_cars_data))
    # 6. WebDriver 종료
    driver.quit()
