import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Load API key
load_dotenv()

# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Output parser
parser = StrOutputParser()

print("--- 🛡️ The Output Parser Guard Lab ---")

try:
    # Raw response
    raw_response = llm.invoke("Say 'Hello' in one word.")

    print(f"\n📦 RAW DATA (The Bag): {raw_response}")
    print(f"Type of Raw: {type(raw_response)}")

    # Parsed response
    clean_text = parser.invoke(raw_response)

    print(f"\n🍔 CLEAN TEXT (The Burger): '{clean_text}'")
    print(f"Type of Clean: {type(clean_text)}")

except Exception as e:
    print(f"❌ ERROR: {e}")