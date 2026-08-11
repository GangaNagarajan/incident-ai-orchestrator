from pydantic import BaseModel


class IncidentRequest(BaseModel):

    incident_id: str

    title: str

    description: str

    application: str

    environment: str

    status: str = "OPEN"