
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.runnables import RunnableBinding
import os
from dotenv import load_dotenv

#import all the env variable from .env file
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')


# create the model
gpt_turbo_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)
prompt_template = '''
Anser the following based on provided context:
    {context}
'''
my_prompt = ChatPromptTemplate.from_template(prompt_template)


## create the vector stor DB
webbased_loader = WebBaseLoader(web_path='https://en.wikipedia.org/wiki/Roger_Federer')
texts_docs= webbased_loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
splitted_docs = splitter.split_documents(texts_docs)

embedding_1024 = OpenAIEmbeddings()

db = FAISS.from_documents(splitted_docs,embedding=embedding_1024)
# create retriver from vector
retrieve_vectorr:VectorStoreRetriever = db.as_retriever()
#print(retrieve_vectorr)

# The output can also be retireved as list of documents

#create_stuff_documents_chain :Create a chain for passing a list of Documents to a model.

ur_document_chain = create_stuff_documents_chain(llm = gpt_turbo_llm,prompt= my_prompt)
#print(type(ur_document_chain))

# Below id the manual way to give the documents inside the context.

result = ur_document_chain.invoke(input={
    "input":"The LangChain Expression Language (LCEL) is a declarative way to compose Runnables",
    "context":[
        Document(page_content='The LangChain Expression Language (LCEL) is a declarative way to compose Runnables into chains. Any chain constructed this way will automatically have sync, async, batch, and streaming support.',        
         meta_Data= "source is wikipedia"    
        )]
})
#print(result)


# create retriver chain

retrieval_chain:RunnableBinding= create_retrieval_chain(retriever=retrieve_vectorr,combine_docs_chain=ur_document_chain)
print(f'type of chain{type(retrieval_chain)}')
#print(retrieval_chain)

# Below is the modernway to get the similarity search . Note the context is not give explictly here. beacuse the context is present 
# in the create_retrieval_chain where we give the argument as document chain

response = retrieval_chain.invoke({"input":"A Wimbledon junior champion in 1998 and former ball boy"})
print(response['answer'])






