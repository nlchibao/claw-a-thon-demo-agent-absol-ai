import json
from pathlib import Path

from models.incident import Incident


class IncidentLoader:

    def __init__(self):
        self.base_path = Path("data/incidents")

    def load(self, incident_id: str):

        number = incident_id.split("_")[1]

        path = (
            self.base_path
            / f"incident_{number}.json"
        )

        with open(path, "r") as f:
            data = json.load(f)

        return Incident(**data)