from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=1.5)

results = model.invoke("Write a 5 line poem on cricket")
print(results.text)
    