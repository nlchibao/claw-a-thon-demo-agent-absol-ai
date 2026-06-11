from services.daily_incident_agent import (
    DailyIncidentAgent
)


class AbsolAgent:

    def run(self):

        return (
            DailyIncidentAgent()
            .run()
        )