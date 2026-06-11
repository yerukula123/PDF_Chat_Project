import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API key
load_dotenv()

# Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Parser
parser = StrOutputParser()

# Template with two variables
template = """
You are a helpful assistant.
Explain the following subject: {subject}
Use a {tone} tone.
Keep the explanation under 3 sentences.
"""

prompt_template = ChatPromptTemplate.from_template(template)

# Build chain
chain = prompt_template | model | parser

print("--- 🥪 The Mad-Libs Challenge: Multiple Inputs ---")

try:
    user_inputs = {
        "subject": "Quantum Computing",
        "tone": "extremely grumpy"
    }

    result = chain.invoke(user_inputs)

    print("\nAI Response:")
    print(result)

except Exception as e:
    print(f"❌ ERROR: {e}")