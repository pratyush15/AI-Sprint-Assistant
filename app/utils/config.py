from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    DATABASE_URL = os.getenv("DATABASE_URL")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")
    OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL")

settings = Settings()