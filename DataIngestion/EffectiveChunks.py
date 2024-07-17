from langchain_community.document_loaders import TextLoader, WebBaseLoader
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter, CharacterTextSplitter
import os
from typing import List
from langchain.schema import Document
from termcolor import COLORS, colored

#for colors
my_colors = list(COLORS.keys())
print(len(my_colors))

file_name_smal='small_sample_file.txt'
# text read and convert to documents
text_reader_path =os.path.join(os.path.dirname(__file__),file_name_smal)
loader_txt = TextLoader(text_reader_path)
document_content :List[Document] = loader_txt.load()


file_content=''
def get_file_content(path:str)->str:
    with open(path) as f:
        file_content= f.read()
    return file_content
   


def getColoredContent(document_content:List[Document])->str:
    content=''
    for i , page in enumerate(document_content):
        content+=colored(document_content[i].page_content,color=my_colors[i%len(my_colors)])
    return content
    

#character text splitter
charcter_splitter = CharacterTextSplitter(chunk_size=30,chunk_overlap=5)
docs =charcter_splitter.create_documents([get_file_content(text_reader_path)])
entier_content=print(getColoredContent(docs))

#RecursivceCharcaterSplitter
print("***************RECURSIVECHARSPLITTER************************")
print("***************RECURSIVECHARSPLITTER************************")
print("***************RECURSIVECHARSPLITTER************************")
rec_char_splitter = RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=5, strip_whitespace=False, keep_separator= True)
docs =rec_char_splitter.create_documents([get_file_content(text_reader_path)])
entier_content=print(getColoredContent(docs))


