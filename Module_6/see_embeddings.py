from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

text = "The quick brown fox jumps over the lazy dog."

embedding = model.encode(text)

print("--- EMBEDDING REVEALED ---")
print(f"First 10 numbers of the vector: {embedding[:10]}")
print(f"Total numbers (Dimensions) in this vector: {len(embedding)}")

print("\nYour text has been successfully turned into a 'Vector'!")