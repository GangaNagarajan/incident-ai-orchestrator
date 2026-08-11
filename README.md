# 🚨 Incident AI Orchestrator

## Multi-Agent AI Platform for Intelligent Incident Management using AutoGen Core, MCP, RAG and Agentic AI

---

## 📌 Overview

Incident AI Orchestrator is an enterprise-grade **Agentic AI based incident management automation platform** that uses multiple specialized AI agents to analyze, diagnose, and resolve production incidents.

The platform simulates how modern enterprises handle IT incidents by coordinating multiple autonomous agents:

- Incident classification
- Dynamic workflow orchestration
- Application monitoring
- Log analysis
- Knowledge retrieval using RAG
- Root Cause Analysis (RCA)
- Resolution recommendation
- Approval workflow
- Incident communication and updates

The solution is built using:

- **Microsoft AutoGen Core** for multi-agent communication
- **Model Context Protocol (MCP)** for external tool integration
- **RAG (Retrieval Augmented Generation)** for enterprise knowledge retrieval
- **FAISS Vector Database** for semantic search
- **Sentence Transformers** for embeddings
- **Python** based agent architecture

---

# 🎯 Business Problem

Large enterprises receive thousands of production incidents every day through platforms like:

- ServiceNow
- Jira Service Management
- BMC Remedy

Manual incident resolution involves:

1. Reading incident description
2. Identifying impacted application
3. Checking monitoring dashboards
4. Searching previous incidents
5. Reviewing logs
6. Finding root cause
7. Suggesting resolution
8. Getting approval
9. Updating incident records


This process is:

- Time consuming
- Error prone
- Dependent on human expertise
- Difficult to scale


## Solution

Incident AI Orchestrator introduces autonomous AI agents that collaborate to reduce:

- Mean Time To Detect (MTTD)
- Mean Time To Resolve (MTTR)
- Manual investigation effort

---

# 🏗️ High Level Architecture

            Incident Created
                  |
                  |
          Ticket Agent
                  |
                  |
         Triaging Agent
                  |
                  |
    Master Orchestrator Agent
                  |
    --------------------------------
    |              |               |
    |              |               |
Monitoring Knowledge RCA
Agent Agent Agent
| |
| |
MCP Tools RAG Pipeline
|
|

| | |
Health Logs Deployment

                  |
                  |
      Recommendation Agent

                  |
                  |
        Approval Agent

                  |
                  |
    Incident Update Agent

                  |
                  |
          Final Resolution

---

# 🤖 Agent Architecture

## 1. Ticket Agent

### Responsibility

Receives new incidents and forwards them into the AI workflow.


Input:

