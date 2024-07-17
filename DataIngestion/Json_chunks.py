import json
import requests
from langchain.schema import Document
from langchain.text_splitter import RecursiveJsonSplitter, RecursiveCharacterTextSplitter
from termcolor import COLORS, colored
from typing import List, Dict
import os


#Print the chunked json as texts. Each chunks is printed in different colors
my_colors =  list(COLORS.keys())
def getColoredContent(document_content:List[Dict])->str:
    content=''
    for i , page in enumerate(document_content):
        content=colored(json.dumps(document_content[i],indent=4),color=my_colors[i%len(my_colors)])
        print(content)
        #content+=colored(json.dumps(document_content[i],indent=4),color=my_colors[i%len(my_colors)])
    return content
    

# Example 1: When json is present in web
pets_json = requests.get('https://petstore.swagger.io/v2/swagger.json').json()
json_splitter = RecursiveJsonSplitter(max_chunk_size=1000)
create_json= json_splitter.split_json(pets_json)
#print(getColoredContent(create_json))





# Example 2: When json is present in a file
text_reader_path =os.path.join(os.path.dirname(__file__),'sampleOpenAPI.json')

# reading and returning the json , present in file
def get_Json_from_file(path_of_file:str)->dict:
    content=''
    with  open(path_of_file) as f:
        content = f.read()
    return json.loads(content)

# reading and returning the json  in form of text, present in file
def get_Json_from_file_as_text(path_of_file:str)->str:
    content=''
    with  open(path_of_file) as f:
        content = f.read()
    return content


json_splitter = RecursiveJsonSplitter(max_chunk_size=300)
json_content=get_Json_from_file(text_reader_path)
create_json= json_splitter.split_json(json_content,convert_lists=False)
#getColoredContent(create_json)
#print(getColoredContent(create_json))

json_text_splitter =  RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=5, strip_whitespace=False,separators=['method'], keep_separator= True)
json_content_as_text=get_Json_from_file_as_text(text_reader_path)
create_json= json_text_splitter.split_text(json_content_as_text)
#getColoredContent(create_json)
print(getColoredContent(create_json))


