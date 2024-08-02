from langchain_huggingface import HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
class ModelFactory:

    def __init__(self):
        load_dotenv()
        os.environ['HUGGINGFACEHUB_API_TOKEN']= os.getenv('HUGGINGFACEHUB_API_TOKEN')
        os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

    
    def getLlama(self)->any:
        our_repo_id="codellama/CodeLlama-7b-hf"
        llm_code_llama= HuggingFaceEndpoint(repo_id=our_repo_id, max_new_tokens=128, temperature=0.7, huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_TOKEN'))
        return llm_code_llama
    
    def getGPTModel(self)->any:
        gpt_turbo_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)
        return gpt_turbo_llm

def main():
    factory = ModelFactory()
    llama_model = factory.getLlama()
    gpt_model = factory.getGPTModel()
    print("LLaMA Model:", llama_model)
    print("GPT Model:", gpt_model)

if __name__ == "__main__":
    main()