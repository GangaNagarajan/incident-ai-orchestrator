from fastapi import FastAPI


app = FastAPI(
    title="Incident AI Orchestrator",
    description="Multi-Agent Incident Management Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "Incident AI Orchestrator",
        "message": "Platform is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }