import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("--- 🛠️ LangChain Toolkit Audit ---")

try:
    # Initialize Gemini through LangChain
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    print("✅ SUCCESS: LangChain-Google-Genai toolkit is active.")
    print(f"✅ Model Assigned: {llm.model}")

    if api_key:
        print("✅ Environment: API Key detected and ready for orchestration.")
    else:
        print("⚠️ Warning: API Key missing from .env")

except Exception as e:
    print(f"❌ ERROR: Toolkit check failed. {e}")