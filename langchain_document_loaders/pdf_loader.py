from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("DL_MLE Intern JD 2027.pdf")
docs = loader.load()
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
parser = StrOutputParser()
prompt=PromptTemplate(
    template='Generate a advice for '
)