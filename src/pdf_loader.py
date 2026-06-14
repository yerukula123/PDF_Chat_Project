import os
from langchain_community.document_loaders import PyPDFLoader

file_path = os.path.join("docs", "sample.pdf")

print(f"--- 📂 Loading Document: {file_path} ---")

try:
    loader = PyPDFLoader(file_path)

    pages = loader.load()

    print(f"✅ SUCCESS: Loaded {len(pages)} pages.")

    first_page = pages[0]

    print("\n📄 First Page Preview (First 100 chars):")
    print(first_page.page_content[:100] + "...")

    print("\n🏷️ Metadata Found:")
    print(first_page.metadata)

except Exception as e:
    print(f"❌ ERROR: Could not load PDF. {e}")
    print("Check if 'sample.pdf' is inside the 'docs' folder!")