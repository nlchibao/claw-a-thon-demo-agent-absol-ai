from services.incident_loader import IncidentLoader
from services.log_parser import LogParser
from services.classifier import Classifier

from services.metadata_service import MetadataService
from services.impact_analyzer import ImpactAnalyzer

from services.recommendation_engine import (
    RecommendationEngine
)

from services.severity_engine import (
    SeverityEngine
)


def run(incident_id):

    incident = IncidentLoader().load(
        incident_id
    )

    log_content = LogParser().parse(
        incident.log_file
    )

    category = Classifier().classify(
        log_content
    )

    metadata = MetadataService()

    dataset = metadata.get_dataset_from_dag(
        incident.dag_id
    )

    owner = metadata.get_owner_team(
        dataset
    )

    impacted_assets = (
        ImpactAnalyzer()
        .get_downstream_assets(dataset)
    )

    recommendations = (
        RecommendationEngine()
        .get_actions(category)
    )

    severity = (
        SeverityEngine()
        .calculate(
            category,
            impacted_assets
        )
    )

    print("=" * 50)

    print(
        f"Incident ID: {incident.incident_id}"
    )

    print(
        f"Category: {category}"
    )

    print(
        f"Severity: {severity}"
    )

    print(
        f"Dataset: {dataset}"
    )

    print(
        f"Owner Team: {owner}"
    )

    print(
        f"Affected Assets: {impacted_assets}"
    )

    print(
        f"Recommendations:"
    )

    for item in recommendations:
        print(f" - {item}")

    print("=" * 50)


if __name__ == "__main__":

    run("INC_001")