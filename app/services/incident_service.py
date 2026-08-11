import uuid

from sqlalchemy.orm import Session

from app.repositories.incident_repository import IncidentRepository


class IncidentService:

    def __init__(self):
        self.repository = IncidentRepository()


    def create_incident(
        self,
        db: Session,
        incident
    ):

        incident_data = incident.model_dump()

        incident_data["incident_id"] = (
            f"INC-{uuid.uuid4().hex[:6].upper()}"
        )

        incident_data["status"] = "OPEN"
        incident_data["priority"] = "HIGH"


        return self.repository.save(
            db,
            incident_data
        )


    def get_all_incidents(
        self,
        db: Session
    ):

        return self.repository.get_all(db)


    def get_incident(
        self,
        db: Session,
        incident_id: str
    ):

        return self.repository.get_by_id(
            db,
            incident_id
        )


    def update_incident(
        self,
        db: Session,
        incident_id: str,
        updates
    ):

        return self.repository.update(
            db,
            incident_id,
            updates.model_dump(
                exclude_none=True
            )
        )

    def update_ai_result(
        self,
        db: Session,
        incident_id: str,
        data: dict
    ):

        return self.repository.update_ai_result(
            db,
            incident_id,
            data
        )