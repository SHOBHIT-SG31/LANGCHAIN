#Runnable branch is a control flow component in LangChain that allows you to conditionally route input data two different chains or runables on custom logic
# It functions like an if/elif/else Block for chains where you define a set of condition functions each associated with a runnable(example LLM call, prompt chain ,or tools) the first matching condition is executed if no condition matches a default runnable is used if provided 
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
model2 = ChatGroq(model='llama-3.1-8b-instant')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text {text}',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt1, model1, parser)
branch_chain = RunnableBranch(
    (lambda x:len(x.split()) > 200 , RunnableSequence(prompt2, model1, parser )),
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_gen_chain,branch_chain)
print(final_chain.invoke({'topic': 'Sindoor Surgical Strike'}))
