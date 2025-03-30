import streamlit as st
from rag_chatbot import RAGChatbot

st.title("Local RAG ChatBot")
st.write("Enter a website URL and ask a question about its content.")

url = st.text_input("Website URL", value="https://example.com")
if st.button("Ingest Website"):
    st.write("Scraping and ingesting website content... This may take a minute.")
    chatbot = RAGChatbot()
    try:
        chatbot.ingest_website(url)
        st.session_state.chatbot = chatbot
        st.success("Website ingested successfully!")
    except Exception as e:
        st.error(f"Error during ingestion: {e}")

if "chatbot" in st.session_state:
    query = st.text_input("Your Question")
    if st.button("Get Answer") and query:
        st.write("Generating answer...")
        answer = st.session_state.chatbot.answer_query(query)
        st.write(answer)