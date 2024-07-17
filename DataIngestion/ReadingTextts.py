from langchain_community.document_loaders import TextLoader, WebBaseLoader
from PyPDF2 import PdfReader
import os
import bs4
# https://python.langchain.com/v0.2/docs/integrations/document_loaders/confluence/
# The above link contains all the document loaders in langchain. We can load data from wiki, a2zlyrics


# text read
text_reader_path =os.path.join(os.path.dirname(__file__),'sample3.txt')
print(text_reader_path)
loader_txt = TextLoader(text_reader_path)
document = loader_txt.load()
print(document[0].metadata)
print(document[0].page_content)


#PDF read
pdf_reader_path =os.path.join(os.path.dirname(__file__),'budget_speech.pdf')
pdfreaderObj = PdfReader(pdf_reader_path)
list_of_pages = pdfreaderObj.pages

content=''
for i,pages in enumerate(list_of_pages):
   content+= pages.extract_text()
   
print("**********")
print(f'Content={content}')

# WebBased loader
our_strainer = bs4.SoupStrainer(class_='mw-page-title-main')
web_path_url = 'https://en.wikipedia.org/wiki/India_national_cricket_team'

loader = WebBaseLoader(web_path=web_path_url,bs_kwargs=dict(parse_only=our_strainer))
document = loader.load()
print(document)