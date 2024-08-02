from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

embedings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
query_text='whats in name'
embeddings_result=embedings.embed_query(text=query_text)
#print(embeddings_result)
print(len(embeddings_result))


embeddings_result = embedings.embed_documents([query_text])
print(embeddings_result)

# fibonacci method





