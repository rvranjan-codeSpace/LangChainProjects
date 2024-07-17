
import streamlit as st
from langchain_openai import OpenAI, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
from langchain.chains.sequential import SequentialChain
from langchain.memory import ConversationBufferMemory

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

os.environ["OPENAI_API_KEY"]= openai_key

# Write own custom template

#intilaize LLM
#OPEN AI LLMS
my_llm = OpenAI(temperature=0.8)

#sreamlit framework
st.title("JIRA CHATBOT")
input_text = st.text_input("Search for a User story")

# Create Memory of the chat
company_name_memory= ConversationBufferMemory(input_key='name',memory_key='key1')
company_desc_mmeory= ConversationBufferMemory(input_key='user_story_name',memory_key='key2')
user_story_name_memory= ConversationBufferMemory(input_key='company_description',memory_key='key3')

#1st Promprt tempalate

first_input_prompt = PromptTemplate(
    input_variables= ['name'],
    template= "Tell me details about in 10 words {name}"
)

# LLM  chain is used to run the prompt template
chain_name = LLMChain(llm=my_llm, prompt= first_input_prompt, verbose= True, output_key= "user_story_name", memory=company_name_memory)

#2nd Promprt tempalate
second_input_prompt = PromptTemplate(
    input_variables= ['user_story_name'],
    template= "Describe in 15 words about {user_story_name}"
)

# LLM  chain is used to run the prompt template
chain_desc = LLMChain(llm=my_llm, prompt= second_input_prompt, verbose= True, output_key= "company_description", memory=company_desc_mmeory)


#3nd Promprt tempalate
third_input_prompt = PromptTemplate(
    input_variables= ['company_description'],
    template= "You are a scrum master Create a JIRA user story for an end to end user cases in {company_description}"
)

# LLM  chain is used to run the prompt template
chain_user_Story = LLMChain(llm=my_llm, prompt= second_input_prompt, verbose= True, output_key= "user_story", memory=user_story_name_memory)

parent_chain = SequentialChain(
    chains=[chain_name, chain_desc, chain_user_Story],
    input_variables=["name"],
    output_variables=['user_story_name','company_description','user_story'],
    verbose= True
)


if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander('Company Name'):
         st.info(company_name_memory.buffer)
    
    with st.expander('Company Description'):
         st.info(company_desc_mmeory.buffer)


