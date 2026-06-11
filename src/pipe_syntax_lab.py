from langchain_core.runnables import RunnableLambda

# Station 1: Clean text
def clean_text(input_data):
    return input_data.strip().upper()

# Station 2: Mock AI
def mock_ai(clean_input):
    return f"AI RESPONSE TO: {clean_input}"

# Station 3: Add completion tag
def add_completion(ai_response):
    return f"{ai_response} - COMPLETED"

# Wrap functions as Runnable objects
station_1 = RunnableLambda(clean_text)
station_2 = RunnableLambda(mock_ai)
station_3 = RunnableLambda(add_completion)

# Create the chain
my_first_chain = station_1 | station_2 | station_3

print("--- ⛓️ Testing the Pipe (|) Syntax ---")

# Run the chain
result = my_first_chain.invoke("   hello world   ")

print(f"Final Output: {result}")