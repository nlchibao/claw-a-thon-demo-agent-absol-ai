from services.daily_incident_agent import (
    DailyIncidentAgent
)

from services.summary_service import (
    SummaryService
)

incidents = (
    DailyIncidentAgent()
    .run()
)

summary = (
    SummaryService()
    .summarize(
        incidents
    )
)

print(summary)