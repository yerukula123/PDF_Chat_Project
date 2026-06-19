import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import DeterministicFakeEmbedding
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

st.set_page_config(
    page_title="PDF AI Architect",
    layout="wide"
)

st.title("🤖 Integrated PDF Chat")

@st.cache_resource
def load_resources():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    # Fake embeddings for learning/testing
    embeddings = DeterministicFakeEmbedding(size=384)

    vector_db = FAISS.from_texts(
        ["The project deadline is January 20th."],
        embeddings
    )

    return model, vector_db

model, vector_db = load_resources()

retriever = vector_db.as_retriever()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about the PDF..."):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        template = """
Answer ONLY from the provided context.

Context:
{context}

Question:
{question}
"""

        prompt_template = ChatPromptTemplate.from_template(template)

        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough(),
            }
            | prompt_template
            | model
            | StrOutputParser()
        )

        response = chain.invoke(prompt)

        st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )