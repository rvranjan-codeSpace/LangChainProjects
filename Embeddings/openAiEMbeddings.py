from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_chroma import Chroma

load_dotenv()

os.environ['OPENAI_API_KEY']= os.getenv('OPENAI_API_KEY')
embeddings_1024 = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=1024,)

query_result=embeddings_1024.embed_query("what are you doing")
#print(query_result)


file_content=''
def get_file_content(path:str)->str:
    with open(path) as f:
        file_content= f.read()
    return file_content

file_name_smal='small_sample_file.txt'
# text read and convert to documents
text_reader_path =os.path.join(os.path.dirname(__file__),file_name_smal)
rec_char_splitter = RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=5, strip_whitespace=False, keep_separator= True)
docs =rec_char_splitter.create_documents([get_file_content(text_reader_path)])


# Everytime the created DB has to be fresh .thats y commeting the bellow code. 
# If the code has to work fine, we need to delete ./Chroma_db1 and then execute the code
db = Chroma.from_documents(documents=docs , persist_directory="./Chroma_db1",embedding=embeddings_1024 )

print(f'DB={db} and Type is {type(db)}')

sample_string = 'Python 2.0 was released on 16 October 2000'
result = db.similarity_search(query=sample_string)
print(result)


# loading the db 

db_load = Chroma(persist_directory='./Chroma_db',embedding_function=embeddings_1024)
result_from_load = db_load.similarity_search(query=sample_string)
print(result_from_load[0].page_content)


