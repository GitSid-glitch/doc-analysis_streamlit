# 📄 Document Analysis & AI Chatbot (RAG)

This project is a **document analysis web application** that allows users to upload a document (PDF or DOCX) and **ask questions about its content using AI**.

The system uses **Retrieval-Augmented Generation (RAG)** so that answers are generated **based on the uploaded document**, not on general knowledge or hallucinations.

The application is **fully deployed** and accessible through a public link.

---

## 🚀 Features

- Upload **PDF or DOCX** documents  
- Automatic **text extraction**  
- Intelligent **document chunking**  
- Semantic search using **vector embeddings**  
- AI-powered question answering grounded in document content  
- Optional display of retrieved document context (sources)

Example questions:
- *“Summarize this document”*
- *“What does this section mean?”*
- *“What skills are mentioned?”*
- *“Explain the experience section”*

---

## 🧠 How It Works (Simple Explanation)

1. **Document Upload**  
   User uploads a PDF or DOCX file.

2. **Text Extraction**  
   The app extracts readable text from the document.

3. **Chunking & Embeddings**  
   Text is split into small chunks and converted into vector embeddings.

4. **Retrieval (RAG)**  
   When a question is asked, the most relevant chunks are retrieved.

5. **Answer Generation**  
   A large language model generates an answer using only the retrieved context.

---

## 🏗️ Tech Stack

- **Frontend & Hosting**: Streamlit  
- **Language**: Python  
- **LLM Inference**: Groq (LLaMA-3.1)  
- **Embeddings**: Sentence-Transformers  
- **Vector Store**: FAISS  
- **Document Processing**:
  - PDF: `pdfplumber`
  - DOCX: `python-docx`

---

## 🌐 Live Demo

The app is deployed on **Streamlit Cloud**.

Anyone with the link can:
- Upload a document
- Ask questions
- Receive AI-generated answers
