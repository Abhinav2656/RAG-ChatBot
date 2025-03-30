# 🚀 RAG-Based Chatbot using Groq LLM

## 📚 **Objective**
As a RAG (Retrieval-Augmented Generation) enthusiast, I wanted to build and test a chatbot capable of:
- Scraping website content.
- Generating relevant answers using retrieved information.
- Leveraging Groq LLM for enhanced response accuracy.

---

## ⚡️ **Tech Stack**
- 🐍 Python 3.11+
- 📚 LangChain
- 🦗 Hugging Face (Flan-T5)
- 🧠 Groq LLM (`langchain_groq`)
- 🔎 BeautifulSoup (Scraping)
- 🟣️ FAISS (Vector Store)

---

## 🛠️ **Implementation Steps**
1. **Scraping Module:**  
   - Extracts website content using `BeautifulSoup`.
   - Breaks text into manageable chunks.

2. **Embedding Generation:**  
   - Converts chunks into embeddings using `SentenceTransformer`.

3. **Vector Storage:**  
   - Stores embeddings using FAISS for quick retrieval.

4. **Query Processing:**  
   - Retrieves relevant chunks and sends context to Groq LLM.

5. **Answer Generation:**  
   - Generates an appropriate response with fallback if no context is found.

---

## 💂 **Folder Structure**
```
├── scrape.py          # Scrapes website content
├── embed.py           # Generates embeddings
├── vector_store.py    # Handles vector storage & retrieval
├── rag_chatbot.py     # Main RAG chatbot logic
└── requirements.txt   # Required dependencies
```

---

## 🛆 **Installation**
```bash
# Clone the repository
git clone https://github.com/username/rag-chatbot.git

# Navigate to the project directory
cd rag-chatbot

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
# or
.venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 **Usage**
```bash
# Run the chatbot
python rag_chatbot.py
```

---

## ⚡️ **Features**
- ✅ Website scraping & chunking
- ✅ Context-based retrieval
- ✅ High-quality responses with Groq LLM
- ✅ Handles fallback queries gracefully

---

## 🧩 **Future Improvements**
- 🤖 Improve response relevance with fine-tuning.
- ⚡ Add support for multiple LLM models.
- 📈 Optimize chunking for large websites.
