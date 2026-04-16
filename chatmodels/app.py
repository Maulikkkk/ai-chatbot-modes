import streamlit as st
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# ✅ Get API key from Streamlit secrets
api_key = st.secrets["MISTRAL_API_KEY"]

model = ChatMistralAI(
    model="mistral-small-latest",
    api_key=api_key
)

st.title("🤖 AI Chatbot with Modes")

# --- Mode selection ---
mode_option = st.selectbox(
    "Choose Mode",
    ["Angry", "Funny", "Sad", "Default"]
)

if mode_option == "Angry":
    mode = "You are an angry AI assistant. Respond aggressively, impatiently, and with irritation."
elif mode_option == "Funny":
    mode = "You are a funny AI assistant. Respond with humor, jokes, and witty remarks."
elif mode_option == "Sad":
    mode = "You are a sad AI assistant. Respond in a melancholic, regretful tone."
else:
    mode = "You are a helpful AI assistant."

# --- Initialize state ---
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

# 🔴 Reset if mode changes
if st.session_state.current_mode != mode:
    st.session_state.messages = [SystemMessage(content=mode)]
    st.session_state.current_mode = mode

# 🔴 Reset button
if st.button("🔄 Reset Chat"):
    st.session_state.messages = [SystemMessage(content=mode)]
    st.rerun()

# --- Display chat ---
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# --- Input ---
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.content)