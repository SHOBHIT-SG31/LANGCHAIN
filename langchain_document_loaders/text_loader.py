from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
# from langchain_text_splitters import textloader

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
parser = StrOutputParser()
prompt = PromptTemplate(
    template='Write a summary of the following {rap}',
    input_variables=['rap']
)

loader = TextLoader("rap.txt",encoding='utf-8')

docs = loader.load()
chain = prompt | model | parser
print(chain.invoke({'rap':docs[0].page_content}))
# print(type(docs))
# # print(docs[0])
# print(docs[0].page_content)
# print(docs[0].metadata)