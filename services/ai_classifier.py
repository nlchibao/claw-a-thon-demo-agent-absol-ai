from services.llm_service import LLMService


class AIClassifier:

    def classify(
        self,
        log_content: str
    ):

        prompt = f"""
You are a DataOps incident classifier.

Classify the incident into ONE category only.

Available categories:

- DATA_MISSING
- RESOURCE
- CODE_BUG
- INFRA
- PERMISSION

Rules:

DATA_MISSING:
Missing partition, missing file, missing dataset, schema unavailable.

RESOURCE:
Executor lost, out of memory, YARN killed container, insufficient resources.

CODE_BUG:
Python exception, Spark code issue, KeyError, AttributeError, coding issue.

INFRA:
Network issue, timeout, metastore unavailable, service unavailable.

PERMISSION:
Access denied, permission denied, authorization failure.

Return ONLY the category name.

Log:

{log_content}
"""

        result = (
            LLMService()
            .generate(prompt)
            .strip()
        )

        return result