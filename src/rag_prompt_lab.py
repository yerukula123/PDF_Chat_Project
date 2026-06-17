from langchain_core.prompts import ChatPromptTemplate

system_instructions = """
You are a helpful assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If the answer is not in the context, say 'I am sorry, but the PDF does not contain that information.'
Do not make up an answer.

Context:
{context}
"""

user_input = "{question}"

print("--- 📝 RAG Prompt Engineering Lab ---")

try:
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_instructions),
        ("human", user_input),
    ])

    # Action Item values
    sample_context = "The sky is blue."
    sample_question = "Who won the Super Bowl in 1990?"

    final_prompt = prompt_template.format(
        context=sample_context,
        question=sample_question
    )

    print("\n[AI'S SECRET INSTRUCTIONS]:")
    print(final_prompt)
    print("\n✅ PROMPT READY: Your AI now has a strict boundary!")

except Exception as e:
    print(f"❌ ERROR: Prompt creation failed. {e}")