import streamlit as st

print("--- 🛠️ UI Toolkit Verification ---")

try:
    version = st.__version__
    print(f"✅ Streamlit version {version} is successfully installed!")
    print("🚀 You are ready to run: 'streamlit hello'")
except Exception as e:
    print(f"❌ Installation Error: {e}")