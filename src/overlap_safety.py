from langchain_text_splitters import CharacterTextSplitter

raw_text = "The secret ingredient to a great RAG system is a healthy amount of overlap."

print("--- 🤝 The Overlap Safety Net ---")

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=30,
    chunk_overlap=15
)

chunks = splitter.split_text(raw_text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {repr(chunk)}")

print("\n💡 OBSERVATION: Look at the end of Chunk 1 and the start of Chunk 2.")