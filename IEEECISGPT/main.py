from dotenv import load_dotenv
import os


def configure():
    load_dotenv()
    
configure()

from langchain.llms import OpenAI 
import streamlit as st 

st.title('IEEECIS-GPT')
llm = OpenAI(temperature=0.9,openai_api_key = os.getenv('api_key'))



with st.form('my_form'):
    input_text = st.text_input("What can we do for you today?") 
    submitted = st.form_submit_button('Send')
    
    if submitted:
        st.info((llm(input_text)))