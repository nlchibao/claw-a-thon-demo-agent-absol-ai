import yaml


class ImpactAnalyzer:

    def __init__(self):

        with open("data/lineage.yaml") as f:
            self.lineage = yaml.safe_load(f)

    def get_downstream_assets(self, dataset):

        visited = set()

        def dfs(node):

            if node in visited:
                return

            visited.add(node)

            for child in self.lineage[node]["downstream"]:
                dfs(child)

        dfs(dataset)

        visited.remove(dataset)

        return sorted(list(visited))