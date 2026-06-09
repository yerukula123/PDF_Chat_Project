import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load secrets
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

config = {
    "temperature": 1.5,
    "top_p": 0.9,
    "max_output_tokens": 200
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=config
)

print(f"--- 🎛️ Running with Temp: {config['temperature']} ---")

prompt = "Give me a one-sentence definition of a PDF file."

try:
    response = model.generate_content(prompt)
    print(f"AI Response: {response.text}")
except Exception as e:
    print(f"❌ ERROR: {e}")