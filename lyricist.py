from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(api_key=OPENAI_API_KEY)

st.title("AI 작곡가")

topic_input = st.text_input("주제를 입력하세요")

if topic_input:
    with st.spinner("가사 작성중..."):
        result = chat_model.invoke(topic_input + "에 대한 노래 가사를 써 줘").content
        st.write(result)

