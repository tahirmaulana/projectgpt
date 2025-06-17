import gradio as gr
from core.rag_engine import ProjectGPTBrain
import os
import time

brain = ProjectGPTBrain()

def upload_pdf(file):
    new_path = f"./data/uploads/{os.path.basename(file.name)}"
    os.rename(file.name, new_path)
    report = brain.ingest_pdf(new_path)
    return report

def ask_question(question):
    start_time = time.time()
    response = brain.ask(question)
    latency = f"\n\n⏱️ {round(time.time()-start_time, 1)} detik"
    return response + latency

with gr.Blocks(title="ProjectGPT", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🧠 PROJECTGPT - Semantic Logic Engine")
    
    with gr.Tab("📤 Upload Jurnal"):
        gr.Markdown("Upload PDF jurnal ke knowledge base")
        upload = gr.UploadButton("Pilih File PDF", file_types=[".pdf"])
        report = gr.Textbox(label="Status", interactive=False)
        upload.upload(upload_pdf, upload, report)
    
    with gr.Tab("💬 Tanya"):
        gr.Markdown("Ajukan pertanyaan logis berdasarkan jurnal")
        question = gr.Textbox(label="Pertanyaan", placeholder="Contoh: Apa hubungan quantum computing dengan AI?")
        ask_btn = gr.Button("Cari Jawaban Logis")
        answer = gr.Textbox(label="Jawaban", lines=7, interactive=False)
        ask_btn.click(ask_question, question, answer)
    
    gr.Markdown("> ProjectGPT v1.0 · 100% Local & Free")

app.launch(server_port=7860, share=False)
