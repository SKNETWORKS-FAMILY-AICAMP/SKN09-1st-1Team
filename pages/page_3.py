import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 임시 데이터: 질문과 답변
faq_data = {
    "질문": [
        "주차장 이용 시간은 어떻게 되나요?",
        "주차 요금은 얼마인가요?",
        "장애인 전용 주차 공간은 어디에 있나요?",
        "전기차 충전소는 어디에 있나요?",
        "주차장 예약은 가능한가요?",
        "분실물이 발생했을 때 어떻게 해야 하나요?",
    ],
    "답변": [
        "주차장은 24시간 운영됩니다.",
        "주차 요금은 1시간에 1,000원입니다.",
        "장애인 전용 주차 공간은 입구 근처에 위치해 있습니다.",
        "전기차 충전소는 주차장 B구역에 있습니다.",
        "죄송하지만, 주차장 예약은 제공되지 않습니다.",
        "분실물이 발생한 경우 관리실에 문의하시기 바랍니다.",
    ]
}

# 데이터프레임 생성
faq_df = pd.DataFrame(faq_data)

# Streamlit 앱 시작
st.title("FAQ 검색 시스템")
st.write("검색어를 입력하시면 가장 유사한 질문과 답변을 보여드립니다.")

# 사용자 질문 입력
user_question = st.text_input("질문을 입력하세요:")

# 검색 버튼
if st.button("검색"):
    if user_question.strip() == "":
        st.warning("질문을 입력하세요.")
    else:
        # TF-IDF 벡터화
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(faq_df["질문"].tolist() + [user_question])
        
        # 유사도 계산
        cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
        similarity_scores = cosine_sim.flatten()

        # 가장 유사한 질문의 인덱스 찾기
        most_similar_index = similarity_scores.argmax()
        most_similar_score = similarity_scores[most_similar_index]

        # 유사도가 일정 수준 이상일 경우 결과 출력
        if most_similar_score > 0.2:  # 유사도 임계값 (0.3 이상인 경우만 출력)
            st.subheader("가장 유사한 질문:")
            st.write(faq_df.iloc[most_similar_index]["질문"])
            st.subheader("답변:")
            st.write(faq_df.iloc[most_similar_index]["답변"])
        else:
            st.warning("유사한 질문을 찾을 수 없습니다. 다시 시도해주세요.")

# 전체 FAQ 보기 (옵션)
with st.expander("FAQ 전체 보기"):
    st.dataframe(faq_df)
