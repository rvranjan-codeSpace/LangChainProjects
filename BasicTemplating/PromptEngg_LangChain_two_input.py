
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

os.environ["OPENAI_API_KEY"]= openai_key

prompt_template = '''
    convert the sentence: {sentence} in :{desired_lang} '''
#  prompt_Template with one input variable
my_prompt = PromptTemplate(
    input_variables=['sentence','desired_lang'],
    template= prompt_template
)

#OPEN AI LLMS
llm = OpenAI(temperature=0.8)
chain1= LLMChain(llm=llm, prompt=my_prompt)
result = chain1.invoke({'sentence':"Hi, hows u",'desired_lang':"Hindi"})
print(type(result))
print("Generated text:",result['text'])

# printing other parts of the dictionary "RESULT"
if 'tags' in result:
    print('Tags:',result['tags'])
else:
    print("No TAGS")

if 'callbacks' in result:
    print('Tags:',result['callbacks'])
else:
    print("No CALLBACKS")

