from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

st.header('Research Tool')
# user_input = st.text_input('Enter your prompt')

paper_input = st.selectbox("Select research paper Name",["Attention is all you need","BERT: Pre-training of deep bidirectional transformers","GPT-3 Language model are few-shot learner","Diffusion models beats GANs on Image synthesis"])

style_input=st.selectbox("Select explanation Style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])

length_input=st.selectbox("Select Explanation Length",["Short (1-2paragraph)","Medium (3-5paragraph)","Long(detail explanation)"])

template = load_prompt('template.json')

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