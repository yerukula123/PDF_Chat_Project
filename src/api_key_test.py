my_secret_key = "PASTE_YOUR_KEY_HERE"

def check_key_format(key):
    if key == "PASTE_YOUR_KEY_HERE":
        print("❌ ERROR: You haven't pasted your actual key yet!")
    elif len(key) < 20:
        print("⚠️ WARNING: That key looks a bit too short to be real.")
    else:
        hidden_key = key[:4] + "...." + key[-4:]
        print(f"✅ SUCCESS: Key detected! (Formatted as: {hidden_key})")
        print("Your Python script is now ready to talk to the AI.")

if __name__ == "__main__":
    check_key_format(my_secret_key)