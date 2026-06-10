from services.incident_loader import IncidentLoader
from services.log_parser import LogParser
from services.classifier import Classifier
from services.metadata_service import MetadataService
from services.impact_analyzer import ImpactAnalyzer
from services.recommendation_engine import RecommendationEngine
from services.severity_engine import SeverityEngine


class IncidentService:

    def analyze(self, incident_id):

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

        return {
            "incident_id": incident.incident_id,
            "dag_id": incident.dag_id,
            "dataset": dataset,
            "owner": owner,
            "category": category,
            "severity": severity,
            "impacted_assets": impacted_assets,
            "recommendations": recommendations,
            "log_content": log_content,
        }