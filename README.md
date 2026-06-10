# 🛡️ Absol AI

**Predicting Data Disasters Before They Spread**

Absol AI is an AI-powered DataOps Incident Management Agent designed to help Analytics Engineers and Data Engineers automatically detect, analyze, prioritize, and respond to failed data pipelines.

Inspired by the Pokémon **Absol**, known for sensing disasters before they occur, Absol AI proactively investigates data incidents before they propagate downstream and impact business users.

---

# 🚀 Problem Statement

In modern data platforms, Analytics Engineers spend significant time every day:

* Monitoring Airflow DAG failures
* Reading lengthy logs
* Identifying root causes
* Assessing downstream impacts
* Discovering affected stakeholders
* Drafting notifications manually

This process is repetitive, time-consuming, and highly dependent on human expertise.

---

# 💡 Solution

Absol AI automates the incident investigation workflow.

Instead of manually reviewing failures, operators simply launch an investigation and the agent will:

1. Detect failed incidents
2. Analyze logs
3. Classify root causes
4. Evaluate business impact
5. Discover stakeholders
6. Generate Root Cause Analysis (RCA)
7. Draft stakeholder notifications
8. Produce executive summaries

---

# 🏗️ Architecture

```text
Incident Data
    │
    ▼
Log Parser
    │
    ▼
Classification Engine
    │
    ├── DATA_MISSING
    ├── RESOURCE
    ├── CODE_BUG
    ├── INFRA
    └── PERMISSION
    │
    ▼
Impact Analyzer
    │
    ▼
Stakeholder Discovery
    │
    ▼
LLM Layer (Qwen 3.5 27B)
    │
    ├── Executive Summary
    ├── Root Cause Analysis
    └── Notification Draft
    │
    ▼
Streamlit Dashboard
```

---

# 🤖 Agent Workflow

```text
Scan Incidents
    ↓
Parse Logs
    ↓
Classify Root Cause
    ↓
Evaluate Business Impact
    ↓
Discover Stakeholders
    ↓
Generate Notifications
    ↓
Produce Executive Summary
```

---

# 📊 Features

## Executive Summary

Absol AI automatically generates a daily executive summary for platform operators and management teams.

### Example

* Total incidents detected
* High severity incidents
* Business impact assessment
* Recommended actions

---

## Incident Prioritization

Incidents are automatically ranked based on:

* Severity
* Impact scope
* Number of affected downstream assets

The agent highlights the most critical incidents first.

---

## AI Root Cause Analysis

For each incident, Absol AI generates:

* Root cause analysis
* Business impact
* Investigation steps
* Recommended resolution

Powered by Qwen 3.5 27B.

---

## Stakeholder Discovery

The agent automatically identifies:

* Data owners
* Platform owners
* Impacted downstream consumers

using lineage metadata.

---

## Notification Draft Generation

Absol AI automatically drafts stakeholder notifications including:

* Incident description
* Impact summary
* Recommended actions
* Escalation information

---

# 📂 Project Structure

```text
agent/
│
├── data/
│   ├── incidents/
│   ├── logs/
│   ├── dags.yaml
│   ├── datasets.yaml
│   ├── lineage.yaml
│   ├── teams.yaml
│   └── playbooks.yaml
│
├── services/
│   ├── daily_incident_agent.py
│   ├── incident_loader.py
│   ├── classifier.py
│   ├── impact_analyzer.py
│   ├── metadata_service.py
│   ├── notification_service.py
│   ├── executive_summary_service.py
│   ├── rca_service.py
│   └── llm_service.py
│
├── ui/
│   └── app.py
│
└── README.md
```

---

# 🧠 AI Components

## LLM Provider

Qwen 3.5 27B

### Capabilities

* Executive Summary Generation
* Root Cause Analysis
* Stakeholder Communication Drafting

---

# 🎯 Demo Scenario

### Incident

```text
INC_001
```

### Category

```text
DATA_MISSING
```

### Dataset

```text
customer_feature
```

### Impact

```text
risk_score
fraud_alert
risk_dashboard
```

### Agent Output

```text
Root Cause Analysis

Business Impact

Recommended Actions

Stakeholder Notification Draft
```

---

# 📈 Business Impact

### Before Absol AI

* Manual log investigation
* Manual stakeholder discovery
* Manual notification drafting
* 30-60 minutes per day

### After Absol AI

* Automated incident analysis
* Automated impact assessment
* Automated stakeholder identification
* AI-generated communications

Estimated investigation time reduced to less than 5 minutes.

---

# 🔮 Future Enhancements

* Airflow API integration
* Real-time monitoring
* Slack integration
* Microsoft Teams integration
* Email delivery service
* Automated incident remediation
* Multi-agent collaboration

---

# 👥 Team

Gogo

Absol AI

"Predicting Data Disasters Before They Spread"
