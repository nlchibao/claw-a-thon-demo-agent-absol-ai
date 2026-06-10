from collections import Counter


class SummaryService:

    def summarize(
        self,
        incidents
    ):

        categories = Counter(
            [
                x["category"]
                for x in incidents
            ]
        )

        severities = Counter(
            [
                x["severity"]
                for x in incidents
            ]
        )

        return {

            "total_incidents":
                len(incidents),

            "categories":
                dict(categories),

            "severities":
                dict(severities)
        }