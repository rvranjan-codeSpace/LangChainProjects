from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama



embeddings = (OllamaEmbeddings(model='llama3'))

model = Ollama(model='llama3')
result = model.invoke('what is langchain')
print(result)

result1= embeddings.embed_documents(
    [
        'I am a good body',
        'I am a super goood boy'
    ]
)
print(len(result1))

for index,docs in enumerate(result1):
    print(type(docs[index]))
    print(docs[index])


