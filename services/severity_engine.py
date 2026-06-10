class SeverityEngine:

    def calculate(
        self,
        category,
        impacted_assets
    ):

        score = 0

        if category == "DATA_MISSING":
            score += 40

        if len(impacted_assets) >= 3:
            score += 40

        if len(impacted_assets) >= 1:
            score += 20

        if score >= 80:
            return "HIGH"

        if score >= 50:
            return "MEDIUM"

        return "LOW"