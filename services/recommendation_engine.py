import yaml


class RecommendationEngine:

    def __init__(self):

        with open("data/playbooks.yaml") as f:
            self.playbooks = yaml.safe_load(f)

    def get_actions(self, category):

        return self.playbooks[category]["actions"]