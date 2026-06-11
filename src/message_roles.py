import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key
load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# System Message (Persona)
system_instruction = SystemMessage(
    content="You are a medieval knight. Use old English and talk about swords."
)

# Human Message
user_input = HumanMessage(
    content="What is a Large Language Model?"
)

messages = [system_instruction, user_input]

print("--- 🎭 Knight Persona Test ---")

try:
    response = llm.invoke(messages)

    print("\nKnight AI says:\n")
    print(response.content)

except Exception as e:
    print(f"❌ ERROR: {e}")