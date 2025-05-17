# ProvectusInternship_EduardTsakanyan

This project is a Python-based RAG (Retrieval-Augmented Generation) service for managing and retrieving information about concert tours in 2025–2026. It was developed as a test task for the Provectus ML Internship.

---

##  Features

###  Document Ingestion
- Accepts plain text concert-related documents.
- Verifies that the document is related to concert tours.
- Summarizes the content using an LLM.
- Stores summaries in a FAISS vector database.

###  Question Answering
- Users can ask specific questions about ingested documents.
- Answers are based only on stored summaries — no general knowledge used.

###  UI with Streamlit
- Clean and simple interface for uploading documents and asking questions.


##  Project Structure

ProvectusInternship_EduardTsakanyan/
  app/
   init.py
   ingestion.py # Document ingestion and summarization
   qa.py # Question-answering logic
   vector_store.py # FAISS vector database logic
  
  data/
   faiss.index # Vector index file
   meta.pkl # Stores metadata for documents
  
  ui.py # Streamlit user interface
  requirements.txt # Python dependencies
  README.md # Project overview

---

##  Setup Instructions

1. Clone the Repository

2. Install Dependencies
   pip install -r requirements.txt

3. Run the app
   streamlit run ui.py









  
