from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class IncidentMessage:
    """
    Shared incident context exchanged between agents.
    """

    context: Dict[str, Any] = field(default_factory=dict)