import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

my_text = "I love learning about Artificial Intelligence!"

print(f"--- 🧬 Transforming: '{my_text}' ---")

try:
    result = genai.embed_content(
        model="models/gemini-embedding-001",
        content=my_text
    )

    vector = result["embedding"]

    print(f"✅ Success! Your sentence is now a vector of {len(vector)} numbers.")
    print(f"First 10 numbers:\n{vector[:10]}")
    print(f"\nExample coordinate 1: {vector[0]}")

except Exception as e:
    print(f"❌ Error: {e}")