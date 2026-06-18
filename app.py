import streamlit as st

st.set_page_config(
    page_title="PDF Architect",
    layout="wide"
)

with st.sidebar:
    st.title("🛠️ Control Center")

    st.info("Step 1: Upload your PDF\nStep 2: Ask a question")

    st.divider()

    st.markdown("### 🚦 System Status")
    st.success("PDF Engine: Ready")

    # Add your name here
    st.write("User: Sathish")

    st.caption("v1.0.4 - Phase 2 Internship")

st.title("💬 Chat with your PDF")

st.write("The main area is now clean and ready for your conversation.")

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Recent Activity")
    st.write("No questions asked yet.")

with col2:
    st.button("Clear Chat History")