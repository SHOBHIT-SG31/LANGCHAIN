from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header('Research Tool')
# user_input = st.text_input('Enter your prompt')

paper_input = st.selectbox("Select research paper Name",["Attention is all you need","BERT: Pre-training of deep bidirectional transformers","GPT-3 Language model are few-shot learner","Diffusion models beats GANs on Image synthesis"])

style_input=st.selectbox("Select explanation Style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])

length_input=st.selectbox("Select Explanation Length",["Short (1-2paragraph)","Medium (3-5paragraph)","Long(detail explanation)"])

#template
template = PromptTemplate(
    template="""
Please Summarize the research Paper titled "{paper_input}" with the following specification:
Explanation Style : {style_input}
Explanation Length : {length_input}
1. Mathematical details:
    - Include relevant Mathematical equations if present in the paper.
    - Explain the mathematical concept using simple, intutive code snippets where applicable.
2. Analogies:
    - Use relatable analogies to simplify the complex ideas.
If certain information is not available in the paper, respond with "Insufficient information available" instead of guessing .
Ensure the summary is clear, accurate and aligned with the provided style and length.
""",
input_variables=['paper_input','style_input','length_input']

)

# fill the placeholders 
prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input
})

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.text)