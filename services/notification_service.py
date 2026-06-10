class NotificationService:

    def generate(self, incident):

        impacted_assets = "\n".join(
            [
                f"- {asset}"
                for asset in incident[
                    "impacted_assets"
                ]
            ]
        )

        recommendations = "\n".join(
            [
                f"- {action}"
                for action in incident[
                    "recommendations"
                ]
            ]
        )

        impacted_consumers = "\n".join(
            [
                f"- {consumer}"
                for consumer in incident.get(
                    "impacted_consumers",
                    []
                )
            ]
        )

        if not impacted_consumers:

            impacted_consumers = (
                "- No impacted consumers identified"
            )

        email_body = f"""
To:
{incident['owner']}@demo.com

CC:
{chr(10).join(
    incident.get(
        "impacted_consumers",
        []
    )
)}

Subject:
[{incident['severity']}] Data Pipeline Incident - {incident['dataset']}

Body:

Dear Team,

Absol AI has detected a data incident and completed an initial investigation.

==================================================

Incident ID:
{incident['incident_id']}

Category:
{incident['category']}

Severity:
{incident['severity']}

Affected Dataset:
{incident['dataset']}

Owner Team:
{incident['owner']}

==================================================

Potentially Impacted Assets:

{impacted_assets}

==================================================

Impacted Stakeholders:

{impacted_consumers}

==================================================

Recommended Actions:

{recommendations}

==================================================

Please note that downstream reports and analytics
may contain incomplete or inaccurate data until
the incident has been resolved.

Absol AI recommends prioritizing investigation
and notifying affected consumers.

Regards,

Absol AI
Predicting Data Disasters Before They Spread
"""

        return email_body