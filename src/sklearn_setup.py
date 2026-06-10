from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Dummy vectors
vector_a = np.array([[0.1, 0.2, 0.3]])
vector_b = np.array([[0.1, 0.2, 0.4]])

print("--- 🛠️ Scikit-Learn Toolkit Check ---")

try:
    similarity_score = cosine_similarity(vector_a, vector_b)

    print("✅ SUCCESS: Scikit-learn is installed and running.")
    print(f"Similarity Calculation Result: {similarity_score[0][0]:.4f}")

except Exception as e:
    print(f"❌ ERROR: Scikit-learn check failed. {e}")