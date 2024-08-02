from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
import os
from langchain.schema import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from my_cosnt import promt,addition_of_two_num
from ModelFac import ModelFactory
import logging

logging.basicConfig(level=logging.WARNING)

formatted_string = promt.format(program="john")
print(formatted_string)

#import all the env variable from .env file
load_dotenv()

os.environ['HUGGINGFACEHUB_API_TOKEN']= os.getenv('HUGGINGFACEHUB_API_TOKEN')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT']="CODE_LLAMA_TEST"
os.environ['LANGCHAIN_TRACING_V2']="true"

# use prompt template of langchain with hugging face
my_template:str="write an esaay on cow in less than 100 words"
my_prompt:PromptTemplate = PromptTemplate(template = my_template)


my_llm=ModelFactory().getGPTModel()
# creating my_chain with LLMChain is old way of doin it and this is deprecated
#my_chain:LLMChain = LLMChain(llm=my_llm, prompt=my_prompt)

my_chain_new = my_prompt | my_llm | StrOutputParser()

response = my_chain_new.invoke()
print(response)





