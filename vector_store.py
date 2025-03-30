# vector_store.py
import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []  # store the associated texts

    def add(self, embeddings, texts):
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding, top_k: int = 5):
        distances, indices = self.index.search(query_embedding, top_k)
        results = []
        for distance, idx in zip(distances[0], indices[0]):
            if idx < len(self.texts):
                results.append((self.texts[idx], distance))
        return results

def tensor_to_numpy(tensor):
    if hasattr(tensor, "cpu"):
        return tensor.cpu().detach().numpy().astype('float32')
    return np.array(tensor).astype('float32')
