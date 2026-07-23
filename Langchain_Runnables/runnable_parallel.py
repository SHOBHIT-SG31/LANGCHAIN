from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()
model1 = ChatGroq(model='llama-3.1-8b-instant')
model2 = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
prompt1 = PromptTemplate(
    template = 'Generate a tweet about the {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model1,parser),
    'linkedin':RunnableSequence(prompt2,model2,parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkedin'])