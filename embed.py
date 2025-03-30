# embed.py
from sentence_transformers import SentenceTransformer

# Load the model (this will download the model if not cached)
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    return model.encode(text, convert_to_tensor=True)
