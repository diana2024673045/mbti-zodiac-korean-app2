import streamlit as st 
st.set_page_config(page_title="MBTI + 별자리 + 띠 분석기", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6f2ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

from data import mbti_data, zodiac_data, animal_data
from analyzer import analyze_personality

st.title("♥︎ MBTI + 별자리 + 띠 성격 분석기 ♥︎")
st.markdown("당신의 성격을 세 가지 요소로 알아보세요: **MBTI**, **별자리**, **띠**")

name = st.text_input(" 이름을 입력하세요:", "")

mbti = st.selectbox("⭐️ MBTI를 선택하세요:", list(mbti_data.keys()))
zodiac = st.selectbox("🌙 별자리를 선택하세요:", list(zodiac_data.keys()))
animal = st.selectbox("☀️ 띠를 선택하세요:", list(animal_data.keys()))

if st.button("💫 분석하기"):
    st.subheader(f"♥︎ {name}님의 성격 분석 결과♥︎")
    
    st.markdown(f"**MBTI ({mbti})**: {mbti_data[mbti]}")
    st.markdown(f"**별자리 ({zodiac})**: {zodiac_data[zodiac]}")
    st.markdown(f"**띠 ({animal})**: {animal_data[animal]}")
    
    st.markdown("---")
    st.markdown("### ♥︎ 종합 해석♥︎")
    result = analyze_personality(mbti, zodiac, animal)
    st.markdown(result)
