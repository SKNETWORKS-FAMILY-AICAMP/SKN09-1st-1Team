# import pymysql
# import pandas as pd

# #DB 연결
# conn = pymysql.connect(
#     host = 'localhost',
#     user = 'squirrel',
#     password = 'squirrel',
#     database = 'cardb'
# )

# cur = conn.cursor()

# parking_datas = 'data-file/parking_place_rate.xlsx'
# df = pd.read_excel(parking_datas, header=[0])


# #df의 컬럼명들을 지정 (table 컬럼명과 같음)
# df.columns = ['region', 'state_year', 'parking_rate', 'parking_spaces', 'regist_cars']
# # print(df)

# # '-' 값들 싹다 None으로 변환
# df['parking_rate'] = df['parking_rate'].replace('-',None)
# df['parking_spaces'] = df['parking_spaces'].replace('-',None)
# df['regist_cars'] = df['regist_cars'].replace('-',None)

# # region 테이블 삽입
# for region in df['region'].unique():
#     cur.execute('select region_id from regions where region_name = %s', (region,))
#     result = cur.fetchone()
#     if result is None:
#         cur.execute('insert into regions (region_name) values (%s)',(region,))
        
# # parking_stats 테이블 삽입
# # 쿼리가 너무 길어 일단 먼저 설계
# insert_parking_stats = '''
#     insert into parking_stats (region_id, state_year, parking_spaces, regist_cars)
#     values (
#         (select region_id from regions where region_name = %s), %s, %s, %s
#     )
# '''
# for index, row in df.iterrows():
#     # 어디서 에러났는지 확인하기위한 try구문
#     try:
#         cur.execute(insert_parking_stats,(row['region'], row['state_year'], row['parking_spaces'], row['regist_cars']))
#     except Exception as e:
#         print(f'에러 인덱스{index}, {e}')
        
# # parking_rates 데이터 삽입
# # 예도 먼저 sql문
# insert_parking_rates = '''
#     INSERT INTO parking_rates (state_id, parking_rate)
#     VALUES (
#         (SELECT state_id FROM parking_stats WHERE region_id = (SELECT region_id FROM regions WHERE region_name = %s) AND state_year = %s), %s
#     )
# '''
# for index, row in df.iterrows():
#     try:
#         cur.execute(insert_parking_rates, (row['region'], row['state_year'], row['parking_rate']))
#     except Exception as e:
#         print(f'error {index}, {e}')
        
# conn.commit()
# cur.close()
# conn.close()

# # ------------------------------------------------------

# # DB 연결
# conn = pymysql.connect(
#     host='localhost',
#     user='squirrel',
#     password='squirrel',
#     database='cardb'
# )
# cur = conn.cursor()

# # 원하는 도시와 년도 리스트 (예시: 서울특별시, 부산광역시, 2020, 2021년)
# cities = ['서울특별시', '부산광역시']
# years = [2020, 2021]

# # SQL 쿼리 작성: 여러 도시와 년도에 대한 주차장 확보율 조회
# query = """
# SELECT 
#     r.region_name,
#     ps.state_year,
#     pr.parking_rate
# FROM 
#     regions r
# JOIN 
#     parking_stats ps ON r.region_id = ps.region_id
# JOIN 
#     parking_rates pr ON ps.state_id = pr.state_id
# WHERE 
#     r.region_name IN (%s) 
#     AND ps.state_year IN (%s)
# """

# # 쿼리 실행 시 파라미터로 사용할 도시와 년도 리스트를 튜플로 변환
# cities_placeholder = ', '.join(['%s'] * len(cities))  # '%s, %s' 형태로 변환
# years_placeholder = ', '.join(['%s'] * len(years))  # '%s, %s' 형태로 변환

# # 최종 쿼리
# final_query = query % (cities_placeholder, years_placeholder)

# # 파라미터 전달하여 쿼리 실행
# cur.execute(final_query, cities + years)

# # 결과를 DataFrame으로 가져오기
# result = cur.fetchall()
# df = pd.DataFrame(result, columns=['Region', 'Year', 'Parking Rate'])

# # 결과 출력
# print(df)

# # 연결 종료
# cur.close()
# conn.close()
import streamlit as st

st.title("Streamlit Popup 예제")

with st.expander("팝업창 보기"):
    st.write("여기에 팝업과 같은 내용을 표시합니다!")
    st.button("확인")