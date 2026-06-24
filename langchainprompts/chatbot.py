# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
# chat_history = []

# while True:
#     user_input = input('You: ')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.text)
#     print('AI: ', result.text)

# print(chat_history)

# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# # Load environment variables (API key etc.)
# load_dotenv()

# # Initialize model
# model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

# # Streamlit page setup
# st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
# st.title("💬 ALASKA")

# # Session state to store chat history
# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# # Display previous messages
# for msg in st.session_state["messages"]:
#     if msg["role"] == "user":
#         st.chat_message("user").markdown(msg["content"])
#     else:
#         st.chat_message("assistant").markdown(msg["content"])

# # Chat input box
# user_input = st.chat_input("Type your message...")

# if user_input:
#     # Show user message
#     st.chat_message("user").markdown(user_input)
#     st.session_state["messages"].append({"role": "user", "content": user_input})

#     # Get AI response
#     response = model.invoke(user_input)

#     # Show AI response
#     st.chat_message("assistant").markdown(response.text)
#     st.session_state["messages"].append({"role": "assistant", "content": response.text})

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

# Streamlit page setup
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("💬 ALASKA")

# Keep chat history in session
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Show previous messages
for i, msg in enumerate(st.session_state["chat_history"]):
    if i % 2 == 0:  # user messages (even index)
        st.chat_message("user").markdown(msg)
    else:           # AI messages (odd index)
        st.chat_message("assistant").markdown(msg)

# Input box at bottom
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state["chat_history"].append(user_input)

    # Get AI response (send full history if you want context)
    response = model.invoke(st.session_state["chat_history"])

    # Show AI reply
    st.chat_message("assistant").markdown(response.text)
    st.session_state["chat_history"].append(response.text)
