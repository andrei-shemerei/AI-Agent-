import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

Settings.llm = None

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_index(data, index_name):
    index=None
    if not os.path.exists(index_name):
        print("Start building index", index_name)
        index =VectorStoreIndex.from_documents(data, embed_model=embed_model, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name), embed_model=embed_model)

    return index


pdf_path = os.path.join("data", "Poland.pdf")
document_data = PDFReader().load_data(file=pdf_path)
document_index = get_index(document_data, "document")
document_engine = document_index.as_query_engine()

