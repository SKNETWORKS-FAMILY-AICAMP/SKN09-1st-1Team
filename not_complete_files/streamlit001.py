import streamlit as st
import pandas as pd

# 임시 데이터 생성
data = {
    "지역": ["서울", "부산", "대구", "인천", "광주", "대전", "울산"],
    "등록대수": [1000000, 500000, 300000, 400000, 200000, 250000, 180000],
    "주차구획수": [700000, 350000, 250000, 300000, 150000, 200000, 140000],
    "확보율": [70.0, 70.0, 83.33, 75.0, 75.0, 80.0, 77.78],
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# Streamlit 앱 시작
st.title("자동차 등록 대수 및 주차 정보")
st.write("지역별 자동차 등록 대수, 주차 구획수, 주차 공간 확보율을 확인하세요.")

# 지역 선택 셀렉박스
regions = df['지역'].unique()
selected_region = st.selectbox("지역을 선택하세요:", regions)

# 선택한 지역의 데이터 필터링
filtered_data = df[df['지역'] == selected_region]

# 지역 데이터 표시
if not filtered_data.empty:
    st.subheader(f"선택한 지역: {selected_region}")
    st.write("해당 지역의 주차 관련 정보는 다음과 같습니다:")
    st.write(filtered_data)
else:
    st.warning("선택한 지역에 대한 데이터가 없습니다.")

# 전체 데이터 테이블 표시 (옵션)
with st.expander("전체 데이터 보기"):
    st.dataframe(df)
