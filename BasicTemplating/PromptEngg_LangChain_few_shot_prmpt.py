

from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

os.environ["OPENAI_API_KEY"]= openai_key

# create examples of few shot prompt template

examples = [
    {"Word":"happy","antonym":"sad"},
    {"Word":"tall","antonym":"short"}
]

dic_example= {"Word":"happy","antonym":"sad"}
    

exmample_prompt_template = ''' Word:{Word} 
antonym:{antonym}
'''
print(exmample_prompt_template.format(**dic_example))


#  prompt_Template with one input variable
my_prompt = PromptTemplate(
    input_variables=['Word','antonym'],
    template= exmample_prompt_template
)
print(my_prompt.format(**dic_example))

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt= my_prompt,
    #A prompt template string to put before the examples
    prefix='Give the antonym of every input\n',
    suffix='Word:{input}\n antonym:',
    input_variables=['input'],
    example_separator='\n'
)

print(few_shot_prompt.format(input='big'))

#OPEN AI LLMS
llm = OpenAI(temperature=0.8)
chain1= LLMChain(llm=llm, prompt=few_shot_prompt)
#result = chain1.invoke({'input':'big'})
#print(type(result))
#print("Generated text:",result)



