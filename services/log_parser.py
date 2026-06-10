from pathlib import Path


class LogParser:

    def parse(self, log_file: str):

        path = Path("data/logs") / log_file

        with open(path, "r") as f:
            content = f.read()

        return content