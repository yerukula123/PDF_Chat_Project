from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def run_milestone_pipeline():
    print("🚀 --- STARTING RETRIEVAL MILESTONE PIPELINE ---")

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    embeddings = DeterministicFakeEmbedding(size=384)

    loader = PyPDFLoader("docs/textbook.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    print(f"📦 PDF Liquidated into {len(chunks)} chunks.")

    vector_db = FAISS.from_documents(chunks, embeddings)

    retriever = vector_db.as_retriever(
        search_kwargs={"k": 3}
    )

    print("⚙️ Vector Database & Retriever Online.")

    template = """
Answer based ONLY on the following context.

Context:
{context}

Question:
{question}
"""

    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | model
        | StrOutputParser()
    )

    user_query = "What is the most important takeaway from this document?"

    print(f"\n❓ User Question: {user_query}")

    answer = rag_chain.invoke(user_query)

    print("\n🤖 AI Answer:")
    print(answer)

    print("\n📍 Verified Sources:")

    sources = retriever.invoke(user_query)

    for doc in sources:
        print(
            f"- Page {doc.metadata.get('page',0)+1}: "
            f"{doc.metadata.get('source','Unknown')}"
        )

try:
    run_milestone_pipeline()

except Exception as e:
    print(f"❌ Pipeline Failure: {e}")