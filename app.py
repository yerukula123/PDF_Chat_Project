import streamlit as st
import random

st.set_page_config(
    page_title="Magic Rerun Lab",
    page_icon="🪄"
)

st.title("🪄 The Magic Execution Lab")

lucky_number = random.randint(1, 100)
st.write(f"🎲 Your 'Lucky Number' for this rerun is: **{lucky_number}**")

if st.button("Trigger a Rerun"):
    st.write("The button was clicked! Streamlit is rerunning...")

user_text = st.text_input("Type something and hit Enter:")
if user_text:
    st.write(f"You typed: {user_text}")

st.info("✨ I am a Real-Time Developer now!")