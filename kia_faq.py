
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pymysql

# --- 1) MySQL 데이터베이스 연결 ---
connection = pymysql.connect(
    host='localhost',
    user='squirrel',
    password='squirrel',
    db='cardb',
    charset='utf8mb4'
)
cursor = connection.cursor()

# --------------------------------
    # 김도연 작업

driver = webdriver.Chrome()

url = 'https://www.kia.com/kr/customer-service/center/faq'

driver.get(url)
time.sleep(5)   # 로딩 오래걸려서 5초이상 꼭!


# FAQ 추출 함수
def extract_faq_simple():
    faq_data = []  # 결과 저장용 리스트


    # 모든 질문 버튼 요소 가져오기
    question_buttons = driver.find_elements(By.CSS_SELECTOR, "button[data-cmp-hook-accordion='button']")



    for button in question_buttons:


        # 1. 질문 텍스트 추출
        question_text = button.find_element(By.CLASS_NAME, "cmp-accordion__title").text
        # print(f"질문: {question_text}")


        # 2. 버튼 클릭
        button.click()
        time.sleep(1)  # 답변 로드 대기


        # 3. 답변 텍스트 추출
        panel_id = button.get_attribute("aria-controls")  # 연결된 패널 ID
        answer_panel = driver.find_element(By.ID, panel_id)  # 패널 찾기
        answer_text = answer_panel.text  # 패널의 텍스트 추출
        # print(f"답변: {answer_text}")


        # 4. 결과 저장
        faq_data.append({"question": question_text, "answer": answer_text})
        
        # 쿼리로 DB 저장
        query = "INSERT INTO faq_kia (question, answer) VALUES (%s, %s)"
        cursor.execute(query, (question_text, answer_text))
        connection.commit()  # 변경 사항 저장

        
        
        
        '''
        ## SQL 구문이라면
        ## code는 auto_increment로 사용해서 null
        ## table은 code, ques_content, ans_content로 3가지지
        query ="insert into table1 (code, ques_content, ans_content) values (null,%s,%s)"
        cursor.execute(query, question_text,answer_text)
        '''
    return faq_data

# 함수 실행
faq_results = extract_faq_simple()

driver.quit()

# 결과 출력
for idx, faq in enumerate(faq_results):
    print(idx+1)
    print(f"Question: {faq['question']}")
    print(f"Answer: {faq['answer']}")
    print("-" * 40)


# --- 3) 결과를 파일에 저장 ---
with open("faq_data.txt", "w", encoding="utf-8") as file:
    for idx, info in enumerate(faq_results, start=1):
        file.write(f"[질문 {idx}]\n질문: {info['question']}\n답변: {info['answer']}\n\n")

print("FAQ 데이터가 성공적으로 스크랩되어 데이터베이스와 텍스트 파일에 저장되었습니다.")

driver.quit()
cursor.close()
connection.close()
