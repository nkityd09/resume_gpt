import streamlit as st
import openai
import langchain
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone


PAGE_CONFIG = {"page_title":"ResumeGPT", 
               #"page_icon":image, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)

st.title("ChatGPT")

model_name = 'text-embedding-ada-002'
embed = OpenAIEmbeddings(
    model=model_name,
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)
text_field = "text"

pinecone.init(
    api_key=st.secrets["PINECONE_API_KEY"],
    environment=st.secrets["PINECONE_ENV"]
)
index = pinecone.Index('resume')
vectorstore = Pinecone(index, embed.embed_query, text_field)
    
llm = OpenAI(temperature=0, openai_api_key=st.secrets["OPENAI_API_KEY"])
chain = load_qa_chain(llm, chain_type = "stuff")


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi, I'm ResumeGPT, created by Ankit! I can assist you with answering any questions you may have with regards to Ankit's Professional experience. Some Examples: \n 1. What are the companies Ankit has worked for ? \n 2. How many years of experience does Ankit have ? \n 3. Where did Ankit complete his Master's from ? "}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    docs = vectorstore.similarity_search(prompt)
    response = chain.run(input_documents=docs, question=prompt)
    #msg = response.choices[0].message
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

