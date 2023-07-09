import streamlit as st
import openai
import langchain

PAGE_CONFIG = {"page_title":"ResumeGPT", 
               #"page_icon":image, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)

st.title("Ankit's ResumeGPT")

with st.chat_message("user"):
    st.write("Hello 👋")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")