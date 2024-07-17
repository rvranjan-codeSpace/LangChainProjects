
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

os.environ["OPENAI_API_KEY"]= openai_key

prompt_template = '''
You are a product owner of {var_comp_name}. Act as an expert creating user stories for {var_comp_name} for end to end journey of a typical use case at {var_comp_name} 
in less than 50 words
'''
#  prompt_Template with one input variable
my_prompt = PromptTemplate(
    input_variables=['var_comp_name'],
    template= prompt_template
)

#OPEN AI LLMS
llm = OpenAI(temperature=0.8)
chain1= LLMChain(llm=llm, prompt=my_prompt)
result = chain1.invoke('Altimetrik')
print(type(result))
print("Generated text:",result['text'])

if 'tags' in result:
    print('Tags:',result['tags'])
else:
    print("No TAGS")

if 'callbacks' in result:
    print('Tags:',result['callbacks'])
else:
    print("No CALLBACKS")

