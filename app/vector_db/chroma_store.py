
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from app.utils.config import settings


embeddings = OllamaEmbeddings(
    model=settings.OLLAMA_EMBED_MODEL,
    base_url=settings.OLLAMA_BASE_URL,
)

vector_store = Chroma(
    collection_name="tickets",
    embedding_function=embeddings,
    persist_directory=settings.CHROMA_DB_PATH,
)


def add_document(doc_id: str, text: str):
    vector_store.add_texts(
        texts=[text],
        ids=[doc_id]
    )


def search_documents(query: str, k: int = 5):
    return vector_store.similarity_search_with_score(
        query,
        k=k
    )


def document_exists(doc_id: str):
    data = vector_store.get(
        ids=[doc_id]
    )

    return len(data["ids"]) > 0




