from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import Struct
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

schema = [
    ResponseSchema(name='fact1', description='Fact1 about the topic'),
    ResponseSchema(name='fact2', description='Fact2 about the topic'),
    ResponseSchema(name='fact3', description='Fact3 about the topic')
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about topic \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions' : parser.get_format_instructions()}
)

prompt = template.invoke({'topic':'black hole'})
result = model.invoke(prompt)
final_result = parser.parse(result.text)
print(final_result)