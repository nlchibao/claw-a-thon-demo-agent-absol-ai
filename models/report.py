from dataclasses import dataclass
from typing import List


@dataclass
class Report:
    incident_id: str
    category: str
    severity: str
    dataset: str
    affected_assets: List[str]
    recommendations: List[str]