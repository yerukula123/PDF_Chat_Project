from langchain_text_splitters import CharacterTextSplitter

raw_text = """
The CPU is the brain of the computer. It handles all instructions.
Python is a great language for beginners because its syntax is clean.
Artificial Intelligence is changing the world as we know it today.
"""

print("--- ✂️ The Brutal Chop: Fixed-Size Chunking ---")

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=35,
    chunk_overlap=0
)

chunks = splitter.split_text(raw_text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} ({len(chunk)} chars): {repr(chunk)}")

print("\n⚠️ NOTICE: Look for words split across chunks.")