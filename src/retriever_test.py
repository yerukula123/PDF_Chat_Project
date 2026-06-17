from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding

embeddings = DeterministicFakeEmbedding(size=384)

texts = [
    "The CPU is the central processing unit of a computer.",
    "Photosynthesis is how plants turn sunlight into energy.",
    "The Great Wall of China is visible from some satellite orbits.",
    "Python is a popular programming language for data science."
]

vector_db = FAISS.from_texts(texts, embeddings)

retriever = vector_db.as_retriever(search_kwargs={"k": 2})

question = "What is a computer?"

docs = retriever.invoke(question)

print(f"Question: {question}")
for i, doc in enumerate(docs):
    print(f"Chunk {i+1}: {doc.page_content}")