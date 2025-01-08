import streamlit as st
import pandas as pd
import mysql.connector

# DB 연결 함수


def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='squirrel',       # 사용자명
        password='squirrel',  # 비밀번호
        database='car_database'  # 사용할 데이터베이스
    )
    return connection



# Streamlit으로 출력
st.title("차량 정보 조회 사이트")

st.write('조회를 원하는 회사를 선택하세요')


# 회사 목록 (예시 데이터)
companies = ['Kia', 'Hyundai', 'Toyota', 'BMW']

# 세션 상태 초기화
if 'selected_company' not in st.session_state:
    st.session_state.selected_company = None
if 'car_list' not in st.session_state:
    st.session_state.car_list = []
if 'selected_car' not in st.session_state:
    st.session_state.selected_car = None



# 회사 선택 UI
selected_company = st.selectbox('차량 회사 선택', companies)

# 선택된 회사에 따른 차량 목록 업데이트 (DB 연동 대신 예시 데이터 사용)
if selected_company != st.session_state.selected_company:
    st.session_state.selected_company = selected_company
    
    # 예시 데이터 (DB에서 가져온다고 가정)
    if selected_company == 'Kia':
        st.session_state.car_list = [
            {'name': 'Kia Sorento', 'price': '3,213~4,161만원', 'mileage': '14.3~16.2 km/ℓ', 'power': '235hp', 'torque': '35.7kg.m'},
            {'name': 'Kia Sportage', 'price': '2,100~3,700만원', 'mileage': '12.5~14.5 km/ℓ', 'power': '200hp', 'torque': '30.0kg.m'}
        ]
    elif selected_company == 'Hyundai':
        st.session_state.car_list = [
            {'name': 'Hyundai Santa Fe', 'price': '2,500~3,800만원', 'mileage': '11.0~13.0 km/ℓ', 'power': '180hp', 'torque': '32.0kg.m'},
            {'name': 'Hyundai Tucson', 'price': '2,100~3,300만원', 'mileage': '13.5~15.0 km/ℓ', 'power': '185hp', 'torque': '34.5kg.m'}
        ]
    elif selected_company == 'Toyota':
        st.session_state.car_list = [
            {'name': 'Toyota RAV4', 'price': '2,800~4,000만원', 'mileage': '12.0~14.0 km/ℓ', 'power': '190hp', 'torque': '33.0kg.m'},
            {'name': 'Toyota Corolla', 'price': '2,100~3,000만원', 'mileage': '14.0~16.0 km/ℓ', 'power': '150hp', 'torque': '28.0kg.m'}
        ]
    elif selected_company == 'BMW':
        st.session_state.car_list = [
            {'name': 'BMW X5', 'price': '7,500~9,000만원', 'mileage': '8.0~10.0 km/ℓ', 'power': '300hp', 'torque': '60.0kg.m'},
            {'name': 'BMW 3 Series', 'price': '5,000~6,500만원', 'mileage': '10.0~12.0 km/ℓ', 'power': '250hp', 'torque': '50.0kg.m'}
        ]

# 차량 목록 출력
if st.session_state.car_list:
    st.write(f"{selected_company} 회사의 차량 목록:")
    for car in st.session_state.car_list:
        if st.button(f"차량명: {car['name']} - 가격: {car['price']}"):
            # 차량 상세 정보를 세션 상태에 저장
            st.session_state.selected_car = car

# 선택된 차량의 상세 정보 표시
if st.session_state.selected_car:
    st.subheader("차량 상세 정보")
    car = st.session_state.selected_car
    st.write(f"**차량명**: {car['name']}")
    st.write(f"**가격**: {car['price']}")
    st.write(f"**연비**: {car['mileage']}")
    st.write(f"**출력**: {car['power']}")
    st.write(f"**토크**: {car['torque']}")





if st.button('kia'):
    st.write('cars info') #f'{cursor.fetchall()}')

if st.button('Hyundai'):
    st.write('현대차량 정보')


