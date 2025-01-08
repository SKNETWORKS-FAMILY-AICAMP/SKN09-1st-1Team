#ctrl+A 하고 주석 제거 하면 다시 페이지생성됨됨
import streamlit as st
import pymysql
import pandas as pd

# MySQL 연결 함수
def connect_to_db():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="testdb",
        charset="utf8mb4"
    )
    return connection

# 데이터 가져오기 함수
def fetch_data(query, params=None):
    try:
        connection = connect_to_db()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, params or ())
        result = cursor.fetchall()
        connection.close()
        return result
    except pymysql.MySQLError as e:
        st.error(f"MySQL 오류 발생: {e}")
        return []

# Streamlit 페이지: 차량 정보 조회 시스템
st.title("차량 정보 조회 시스템")
st.subheader("차량 이름을 선택하여 정보를 조회하세요.")

# 1. 차량 이름(car_name) 목록 가져오기
query = "SELECT DISTINCT car_name FROM car_tb"
car_names = [row['car_name'] for row in fetch_data(query)]

if car_names:
    # 차량 이름 선택 셀렉박스
    selected_car_name = st.selectbox("차량 이름을 선택하세요:", car_names)

    # 2. 선택한 차량의 정보 조회
    if selected_car_name:
        query = """
        SELECT *
        FROM car_tb
        WHERE car_name = %s
        """
        car_info = fetch_data(query, (selected_car_name,))

        # 결과 출력
        if car_info:
            df = pd.DataFrame(car_info)
            st.write(f"**{selected_car_name}**의 정보는 다음과 같습니다:")
            st.dataframe(df)
        else:
            st.write(f"**{selected_car_name}**의 정보를 찾을 수 없습니다.")
else:
    st.write("데이터베이스에서 차량 이름 정보를 가져올 수 없습니다.")
