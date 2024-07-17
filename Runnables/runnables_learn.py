
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

os.environ["OPENAI_API_KEY"]= openai_key

prompte = '''you are good boy'''

#OPEN AI LLMS
llm = OpenAI(temperature=0.8)

#result =llm.invoke(prompte)
#print(result)

#####  RUNNABLE PASSTHROUGH ##########

chain_passthrough = RunnablePassthrough() | RunnablePassthrough() | RunnablePassthrough()
result = chain_passthrough.invoke(prompte)
print(result)

#####  RUNNABLE LAMDA ##########

def convertToUpper(text:str)->str:
    return text.upper

chain_lambda = RunnablePassthrough()| RunnableLambda(convertToUpper)
result = chain_lambda.invoke(prompte)
print(result)

#####  RUNNABLE PARALLEL     ##########

chain = RunnableParallel({'x':RunnablePassthrough(),'y':RunnablePassthrough(),'z':RunnablePassthrough()})
result = chain.invoke({'name':'rajan','age':'29'})
print(result)

chain = RunnableParallel({'details':RunnablePassthrough(),'blogDetails':lambda x:x['blog']})
result = chain.invoke({
    'name':'rajan',
    'age':'34',
    'blog':'blogspot.com'
})
print(result)


#####  RUNNABLE ASSIGN:: This assigns a new key     ##########

chain = RunnableParallel(({'x':RunnablePassthrough()})).assign(new_key=RunnableLambda(lambda x:'new_name'))
result= chain.invoke({"name":'kim','age':'2'})
print(result)

