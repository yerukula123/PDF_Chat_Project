from langchain_core.prompts import ChatPromptTemplate

# Template with TWO variables
template = "You are a professional tutor. Explain {topic} to a {audience} in exactly two sentences."

# Create prompt template
prompt_template = ChatPromptTemplate.from_template(template)

print("--- 📝 The Prompt Template Lab ---")

# Example 1
formatted_prompt = prompt_template.format_messages(
    topic="Gravity",
    audience="5-year-old"
)

print("Final Prompt to AI:")
print(formatted_prompt[0].content)

# Example 2
second_prompt = prompt_template.format_messages(
    topic="Artificial Intelligence",
    audience="college student"
)

print("\nSecond Dynamic Prompt:")
print(second_prompt[0].content)

print("\n✅ SUCCESS: The template is dynamically filling multiple blanks!")