from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding

# Same embedding model used to create the database
embeddings = DeterministicFakeEmbedding(size=384)

# Load the existing vector database
db = FAISS.load_local(
    "processed_pdf_bank",
    embeddings,
    allow_dangerous_deserialization=True
)

# Ask about the secret password
user_question = "What is the secret password?"

print(f"--- SEARCHING FOR: {user_question} ---")

# Get top 3 results
results = db.similarity_search(user_question, k=3)

print(f"\nFound {len(results)} relevant paragraphs:\n")

for i, doc in enumerate(results):
    print(f"Result #{i+1}:")
    print(f"{doc.page_content}\n")