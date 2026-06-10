import os
import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Cosine Similarity Function
def calculate_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# Sentences to compare
sentences = [
    "The cat is sleeping on the mat.",
    "A kitten is napping on the rug.",
    "A feline is resting on the floor."
]

try:
    embeddings = []

    for sentence in sentences:
        result = genai.embed_content(
            model="models/gemini-embedding-001",
            content=sentence
        )
        embeddings.append(result["embedding"])

    sim_AB = calculate_similarity(embeddings[0], embeddings[1])
    sim_AC = calculate_similarity(embeddings[0], embeddings[2])

    print("--- 📏 Measuring Meaning (Cosine Similarity) ---")
    print(f"Similarity (Cat vs Kitten): {sim_AB:.4f}")
    print(f"Similarity (Cat vs Feline): {sim_AC:.4f}")

    print("\n✅ RESULT: Similar meanings produce higher similarity scores!")

except Exception as e:
    print(f"❌ ERROR: {e}")