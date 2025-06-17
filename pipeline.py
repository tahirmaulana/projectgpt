from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import FARMReader, TransformersReader, DensePassageRetriever
from haystack.pipelines import ExtractiveQAPipeline
from haystack import Document

# Buat document store
document_store = InMemoryDocumentStore()

# Sample dokumen
docs = [
    Document(content="Haystack is an open-source NLP framework."),
    Document(content="It supports question answering, semantic search, and more.")
]

# Simpan dokumen
document_store.write_documents(docs)

# Retriever & Reader
retriever = DensePassageRetriever(document_store=document_store)
document_store.update_embeddings(retriever)

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

# Pipeline QA ekstraktif
pipe = ExtractiveQAPipeline(reader, retriever)

# Contoh query
query = "What is Haystack?"

result = pipe.run(query=query, params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 1}})

print(result["answers"][0].answer)
