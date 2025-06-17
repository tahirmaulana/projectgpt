from unstructured.partition.pdf import partition_pdf
import os
import re
import time

def process_pdf(filepath: str):
    elements = partition_pdf(filepath, strategy="hi_res")
    full_text = "\n\n".join([el.text for el in elements if el.text.strip()])
    
    filename = os.path.basename(filepath)
    judul = re.sub(r"\.pdf$", "", filename).replace("_", " ")
    
    metadata = {
        "judul": judul,
        "sumber": filename,
        "timestamp": int(time.time())
    }
    
    chunk_size = 512
    chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size - 50)]
    return chunks, metadata
