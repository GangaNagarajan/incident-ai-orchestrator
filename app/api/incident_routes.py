from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.incident_schema import (
    IncidentCreate,
    IncidentUpdate
)

from app.services.incident_service import IncidentService
from app.database.session import get_db

from app.services.incident_orchestrator_service import (
    IncidentOrchestratorService
)


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


service = IncidentService()

orchestrator_service = IncidentOrchestratorService()


# ============================================================
# CREATE INCIDENT
# ============================================================

@router.post("/")
def create_incident(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):

    return service.create_incident(
        db,
        incident
    )


# ============================================================
# GET ALL INCIDENTS
# ============================================================

@router.get("/")
def get_all_incidents(
    db: Session = Depends(get_db)
):

    return service.get_all_incidents(
        db
    )


# ============================================================
# GET SINGLE INCIDENT
# ============================================================

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


# ============================================================
# UPDATE INCIDENT
# ============================================================

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


# ============================================================
# START AI ANALYSIS
# ============================================================

@router.post("/{incident_id}/process")
async def process_incident(
    incident_id: str,
    db: Session = Depends(get_db)
):

    print(
        f"\n[API] AI processing requested for {incident_id}"
    )

    # --------------------------------------------------------
    # Get incident
    # --------------------------------------------------------

    incident = service.get_incident(
        db,
        incident_id
    )

    if not incident:

        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    # --------------------------------------------------------
    # Start orchestrator
    # Scope validation is handled inside the workflow.
    # --------------------------------------------------------

    result = await orchestrator_service.process_incident(
        incident
    )

    # --------------------------------------------------------
    # Return persisted workflow result
    # --------------------------------------------------------

    return result


# ============================================================
# GET AI ANALYSIS
# ============================================================

@router.get("/{incident_id}/analysis")
def get_analysis(
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

    return {

        "incident_id":
            incident.incident_id,

        # ----------------------------------------
        # AI workflow status
        # PENDING / RUNNING / COMPLETED /
        # REJECTED / FAILED
        # ----------------------------------------

        "analysis_status":
            incident.analysis_status,

        # ----------------------------------------
        # Failure information
        # ----------------------------------------

        "analysis_error":
            incident.analysis_error,

        # ----------------------------------------
        # Scope rejection information
        # ----------------------------------------

        "rejection_reason":
            incident.rejection_reason,

        # ----------------------------------------
        # Incident information
        # ----------------------------------------

        "status":
            incident.status,

        "priority":
            incident.priority,

        # ----------------------------------------
        # AI analysis results
        # ----------------------------------------

        "root_cause":
            incident.root_cause,

        "confidence":
            incident.confidence,

        "knowledge":
            incident.knowledge,

        "recommendations":
            incident.recommendations,

        "approval_status":
            incident.approval_status,

        "summary":
            incident.incident_summary
    }