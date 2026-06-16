import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

pizza_vector = np.array([[0.9, 0.1]])
burger_vector = np.array([[0.8, 0.2]])
phone_vector = np.array([[0.1, 0.9]])
sushi_vector = np.array([[0.85, 0.15]])

food_score = cosine_similarity(pizza_vector, burger_vector)
tech_score = cosine_similarity(pizza_vector, phone_vector)
sushi_score = cosine_similarity(pizza_vector, sushi_vector)

print("--- SIMILARITY AUDIT ---")
print(f"Similarity Score (Pizza vs Burger): {food_score[0][0]:.4f}")
print(f"Similarity Score (Pizza vs Smartphone): {tech_score[0][0]:.4f}")
print(f"Similarity Score (Pizza vs Sushi): {sushi_score[0][0]:.4f}")

if food_score > tech_score:
    print("\nResult: The computer knows Pizza is more like a Burger than a Phone!")