from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.incident_schema import (
    IncidentCreate,
    IncidentUpdate
)

from app.services.incident_service import IncidentService
from app.database.session import get_db


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


service = IncidentService()


@router.post("/")
def create_incident(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):

    return service.create_incident(
        db,
        incident
    )


@router.get("/")
def get_all_incidents(
    db: Session = Depends(get_db)
):

    return service.get_all_incidents(
        db
    )


@router.get("/{incident_id}")
def get_incident(
    incident_id: str,
    db: Session = Depends(get_db)
):

    incident = service.get_incident(
        db,
        incident_id
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident


@router.put("/{incident_id}")
def update_incident(
    incident_id: str,
    updates: IncidentUpdate,
    db: Session = Depends(get_db)
):

    incident = service.update_incident(
        db,
        incident_id,
        updates
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident