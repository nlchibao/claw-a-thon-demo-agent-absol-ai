# 🛡️ ABSOL AI

## Predicting Data Disasters Before They Spread

Absol AI is an AI-powered Data Incident Investigation Agent designed to help data teams quickly understand, prioritize, and respond to data incidents before they impact business operations.

Inspired by Absol's ability to sense disasters before they occur, Absol AI automatically investigates failed data pipelines, identifies root causes, evaluates downstream business impact, discovers affected stakeholders, and generates actionable remediation recommendations.

The current prototype demonstrates a complete incident investigation workflow using simulated incident, log, and lineage data. In production environments, Absol AI can integrate with Apache Airflow for pipeline failure monitoring, DataHub for lineage analysis, and Outlook for automated stakeholder communication.

By combining AI-powered reasoning with data observability concepts, Absol AI helps organizations reduce investigation time, improve operational visibility, and minimize business risks caused by data failures.

---

# Problem Statement

Modern data platforms rely on hundreds of daily pipelines, datasets, dashboards, and machine learning features.

When a pipeline fails, engineers often spend significant time:

* Reading Spark and Airflow logs
* Identifying root causes manually
* Assessing downstream impact
* Finding affected stakeholders
* Communicating incidents
* Recommending mitigation plans

As organizations scale, this process becomes increasingly difficult and expensive.

Absol AI automates the entire workflow.

---

# Solution Overview

Absol AI continuously analyzes failed data pipelines and automatically:

1. Identifies root causes
2. Classifies incident categories
3. Evaluates business impact
4. Discovers affected stakeholders
5. Generates remediation recommendations
6. Produces AI-powered executive summaries
7. Drafts stakeholder notifications

All results are presented through an interactive dashboard.

---

# How Absol AI Works

## Production Architecture

```text
Airflow Logs
        \
         \
          > ABSOL AI
         /
DataHub Lineage

        ↓

Incident Prioritization

Root Cause Analysis

Impact Assessment

Stakeholder Discovery

Notification Generation

        ↓

Outlook Email
```

## Current Demo Architecture

```text
Simulated Incident Files
Simulated Log Files
Simulated Lineage Files

        ↓

      ABSOL AI

        ↓

Streamlit Dashboard
```

This prototype uses simulated datasets to demonstrate the complete workflow while maintaining a production-ready architecture for future integrations.

---

# Key Features

## 🤖 Automated Incident Investigation

Absol AI automatically processes incident metadata and logs to produce investigation reports.

Extracted information includes:

* Incident ID
* Failed DAG
* Dataset Owner
* Failure Category
* Severity Level
* Impacted Downstream Assets

---

## 🧠 Hybrid Classification Engine

### Rule-Based Classification

Known patterns are classified immediately:

* DATA_MISSING
* RESOURCE
* CODE_BUG
* INFRA
* PERMISSION

### AI Classification Fallback

When no rule matches a failure pattern, Absol AI automatically invokes an LLM-based classifier.

Benefits:

* Handles unseen failures
* Adapts to new incidents
* Reduces manual intervention

---

## 🔍 AI Root Cause Analysis

Absol AI generates detailed explanations describing:

* Why the failure occurred
* Potential downstream impact
* Suggested mitigation steps

This allows engineers to investigate incidents significantly faster.

---

## 📊 Impact Assessment

Absol AI evaluates:

### Impacted Assets

Examples:

* customer_feature
* risk_score
* fraud_alert
* risk_dashboard
* fraud_dashboard

### Impacted Stakeholders

Examples:

* Customer Platform Team
* Risk Team
* Fraud Analytics Team
* Finance BI Team

---

## 🛠 Recommendation Engine

Category-specific remediation playbooks are automatically generated.

### DATA_MISSING

* Check upstream ingestion DAG
* Verify source path
* Contact source owner

### RESOURCE

* Retry DAG
* Check cluster utilization
* Increase executor memory

---

## 📧 Notification Draft Generation

Absol AI automatically generates stakeholder communication drafts including:

* Owner team
* Impacted consumers
* Severity
* Impacted assets
* Recommended actions

---

## 📈 AI Executive Summary

Management-friendly summaries provide:

* Daily incident overview
* Severity distribution
* Operational risk assessment
* Recommended priorities

---

# Architecture

```text
Failed Pipeline
       |
       v
Incident Loader
       |
       v
Log Parser
       |
       v
Rule-Based Classifier
       |
       +------------------+
       |                  |
       | No Match         |
       v                  |
AI Classifier             |
       |                  |
       +------------------+
               |
               v
Impact Analyzer
               |
               v
Stakeholder Discovery
               |
               v
Recommendation Engine
               |
               v
Severity Engine
               |
               v
AI RCA Generator
               |
               v
Notification Generator
               |
               v
Streamlit Dashboard
```

---

# Project Structure

```text
project/
│
├── agents/
│   └── absol_agent.py
│
├── data/
│   ├── incidents/
│   ├── logs/
│   ├── dags.yaml
│   ├── datasets.yaml
│   ├── lineage.yaml
│   ├── stakeholders.yaml
│   └── playbooks.yaml
│
├── services/
│   ├── ai_classifier.py
│   ├── classifier.py
│   ├── executive_summary_service.py
│   ├── impact_analyzer.py
│   ├── incident_service.py
│   ├── notification_service.py
│   ├── prioritization_service.py
│   ├── recommendation_engine.py
│   ├── rca_service.py
│   ├── severity_engine.py
│   └── summary_service.py
│
├── ui/
│   └── app.py
│
├── assets/
│   └── absol_logo.png
│
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
```

