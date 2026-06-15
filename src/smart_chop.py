from langchain_text_splitters import RecursiveCharacterTextSplitter

raw_text = """
The CPU is the heart of the computer. It executes instructions.

Python is a high-level language. It is known for its readability.
This makes it great for Artificial Intelligence projects.
"""

print("--- 🧠 The Smart Chop: Recursive Splitting ---")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(raw_text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} ({len(chunk)} chars): {repr(chunk)}")

print("\n💡 OBSERVATION: Notice how the sentences usually stay whole!")