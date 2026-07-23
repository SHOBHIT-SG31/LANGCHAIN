# Runnable lambda allows you to apply custom python functions within an AI pipeline 
# It act as Middleware Between different AI components Enabling preprocessing transformation ,API calling, filtering end post processing In a Langchain
#example 
# from langchain_core.runnables import RunnableLambda
# def word_counter(text):
#     return len(text.split())
# runnable_word_counter = RunnableLambda(word_counter)
# print(runnable_word_counter.invoke('Hi there how are you?'))

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
model2 = ChatGroq(model='llama-3.1-8b-instant')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)
def word_counter(text):
    return (len(text.split()))

joke_gen_chain = RunnableSequence(prompt1, model1, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_counter': RunnableLambda(word_counter)
    #'word_counter': RunnableLambda(lambda x:len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
print(final_chain.invoke({'topic':'AI'}))