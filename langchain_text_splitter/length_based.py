from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('D:\Drive D\GenAI\GenAI Langchain\LangChain 03\langchain_document_loaders\DL_MLE Intern JD 2027.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result=splitter.split_documents(docs)
print(result[0])