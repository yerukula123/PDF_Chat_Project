import sys

try:
    import faiss
    print("✅ FAISS is installed and ready!")
except ImportError:
    print("❌ FAISS is MISSING. Check installation.")

try:
    from langchain_community.vectorstores import FAISS
    print("✅ LangChain-FAISS integration is ready!")
except ImportError:
    print("❌ LangChain Community is MISSING.")

print(f"Running on Python version: {sys.version}")