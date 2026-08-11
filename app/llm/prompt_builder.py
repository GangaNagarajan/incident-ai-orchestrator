from app.llm.system_prompts import RCA_SYSTEM_PROMPT


def build_rca_prompt(context: dict):

    monitoring = context.get(
        "agent_outputs",
        {}
    ).get(
        "monitoring",
        {}
    )

    knowledge = context.get(
        "agent_outputs",
        {}
    ).get(
        "knowledge",
        {}
    )

    prompt = f"""
Incident

Title:
{context.get("title")}

Description:
{context.get("description")}

Application:
{context.get("application")}

Monitoring

{monitoring}

Knowledge

{knowledge}
"""

    return RCA_SYSTEM_PROMPT, prompt