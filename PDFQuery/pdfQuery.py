from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from typing_extensions import Concatenate
from langchain_openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

# Learn how to import the file from parent directoy
# from ..constants is not working perhaps beccause of the virtual enviroment

#print(f'__file={__file__}')
abs_path = os.path.abspath(__file__)
#print(f'abspath= {abs_path}')

os_path_dir_name= os.path.dirname(os.path.abspath(__file__))

#print(f'os_path_dir_name= {os_path_dir_name}')

os_path_dir_name2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(f'os_path_dir_name2= {os_path_dir_name2}')

os.environ['OPENAI_API_KEY'] = openai_key
pdf_reader_path =os.path.join(os.path.dirname(__file__),'budget_speech.pdf')

#print(f'pdf_reader_path={pdf_reader_path}')
#print(pdf_reader_path)

pdf_Reader_obj = PdfReader(pdf_reader_path)

content=''
for i , page in enumerate(pdf_Reader_obj.pages):
    raw_content = page.extract_text()
    if raw_content:
        content += raw_content

text_splitter = CharacterTextSplitter(
    separator= "\n",
    chunk_size = 800,
    chunk_overlap = 200,
    length_function = len
)

texts = text_splitter.split_text(content)

embeddings = OpenAIEmbeddings()
document_search = FAISS.from_texts(texts,embeddings)

chain = load_qa_chain(OpenAI(),chain_type="stuff")

query = "Who is giving this speech ?"

docs = document_search.similarity_search(query)
inputs = {
    "input_documents": docs,
    "question": query
}

answer = chain.invoke(inputs)
print(answer['output_text'])

