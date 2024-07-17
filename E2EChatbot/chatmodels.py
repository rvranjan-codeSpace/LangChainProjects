from langchain.chat_models import  init_chat_model
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv

#import all the env variable from .env file
load_dotenv()


os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_TRACING_V2']="true"

gpt_turbo_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)
system_msg= SystemMessage(content="you are a java-Selenium AI assistant")
print(type(system_msg))
print(system_msg)
output = gpt_turbo_llm.invoke([
    SystemMessage(content="you are a java-Selenium AI assistant"),
    HumanMessage(content="what is explicit wait")
])
print(type(output))
print(output)

