import ollama
from .chroma_manager import ProjectGPTDB
from .pdf_processor import process_pdf
import os

class ProjectGPTBrain:
    def __init__(self):
        self.db = ProjectGPTDB()
        self.llm = "mistral"
    
    def ingest_pdf(self, filepath: str):
        chunks, metadata = process_pdf(filepath)
        self.db.inject_knowledge(chunks, [metadata]*len(chunks))
        os.rename(filepath, f"./data/processed/{os.path.basename(filepath)}")
        return f"✅ {len(chunks)} chunk tersimpan"
    
    def ask(self, question: str):
        results = self.db.query(question)
        context = "\n\n".join(results["documents"][0])
        
        prompt = f"""
        [PROJECTGPT - SEMANTIC LOGIC MODE]
        Context: {context}
        
        Question: {question}
        
        Aturan:
        1. Jawab HANYA berdasarkan context
        2. Gunakan logika deduktif/induktif
        3. Format: [KESIMPULAN] + [PENJELASAN LOGIS]
        4. Jangan tambahkan informasi di luar context!
        """
        
        response = ollama.chat(
            model=self.llm,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
