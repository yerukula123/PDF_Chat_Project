import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("--- 🔐 Security Guard Report ---")

if api_key:
    print(f"✅ SUCCESS: Guard found the key! Starts with: {api_key[:4]}...")
    print("Your code is now authenticated and ready for AI.")
else:
    print("❌ ERROR: The guard couldn't find 'GOOGLE_API_KEY'.")
    print("Check if your .env file is in the root folder and spelled correctly.")