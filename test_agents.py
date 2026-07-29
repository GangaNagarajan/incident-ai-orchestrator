from app.orchestrator.autogen_manager import IncidentOrchestrator


incident = {

    "incident_id": "INC1001",

    "title": "Payment API Failure",

    "description":
    "Payment API returning 503 errors due to database connection timeout",

    "application":
    "Payment Service",

    "environment":
    "PRODUCTION"
}


orchestrator = IncidentOrchestrator()


result = orchestrator.process_incident(
    incident
)


print("\nFinal Incident Context")

print(
    result.model_dump_json(
        indent=2
    )
)