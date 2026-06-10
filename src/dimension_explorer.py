import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

inputs = [
    "Python",
    "The quick brown fox jumps over the lazy dog."
]

print("--- 🗺️ Exploring the Multi-Dimensional Map ---")

try:
    for text in inputs:
        result = genai.embed_content(
            model="models/gemini-embedding-001",
            content=text
        )

        vector = result["embedding"]

        print(f"\nInput: '{text}'")
        print(f"Total Dimensions: {len(vector)}")
        print(f"First 3 Dimensions: {vector[:3]}")
        print(f"Last 3 Dimensions: {vector[-3:]}")

    print("\n✅ OBSERVATION: No matter the length of the text,")
    print("the number of dimensions stays the same!")

except Exception as e:
    print(f"❌ Error: {e}")