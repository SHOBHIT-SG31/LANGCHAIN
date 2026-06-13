from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=1.8)

results = model.invoke("Suggest me 5 indian person names")
print(results.content)
