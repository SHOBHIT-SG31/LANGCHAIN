from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1. detailed report 
template1=PromptTemplate(
    template = "Write a detailed prompt on {topic}",
    input_vaariables = ['topic']
)


#2. summary

template2 = PromptTemplate(
    template = "Write a 5 line summary on the following text. /n {text}",   
    input_variables = ['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.text})

result1 = model.invoke(prompt2)

print(result1.text)