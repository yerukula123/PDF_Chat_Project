import streamlit as st

st.set_page_config(
    page_title="PDF Loader",
    layout="wide"
)

with st.sidebar:
    st.title("📂 Document Center")

    uploaded_file = st.file_uploader(
        "Upload a PDF textbook",
        type="pdf"
    )

    if uploaded_file is not None:
        st.success(f"Successfully uploaded: {uploaded_file.name}")

        file_size = len(uploaded_file.getvalue()) / 1024
        st.info(f"File Size: {file_size:.2f} KB")
    else:
        st.warning("Please upload a PDF to begin.")

st.title("🤖 AI Research Assistant")
st.write("Upload a document in the sidebar to start the conversation.")