from langchain_ollama import ChatOllama
from app.utils.config import settings


llm = ChatOllama(
    model=settings.OLLAMA_MODEL,
    base_url=settings.OLLAMA_BASE_URL,
    temperature=0.2,
)


def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to the local Ollama model and returns the response.
    """
    response = llm.invoke(prompt)
    return response.content