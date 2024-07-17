import streamlit as st
from langchain_openai import OpenAI
from langchain.schema import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os

#import all the env variable from .env file
load_dotenv()

#intilize llm
#model has to be chat completion model and not chat model
llm=OpenAI(model_name='gpt-3.5-turbo-instruct',temperature=0.6,openai_api_key=os.getenv('OPENAI_API_KEY'))

st.set_page_config(page_title="This is conversational chat model")
st.header('Simple Langchain Application')

if "converse" not in st.session_state:
        st.session_state['converse']=[
              SystemMessage(content="This is a conversational Chatbot")
        ]
        print(st.session_state)


def get_response(query):
    st.session_state['converse'].append(HumanMessage(content=query))
    print(st.session_state)
    response = llm.invoke(st.session_state['converse'])
    print("*****************************")
    print(response)
    st.session_state['converse'].append(AIMessage(content=response))
    #print(st.session_state)
    print(type[response])
    return ""

get_response("what is the capital of Australia")
    