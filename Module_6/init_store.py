from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding

# Create a fake embedding model with 384 dimensions
embeddings = DeterministicFakeEmbedding(size=384)

# Starter text
text_data = ["Initial knowledge base started."]

# Create FAISS vector store
vector_store = FAISS.from_texts(text_data, embeddings)

# Save locally
vector_store.save_local("my_local_bank")

print("--- SYSTEM MESSAGE ---")
print("✅ Local Vector Store 'my_local_bank' has been created!")
print("Look at your VS Code Explorer to see the new folder.")