import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load secrets from .env
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel('gemini-2.5-flash')

print("--- 📡 Sending First API Call ---")

try:
    response = model.generate_content(
        "Hello AI! I am building a Chat with PDF app. Say hi back!"
    )

    print(f"AI Response: {response.text}")
    print("\n✅ SUCCESS: Your connection to the LLM is LIVE!")

except Exception as e:
    print(f"❌ ERROR: Connection failed. {e}")