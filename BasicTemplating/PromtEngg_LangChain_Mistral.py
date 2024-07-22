from langchain_community.llms.ollama import Ollama
from langchain.chains.llm import LLMChain
from langchain_core.language_models.llms import BaseLLM
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate

class MistralDemo:
    
    def getLLm(self, model_name)->Ollama:
        return Ollama(model=model_name)

    def generateTemplate(self, sys_msg:str, human_msg:str)->ChatPromptTemplate:
       return ChatPromptTemplate.from_messages(
            [
                ('system',sys_msg),
                ('human',human_msg)
            ]
        )

def main():
    _obj= MistralDemo()

    # Define your prompt using the prompt template
    llm = _obj.getLLm('mistral')
    print(type(llm))
    prompt= _obj.generateTemplate("You are a helpful AI assistant","what is {your_input}")
    print(prompt)
    # Create the chain
    chain = prompt | llm | StrOutputParser()
    result= chain.invoke({"your_input":'Cricket'})
    print(result)

if __name__ == "__main__":
    main()
