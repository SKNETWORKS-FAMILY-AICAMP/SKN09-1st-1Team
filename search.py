import streamlit as st
import pymysql
import pandas as pd

# DB 연결
conn = pymysql.connect(
    host='localhost',
    user='squirrel',
    password='squirrel',
    database='cardb'
)
cur = conn.cursor()

# Streamlit UI 구성
st.title("차량 등록 현황 검색")


# 각 필터 활성화 버튼
use_month_filter = st.checkbox("년월 필터 사용")
use_region_filter = st.checkbox("지역 필터 사용")
use_car_type_filter = st.checkbox("차량 유형 필터 사용")
use_race_type_filter = st.checkbox("사용 유형 필터 사용")
use_vehicle_count_filter = st.checkbox("차량 수 필터 사용")

# 삽입된 년월 데이터 가져오기
cur.execute('select month_year from car_monthly')
rows = cur.fetchall()
month_list = [row[0] for row in rows]

# 년월 필터 조건
if use_month_filter:
    st.subheader("년-월 필터 세부 설정정")
    year_month = st.selectbox('년-월 선택',['전체'] + month_list)
    
    
# 삽입된 지역 데이터 가져오기
# 시도 이름름
cur.execute('select distinct sido_name from car_region')
rows = cur.fetchall()
sido_name_list = [row[0] for row in rows]
#시군구이름 
cur.execute('select sigungu_name from car_region')
rows = cur.fetchall()
sigungu_name_list = [row[0] for row in rows]
    
# 지역 필터 조건
if use_region_filter:
    st.subheader("지역 필터 세부 설정")
    use_sido_filter = st.checkbox("시도명 필터 사용")
    use_sigungu_filter = st.checkbox("시군구 필터 사용")

    sido = None
    sigungu = None

    if use_sido_filter:
        sido = st.multiselect("시도명 선택", ["전체"] + sido_name_list)

    #살짝 기분 좋은 처리
    if use_sigungu_filter and sido:
        sigungu_name_list = []
        selected_sidos = [s for s in sido if s != '전체']
        if selected_sidos:
            format_strings = ','.join(['%s'] * len(selected_sidos))
            cur.execute(f'SELECT DISTINCT sigungu_name FROM car_region WHERE sido_name IN ({format_strings})', tuple(selected_sidos))
            rows = cur.fetchall()
            sigungu_name_list.extend([row[0] for row in rows])
                    
    if use_sigungu_filter:
        sigungu = st.multiselect("시군구 선택", ["전체"] + sigungu_name_list)  # 예시 데이터


# 차량 유형 데이터 검색
cur.execute('select type_name from car_type')
rows = cur.fetchall()
type_name_list = [row[0] for row in rows]

# 차량 유형 필터 조건
if use_car_type_filter:
    st.subheader("차량 유형 필터 세부 설정")
    car_types = st.multiselect("차량 유형 선택",['전체'] + type_name_list)


# 사용 유형 데이터 검색
cur.execute('select race_name from race_type')
rows = cur.fetchall()
race_name_list = [row[0] for row in rows]
    
# 사용 유형 필터 조건
if use_race_type_filter:
    st.subheader("사용 유형 필터 세부 설정")
    race_types = st.multiselect("사용 유형 선택", race_name_list)


# 차량 수 필터 조건
if use_vehicle_count_filter:
    st.subheader("차량 수 필터 세부 설정")
    use_min_count_filter = st.checkbox('최소 차량 수 필터 사용')
    use_max_count_filter = st.checkbox('최대 차량 수 필터 사용')
    
    min_count = None
    max_count = None
    
    if use_min_count_filter:
        min_count = st.number_input("최소 차량 수", min_value=0, value=0) 
    
    if use_max_count_filter:
        max_count = st.number_input("최대 차량 수", min_value=0, value=100000)


# 검색 버튼
if st.button("검색"):
    # 기본 SQL 쿼리
    query = """
    SELECT m.month_year AS 월, r.sido_name AS 시도명, r.sigungu_name AS 시군구, 
           t.type_name AS 차량유형, rc.race_name AS 사용유형, d.vehicle_count AS 차량수
    FROM car_data d
    left JOIN car_monthly m ON d.monthly_id = m.monthly_id
    left JOIN car_region r ON d.region_id = r.region_id
    left JOIN car_type t ON d.type_id = t.type_id
    left JOIN race_type rc ON d.race_id = rc.race_id
    WHERE 1 = 1
    """  # 기본 쿼리
    params = []  # 파라미터 리스트

    # 년월 필터 조건
    if use_month_filter and year_month and year_month != "전체":
        query += " AND m.month_year = %s"
        params.append(year_month)

    # 지역 필터 조건
    if use_region_filter:
        if use_sido_filter and sido and "전체" not in sido:
            query += " AND r.sido_name IN (" + ",".join(["%s"] * len(sido)) + ")"
            params.extend(sido)
        if use_sigungu_filter and sigungu and "전체" not in sigungu:
            query += " AND r.sigungu_name IN (" + ",".join(["%s"] * len(sigungu)) + ")"
            params.extend(sigungu)

    # 차량 유형 필터 조건
    if use_car_type_filter and car_types and "전체" not in car_types:
        query += " AND t.type_name IN (" + ",".join(["%s"] * len(car_types)) + ")"
        params.extend(car_types)

    # 사용 유형 필터 조건
    if use_race_type_filter and race_types and "전체" not in race_types:
        query += " AND rc.race_name IN (" + ",".join(["%s"] * len(race_types)) + ")"
        params.extend(race_types)

    # 차량 수 필터 조건
    if use_vehicle_count_filter:
        if use_min_count_filter and use_max_count_filter:
            query += " AND d.vehicle_count BETWEEN %s AND %s"
            params.extend([min_count, max_count])
        elif use_min_count_filter:
            query += " AND d.vehicle_count >= %s"
            params.append(min_count)
        elif use_max_count_filter:
            query += " AND d.vehicle_count <= %s"
            params.append(max_count)

    # 쿼리 실행
    cur.execute(query, params)
    results = cur.fetchall()

    # 결과 출력
    if results:
        df = pd.DataFrame(results, columns=["월", "시도명", "시군구", "차량유형", "사용유형", "차량수"])
        st.dataframe(df)
    else:
        st.write("검색 결과가 없습니다.")

