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

# Prompt template
prompt = ChatPromptTemplate.from_template(
    "Tell me a fun fact about {topic}"
)

# Output parser
parser = StrOutputParser()

# Chain
chain = prompt | model | parser

print("--- ⛓️ Running My First LangChain ---")

try:
    result = chain.invoke({"topic": "Ancient Rome"})
    print(f"\nResult:\n{result}")

except Exception as e:
    print(f"❌ ERROR: {e}")