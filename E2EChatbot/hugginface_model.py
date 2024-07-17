from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key,HUGGINGFACEHUB_API_TOKEN
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

text = "what is capital of India"
llm_open_Ai = OpenAI(openai_api_key = openai_key, temperature= 0.6)
llm_open_Ai.invoke(text)



llm_huggingFace = HuggingFaceEndpoint(repo_id='google/flan-t5-large',model_kwargs={'temprature':0.6,'max_length':64})
#print(llm_huggingFace.invoke(text))

#another way of invoking the the invoke is through chains

prompt_template = '''Tell me a joke on {word} in language {desired_lang}'''
my_prompt = PromptTemplate(
    input_variables=['word','desired_lang'],
    template= prompt_template
)

chain_openai=LLMChain(llm=llm_open_Ai, prompt=my_prompt)
result = chain_openai.invoke({
    "word": 'dog',
    "desired_lang":"english"
})

print(result)



