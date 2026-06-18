import streamlit as st

st.set_page_config(
    page_title="PDF Chat Bot",
    page_icon="🚀"
)

st.title("🚀 Chat with your PDF")

st.subheader(
    "Turn your textbooks into an interactive conversation."
)

st.write(
    "Welcome! This app uses RAG technology to answer questions from your documents."
)

if st.button("Say Hello to my AI"):
    st.success(
        "Hello, Future AI Engineer! Your interface is working."
    )

st.sidebar.title("App Settings")
st.sidebar.info(
    "Upload your PDF to get started."
)