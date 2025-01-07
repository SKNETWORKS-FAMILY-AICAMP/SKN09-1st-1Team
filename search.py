
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title('전국차량조회')
st.header('')
st.subheader('')

st.write()

reg, typ = st.columns(2)

with reg:
    region_opt = ['인천','선택하세요','서울','제주'] # 옵션 입력 필요
    region_check = st.selectbox('지역을 선택하세요', region_opt, placeholder = '지역을 선택하세요')

# 옵션 입력 필요
with typ:
    type_opt = ['SUV','선택하세요','승용','승합']
    type_check = st.selectbox('확인하고 싶은 내용을 선택하세요',type_opt, placeholder='확인하고 싶은 항목을 선택하세요')

vdf = {
        'Region': ['서울', '부산', '대구', '인천', '광주', '서울', '부산', '대구', '인천', '광주'],
        'Vehicle Type': ['승용', '승용', '승용', '승용', '승용', 'SUV', 'SUV', 'SUV', 'SUV', 'SUV'],
        'Count': [521, 320, 150, 400, 230, 110, 85, 90, 160, 120]
    } 
st.write()
st.write()

if region_check != '선택하세요' or type_check !='선택하세요':
    if st.button('조회'):
    #st.write('선택한 항목 :',region_check,',', type_check)
    #st.write(" ((수정)) ")

        # 차트로 시각화
        if region_check != '선택하세요' and type_check !='선택하세요':
            st.subheader(f'{region_check}지역 {type_check}차량 등록 대수 차트')
        else: 
            st.subheader('조회 차트')

            
        fig, ax = plt.subplots()

        bars = ax.bar(vdf['Region'], vdf['Count'], color='skyblue')
        for bar in bars:
            yval = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width()/2,
                yval + 10,
                int(yval),
                ha = 'center',
                va = 'bottom',
                fontsize = 7,
                color = 'black'
            )
        ax.set_title('vehicle registrations by region', fontsize=12)
        ax.set_xlabel('region', fontsize=8)
        ax.set_ylabel('vehicle', fontsize=8)
        st.pyplot(fig)


