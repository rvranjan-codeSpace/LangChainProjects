from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser, StrOutputParser
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

chat_gpt_turbo_llm = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_key, temperature=0.6)


class CommaSeparatedOutput(BaseOutputParser):
    def parse(self, text:str):
        print(f'str in the output={text}')
        return text.strip().split(':')


system_template = '''
        you are a helpful assitant. WHen the user gives any input, generate the synonym 
        in comma separated
         '''
human_template = "{text}"
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', system_template),
        ('human',human_template)
    ]
)
print(chat_prompt)

chain = chat_prompt | chat_gpt_turbo_llm | CommaSeparatedOutput()
result = chain.invoke({"text":'beautiful'})

print(result)
print(type(result))

chain2 = chat_prompt | chat_gpt_turbo_llm | StrOutputParser()
result2 = chain2.invoke({"text":'beautiful'})
print(f'Output with default StringOutpUtParsers is {result2}')