import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = os.path.join("docs", "textbook.pdf")

print("--- 🚀 MILESTONE: Starting Data Liquidation Pipeline ---")

try:
    loader = PyPDFLoader(file_path)
    raw_pages = loader.load()

    print(f"📦 Phase 1: Loaded {len(raw_pages)} raw pages from PDF.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )

    final_chunks = text_splitter.split_documents(raw_pages)

    print(f"✂️ Phase 2: Chopped PDF into {len(final_chunks)} optimized chunks.")

    print("\n--- 🔍 SAMPLE CHUNK AUDIT ---")
    print(f"📄 Content: {final_chunks[0].page_content[:100]}...")
    print(f"🏷️ Metadata: {final_chunks[0].metadata}")

    print("\n✅ MILESTONE COMPLETE: Your data is liquidated and ready for the Vector Bank!")

except Exception as e:
    print(f"❌ MILESTONE FAILED: {e}")