from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.incident_schema import (
    IncidentCreate,
    IncidentUpdate
)

from app.schemas.agent_context_schema import IncidentContext

from app.services.incident_service import IncidentService

from app.database.session import get_db

from app.services.incident_orchestrator_service import (
    IncidentOrchestratorService
)

from app.agents.scope_agent import ScopeAgent


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


service = IncidentService()

orchestrator_service = IncidentOrchestratorService()

scope_agent = ScopeAgent()


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


@router.post("/{incident_id}/process")
async def process_incident(
    incident_id: str,
    db: Session = Depends(get_db)
):

    print(
        f"\n[API] AI processing requested for {incident_id}"
    )

    # -----------------------------------------
    # GET INCIDENT
    # -----------------------------------------

    incident = service.get_incident(
        db,
        incident_id
    )

    if not incident:

        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    # -----------------------------------------
    # SCOPE VALIDATION
    # -----------------------------------------

    print(
        "[API] Validating incident scope..."
    )

    context = IncidentContext(

        incident_id=
            incident.incident_id,

        title=
            incident.title,

        description=
            incident.description,

        application=
            incident.application,

        environment=
            incident.environment,

        status=
            incident.status,

        agent_outputs={}
    )

    updated_context = scope_agent.process(
        context
    )

    scope = updated_context.agent_outputs.get(
        "scope",
        {}
    )

    # -----------------------------------------
    # REJECT NON-INCIDENT
    # -----------------------------------------

    if scope.get("is_incident") is False:

        print(
            "[API] Non-incident request rejected"
        )

        return {

            "status":
                "REJECTED",

            "message":
                "This is not an enterprise IT incident.",

            "reason":
                scope.get(
                    "reason",
                    "Request is outside enterprise IT incident scope."
                )

        }

    # -----------------------------------------
    # START AI WORKFLOW
    # -----------------------------------------

    print(
        "[API] Incident validated."
    )

    print(
        "[API] Starting full AI workflow..."
    )

    result = await orchestrator_service.process_incident(
        incident
    )

    return {

        "status":
            "STARTED",

        "message":
            "Incident AI workflow started",

        "result":
            result

    }


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

        "status":
            incident.status,

        "priority":
            incident.priority,

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