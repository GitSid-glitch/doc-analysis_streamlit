def run_rag(llm, vectorstore, question: str, k: int = 3):
    docs = vectorstore.similarity_search(question, k=k)
    context = "\n\n".join(doc.page_content for doc in docs)
    prompt = f"""
You are a helpful AI assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""
    response = llm.invoke(prompt)
    answer_text = (
        response.content
        if hasattr(response, "content")
        else str(response)
    )

    return answer_text, docs