# We use a dictionary to simulate the 'Scoreboard' of the LLM

prompt = "Artificial Intelligence will change the"

word_scores = {
    "world": 0.01,
    "future": 0.05,
    "internet": 0.04,
    "weather": 0.90
}

print(f"Prompt: {prompt}...")
print("-" * 30)

for word, probability in word_scores.items():
    percent = f"{probability * 100:.0f}%"
    visual_bar = "█" * int(probability * 20)
    print(f"{word.ljust(10)} | {percent.ljust(5)} | {visual_bar}")

top_choice = max(word_scores, key=word_scores.get)

print("-" * 30)
print(f"AI Decision: The most likely next token is '{top_choice}'.")