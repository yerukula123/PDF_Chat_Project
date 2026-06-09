import random

# The 'Prompt' or starting sentence
context = "The AI read the PDF and decided to"

# Possible 'Next Tokens' (words)
possible_next_words = ["summarize", "analyze", "explain", "rewrite"]

# Choose a random word
chosen_word = random.choice(possible_next_words)

# Combine the context with the prediction
final_output = f"{context} {chosen_word} the content."

print("--- AI Prediction Simulation ---")
print(f"Input Context: {context}...")
print(f"AI Prediction: {chosen_word}")
print(f"Final Sentence: {final_output}")

print("\nNote: In our project, the LLM will use the PDF text to make these predictions!")