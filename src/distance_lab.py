import os
import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Euclidean Distance Function
def calculate_euclidean(v1, v2):
    return np.linalg.norm(np.array(v1) - np.array(v2))

# Sentences
text_a = "The dog is in the park."
text_b = "I want to buy a new laptop."

try:
    # Generate embeddings
    vec_a = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text_a
    )["embedding"]

    vec_b = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text_b
    )["embedding"]

    # Calculate distance
    dist = calculate_euclidean(vec_a, vec_b)

    print("--- 📏 Measuring Space (Euclidean Distance) ---")
    print(f"Sentence A: {text_a}")
    print(f"Sentence B: {text_b}")
    print(f"Straight-Line Distance: {dist:.4f}")

    if dist < 0.6:
        print("✅ RESULT: These points are very close in space!")
    else:
        print("❌ RESULT: These points are far apart.")

except Exception as e:
    print(f"❌ ERROR: {e}")