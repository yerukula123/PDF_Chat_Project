import os
import google.generativeai as genai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv


def run_embedding_milestone():
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)

    print("🚀 --- MODULE 3: EMBEDDING MILESTONE --- 🚀")

    knowledge_base = [
        "The mitochondria is the powerhouse of the cell.",
        "The speed of light is approximately 299,792 kilometers per second.",
        "VS Code is a popular source-code editor made by Microsoft.",
        "RAG stands for Retrieval-Augmented Generation."
    ]

    user_query = "What is the primary energy source for cellular activity?"

    try:
        print("🛰️ Generating knowledge base embeddings...")

        kb_embeddings = [
            genai.embed_content(
                model="models/gemini-embedding-001",
                content=text
            )["embedding"]
            for text in knowledge_base
        ]

        print("🔍 Embedding user query...")

        query_vec = genai.embed_content(
            model="models/gemini-embedding-001",
            content=user_query
        )["embedding"]

        scores = cosine_similarity([query_vec], kb_embeddings)[0]

        best_idx = np.argmax(scores)
        top_score = scores[best_idx]

        print("\n--- MILESTONE REPORT ---")
        print(f"Top Match: {knowledge_base[best_idx]}")
        print(f"Confidence: {top_score:.4f}")

        if top_score > 0.6:
            print("\n✅ VERIFIED: Semantic search is accurate and responsive.")
        else:
            print("\n⚠️ WARNING: Low similarity score. Check model configuration.")

    except Exception as e:
        print(f"❌ MILESTONE FAILED: {e}")


if __name__ == "__main__":
    run_embedding_milestone()