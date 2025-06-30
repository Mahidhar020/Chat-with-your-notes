import streamlit as st
from utils.pdf_handler import load_pdf_text, create_vector_store, answer_query

st.set_page_config(page_title="Chat with Your Notes", layout="wide")
st.title("Chat with Your Notes")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
if uploaded_file:
    with st.spinner("Reading PDF..."):
        text = load_pdf_text(uploaded_file)
        vectordb = create_vector_store(text)

    query = st.text_input("Ask a question about your notes:")
    if query:
        with st.spinner("Thinking..."):
            response = answer_query(vectordb, query)
            st.markdown(f"**Answer:** {response}")