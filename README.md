# Incident AI Orchestrator

## Overview

Multi-agent incident management platform built using:

- Python
- Microsoft AutoGen Core
- Agentic AI Architecture
- Event-driven agent communication


## Current Agents

### Ticket Agent
Creates and validates incidents.

### Triaging Agent
Classifies incident severity and category.

### Monitoring Agent
Checks application health.

### Knowledge Agent
Retrieves historical solutions.

### RCA Agent
Determines probable root cause.


## Architecture


Ticket Agent
      |
      v
Triaging Agent
      |
 ----------------
 |              |
Monitoring   Knowledge
 |              |
 ----------------
       |
       v
Orchestrator
       |
       v
RCA Agent


## Future Enhancements

- Recommendation Agent
- Human Approval Workflow
- ServiceNow Integration
- Jira Integration
- MCP Tool Integration
- RAG Knowledge Base
- LLM-based RCA