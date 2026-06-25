# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
# chat_history = [
#     SystemMessage(content='You are a helpful AI assistant')
# ]

# while True:
#     user_input = input('You: ')
#     chat_history.append(HumanMessage(content='user_input'))
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(AIMessage(content='result.text'))
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

# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# # Load API key from .env
# load_dotenv()

# # Initialize Gemini model
# model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

# # Streamlit page setup
# st.set_page_config(page_title="ALASKA Chatbot", page_icon="🤖")
# st.title("💬 ALASKA")

# # Keep chat history in session
# if "chat_history" not in st.session_state:
#     st.session_state["chat_history"] = []

# # Show previous messages
# for i, msg in enumerate(st.session_state["chat_history"]):
#     if i % 2 == 0:  # user messages (even index)
#         st.chat_message("user").markdown(msg)
#     else:           # AI messages (odd index)
#         st.chat_message("assistant").markdown(msg)

# # Input box at bottom
# user_input = st.chat_input("Type your message...")

# if user_input:
#     # Show user message
#     st.chat_message("user").markdown(user_input)
#     st.session_state["chat_history"].append(user_input)

#     # Get AI response (send full history if you want context)
#     response = model.invoke(st.session_state["chat_history"])

#     # Show AI reply
#     st.chat_message("assistant").markdown(response.text)
#     st.session_state["chat_history"].append(response.text)

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from datetime import datetime

# Load API key from .env
load_dotenv()

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

# Streamlit page setup
st.set_page_config(page_title="ALASKA Chatbot", page_icon="🤖")
st.title("💬 ALASKA")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "all_conversations" not in st.session_state:
    st.session_state["all_conversations"] = []

# Sidebar for history + new chat
st.sidebar.title("🗂 Chat History")

# Show past conversations in sidebar
for idx, conv in enumerate(st.session_state["all_conversations"]):
    st.sidebar.write(f"Conversation {idx+1} ({conv['timestamp']})")

# Button to start new conversation
if st.sidebar.button("➕ New Conversation"):
    if st.session_state["chat_history"]:
        # IMPORTANT: use .copy() so old messages are preserved
        st.session_state["all_conversations"].append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": st.session_state["chat_history"].copy()
        })
    # Clear current chat
    st.session_state["chat_history"] = []

# Show current chat (no timestamp here)
for i, msg in enumerate(st.session_state["chat_history"]):
    role = "user" if i % 2 == 0 else "assistant"
    st.chat_message(role).markdown(msg)

# Input box at bottom
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state["chat_history"].append(user_input)

    # Get AI response
    response = model.invoke(st.session_state["chat_history"])
    st.chat_message("assistant").markdown(response.text)
    st.session_state["chat_history"].append(response.text)
