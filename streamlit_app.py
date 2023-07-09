import streamlit as st
import openai

st.title("Ankit's ResumeGPT")

with st.chat_message("user"):
    st.write("Hello 👋")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")