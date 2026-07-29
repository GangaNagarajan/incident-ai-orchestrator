from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class IncidentMessage:

    context: Dict[str, Any]