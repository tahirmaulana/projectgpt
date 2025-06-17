from unstructured.partition.pdf import partition_pdf
import os
import re

def process_pdf(filepath: str):
    elements = partition_pdf(filepath, strategy="hi_res")
    full_text = "\n\n".join([el.text for el in elements if el.text.strip()])
    
    # Generate metadata from filename
    filename = os.path.basename(filepath)
    judul = re.sub(r"\.pdf$", "", filename).replace("_", " ")
    
    metadata = {
        "judul": judul,
        "sumber": filename,
        "timestamp": int(time.time())
    }
    
    # Simple chunking (512 karakter)
    chunks = [full_text[i:i+512] for i in range(0, len(full_text), 500)]
    return chunks, metadata
