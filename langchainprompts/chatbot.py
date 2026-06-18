# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

# while True:
#     user_input = input('You: ')
#     if user_input == 'exit':
#         break
#     result = model.invoke(user_input)
#     print('AI: ', result.text)

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables (API key etc.)
load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

# Streamlit page setup
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("💬 ALASKA")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Chat input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Get AI response
    response = model.invoke(user_input)

    # Show AI response
    st.chat_message("assistant").markdown(response.text)
    st.session_state["messages"].append({"role": "assistant", "content": response.text})
