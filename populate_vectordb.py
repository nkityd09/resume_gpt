from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

loader = UnstructuredPDFLoader("/content/Ankit_Yadav_Resume.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
texts = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)

#initialize pinecone

pinecone.init(
    api_key="4705a938-fffa-46d0-a157-860f2b7015ff",
    environment="us-west4-gcp-free"
)
index_name="resume"

docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)