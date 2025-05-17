import streamlit as st
from app.ingestion import ingest_document
from app.qa import answer_question

st.set_page_config(page_title="Concert Tour Assistant", layout="centered")

st.title(" Concert Tour Assistant (2025–2026)")

mode = st.radio("Choose mode", [" Ingest Document", " Ask Question"])

if mode == " Ingest Document":
    st.subheader("Add a concert tour document")
    user_text = st.text_area("Paste your document text here", height=250)

    if st.button("Ingest Document"):
        if user_text.strip():
            result = ingest_document(user_text)
            st.success(result)
        else:
            st.warning("Please paste some text before clicking ingest.")
else:
    st.subheader("Ask about concert tours")
    question = st.text_input("Enter your question")

    if st.button("Ask"):
        if question.strip():
            answer = answer_question(question)
            st.info(f" {answer}")
        else:
            st.warning("Please enter a question.")
