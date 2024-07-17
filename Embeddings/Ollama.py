from langchain_community.embeddings import OllamaEmbeddings
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter


embeddings = (OllamaEmbeddings(model='gemma:2b'))

result1= embeddings.embed_documents(
    [
        'I am a good body',
        'I am a super goood boy'
    ]
)

print(result1)


