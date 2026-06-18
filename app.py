import streamlit as st

# Page Setup
st.set_page_config(
    page_title="PDF Chat Room",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("📂 Documents")
    st.file_uploader("Upload PDF", type="pdf")

# Main Area
st.title("🤖 PDF Research Room")

# Example User Bubble
with st.chat_message("user"):
    st.write("Hello! Can you help me find information in my PDF?")

# Example Assistant Bubble
with st.chat_message("assistant"):
    st.write("Of course! Please upload a file and ask away.")

# Chat Input
if user_prompt := st.chat_input("Type your question here..."):

    with st.chat_message("user"):
        st.write(user_prompt)

    with st.chat_message("assistant"):
        st.write(f"I am processing your question: '{user_prompt}'")