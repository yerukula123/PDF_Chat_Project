import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

long_text = "The quick brown fox jumps over the lazy dog. " * 50

print("--- 🧠 Memory Limit Audit ---")

try:
    token_count = llm.get_num_tokens(long_text)

    print(f"Text length: {len(long_text)} characters")
    print(f"Token count: {token_count} tokens")

    if token_count < 1000000:
        print("✅ STATUS: This chunk fits on the Gemini 'Desk'.")
    else:
        print("❌ STATUS: Memory Overflow! You must chop this PDF into pieces.")

except Exception as e:
    print(f"❌ ERROR: {e}")