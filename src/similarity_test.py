import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding

load_dotenv()

# Using fake embeddings to avoid Google API model errors
embeddings = DeterministicFakeEmbedding(size=384)

print("--- 🔍 Similarity Search Health Check ---")

try:
    loader = PyPDFLoader("docs/textbook.pdf")
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(pages)

    vector_db = FAISS.from_documents(chunks, embeddings)

    query = "What is the main subject of this document?"

    results = vector_db.similarity_search(query, k=2)

    print(f"❓ Query: {query}")
    print(f"✅ Found {len(results)} relevant chunks in the PDF.\n")

    for i, res in enumerate(results):
        print(f"📦 MATCH {i+1} (Page {res.metadata.get('page', 0)+1}):")
        print(res.page_content[:200])
        print("-" * 30)

except Exception as e:
    print(f"❌ TEST FAILED: {e}")