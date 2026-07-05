from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal 
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
model2 = ChatGroq(model='llama-3.1-8b-instant')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['Positive','Negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template = 'Classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt | model1 | parser2
result = classifier_chain.invoke({'feedback':'This is a wonderful smartphone'}).sentiment
print(result)
