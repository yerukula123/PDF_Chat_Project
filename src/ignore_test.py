import subprocess

def check_visibility():
    print("--- 🕵️ Git Invisibility Test ---")

    try:
        packing_list = subprocess.check_output(['git', 'ls-files']).decode('utf-8')

        if ".env" in packing_list:
            print("❌ DANGER: Your .env file is VISIBLE to Git!")
            print("Action: Remove it from Git immediately using the terminal.")
        else:
            print("✅ SAFE: Your .env file is invisible to Git.")
            print("You can now safely share your code without leaking keys.")

    except Exception as e:
        print(f"Error checking Git: {e}")

if __name__ == "__main__":
    check_visibility()