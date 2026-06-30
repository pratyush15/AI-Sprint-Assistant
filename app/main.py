from fastapi import FastAPI
from app.utils.config import settings
from app.database.db import Base
from app.database.db import engine
from app.api.routes import router
from app.api.ai_routes import router as ai_router
from app.api.vector_routes import router as vector_router
from app.api.sprint_routes import (
    router as sprint_router
)
from app.database.embedding_seed import (
    seed_embeddings
)
from app.database.seed import seed_database

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
seed_database()
seed_embeddings()
app.include_router(router) 
app.include_router(ai_router)
app.include_router(vector_router)
app.include_router(
    sprint_router
)

@app.get("/")
def home():
    return {
        "message": "AI Sprint Assistant Backend is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }




