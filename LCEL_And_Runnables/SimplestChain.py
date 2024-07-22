from langchain.chat_models import  init_chat_model
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

#import all the env variable from .env file
load_dotenv()


os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)

# Without usage of Chain
system_msg= SystemMessage(content="you are a java-Selenium AI assistant")
#print(type(system_msg))
#print(system_msg)
output = model.invoke([
    SystemMessage(content="you are a java-Selenium AI assistant"),
    HumanMessage(content="what is explicit wait")
])
#print(type(output))
#print(output)

# The output can also be retireved as list of documents

System_prompt = ''' you are an expert in {topic} '''
system_prompt_template=ChatPromptTemplate.from_template(System_prompt)
print(system_prompt_template.invoke({'topic':'Selenium'}))

humanMessage = [HumanMessage(content=' you are an expert in Selenium ')]
print(model.invoke(humanMessage))

