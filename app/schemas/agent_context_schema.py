from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class IncidentContext(BaseModel):

    incident_id: str

    title: str

    description: str

    application: str

    environment: str

    status: str = "OPEN"

    priority: Optional[str] = None

    category: Optional[str] = None

    next_agents: List[str] = Field(
        default_factory=list
    )

    agent_outputs: Dict = Field(
        default_factory=dict
    )