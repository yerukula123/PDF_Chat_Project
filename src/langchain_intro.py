from langchain_core.messages import HumanMessage
import langchain

print("--- 🏗️ LangChain Architecture Audit ---")

version = langchain.__version__
print(f"✅ Framework Detected: LangChain version {version}")

test_message = HumanMessage(content="Hello Architect!")

if test_message.content == "Hello Architect!":
    print("✅ Objects: LangChain Message blocks are snapping together perfectly.")
    print(f"Message Role: {test_message.type}")
else:
    print("❌ Error: Architecture blocks are misaligned.")

print("\nNote: In the next lesson, we will install the full 'Conductor' toolkit!")