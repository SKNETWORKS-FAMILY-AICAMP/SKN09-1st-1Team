import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- 1) MySQL 연결 ---
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='testdb',
    charset='utf8mb4'
)
cursor = connection.cursor()

# car_tb에서 모든 CAR_NAME 가져오기
cursor.execute("SELECT CAR_NAME FROM car_tb")
rows = cursor.fetchall()  # 예: [('K3',), ('메르세데스-벤츠 GLE 쿠페',), ...]

# car_tb에 필요한 컬럼 추가
# 이미 실행된 적이 있다면 에러가 발생할 수 있으므로, 필요시 'IF NOT EXISTS' 로 감싸거나 확인 후 실행

# --- 2) Selenium WebDriver 초기화 ---
driver = webdriver.Chrome()
car_data = []  # 최종 크롤링 결과를 저장할 리스트

# INSERT 구문 (car_tb 테이블에 실제 존재하는 컬럼 14개)
insert_query = """
INSERT INTO car_tb (
    CAR_NAME, CAR_PRICE, CAR_FUEL, mileage, power, torque, displacement,
    engine, drive, transmission, length, height, width, wheelbase
) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# 크롤링한 dt, dd가 가질 수 있는 한글 라벨과 -> DB 컬럼명 매핑
label_to_col = {
    "가격": "CAR_PRICE",
    "연료": "CAR_FUEL",
    "연비": "mileage",
    "출력": "power",
    "토크": "torque",
    "배기": "displacement",
    "엔진": "engine",
    "구동": "drive",
    "변속": "transmission",
    "전장": "length",
    "전고": "height",
    "전폭": "width",
    "축거": "wheelbase",
}

for row in rows:
    db_car_name = row[0]  # DB에서 가져온 차량명 (ex. "K3", "C-Class", ...)

    # --- (A) 네이버 검색 ---
    search_url = f"https://search.naver.com/search.naver?query={db_car_name}"
    driver.get(search_url)
    time.sleep(0.2)

    # --- (B) "기본정보" 탭 클릭 ---
    tabs = driver.find_elements(By.CSS_SELECTOR, "li a span")
    for tab in tabs:
        if tab.text.strip() == "기본정보":
            tab.click()
            break
    time.sleep(0.2)  # 탭 클릭 후 잠깐 대기

    # --- (C) .cm_info_box 영역 탐색 ---
    car_area_elems = driver.find_elements(By.CSS_SELECTOR, ".cm_info_box")
    for area_elem in car_area_elems:
        # 1) 차량 이름 추출 (span.area_text_title > strong._text)
        try:
            car_name_element = area_elem.find_element(By.CSS_SELECTOR, "span.area_text_title strong._text")
            parsed_car_name = car_name_element.text.strip()
        except:
            parsed_car_name = ""

        # 2) dt, dd 쌍 추출
        dts = area_elem.find_elements(By.TAG_NAME, "dt")
        dds = area_elem.find_elements(By.TAG_NAME, "dd")

        # 임시 dict: DB에 넣을 컬럼을 키로, 값은 기본값 ""
        data_dict = {
            "CAR_NAME": db_car_name,  # 혹은 db_car_name 을 저장해도 됨
            "CAR_PRICE": "",
            "CAR_FUEL": "",
            "mileage": "",
            "power": "",
            "torque": "",
            "displacement": "",
            "engine": "",
            "drive": "",
            "transmission": "",
            "length": "",
            "height": "",
            "width": "",
            "wheelbase": ""
        }

        # dt, dd를 순회하며 label을 해석
        for dt_obj, dd_obj in zip(dts, dds):
            label = dt_obj.text.strip()
            value = dd_obj.text.strip()

            # label_to_col 매핑 테이블에 있는 라벨만 추가
            if label in label_to_col:
                col_name = label_to_col[label]  # 예: "가격" -> "price"
                data_dict[col_name] = value

        # 이제 data_dict를 INSERT 하기 위한 튜플로 변환
        insert_values = (
            data_dict["CAR_NAME"],      # %s
            data_dict["CAR_PRICE"],         # %s
            data_dict["CAR_FUEL"],          # %s
            data_dict["mileage"],       # %s
            data_dict["power"],         # %s
            data_dict["torque"],        # %s
            data_dict["displacement"],  # %s
            data_dict["engine"],        # %s
            data_dict["drive"],         # %s
            data_dict["transmission"],  # %s
            data_dict["length"],        # %s
            data_dict["height"],        # %s
            data_dict["width"],         # %s
            data_dict["wheelbase"]      # %s
        )

        # DB INSERT
        cursor.execute(insert_query, insert_values)
        connection.commit()

        # 리스트에도 누적(파일 저장용)
        car_data.append(data_dict)

# --- 3) 종료 ---
driver.quit()
cursor.close()
connection.close()

# --- 4) 결과를 파일에 저장 ---
with open("car_data.txt", "w", encoding="utf-8") as file:
    for idx, info in enumerate(car_data, start=1):
        file.write(f"[차량 {idx}]\n")
        for k, v in info.items():
            file.write(f"{k}: {v}\n")
        file.write("\n")

print("데이터가 car_data.txt 파일에 저장되었습니다.")


