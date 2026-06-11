import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load environment variables
load_dotenv()


def run_milestone():
    print("🚀 --- MODULE 4: ORCHESTRATION MILESTONE --- 🚀")

    # Initialize the AI Model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    # Prompt Template
    template = """
You are a professional research assistant.

Provide a summary of the following topic: {topic}

The target audience is: {audience}

Format the output as a 3-bullet point list.
"""

    prompt = ChatPromptTemplate.from_template(template)

    # Output Parser
    parser = StrOutputParser()

    # Build Chain
    chain = prompt | llm | parser

    print("📡 Chain initialized. Sending orchestration request...")

    try:
        response = chain.invoke(
            {
                "topic": "The importance of Vector Databases in AI",
                "audience": "complete beginners",
            }
        )

        print("\n--- FINAL SUMMARY REPORT ---")
        print(response)
        print("\n✅ MILESTONE REACHED: Your AI Orchestration is flawless!")

    except Exception as e:
        print(f"❌ MILESTONE FAILED: {e}")


if __name__ == "__main__":
    run_milestone()