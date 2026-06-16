from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding

# 1. PREPARE OUR CHUNKS
pdf_chunks = [
    "The heart pumps blood to the rest of the body.",
    "The lungs are responsible for oxygenating the blood.",
    "The brain sends electrical signals to the muscles.",
    "Digestion begins in the mouth with saliva.",
    "The kidneys help remove waste from the body.",
    "Bones provide structure and support for movement."
]

# 2. SETUP THE EMBEDDING MODEL
embeddings = DeterministicFakeEmbedding(size=384)

print("--- STARTING THE ASSEMBLY LINE ---")

# 3. CONVERT TEXT TO VECTORS AND STORE THEM
vector_db = FAISS.from_texts(pdf_chunks, embeddings)

# 4. VERIFY THE NUMBER OF ITEMS
total_items = vector_db.index.ntotal

print(f"Success! We converted {len(pdf_chunks)} chunks into vectors.")
print(f"The Memory Bank now contains {total_items} indexed items.")

# 5. SAVE THE VECTOR DATABASE
vector_db.save_local("processed_pdf_bank")

print("✅ Vector database saved successfully!")