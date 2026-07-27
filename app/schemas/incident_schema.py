from pydantic import BaseModel, Field
from typing import Optional


class IncidentCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str
    application: str
    environment: str


class IncidentResponse(BaseModel):
    incident_id: str
    title: str
    description: str
    application: str
    environment: str
    status: str
    priority: str


class IncidentUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None