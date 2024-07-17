
import streamlit as st
from langchain_openai import OpenAI

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

os.environ["OPENAI_API_KEY"]= openai_key

#sreamlit framework
st.title("JIRA CHATBOT")
input_text = st.text_input("Search for a User story")

#OPEN AI LLMS
llm = OpenAI(temperature=0.8)


if input_text:
    st.write(llm.invoke(input_text))
    st.table