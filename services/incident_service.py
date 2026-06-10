from services.incident_loader import IncidentLoader
from services.log_parser import LogParser
from services.classifier import Classifier
from services.metadata_service import MetadataService
from services.impact_analyzer import ImpactAnalyzer
from services.recommendation_engine import RecommendationEngine
from services.severity_engine import SeverityEngine
from services.ai_classifier import (
    AIClassifier
)
from services.stakeholder_service import (
    StakeholderService
)


class IncidentService:

    def analyze(self, incident_id):

        incident = IncidentLoader().load(
            incident_id
        )

        log_content = LogParser().parse(
            incident.log_file
        )

        # category = Classifier().classify(
        #     log_content
        # )
        rule_category = (
            Classifier()
            .classify(
                log_content
            )
        )

        classification_source = "RULE_ENGINE"

        if rule_category is None:

            category = (
                AIClassifier()
                .classify(
                    log_content
                )
            )

            classification_source = (
                "AI_CLASSIFIER"
            )

        else:

            category = rule_category

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

        impacted_consumers = (
            StakeholderService()
            .get_impacted_consumers(
                impacted_assets
            )
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
            "classification_source": (
                classification_source
            ),
            "severity": severity,
            "impacted_assets": impacted_assets,
            "impacted_consumers":
                impacted_consumers,
            "recommendations": recommendations,
            "log_content": log_content,
        }