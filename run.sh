#!/bin/bash

# Setup environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install chromadb sentence-transformers unstructured[pdf] pypdf gradio ollama

# Download embedding model
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Create folders
mkdir -p data/{uploads,processed,chroma_db}

# Run!
echo "PROJECTGPT STARTING... ACCESS http://localhost:7860"
python ui/app.py