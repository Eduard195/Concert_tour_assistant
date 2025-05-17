from app.vector_store import search_similar_documents
from transformers import pipeline


qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

def answer_question(question: str) -> str:
    results = search_similar_documents(question, k=3)

    if not results:
        return "Sorry, I couldn’t find any relevant information in the ingested documents."

    context = " ".join([doc["summary"] for doc in results])
    prompt = f"Answer the following based on the context:\nContext: {context}\nQuestion: {question}"

    answer = qa_model(prompt, max_length=128, do_sample=False)[0]["generated_text"]
    return answer
