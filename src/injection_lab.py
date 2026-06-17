from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Use fake embeddings to avoid embedding API issues
embeddings = DeterministicFakeEmbedding(size=384)

texts = [
    "The secret code to the vault is 12345.",
    "The vault is located in the basement."
]

vector_db = FAISS.from_texts(texts, embeddings)
retriever = vector_db.as_retriever()

template = """Answer based on this context:

{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

print("--- 🔬 Context Injection Lab: Debugging Mode ---")

try:
    user_query = "What is the secret code?"

    retrieved_docs = retriever.invoke(user_query)

    context_text = "\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    print("\n💉 INJECTED CONTEXT FOUND:")
    print("--------------------------------")
    print(context_text)
    print("--------------------------------")

    final_combined_prompt = prompt.format(
        context=context_text,
        question=user_query
    )

    print("\n📝 FINAL PROMPT SENT TO AI'S BRAIN:")
    print(final_combined_prompt)

    response = model.invoke(final_combined_prompt)

    print(f"\n🤖 AI ANSWER: {response.content}")

except Exception as e:
    print(f"❌ Lab Error: {e}")