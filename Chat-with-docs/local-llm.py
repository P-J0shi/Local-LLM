import streamlit as st
from langchain_ollama.llms import OllamaLLM


model = OllamaLLM(model="llama3.2")
st.title("Local LLM")
prompt = st.chat_input("Enter your question here:")

if prompt:
        response = model.invoke(prompt)
        st.write(response)