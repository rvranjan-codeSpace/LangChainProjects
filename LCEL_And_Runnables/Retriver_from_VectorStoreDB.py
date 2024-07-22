from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever


import os
import sys

webbased_loader = WebBaseLoader(web_path='https://en.wikipedia.org/wiki/Roger_Federer')
texts_docs= webbased_loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
splitted_docs = splitter.split_documents(texts_docs)

embedding_1024 = OpenAIEmbeddings()

db = FAISS.from_documents(splitted_docs,embedding=embedding_1024)
# create retriver from vector
retriever:VectorStoreRetriever = db.as_retriever()

# create retriver from document chain


print(retriever)
                   