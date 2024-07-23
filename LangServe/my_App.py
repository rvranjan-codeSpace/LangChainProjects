
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
from langchain_core.language_models.llms import BaseLLM
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
import os
import sys
from langserve import add_routes
from starlette.applications import Starlette
from langserve.server import _EndpointConfiguration
import uvicorn

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

os.environ["OPENAI_API_KEY"]= openai_key

#OPEN AI LLMS
llm = OpenAI(temperature=0.8)

#Creating the app
app = FastAPI(title="Simple LangServe App", version="1.0.0",description="POC")
print(type(app))

# Create the End point direclty using OpenAI
route_openAI:_EndpointConfiguration= add_routes(app= app, path="/askanything",runnable=llm)

# Create end point using chat template
prompt_question=ChatPromptTemplate.from_template("Write an essay about {input_var} in 100 words")

route_essay:_EndpointConfiguration= add_routes(app= app, path="/question",runnable=prompt_question|llm)

if __name__=='__main__':
    uvicorn.run(host="127.0.0.1",port=8002,app=app)