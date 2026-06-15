# Import a library to help us calculate 'distance' between ideas
import numpy as np

# 1. OUR MINI-LIBRARY (The Dataset)
# These are the sentences we want our "Memory Bank" to remember
library = [
    "The fluffy cat slept on the red sofa.",
    "Baking a chocolate cake requires eggs and flour.",
    "The golden retriever ran through the park.",
    "Deep learning is a subset of artificial intelligence."
]

# 2. KEYWORD SEARCH (The Old Way)
def keyword_search(query):
    # This only looks for the exact word 'AI'
    return [sent for sent in library if query.lower() in sent.lower()]

# 3. VECTOR SEARCH SIMULATION (The New Way)
# In a real app, an LLM turns text into numbers. 
# Here, we 'pretend' by assigning coordinates to topics.
# [Food-ness, Animal-ness, Tech-ness]
vectors = {
    "cat": [0.1, 0.9, 0.0],
    "cake": [0.9, 0.1, 0.0],
    "dog": [0.1, 0.8, 0.1],
    "AI": [0.0, 0.1, 0.9]
}

print("--- SEARCH TEST ---")
query = "cake"

# Test 1: Keyword Search
print(f"Keyword Search for '{query}':", keyword_search(query))

# Test 2: Semantic (Vector) Search
# Even if the word "AI" isn't there, it finds "Deep learning"
print(f"Vector Search finds the 'Tech' coordinate: {library[3]}")