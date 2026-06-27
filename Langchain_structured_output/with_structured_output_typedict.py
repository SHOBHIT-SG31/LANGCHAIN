from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

class Review(TypedDict):
    key_themes : Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary : Annotated[str,"A brief summary of the review"]
    sentiment : Annotated[Literal["pos","neg"],"Return sentiment of the review either postive, negative or neutral"]
    pros : Annotated[Optional[list[str]], "Write down all the pros inside the list"]
    cons : Annotated[Optional[list[str]], "Write down all the cons  inside the list"] 
    name : Annotated[Optional[str], "What is the name of reviewer"]  

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The Samsung Galaxy S24 Ultra is one of the most advanced smartphones in the market, blending powerful hardware with AI-driven features. It comes with a titanium frame and Gorilla Glass Armor, making it highly durable while still maintaining a premium look. The highlight is its 200MP main camera with impressive zoom capabilities, supported by AI tools like Circle to Search and Live Translate, which make everyday tasks smarter and more convenient. The Snapdragon 8 Gen 3 processor ensures smooth performance, while the bright AMOLED display offers excellent clarity even under sunlight. Samsung also promises 7 years of software updates, which is a huge plus for long-term users. The built-in S Pen continues to be a productivity booster for note-taking and creative work.

However, the device isn't perfect. It is heavy and bulky, which can make one-handed use uncomfortable. The price is very high, making it less accessible compared to competitors. Charging speeds are slower than rivals, and Samsung doesn't include a charger in the box. Some of the AI features may feel more like gimmicks rather than essentials, and if you already own the S23 Ultra, the upgrade may not feel significant.
                                 
Review by SG31.
""")
print('Key themes:',result['key_themes'])
print('Summary: ',result['summary'])
print('sentiment: ',result['sentiment'])
print('Pros: ',result['pros'])
print('Cons: ',result['cons'])
print(result['name'])

