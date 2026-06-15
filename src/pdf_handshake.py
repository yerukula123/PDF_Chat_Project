import os
from langchain_community.document_loaders import PyPDFLoader

pdf_path = os.path.join("docs", "sample.pdf")

print(f"--- 🤝 Initiating PDF Handshake: {pdf_path} ---")

try:
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    page_count = len(pages)

    print("✅ HANDSHAKE SUCCESSFUL!")
    print(f"📄 Total Pages Found: {page_count}")
    print(f"🔍 Content Preview: {pages[0].page_content[:50]}...")

except Exception as e:
    print(f"❌ HANDSHAKE FAILED: {e}")