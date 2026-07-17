from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

prompt = PromptTemplate(
    template = "Suggest a catchy blog title about {topic}",
    input_variables = ["topic"]
)

topic = input("Enter the topic")

# format the prompt manually using prompt template
formatted_prompt = prompt.format(topic=topic)

# call llm directly
blog_title = model.predict(formatted_prompt)

print("Generated Blog Title:", blog_title)