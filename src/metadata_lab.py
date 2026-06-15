import os
from langchain_community.document_loaders import PyPDFLoader

file_path = os.path.join("docs", "sample.pdf")

print(f"--- 🕵️ Metadata Investigation: {file_path} ---")

try:
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    first_page = pages[0]
    evidence_tag = first_page.metadata

    source_file = evidence_tag.get("source")
    page_number = evidence_tag.get("page")

    print("✅ Evidence Found!")
    print(f"📍 Source Location: {source_file}")
    print(f"📖 Page Number: {page_number + 1}")

    print(f"\n📂 Full Raw Metadata:\n{evidence_tag}")

except Exception as e:
    print(f"❌ INVESTIGATION FAILED: {e}")