import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

INDEX_PATH = "data/faiss.index"
META_PATH = "data/meta.pkl"

os.makedirs("data", exist_ok=True)

def get_embedding(text: str):
    return model.encode([text])[0]

def save_metadata(metadata):
    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)

def load_metadata():
    if os.path.exists(META_PATH):
        with open(META_PATH, "rb") as f:
            return pickle.load(f)
    return []

def init_index(dimension=384):
    if os.path.exists(INDEX_PATH):
        return faiss.read_index(INDEX_PATH)
    return faiss.IndexFlatL2(dimension)

def save_index(index):
    faiss.write_index(index, INDEX_PATH)

def add_document_to_index(text: str, metadata: dict):
    index = init_index()
    embedding = get_embedding(text)
    index.add(np.array([embedding]))
    save_index(index)

    meta = load_metadata()
    meta.append(metadata)
    save_metadata(meta)

def search_similar_documents(query: str, k=3):
    index = init_index()
    if index.ntotal == 0:
        return []
    embedding = get_embedding(query)
    distances, indices = index.search(np.array([embedding]), k)
    metadata = load_metadata()
    return [metadata[i] for i in indices[0] if i < len(metadata)]
