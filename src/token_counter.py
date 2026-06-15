import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

sample_text = """
Artificial Intelligence is transforming industries around the world.
Students can use AI tools to learn faster and improve productivity.
However, it is important to understand the technology and use it responsibly.
"""

print("--- 📊 Token vs. Character Audit ---")
print(f"Text: {sample_text}")

try:
    char_count = len(sample_text)
    token_count = llm.get_num_tokens(sample_text)

    print(f"📏 Character Count: {char_count}")
    print(f"🔢 Token Count: {token_count}")
    print(f"💡 Ratio: ~{char_count/token_count:.2f} characters per token")

except Exception as e:
    print(f"❌ ERROR: {e}")