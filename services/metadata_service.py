import yaml


class MetadataService:

    def __init__(self):

        with open("data/dags.yaml") as f:
            self.dags = yaml.safe_load(f)

        with open("data/datasets.yaml") as f:
            self.datasets = yaml.safe_load(f)

        with open("data/teams.yaml") as f:
            self.teams = yaml.safe_load(f)

    def get_dataset_from_dag(self, dag_id):

        return self.dags[dag_id]["output_dataset"]

    def get_owner_team(self, dataset):

        return self.datasets[dataset]["owner_team"]

    def get_team_email(self, team):

        return self.teams[team]["emails"]