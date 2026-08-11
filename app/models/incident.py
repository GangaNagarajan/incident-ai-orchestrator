from sqlalchemy import Column, String, Text

from app.database.base import Base


class Incident(Base):

    __tablename__ = "incidents"

    incident_id = Column(
        String,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    application = Column(
        String,
        nullable=False
    )

    environment = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    priority = Column(
        String,
        nullable=False
    )

    root_cause = Column(
        Text,
        nullable=True
    )

    confidence = Column(
        String,
        nullable=True
    )

    knowledge = Column(
        Text,
        nullable=True
    )

    recommendations = Column(
        Text,
        nullable=True
    )

    approval_status = Column(
        String,
        nullable=True
    )

    incident_summary = Column(
        Text,
        nullable=True
    )