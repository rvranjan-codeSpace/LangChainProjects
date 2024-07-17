from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
import bs4

#import all the env variable from .env file
load_dotenv()


os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT']=os.getenv('WEBSITE_QUERY_AND_SCRAPER')
os.environ['LANGCHAIN_TRACING_V2']="true"


our_strainer = bs4.SoupStrainer(class_='mw-page-title-main') # This will filter out all the texts in this class
#webbased_loader = WebBaseLoader(web_path='https://en.wikipedia.org/wiki/Python_(programming_language))',bs_kwargs=dict(parse_only=our_strainer))
webbased_loader = WebBaseLoader(web_path='https://en.wikipedia.org/wiki/Roger_Federer')
texts_docs= webbased_loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
splitted_docs = splitter.split_documents(texts_docs)
print(len(splitted_docs))

embedding_1024 = OpenAIEmbeddings()
db = FAISS.from_documents(splitted_docs,embedding=embedding_1024)


result = db.similarity_search('when was Roger fedrer born?')
print(result[0].page_content)



