from sqlalchemy.orm import Session

from app.models.incident import Incident


class IncidentRepository:

    def save(self, db: Session, incident_data: dict):

        incident = Incident(
            incident_id=incident_data["incident_id"],
            title=incident_data["title"],
            description=incident_data["description"],
            application=incident_data["application"],
            environment=incident_data["environment"],
            status=incident_data["status"],
            priority=incident_data["priority"]
        )

        db.add(incident)
        db.commit()
        db.refresh(incident)

        return incident


    def get_all(self, db: Session):

        return db.query(Incident).all()


    def get_by_id(
        self,
        db: Session,
        incident_id: str
    ):

        return (
            db.query(Incident)
            .filter(
                Incident.incident_id == incident_id
            )
            .first()
        )


    def update(
        self,
        db: Session,
        incident_id: str,
        updates: dict
    ):

        incident = self.get_by_id(
            db,
            incident_id
        )

        if not incident:
            return None


        for key, value in updates.items():

            setattr(
                incident,
                key,
                value
            )


        db.commit()
        db.refresh(incident)

        return incident