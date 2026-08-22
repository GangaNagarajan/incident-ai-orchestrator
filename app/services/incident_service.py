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

        incident = self.repository.get_by_id(
            db,
            incident_id
        )

        if not incident:
            return None

        # Support both Pydantic models and dictionaries
        if hasattr(updates, "model_dump"):

            update_data = updates.model_dump(
                exclude_unset=True
            )

        elif isinstance(updates, dict):

            update_data = updates

        else:

            raise TypeError(
                "updates must be a dictionary or Pydantic model"
            )

        # Apply updates
        for field, value in update_data.items():

            if hasattr(incident, field):

                setattr(
                    incident,
                    field,
                    value
                )

        db.commit()

        db.refresh(incident)

        return incident

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