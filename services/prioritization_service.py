class PrioritizationService:

    def rank(self, incidents):

        severity_score = {
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1
        }

        ranked = sorted(
            incidents,
            key=lambda x: (
                severity_score.get(
                    x["severity"],
                    0
                ),
                len(
                    x["impacted_assets"]
                )
            ),
            reverse=True
        )

        return ranked