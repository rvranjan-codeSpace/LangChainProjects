from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS,Chroma
from langchain_community.embeddings  import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter
import os


path_of_file = os.path.join(os.path.dirname(__file__),'small_sample_file.txt')

loader = TextLoader(path_of_file)
speech_text=loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
text_splitter_docs=text_splitter.split_documents(speech_text)

ollama_embeddings = OllamaEmbeddings(model='gemma:2b')
db = FAISS.from_documents(text_splitter_docs,embedding=ollama_embeddings)
query_text = 'When was python invented ?'

result_query = db.similarity_search(query_text)
#print(result_query[0].page_content)

# Retriever
# Inorder to use vectorstore db into another Langchain funcitonality we need to convert this to Retirever as below :

retriever = db.as_retriever()
result_query_using_retriever = retriever.invoke(query_text)
#print(result_query_using_retriever)


# FAISS Similarty search with score
result_query_with_score = db.similarity_search_with_score(query_text)
#print(result_query_with_score[0])

# query using vector
embedded_query =ollama_embeddings.embed_query(query_text)
result_with_vectory_query = db.similarity_search_with_score_by_vector(embedded_query)
print(result_with_vectory_query[0])


#### Storing vector DB in local

db.save_local('faiss_index')

new_vector_db= db.load_local('faiss_index',embeddings=ollama_embeddings,allow_dangerous_deserialization=True)
new_search= new_vector_db.similarity_search(query_text)
print("***********************************")
print(new_search[0].page_content)