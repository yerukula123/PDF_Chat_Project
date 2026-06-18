import streamlit as st

# Page Setup
st.set_page_config(page_title="AI Memory Lab", layout="wide")

st.title("🧠 Chat with Memory")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Fake AI response
    response = f"I remembered you said: {prompt}"

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )