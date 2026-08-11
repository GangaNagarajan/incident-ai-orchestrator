from sqlalchemy.orm import Session

from app.models.incident import Incident


class IncidentRepository:

    def save(
        self,
        db: Session,
        incident_data: dict
    ):

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

    def get_all(
        self,
        db: Session
    ):

        return db.query(
            Incident
        ).all()

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
        db.refresh(
            incident
        )

        return incident

    def update_ai_analysis(
        self,
        db: Session,
        incident_id: str,
        agent_outputs: dict
    ):

        incident = self.get_by_id(
            db,
            incident_id
        )

        if not incident:
            return None

        rca = agent_outputs.get(
            "rca",
            {}
        )

        knowledge = agent_outputs.get(
            "knowledge",
            {}
        )

        recommendation = agent_outputs.get(
            "recommendation",
            {}
        )

        approval = agent_outputs.get(
            "approval",
            {}
        )

        incident.root_cause = rca.get(
            "root_cause"
        )

        incident.confidence = str(
            rca.get(
                "confidence",
                ""
            )
        )

        incident.knowledge = str(
            knowledge
        )

        incident.recommendations = str(
            recommendation
        )

        incident.approval_status = approval.get(
            "approval_status"
        )

        incident.incident_summary = (
            agent_outputs
            .get(
                "incident_update",
                {}
            )
            .get(
                "summary"
            )
        )

        incident.status = (
            agent_outputs
            .get(
                "incident_update",
                {}
            )
            .get(
                "status",
                incident.status
            )
        )

        db.commit()

        db.refresh(
            incident
        )

        return incident

    def update_ai_result(
        self,
        db: Session,
        incident_id: str,
        data: dict
    ):

        incident = self.get_by_id(
            db,
            incident_id
        )

        if not incident:
            return None

        for key, value in data.items():

            setattr(
                incident,
                key,
                value
            )

        db.commit()

        db.refresh(
            incident
        )

        return incident