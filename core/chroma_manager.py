import chromadb
import time
from sentence_transformers import SentenceTransformer

class ProjectGPTDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./data/chroma_db")
        self.collection = self.client.get_or_create_collection("projectgpt_knowledge")
        self.embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    
    def inject_knowledge(self, chunks: list, metadata: list):
        ids = [f"doc_{int(time.time())}_{i}" for i in range(len(chunks))]
        embeddings = self.embed_model.encode(chunks).tolist()
        self.collection.add(embeddings=embeddings, documents=chunks, metadatas=metadata, ids=ids)
    
    def query(self, question: str, k=3):
        query_embed = self.embed_model.encode([question]).tolist()
        return self.collection.query(query_embeddings=query_embed, n_results=k)