---

# Dashboard Components

## KPI Overview

Displays:

* Total Incidents
* High Severity Incidents
* Medium Severity Incidents
* Estimated Time Saved

---

## AI Executive Summary

Provides a management-level overview of the incident landscape.

---

## Incident Investigation Center

Displays:

* Prioritized incidents
* Severity levels
* Failure categories
* Investigation controls

---

## Investigation Report

Displays:

* Severity
* Category
* Dataset
* Owner Team
* Classification Source
* Impact Assessment

---

## AI Root Cause Analysis

Generates an AI-powered explanation of the incident.

---

## Stakeholder Notification Draft

Automatically drafts communications for affected teams.

---

# Sample Incident Categories

| Category     | Example                   |
| ------------ | ------------------------- |
| DATA_MISSING | Missing HDFS Path         |
| RESOURCE     | Executor Lost             |
| CODE_BUG     | KeyError / AttributeError |
| INFRA        | Hive Metastore Failure    |
| PERMISSION   | Access Denied             |
| UNKNOWN      | Classified by AI          |

---

# Technology Stack

* Python 3.9
* Streamlit
* Docker
* YAML Metadata Store
* VNG AI Platform MaaS
* Qwen 3.5 27B
* AgentBase Runtime
* AgentBase Container Registry

---

# Environment Variables

Create a `.env` file:

```env
AI_PLATFORM_API_KEY=
AI_PLATFORM_BASE_URL=https://maas-llm-aiplatform-hcm.api.vngcloud.vn/v1
MODEL_NAME=qwen/qwen3-5-27b
```

Do not commit the actual `.env` file.

---

# Local Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run dashboard:

```bash
streamlit run ui/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

# Docker Deployment

Build image:

```bash
docker build -t absol-ai .
```

Run locally:

```bash
docker run -p 8080:8080 absol-ai
```

---

# AgentBase Deployment

## Prerequisites

```bash
export GREENNODE_CLIENT_ID=<your-client-id>
export GREENNODE_CLIENT_SECRET=<your-client-secret>
```

Update application environment:

```bash
cp .env.example .env
```

Update `.env` with AI Platform credentials.

---

## Build Docker Image

```bash
docker build -t absol-ai .
```

---

## Login to AgentBase Container Registry

```bash
bash .claude/skills/agentbase/scripts/cr.sh credentials docker-login
```

---

## Discover Container Registry Information

```bash
bash .claude/skills/agentbase/scripts/cr.sh repo get
```

Expected:

```json
{
  "name": "111480-abp111962",
  "registryUrl": "vcr.vngcloud.vn"
}
```

---

## Tag Image

```bash
docker tag absol-ai \
vcr.vngcloud.vn/111480-abp111962/absol-ai:v1
```

---

## Push Image

```bash
docker push \
vcr.vngcloud.vn/111480-abp111962/absol-ai:v1
```

---

## Create Runtime

```bash
bash .claude/skills/agentbase/scripts/runtime.sh create \
  --name absol-ai \
  --image vcr.vngcloud.vn/111480-abp111962/absol-ai:v1 \
  --flavor runtime-s2-general-2x4 \
  --env-file .env \
  --min-replicas 1 \
  --max-replicas 1 \
  --from-cr
```

---

## Update Existing Runtime

```bash
bash .claude/skills/agentbase/scripts/runtime.sh update \
runtime-1813f7e5-7706-4a3a-a844-098e8a2f1dc5 \
--image vcr.vngcloud.vn/111480-abp111962/absol-ai:v1 \
--flavor runtime-s2-general-2x4 \
--env-file .env \
--from-cr
```

---

# AgentBase Deployment Information

Runtime ID:

```text
runtime-1813f7e5-7706-4a3a-a844-098e8a2f1dc5
```

Endpoint URL:

```text
https://endpoint-f85fa844-b7e2-4b62-8674-4d1c89caae93.agentbase-runtime.aiplatform.vngcloud.vn
```

---

# Business Value

Absol AI helps organizations:

* Reduce incident investigation time
* Improve MTTR (Mean Time To Resolution)
* Improve stakeholder communication
* Increase operational visibility
* Prevent downstream data quality issues

---

# Future Enhancements

* Apache Airflow Integration
* DataHub Lineage Integration
* Outlook Email Delivery
* Slack Notifications
* Microsoft Teams Notifications
* Auto-Remediation Workflows
* Multi-Agent Collaboration

---

# Deployment Status

✅ Dockerized

✅ AgentBase Runtime

✅ AgentBase Container Registry

✅ Managed Endpoint

✅ AI-Powered Incident Investigation

---

# Team Vision

Absol AI aims to transform data incident investigation from a manual, reactive process into an AI-assisted workflow that helps organizations identify issues faster, understand business impact more clearly, and communicate effectively with stakeholders.

Absol AI — Predicting Data Disasters Before They Spread.
