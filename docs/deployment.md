# Absol AI Deployment Summary

## Runtime Information

Runtime ID:

```text
runtime-1813f7e5-7706-4a3a-a844-098e8a2f1dc5
```

Runtime Name:

```text
absol-ai
```

Runtime Status:

```text
ACTIVE
```

Runtime Flavor:

```text
runtime-s2-general-2x4
```

---

## Endpoint Information

Endpoint ID:

```text
endpoint-f85fa844-b7e2-4b62-8674-4d1c89caae93
```

Endpoint Name:

```text
DEFAULT
```

Endpoint Status:

```text
ACTIVE
```

Endpoint URL:

```text
https://endpoint-f85fa844-b7e2-4b62-8674-4d1c89caae93.agentbase-runtime.aiplatform.vngcloud.vn
```

---

## Container Registry Information

Registry URL:

```text
vcr.vngcloud.vn
```

Repository:

```text
111480-abp111962
```

Image:

```text
vcr.vngcloud.vn/111480-abp111962/absol-ai:v1
```

---

## Application Environment Variables

Required variables:

```env
AI_PLATFORM_API_KEY=
AI_PLATFORM_BASE_URL=https://maas-llm-aiplatform-hcm.api.vngcloud.vn/v1
MODEL_NAME=qwen/qwen3-5-27b
```

Notes:

* Do not commit `.env`
* Commit `.env.example` only
* Runtime deployment uses `--env-file .env`

---

## Deployment Commands

### Build Image

```bash
docker build -t absol-ai .
```

### Tag Image

```bash
docker tag absol-ai \
vcr.vngcloud.vn/111480-abp111962/absol-ai:v1
```

### Push Image

```bash
docker push \
vcr.vngcloud.vn/111480-abp111962/absol-ai:v1
```

### Create Runtime

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

## Useful Operations

### List Runtimes

```bash
bash .claude/skills/agentbase/scripts/runtime.sh list
```

### Get Runtime

```bash
bash .claude/skills/agentbase/scripts/runtime.sh get runtime-1813f7e5-7706-4a3a-a844-098e8a2f1dc5
```

### Runtime Logs

```bash
bash .claude/skills/agentbase/scripts/runtime.sh logs runtime-1813f7e5-7706-4a3a-a844-098e8a2f1dc5
```

### List Endpoints

```bash
bash .claude/skills/agentbase/scripts/runtime.sh endpoints list runtime-1813f7e5-7706-4a3a-a844-098e8a2f1dc5
```

### Endpoint Logs

```bash
bash .claude/skills/agentbase/scripts/runtime.sh endpoints logs \
runtime-1813f7e5-7706-4a3a-a844-098e8a2f1dc5 \
endpoint-f85fa844-b7e2-4b62-8674-4d1c89caae93
```

---

## Deployment Notes

This project has been successfully deployed to GreenNode AgentBase Runtime.

Verified components:

* AgentBase Container Registry
* AgentBase Runtime
* Managed Endpoint
* Environment Variable Injection
* Runtime Health Check
* Streamlit Dashboard
* AI Executive Summary
* AI Root Cause Analysis
* Incident Prioritization
* Stakeholder Notification Generation

Deployment verified on:

```text
2026-06-11
```
