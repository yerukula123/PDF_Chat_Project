from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Less creative = more reliable
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Use fake embeddings for course exercises
embeddings = DeterministicFakeEmbedding(size=384)

texts = [
    "The office is open from 9 AM to 5 PM, Monday to Friday."
]

vector_db = FAISS.from_texts(texts, embeddings)
retriever = vector_db.as_retriever()

template = """
You are a strict office assistant.

Use ONLY the following context to answer the question.

If the answer is NOT in the context, exactly say:

'I am sorry, but that information is not in the office manual.'

Do not use your own knowledge.

Context: {context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print("--- 🛡️ Hallucination Guardrail Lab ---")

try:
    print("\nTest 1: Valid Question...")
    print("AI:", chain.invoke("What are the office hours?"))

    print("\nTest 2: Out-of-Context Question...")
    print("AI:", chain.invoke("What is the office address?"))

except Exception as e:
    print(f"❌ Error: {e}")