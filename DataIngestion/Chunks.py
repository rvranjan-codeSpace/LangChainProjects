from langchain_community.document_loaders import TextLoader, WebBaseLoader
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter, CharacterTextSplitter
import os
from typing import List
from langchain.schema import Document
# https://python.langchain.com/v0.2/docs/integrations/document_loaders/confluence/
# The above link contains all the document loaders in langchain. We can load data from wiki, a2zlyrics


# text read
text_reader_path =os.path.join(os.path.dirname(__file__),'sample3.txt')
print(text_reader_path)
loader_txt = TextLoader(text_reader_path)
document :List[Document] = loader_txt.load()


#text split

splitter = RecursiveCharacterTextSplitter(chunk_size= 300,chunk_overlap=50)
final_doc = splitter.split_documents(document)

for i, doc in enumerate(final_doc):
    print(f'page_num,={i} and conent={doc.page_content}')
    


#converting text to documents

content:str= ""
with open(text_reader_path) as f:
    content= f.read()
    #print(content)

documents = splitter.create_documents([content])
print('Document content\n')
print(documents)

