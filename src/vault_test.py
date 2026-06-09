import os

def check_vault():
    print("--- 🛡️ Secret Vault Audit ---")

    if os.path.exists(".env"):
        print("✅ SUCCESS: The .env file was found in the Root folder.")
    else:
        print("❌ ERROR: The .env file is missing! Create it in the main project folder.")

    print("\nNote: In the next lesson, we will install the 'dotenv' tool")
    print("to automatically pull your key into the code.")

if __name__ == "__main__":
    check_vault()