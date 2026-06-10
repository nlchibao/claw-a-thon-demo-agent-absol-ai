# 🛡️ Absol AI

## Predicting Data Disasters Before They Spread

Absol AI is an AI-powered DataOps Incident Commander that automatically investigates failed data pipelines, identifies root causes, evaluates business impact through lineage analysis, discovers affected stakeholders, and prepares incident communications.

Inspired by the Pokémon **Absol**, known for sensing disasters before they happen, Absol AI helps Analytics Engineers, Data Engineers, and Platform Teams detect and respond to data incidents before they spread across the organization.

---

# 🚀 Problem Statement

Modern data platforms process hundreds of pipelines every day.

When a critical pipeline fails, engineers often spend significant time:

* Monitoring Airflow DAG failures
* Reading lengthy Spark logs
* Identifying root causes
* Assessing downstream impacts
* Discovering affected stakeholders
* Drafting stakeholder communications
* Escalating incidents manually

As data ecosystems become increasingly complex, incident investigation becomes slower, more expensive, and more dependent on specialized expertise.

---

# 💡 Solution

Absol AI automates the incident investigation workflow.

Instead of manually reviewing logs and tracing lineage graphs, operators simply launch an investigation and receive:

* Root cause classification
* Business impact assessment
* Downstream lineage analysis
* Stakeholder discovery
* AI-generated RCA
* Stakeholder notification drafts
* Executive incident summaries

---

# 🏗️ System Architecture

```text
Incident Detection
        │
        ▼
Rule-Based Classification
        │
        ▼
Unknown Incident?
        │
 ┌──────┴──────┐
 │             │
 No           Yes
 │             │
 ▼             ▼
Rule       AI Classifier
Engine     (LLM)
 │             │
 └──────┬──────┘
        ▼
Impact Analysis
        ▼
Lineage Traversal
        ▼
Stakeholder Discovery
        ▼
AI Root Cause Analysis
        ▼
Notification Generation
        ▼
Executive Summary
        ▼
Streamlit Dashboard
```

---

# 🤖 Key Features

## 1. Hybrid Incident Classification

Absol AI uses a hybrid classification architecture.

### Rule Engine

Known failures are classified deterministically:

* DATA_MISSING
* RESOURCE
* CODE_BUG
* INFRA
* PERMISSION

### AI Classifier

When no known failure pattern is detected, incidents are escalated to an LLM for semantic classification.

Examples:

* Unable to infer schema
* Partition not found
* Authentication failures
* Socket timeouts
* Out-of-memory errors
* Stage failures

---

## 2. Impact Assessment

Absol AI automatically determines:

* Affected datasets
* Downstream assets
* Business impact scope

using dataset lineage metadata.

Example:

```text
customer_feature
    ↓
risk_score
    ↓
fraud_alert
    ↓
fraud_dashboard
```

---

## 3. Stakeholder Discovery

Absol AI identifies:

### Incident Owners

Responsible teams maintaining affected datasets.

### Downstream Consumers

Business users and operational teams consuming impacted outputs.

Example:

```text
Owner:
risk_data@demo.com

Consumers:
fraud_ops@demo.com
business_team@demo.com
```

---

## 4. AI Root Cause Analysis

For every incident, Absol AI generates:

* Root cause analysis
* Business impact summary
* Investigation rationale
* Recommended next actions

using a Large Language Model.

---

## 5. Notification Draft Generation

Absol AI automatically prepares stakeholder communications.

Generated notifications include:

* Incident details
* Severity
* Impact assessment
* Affected stakeholders
* Recommended actions

---

## 6. Executive Summary

At the beginning of each day, Absol AI produces:

* Incident statistics
* High-priority failures
* Impact overview
* Recommended operational focus

for managers and platform leads.

---

# 📊 Demo Data Platform

The demo environment simulates a fintech data platform containing:

### Raw Datasets

* raw_customer
* raw_transaction
* raw_merchant

### Feature Datasets

* customer_feature
* transaction_feature
* merchant_feature
* device_feature
* kyc_feature

### Scoring Datasets

* risk_score
* merchant_risk_score
* transaction_anomaly_score
* merchant_health_score

### Business Outputs

* risk_dashboard
* fraud_dashboard
* executive_dashboard
* merchant_dashboard
* operation_dashboard
* compliance_report

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
│   ├── stakeholders.yaml
│   ├── teams.yaml
│   └── playbooks.yaml
│
├── services/
│   ├── incident_service.py
│   ├── daily_incident_agent.py
│   ├── classifier.py
│   ├── ai_classifier.py
│   ├── impact_analyzer.py
│   ├── stakeholder_service.py
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

## AI Classifier

Used for semantic incident classification when rule-based matching fails.

## AI RCA Generator

Produces detailed root cause analyses.

## AI Executive Summary Generator

Produces executive-level incident summaries.

## AI Notification Generator

Creates stakeholder communication drafts.

---

# 🎯 Example Incident Investigation

### Incident

```text
INC_016
```

### Log Snippet

```text
java.net.SocketTimeoutException:
Read timed out
```

### Classification

```text
INFRA
```

### Classification Source

```text
AI_CLASSIFIER
```

### Impact

```text
fraud_alert
fraud_dashboard
compliance_report
```

### Stakeholders

```text
fraud_team@demo.com
fraud_ops@demo.com
compliance_team@demo.com
```

### Output

* AI RCA
* Recommended Actions
* Notification Draft

---

# 📈 Business Value

Before Absol AI:

* Manual log investigation
* Manual lineage analysis
* Manual stakeholder discovery
* Manual communication drafting

After Absol AI:

* Automated incident triage
* Automated impact assessment
* Automated stakeholder identification
* AI-assisted communications

Estimated investigation effort can be reduced significantly depending on incident volume and severity.

---

# 🔮 Future Enhancements

* Airflow API Integration
* Slack Integration
* Microsoft Teams Integration
* Email Delivery Service
* Real-Time Monitoring
* Automated Remediation
* Multi-Agent Collaboration
* Data Quality Monitoring
* Incident Trend Analysis

---

# 👥 Team

Claw-A-Thon 2026

## Absol AI

**Predicting Data Disasters Before They Spread**

Inspired by Absol's ability to sense disasters before they happen, Absol AI helps organizations detect, understand, and respond to data incidents before they impact business operations.