```json
{
"incident_id":"INC1001",
"title":"Payment API Failure",
"description":"Payment API returning 503 errors"
}

Output:

Routes incident to Triaging Agent.

2. Triaging Agent
Responsibility

Analyzes incident details and determines:

Incident category
Priority
Required workflow

Example:

Input:

Payment API returning 503 errors due to database connection timeout

Output:

{
"category":"Database Failure",
"priority":"P1"
}

Decision:

Send incident to Master Orchestrator
3. Master Orchestrator Agent
Responsibility

Acts as the brain of the system.

Responsibilities:

Understand incident context
Decide required agents
Dynamically create workflow

Example:

{
"agents_triggered":
[
"monitoring",
"knowledge",
"rca"
]
}
4. Monitoring Agent
Responsibility

Collects application evidence using MCP tools.

The agent integrates with external enterprise systems.

Currently simulated MCP tools:

Monitoring MCP Tool
Log MCP Tool
Deployment MCP Tool

Example output:

{
"health":
{
"status":"DEGRADED",
"cpu_usage":"78%",
"memory_usage":"82%",
"database_connections":"500/500"
}
}

Logs:

[
"ERROR Database connection timeout",
"ERROR Connection pool exhausted"
]

Deployment:

{
"latest_deployment":
"payment-service-v2.4",
"deployment_time":
"30 minutes ago"
}
5. Knowledge Agent (RAG)
Responsibility

Uses Retrieval Augmented Generation to find historical solutions.

Architecture:

Knowledge Documents

        |
        |
 Text Chunking

        |
        |
 Embedding Model

        |
        |
 FAISS Vector Database

        |
        |
 Semantic Retrieval

        |
        |
 Relevant Solutions

Technology:

Sentence Transformers
FAISS

Example:

Query:

Database connection timeout

Retrieved knowledge:

{
"similar_incidents":
[
"INC9732 - Payment API degradation",
"INC9821 - Database timeout issue"
],

"recommended_resolutions":
[
"Restart service",
"Increase database connection pool"
]
}
6. RCA Agent
Responsibility

Analyzes:

Incident description
Monitoring evidence
Logs
Deployment history
Historical incidents

Example:

Input:

Database connections reached maximum capacity
Connection pool exhausted

Output:

{
"root_cause":
"Database connection pool exhausted",

"confidence":
0.98
}

Evidence:

- Database connectivity issue
- Maximum DB connections reached
- Application logs show pool exhaustion
- Recent deployment detected
7. Recommendation Agent
Responsibility

Generates corrective actions.

Example:

{
"recommended_actions":
[
"Increase database connection pool size",
"Restart application services",
"Monitor database utilization",
"Review timeout configuration"
],

"automation_possible":
true,

"requires_approval":
true
}
8. Approval Agent
Responsibility

Controls execution governance.

Example:

{
"approval_required":true,
"approval_status":
"PENDING_APPROVAL"
}

Future integration:

ServiceNow Approval
Teams Approval
Email Approval
9. Incident Update Agent
Responsibility

Updates incident status and communication.

Output:

{
"status":
"IN_PROGRESS",

"updated_by":
"Incident AI Orchestrator"
}
🧠 Agent Communication Flow
Ticket Agent

      |
      v

Triaging Agent

      |
      v

Master Orchestrator

      |
      |
 ---------------------
 |          |          |
 v          v          v

Monitoring Knowledge  RCA

      |
      |
 Recommendation

      |
      |
 Approval

      |
      |
 Incident Update
🔌 MCP Integration
Model Context Protocol

MCP enables AI agents to securely interact with external enterprise systems.

Current MCP simulated integrations:

Monitoring MCP

Provides:

Application health
CPU usage
Memory usage
Log MCP

Provides:

Application logs
Error messages
Deployment MCP

Provides:

Deployment history
Release information

Future integrations:

New Relic
Datadog
Splunk
Prometheus
Jenkins
Azure DevOps
ServiceNow
Jira
🛠️ Technology Stack
Programming Language
Python 3.12
Agent Framework
Microsoft AutoGen Core
AI Frameworks
LangChain
Sentence Transformers
RAG
Vector Database
FAISS
Embedding Model
all-MiniLM-L6-v2
Protocol
MCP (Model Context Protocol)
📂 Project Structure
incident-ai-orchestrator

│
├── app
│
│   ├── agents
│   │
│   │   ├── ticket_agent.py
│   │   ├── triaging_agent.py
│   │   ├── monitoring_agent.py
│   │   ├── knowledge_agent.py
│   │   ├── rca_agent.py
│   │   ├── recommendation_agent.py
│   │   ├── approval_agent.py
│   │   └── incident_update_agent.py
│   │
│   │
│   ├── autogen_core
│   │
│   │   ├── agents
│   │   ├── messages
│   │   └── runtime
│   │
│   │
│   ├── rag
│   │
│   │   ├── embeddings.py
│   │   ├── knowledge_loader.py
│   │   └── vector_store.py
│   │
│   │
│   ├── mcp
│   │
│   │   ├── monitoring_tool.py
│   │   ├── log_tool.py
│   │   └── deployment_tool.py
│
│
├── knowledge_base
│
├── test_autogen_core_flow.py
│
├── requirements.txt
│
└── README.md

⚙️ Installation
Clone Repository
git clone https://github.com/GangaNagarajan/incident-ai-orchestrator.git

cd incident-ai-orchestrator
Create Virtual Environment
python3 -m venv venv

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
▶️ Running the Application

Execute:

python test_autogen_core_flow.py
🧪 Sample Execution
========== Ticket Routed Agent ==========

Processing incident...


========== Triaging Routed Agent ==========

Category: Database Failure
Priority: P1


========== Master Orchestrator ==========

Next Agents:

[
monitoring,
knowledge,
rca
]


========== Monitoring Agent ==========

Collecting application evidence


========== Knowledge Agent ==========

RAG retrieval completed


========== RCA Agent ==========

Root Cause:
Database connection pool exhausted

Confidence:
0.98


========== Recommendation Agent ==========

Recommendations generated


========== Approval Agent ==========

Approval Required


========== Incident Update Agent ==========

Incident Updated Successfully

📊 Final Incident Output Example
{
"incident_id":"INC1001",

"category":
"Database Failure",

"priority":
"P1",

"root_cause":
"Database connection pool exhausted",

"confidence":
0.98,

"recommended_actions":
[
"Increase database connection pool",
"Restart application",
"Review timeout configuration"
]
}
🚀 Future Enhancements
Enterprise Integrations
ServiceNow Connector
Jira Connector
Splunk Connector
Datadog Connector
Advanced AI Capabilities
GPT-4o / Azure OpenAI integration
LLM based RCA reasoning
Automated remediation
Self-healing applications
Observability
LangSmith tracing
Agent execution monitoring
Token monitoring
Cost optimization
Security
RBAC
Human approval workflow
Audit logging
🎯 Interview Explanation

This project demonstrates:

✅ Agentic AI architecture
✅ Multi-agent orchestration
✅ AutoGen Core implementation
✅ MCP based tool calling
✅ RAG pipeline implementation
✅ Vector database integration
✅ Enterprise incident automation
✅ AI driven RCA

👨‍💻 Author

Ganga Nagarajan

Senior AI Engineer | GenAI | Agentic AI | RAG | Python