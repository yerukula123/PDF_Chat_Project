import faiss
import numpy as np

dimension = 64
database_vectors = np.random.random((10, dimension)).astype('float32')

index = faiss.IndexFlatL2(dimension)

print("--- ⚙️ FAISS Engine Health Check ---")

try:
    index.add(database_vectors)
    print(f"✅ FAISS successfully indexed {index.ntotal} paragraphs.")
    print("✅ FAISS Engine is installed and ready for Retrieval!")

except Exception as e:
    print(f"❌ FAISS Engine failure: {e}")