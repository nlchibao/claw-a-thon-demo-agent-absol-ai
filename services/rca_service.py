from services.llm_service import LLMService


class RCAService:

    def generate(
        self,
        incident
    ):

        prompt = f"""
You are a senior DataOps Incident Manager.

Analyze the following incident.

Incident:
{incident}

Provide:

1. Root Cause Analysis
2. Business Impact
3. Investigation Steps
4. Recommended Resolution

Keep the response concise and professional.
"""

        return (
            LLMService()
            .generate(
                prompt
            )
        )