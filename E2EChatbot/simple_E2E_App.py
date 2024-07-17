import streamlit as st
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

#import all the env variable from .env file
load_dotenv()

#intilize llm
#model has to be chat completeion model and not chat model
def intilizalle()->OpenAI:
   return OpenAI(model_name='gpt-3.5-turbo-instruct',temperature=0.6,openai_api_key=os.getenv('OPENAI_API_KEY'))

st.set_page_config(page_title="This is conversational chat model")
st.header('Simple Langchain Application')

# function to ask any qustion to the model
def getOutput(question)->str:
   my_llm = intilizalle()
   response = my_llm.invoke(question)
   return response

input = st.text_input("Your input: ", key= input)
print(f'Input given by the user:{input}')
response = getOutput(input)
print(f'response given by the AI:{response}')
   
submit = st.button('Submit')

if submit:
   st.subheader('The response is:')
   st.write(response)



