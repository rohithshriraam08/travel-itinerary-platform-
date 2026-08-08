from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Travel Itinerary Planning and Sharing Platform",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Travel Itinerary Planning and Sharing Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }