from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# LLM
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Fake embeddings for learning/testing
embeddings = DeterministicFakeEmbedding(size=384)

# Mini knowledge base
vector_db = FAISS.from_texts(
    [
        "The solar system has eight planets.",
        "Jupiter is the largest planet."
    ],
    embeddings
)

retriever = vector_db.as_retriever()

template = """
Answer the question based ONLY on the following context:

{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | model
    | StrOutputParser()
)

print("--- ⛓️ RAG Chain: System Online ---")

try:
    question = "Tell me about Jupiter."

    response = rag_chain.invoke(question)

    print(f"User: {question}")
    print(f"AI: {response}")

except Exception as e:
    print(f"❌ Chain Error: {e}")