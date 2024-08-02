from langchain_community.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langserve import add_routes


class MistralDemo:
    
    def getLLm_Mistral(self, model_name)->Ollama:
        return Ollama(model=model_name)
    
    def getLLm_OPENAI(self, model_name)->any:
        os.environ['OPENAI_API_KEY']= os.getenv('OPENAI_API_KEY')
        load_dotenv()
        gpt_turbo_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)
        return gpt_turbo_llm

    def generateTemplate(self, sys_msg:str, human_msg:str)->ChatPromptTemplate:
       return ChatPromptTemplate.from_messages(
            [
                ('system',sys_msg),
                ('human',human_msg)
            ]
        )
    
    def getApp(self,chain):
        import uvicorn
        applicaiton= FastAPI(title="Mistral model with Ollama", version= "1.0", description="A simple API server with Mistral AI")
        add_routes(applicaiton, chain, path='/chain')
        uvicorn.run(app=applicaiton,host="127.0.0.1", port=8001)
        

def main():
    _obj= MistralDemo()

    # Define your prompt using the prompt template
    #llm = _obj.getLLm('mistral')
    llm = _obj.getLLm_OPENAI('gpt-3.5-turbo')
   
    prompt= _obj.generateTemplate("You are a helpful AI assistant","what is {your_input}")
    print(prompt)
    # Create the chain
    chain = prompt | llm | StrOutputParser()
    result= chain.invoke({"your_input":'Cricket'})
    _obj.getApp(chain)
    print(result)


if __name__ == "__main__":
    main()
    
