from sqlalchemy import Column, String

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
        String,
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