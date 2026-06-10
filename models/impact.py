from dataclasses import dataclass
from typing import List


@dataclass
class Impact:
    dataset: str
    affected_assets: List[str]
    owner_team: str