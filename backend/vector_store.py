from chromadb import Client
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import Chroma
from langchain.schema import Document
from langchain.embeddings import SentenceTransformerEmbeddings

def load_vector_store(text):
    chunks = text.split("\n\n")
    docs = [Document(page_content=chunk) for chunk in chunks if chunk.strip()]
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma.from_documents(docs, embedding)
