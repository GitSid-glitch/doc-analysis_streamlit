import streamlit as st
import os
from backend.rag.rag_pipeline import run_rag
from backend.utils.text_extraction import extract_pdf_text, extract_docx_text
from backend.utils.table_extraction import extract_pdf_tables
from backend.utils.chart_extraction import extract_charts
from backend.utils.eda import describe_table

from backend.rag.text_splitter import split_text
from backend.rag.vectorstore import create_vectorstore
from backend.rag.llm import get_llm

st.set_page_config(page_title="Document Analysis RAG", layout="wide")
st.title("📄 Document Analysis & AI Chatbot")

UPLOAD_DIR = "uploads"
STATIC_DIR = "static"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])

if uploaded_file:
    filepath = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())

    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext == ".pdf":
        text = extract_pdf_text(filepath)
    else:
        text = extract_docx_text(filepath)

    st.subheader("Text Preview")
    st.write(text[:2000])

    if ext == ".pdf":
        try:
            dfs = extract_pdf_tables(filepath)
            st.subheader("Tables")
            for df in dfs:
                st.dataframe(df.head())
                st.json(describe_table(df))
        except:
            st.info("No tables found")

        try:
            chart_paths = extract_charts(filepath, STATIC_DIR)
            st.subheader("Charts")
            for p in chart_paths:
                st.image(p)
        except:
            st.info("No charts found")

    st.divider()
    st.subheader("Ask questions about the document")

    chunks = split_text(text)
    vectorstore = create_vectorstore(chunks)
    llm = get_llm()

    question = st.text_input("Your question")

    if question:
        with st.spinner("Thinking..."):
            answer, sources = run_rag(llm, vectorstore, question)

        st.markdown("### Answer")
        st.write(answer)

        with st.expander("Show retrieved context (sources)"):
            for doc in sources:
                st.write(doc.page_content[:300])
