# We use a simple dictionary to represent 'Attention Weights'

sentence = "The bank of the river"

attention_weights_for_bank = {
    "The": 0.05,
    "bank": 0.10,
    "of": 0.05,
    "the": 0.05,
    "river": 0.75
}

print(f"Analyzing sentence: '{sentence}'")
print(f"Focusing on the word: 'bank'\n")

print("--- Attention Weights (Importance) ---")
for word, weight in attention_weights_for_bank.items():
    bar = "█" * int(weight * 20)
    print(f"{word.ljust(8)}: {bar} ({weight*100}%)")

print("\nConclusion: Because of high attention on 'river',")
print("the AI knows 'bank' means land, not a building.")