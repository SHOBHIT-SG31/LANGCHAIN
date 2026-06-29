from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
parser = JsonOutputParser()
template = PromptTemplate(
    template = 'Give me the name, age and city of a fictional person \n {format_instructions}',
    input_variables = [],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

prompt = template.format()
# print(prompt)
result = model.invoke(prompt)
final_result = parser.parse(result.text)

print(final_result)