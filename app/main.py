from fastapi import FastAPI

from app.api.incident_routes import router as incident_router

from app.database.base import Base
from app.database.database import engine

import app.models.incident


app = FastAPI(
    title="Incident AI Orchestrator",
    version="1.0.0"
)


Base.metadata.create_all(bind=engine)


app.include_router(
    incident_router
)


@app.get("/")
def root():
    return {
        "message": "Incident AI running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }