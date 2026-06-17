from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=0)

result = model.invoke("Write 5 line of poem on cricket")
print(result.text)