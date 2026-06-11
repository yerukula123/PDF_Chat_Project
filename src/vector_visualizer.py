import os
import google.generativeai as genai
import numpy as np
from sklearn.decomposition import PCA
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

data = [
    "The software update fixed the bug.",
    "Python is great for coding.",
    "The forest is full of green trees.",
    "Flowers bloom in the spring."
]

print("--- 🎨 The Vector Visualizer ---")

try:
    embeddings = [
        genai.embed_content(
            model="models/gemini-embedding-001",
            content=text
        )["embedding"]
        for text in data
    ]

    pca = PCA(n_components=2)

    reduced_vectors = pca.fit_transform(np.array(embeddings))

    for i, text in enumerate(data):
        x = reduced_vectors[i][0]
        y = reduced_vectors[i][1]

        print(f"Sentence: {text}")
        print(f"   -> 2D Coordinates: X={x:.2f}, Y={y:.2f}\n")

    print("✅ SUCCESS: High-dimensional vectors reduced to 2D!")

except Exception as e:
    print(f"❌ ERROR: {e}")
    