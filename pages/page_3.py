
import streamlit as st
import pandas as pd
import pymysql

# --- MySQL 데이터베이스 연결 ---
@st.cache_data
def load_faq_data():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='questiondb',
        charset='utf8mb4'
    )
    query = "SELECT id, question, answer FROM faq_kia"
    faq_df = pd.read_sql(query, connection)
    connection.close()
    return faq_df

# FAQ 데이터 로드
faq_df = load_faq_data()

# 키워드 목록 (각 질문에서 추출한 단어들)
keywords = [
    'Kia', 'Digital', 'Key', 'NFC', 
    '직영', '서비스센터', '운영', '시간', 
     '분실', '구입', '기아멤버스', 
     '차', '관리', '필수', '앱', '서비스',
    '기아', '통합', '계정', 'MyKia', '모바일', '디지털키', 
    '일반', '리모컨', '스마트', '핸들', '락', '해제', '방법',
    '전자식', '파킹', '브레이크', '기능',
    '버튼시동', '스마트', '키', '차량', '중립', '주차',
    '스마트', '키', '배터리', '교환방법',
    '내비게이션', '업데이트'
]

# 키워드 선택 박스에 직접적으로 고유한 키워드만 표시
selected_keyword = st.sidebar.selectbox("키워드를 선택하세요:", ["전체"] + sorted(set(keywords)))

# 선택된 키워드에 맞는 질문들만 필터링
if selected_keyword != "전체":
    filtered_faq_df = faq_df[faq_df["question"].str.contains(selected_keyword, case=False, na=False)]
else:
    filtered_faq_df = faq_df

# Streamlit 앱 시작
st.title("FAQ 게시판")
st.write("기아 차량 관련 FAQ를 게시판 형식으로 확인하세요.")

# 게시판 형식으로 질문 표시
st.subheader("질문 목록")
for index, row in filtered_faq_df.iterrows():
    with st.expander(row["question"]):
        st.write(row["answer"])
