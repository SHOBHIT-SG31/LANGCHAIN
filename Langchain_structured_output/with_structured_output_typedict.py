from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

class Review(TypedDict):
    summary : str
    sentiment : str 

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("I bought the Lenovo LOQ laptop thinking it would be perfect for gaming and AI/ML work, but honestly it has been disappointing. The brightness control stopped working properly, and sometimes the slider doesnt even respond. Drivers keep disappearing — first the Intel GPU driver went missing, then even the NVIDIA GPU stopped showing in Device Manager. Because of this, graphics performance dropped badly. The battery life is also poor; it drains quickly even with normal use. On top of that, the laptop feels heavy and heats up fast when running Python or data analytics tasks. Overall, its not reliable and I regret choosing it.")

print('Summary: ',result['summary'])
print('sentiment: ',result['sentiment'])