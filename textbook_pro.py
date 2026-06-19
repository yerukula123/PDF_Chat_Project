import streamlit as st
import tempfile
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DeterministicFakeEmbedding

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Textbook AI Pro",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Textbook AI Pro")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.title("📂 Control Center")

    uploaded_file = st.file_uploader(
        "Upload your PDF textbook",
        type="pdf"
    )

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --------------------------------------------------
# AI SETUP
# --------------------------------------------------
@st.cache_resource
def get_ai_tools():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    embeddings = DeterministicFakeEmbedding(size=384)

    return llm, embeddings


llm, embeddings = get_ai_tools()

# --------------------------------------------------
# PDF PROCESSING
# --------------------------------------------------
@st.cache_resource
def process_pdf(file_bytes):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(file_bytes.getvalue())
        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(pages)

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_db.as_retriever()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# MAIN APP
# --------------------------------------------------
if uploaded_file:

    retriever = process_pdf(uploaded_file)

    st.sidebar.success("✅ Textbook Analyzed!")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input(
        "Ask a question about the textbook..."
    ):

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        template = """
Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

        rag_prompt = ChatPromptTemplate.from_template(
            template
        )

        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | rag_prompt
            | llm
            | StrOutputParser()
        )

        with st.chat_message("assistant"):

            response = chain.invoke(prompt)

            st.markdown(response)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

else:
    st.info(
        "👈 Please upload a PDF in the sidebar to begin."
    )