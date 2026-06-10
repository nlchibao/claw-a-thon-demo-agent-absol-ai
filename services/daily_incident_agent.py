from pathlib import Path

from services.incident_service import (
    IncidentService
)


class DailyIncidentAgent:

    def run(self):

        results = []

        incident_dir = Path(
            "data/incidents"
        )

        for file in sorted(
            incident_dir.glob(
                "*.json"
            )
        ):

            number = (
                file.stem.split("_")[1]
            )

            incident_id = (
                f"INC_{number}"
            )

            result = (
                IncidentService()
                .analyze(
                    incident_id
                )
            )

            results.append(
                result
            )

        return results