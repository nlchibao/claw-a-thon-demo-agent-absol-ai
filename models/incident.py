from dataclasses import dataclass


@dataclass
class Incident:
    incident_id: str
    dag_id: str
    task_id: str
    status: str
    execution_date: str
    log_file: str