# Import the FAISS class to handle our vector database
from langchain_community.vectorstores import FAISS
# Import the same embedding model we have been using
from langchain_community.embeddings import DeterministicFakeEmbedding

# 1. SETUP THE MODEL: Must match the size (384) from previous lessons
embeddings = DeterministicFakeEmbedding(size=384)

# 2. LOAD THE EXISTING BANK: We are opening the folder we created in Topic 5
# We use allow_dangerous_deserialization=True because we trust our own local files
db = FAISS.load_local("processed_pdf_bank", embeddings, allow_dangerous_deserialization=True)

print(f"Initial count in the bank: {db.index.ntotal}")

# 3. NEW INFORMATION: This is the data we want to 'Upsert'
new_data = [
    "I enjoy learning Artificial Intelligence and Machine Learning.",
    "I practice Python programming every day to improve my coding skills.",
    "I am building AI projects and learning about vector databases and RAG systems."
]

# 4. THE UPSERT COMMAND: Adding new chunks to the existing database
db.add_texts(new_data)

# 5. SAVE THE UPDATED BANK: Overwriting the folder with the new, bigger 'brain'
db.save_local("processed_pdf_bank")

print("--- UPSERT SUCCESSFUL ---")
print(f"New count in the bank: {db.index.ntotal}")
print("The new information has been merged into 'processed_pdf_bank'.")
