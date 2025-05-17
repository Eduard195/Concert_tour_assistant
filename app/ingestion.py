from transformers import pipeline
from app.vector_store import add_document_to_index


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def is_concert_related_ai(text: str) -> bool:
    labels = ["concert tour", "other"]
    result = classifier(text, labels)
    top_label = result["labels"][0]
    top_score = result["scores"][0]
    return top_label == "concert tour" and top_score > 0.7

def summarize_document(text: str) -> str:
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

def ingest_document(text: str) -> str:
    if not is_concert_related_ai(text):
        return "Sorry, I cannot ingest documents with other themes."

    summary = summarize_document(text)
    
    metadata = {
        "summary": summary,
        "original": text
    }
    add_document_to_index(summary, metadata)

    return f"Thank you for sharing! Your document has been successfully added to the database.\nHere is a brief summary of the data from the document:\n{summary}"
