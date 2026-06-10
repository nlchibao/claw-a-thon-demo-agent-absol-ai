import yaml


class StakeholderService:

    def __init__(self):

        with open(
            "data/stakeholders.yaml",
            "r"
        ) as f:

            self.data = yaml.safe_load(f)

    def get_impacted_consumers(
        self,
        impacted_assets
    ):

        consumers = []

        for asset in impacted_assets:

            asset_info = (
                self.data.get(
                    asset,
                    {}
                )
            )

            consumers.extend(
                asset_info.get(
                    "consumers",
                    []
                )
            )

        return sorted(
            list(
                set(consumers)
            )
        )