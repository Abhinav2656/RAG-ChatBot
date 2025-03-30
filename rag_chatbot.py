from scrape import scrape_website
from embed import get_embedding
from vector_store import VectorStore, tensor_to_numpy
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import numpy as np

# Initialize Groq LLM with API key and model
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key="your_groq_api_key")

# Define prompt templates
prompt_with_context = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "You are an AI assistant that answers questions using the context below.\n\n"
        "Context:\n{context}\n\n"
        "Question: {question}\n"
        "Answer:"
    )
)

prompt_without_context = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are an AI assistant who answers questions to the best of your knowledge.\n\n"
        "Question: {question}\n"
        "Answer:"
    )
)

# Chunk text into manageable pieces
def chunk_text(text: str, max_chunk_size: int = 500):
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + '. '
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + '. '
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# RAG Chatbot class
class RAGChatbot:
    def __init__(self):
        self.dim = 384
        self.store = VectorStore(dim=self.dim)

    def ingest_website(self, url: str):
        text = scrape_website(url)
        chunks = chunk_text(text)
        embeddings = []
        for chunk in chunks:
            emb = get_embedding(chunk)
            embeddings.append(tensor_to_numpy(emb))
        
        embeddings = np.vstack(embeddings)
        self.store.add(embeddings, chunks)
    
    def generate_answer(self, question: str, context: str = None) -> str:
        if context:
            chain = LLMChain(llm=llm, prompt=prompt_with_context)
            prompt_input = {"context": context, "question": question}
        else:
            chain = LLMChain(llm=llm, prompt=prompt_without_context)
            prompt_input = {"question": question}
        
        response = chain.run(prompt_input)
        return response

    def answer_query(self, query: str, top_k: int = 5):
        # Generate query embedding
        query_embedding = get_embedding(query)
        query_embedding = tensor_to_numpy(query_embedding).reshape(1, -1)
        
        # Retrieve relevant chunks
        retrieved = self.store.search(query_embedding, top_k=top_k)
        relevant_chunks = [chunk for chunk, distance in retrieved if distance < 0.5]
        
        # Combine relevant chunks as context or leave empty
        context = "\n".join(relevant_chunks) if relevant_chunks else None
        
        # Generate the final answer
        answer = self.generate_answer(query, context)
        return answer
