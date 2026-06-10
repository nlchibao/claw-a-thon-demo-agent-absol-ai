class Classifier:

    def classify(self, log_content: str):

        text = log_content.lower()

        if (
            "path does not exist" in text
            or "filenotfoundexception" in text
        ):
            return "DATA_MISSING"

        if (
            "executorlostfailure" in text
            or "container killed by yarn" in text
        ):
            return "RESOURCE"

        if (
            "keyerror" in text
            or "attributeerror" in text
            or "traceback" in text
        ):
            return "CODE_BUG"

        if (
            "metastore unavailable" in text
            or "connection timeout" in text
        ):
            return "INFRA"

        if (
            "permission denied" in text
            or "access denied" in text
        ):
            return "PERMISSION"

        return None