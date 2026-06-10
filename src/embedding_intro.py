import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

text_1 = "I love training AI models."
text_2 = "Machine learning is my favorite hobby."

print("--- 🧠 Generating Embedding Vectors ---")

try:
    result_1 = genai.embed_content(
       model="models/gemini-embedding-001",
        content=text_1
    )

    result_2 = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text_2
    )

    vector_1 = result_1["embedding"]

    print(f"Sentence: '{text_1}'")
    print(f"Vector Length: {len(vector_1)} numbers")
    print(f"First 5 numbers of the coordinate: {vector_1[:5]}")

    print("\n✅ SUCCESS: You have turned human language into computer math!")

except Exception as e:
    print(f"❌ ERROR: {e}")