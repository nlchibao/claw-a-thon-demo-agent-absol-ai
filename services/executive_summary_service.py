from services.llm_service import (
    LLMService
)


class ExecutiveSummaryService:

    def generate(
        self,
        incidents,
        summary
    ):

        prompt = f"""
You are a senior DataOps Incident Manager.

Analyze today's incidents.

Summary:
{summary}

Incidents:
{incidents}

Provide:

1. Executive Summary
2. Most Critical Incident
3. Business Impact
4. Recommended Actions

Maximum 150 words.
"""

        return (
            LLMService()
            .generate(
                prompt
            )
        )