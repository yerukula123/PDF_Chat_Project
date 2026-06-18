from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding
from langchain_core.documents import Document

embeddings = DeterministicFakeEmbedding(size=384)

mock_docs = [
    Document(
        page_content="The company was founded in 1999.",
        metadata={"source": "manual.pdf", "page": 1}
    ),
    Document(
        page_content="Our headquarters are in San Francisco.",
        metadata={"source": "manual.pdf", "page": 5}
    ),
    Document(
        page_content="The CEO is Jane Doe.",
        metadata={"source": "manual.pdf", "page": 12}
    )
]

print("--- 📄 Source Attribution Audit ---")

try:
    vector_db = FAISS.from_documents(mock_docs, embeddings)

    query = "Where is the company located?"

    results = vector_db.similarity_search(query, k=1)

    if results:
        print(f"🤖 AI Answer: {results[0].page_content}")
        print(f"📍 Source: {results[0].metadata['source']}")
        print(f"📖 Found on Page: {results[0].metadata['page']}")
    else:
        print("No results found")

except Exception as e:
    print(f"❌ Audit Error: {e}")