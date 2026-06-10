import os
import google.generativeai as genai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Simulated PDF chunks
pdf_data = [
    "The CPU is the brain of the computer.",
    "Python is a high-level programming language.",
    "Photosynthesis is how plants make food from sunlight.",
    "The Great Wall of China is a historic landmark."
]

# User query
query = "Tell me about the central processing unit."

print("--- 🧪 Semantic Search Lab ---")
print(f"User Query: '{query}'")

try:
    # Create embeddings for PDF chunks
    pdf_embeddings = [
        genai.embed_content(
            model="models/gemini-embedding-001",
            content=text
        )["embedding"]
        for text in pdf_data
    ]

    # Create embedding for query
    query_embedding = genai.embed_content(
        model="models/gemini-embedding-001",
        content=query
    )["embedding"]

    # Compare query with all chunks
    scores = cosine_similarity([query_embedding], pdf_embeddings)[0]

    # Find best match
    best_match_index = np.argmax(scores)

    print("\nTop Match Found:")
    print(pdf_data[best_match_index])
    print(f"Confidence Score: {scores[best_match_index]:.4f}")

except Exception as e:
    print(f"❌ ERROR: {e}")