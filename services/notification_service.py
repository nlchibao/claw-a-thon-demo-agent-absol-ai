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

        email_body = f"""
To: {incident['owner']}@demo.com

Subject:
[{incident['severity']}] Data Pipeline Incident - {incident['dataset']}

Body:

Dear Team,

Absol AI has detected a {incident['category']} incident.

Incident ID:
{incident['incident_id']}

Affected Dataset:
{incident['dataset']}

Owner Team:
{incident['owner']}

Potentially Impacted Assets:
{impacted_assets}

Recommended Actions:
{recommendations}

Please investigate the issue as soon as possible.

Regards,
Absol AI
"""

        return email_body