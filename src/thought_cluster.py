import os
import google.generativeai as genai
import numpy as np
from sklearn.cluster import KMeans
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

sentences = [
    "Apples are a great source of fiber.",
    "Bananas contain high levels of potassium.",
    "Python is a versatile programming language.",
    "Java is used for building enterprise apps.",
    "Oranges are famous for Vitamin C.",
    "C++ is a powerful language for systems.",
    "The moon orbits the Earth.",
    "Astronauts travel into outer space."
]

print("--- 🧠 Clustering Your Thoughts ---")

try:
    embeddings = [
        genai.embed_content(
            model="models/gemini-embedding-001",
            content=s
        )["embedding"]
        for s in sentences
    ]

    matrix = np.array(embeddings)

    # 3 clusters: Fruit, Programming, Space
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    kmeans.fit(matrix)
    labels = kmeans.labels_

    for i, sentence in enumerate(sentences):
        print(f"Group {labels[i]} | {sentence}")

    print("\n✅ SUCCESS: The AI automatically grouped similar topics!")

except Exception as e:
    print(f"❌ ERROR: {e}")