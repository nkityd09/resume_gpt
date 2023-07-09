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
    st.write("""Hi, I'm ResumeGPT, created by Ankit! I can assist you with answering any questions you may have with regards to Ankit's Professional experience \n Some Examples: \n 
    1. What are the companies Ankit has worked for ? \n
    2. How many years of experience does Ankit have ? \n
    3. Where did Ankit complete his Master's from ?
    """)

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")