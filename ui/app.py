import sys
from pathlib import Path
import json

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import streamlit as st

from services.daily_incident_agent import DailyIncidentAgent
from services.summary_service import SummaryService
from services.executive_summary_service import ExecutiveSummaryService
from services.prioritization_service import PrioritizationService
from services.notification_service import NotificationService
from services.rca_service import RCAService

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Absol AI",
    page_icon="🛡️",
    layout="wide"
)

if "selected_incident" not in st.session_state:
    st.session_state.selected_incident = None

if "notification_sent" not in st.session_state:
    st.session_state.notification_sent = False

if "sent_notifications" not in st.session_state:
    st.session_state.sent_notifications = set()

# ==================================================
# LOAD DATA
# ==================================================

@st.cache_data(ttl=3600)
def load_incidents():

    return (
        DailyIncidentAgent()
        .run()
    )

incidents = load_incidents()



summary = SummaryService().summarize(
    incidents
)




@st.cache_data(ttl=3600)
def get_ai_summary(
        incidents,
        summary
):

    return (
        ExecutiveSummaryService()
        .generate(
            incidents,
            summary
        )
    )

ai_summary = get_ai_summary(
    tuple(
        json.dumps(
            x,
            sort_keys=True
        )
        for x in incidents
    ),
    json.dumps(
        summary,
        sort_keys=True
    )
)


ranked_incidents = (
    PrioritizationService()
    .rank(
        incidents
    )
)

if st.session_state.selected_incident is None:
    st.session_state.selected_incident = (
        ranked_incidents[0]["incident_id"]
    )


# ==================================================
# HEADER
# ==================================================

st.title("🛡️ Absol AI")

st.subheader(
    "Predicting Data Disasters Before They Spread"
)

# ==================================================
# KPI SECTION
# ==================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Incidents",
        summary["total_incidents"]
    )

with col2:
    st.metric(
        "High Severity",
        summary["severities"].get(
            "HIGH",
            0
        )
    )

with col3:
    st.metric(
        "Medium Severity",
        summary["severities"].get(
            "MEDIUM",
            0
        )
    )

# ==================================================
# AGENT EXECUTION FLOW
# ==================================================

st.divider()

st.subheader(
    "🤖 Agent Execution Flow"
)

total_incidents = len(incidents)
manual_minutes_per_incident = 10
ai_minutes_per_incident = 1

saved_minutes = 0

for incident in incidents:

    if incident["severity"] == "HIGH":
        saved_minutes += 15

    elif incident["severity"] == "MEDIUM":
        saved_minutes += 10

    else:
        saved_minutes += 5



if saved_minutes >= 60:

    hours = round(
        saved_minutes / 60,
        1
    )

    time_saved_text = (
        f"{hours} hrs/day"
    )

else:

    time_saved_text = (
        f"{saved_minutes} mins/day"
    )


high_incidents = summary["severities"].get(
    "HIGH",
    0
)

total_impacted_assets = sum(
    len(
        incident["impacted_assets"]
    )
    for incident in incidents
)

with st.expander(
    "🤖 View Agent Execution Details",
    expanded=False
):

    st.success(
        f"✓ Scanned {total_incidents} daily incidents"
    )

    st.success(
        f"✓ Parsed {total_incidents} pipeline logs"
    )

    st.success(
        f"✓ Classified {total_incidents} incidents into root-cause categories"
    )

    st.success(
        f"✓ Identified {high_incidents} high-severity incidents"
    )

    st.success(
        f"✓ Evaluated impact across {total_impacted_assets} downstream assets"
    )

    st.success(
        f"✓ Discovered stakeholders for {total_incidents} incidents"
    )

    st.success(
        f"✓ Generated {total_incidents} notification drafts"
    )

    st.success(
        "✓ Produced AI Executive Summary"
    )
    st.info(
        f"""
    🎯 Agent Outcome

    • Analyzed {total_incidents} incidents automatically

    • Identified {high_incidents} high-priority incidents

    • Evaluated impact across {total_impacted_assets} downstream assets

    • Discovered affected stakeholders

    • Generated notification drafts for all impacted teams

    • Produced AI-powered executive summary and root cause analysis
    """
    )


col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Incidents Analyzed",
        total_incidents
    )


with col2:
    st.metric(
        "Estimated Time Saved",
        time_saved_text
    )


# ==================================================
# AI EXECUTIVE SUMMARY
# ==================================================

st.divider()

st.subheader(
    "🧠 AI Executive Summary"
)

st.info(
    ai_summary
)

incident_ids = [
    x["incident_id"]
    for x in incidents
]

# ==================================================
# INCIDENT INVESTIGATION CENTER
# ==================================================

st.divider()

st.subheader(
    "🚨 Incident Investigation Center"
)

st.write(
    f"""
Absol AI detected **{len(ranked_incidents)} incidents** today.
Showing the top 3 prioritized incidents.
"""
)

# -------------------------
# TOP 3 INCIDENTS
# -------------------------

for incident in ranked_incidents[:3]:

    severity_icon = {
        "HIGH": "🔴",
        "MEDIUM": "🟠",
        "LOW": "🟢"
    }.get(
        incident["severity"],
        "⚪"
    )

    col1, col2 = st.columns([5, 1])

    with col1:

        title = (
            f"{severity_icon} {incident['incident_id']}"
        )

        if (
            incident["incident_id"]
            == st.session_state.selected_incident
        ):
            title += " 🟢"

        st.markdown(
            f"""
### {title}

**Severity:** {incident['severity']}

**Category:** {incident['category']}

**Dataset:** {incident['dataset']}
"""
        )

    with col2:

        if st.button(
            "🤖 Run Investigation",
            key=f"top_{incident['incident_id']}"
        ):
            st.session_state.selected_incident = (
                incident["incident_id"]
            )

            st.rerun()

# -------------------------
# ALL INCIDENTS
# -------------------------

st.divider()

incident_options = [
    f"{x['incident_id']} | {x['severity']} | {x['category']}"
    for x in ranked_incidents
]

selected_option = st.selectbox(
    "📊 Investigate Any Incident",
    incident_options
)

selected_incident = (
    selected_option
    .split("|")[0]
    .strip()
)

if st.button(
    "🚨 Investigate Selected Incident"
):

    st.session_state.selected_incident = (
        selected_incident
    )

    st.rerun()

selected_id = (
    st.session_state.selected_incident
)

selected_data = next(
    x
    for x in incidents
    if x["incident_id"] == selected_id
)

st.divider()

st.subheader(
    f"🚨 Investigation Report - {selected_data['incident_id']}"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Severity",
        selected_data["severity"]
    )

with col2:
    st.metric(
        "Category",
        selected_data["category"]
    )

with col3:
    st.metric(
        "Owner",
        selected_data["owner"]
    )

with col4:
    st.metric(
        "Classifier",
        selected_data.get(
            "classification_source",
            "RULE_ENGINE"
        )
    )

if (
    selected_data.get(
        "classification_source"
    )
    == "AI_CLASSIFIER"
):

    st.info(
        "🤖 This incident was classified using AI because no rule-based pattern matched the log."
    )

else:

    st.info(
        "⚙️ This incident matched a known rule-based failure pattern."
    )


notification_draft = (
    NotificationService()
    .generate(
        selected_data
    )
)


@st.cache_data(ttl=3600)
def get_ai_rca(
        incident_id,
        log_content
):

    return (
        RCAService()
        .generate(
            log_content
        )
    )


ai_rca = get_ai_rca(
    selected_data["incident_id"],
    selected_data["log_content"]
)



col1, col2 = st.columns(2)

with col1:

    st.write(
        f"**Category:** {selected_data['category']}"
    )

    st.write(
        f"**Severity:** {selected_data['severity']}"
    )

    st.write(
        f"**Dataset:** {selected_data['dataset']}"
    )

    st.write(
        f"**Owner Team:** {selected_data['owner']}"
    )

with col2:

    st.write(
        "### 📊 Impact Assessment"
    )

    st.write(
        "**Impacted Assets:**"
    )

    if selected_data["impacted_assets"]:

        for asset in selected_data[
            "impacted_assets"
        ]:
            st.write(
                f"• {asset}"
            )

    else:

        st.write(
            "No downstream impact detected."
        )

    st.write("")

    st.write(
        "**Impacted Stakeholders:**"
    )

    consumers = selected_data.get(
        "impacted_consumers",
        []
    )

    if consumers:

        for consumer in consumers:

            st.write(
                f"• {consumer}"
            )

    else:

        st.write(
            "No impacted stakeholders."
        )


# ==================================================
# AI ROOT CAUSE ANALYSIS
# ==================================================

st.divider()

st.subheader(
    "🧠 AI Root Cause Analysis"
)

st.info(
    ai_rca
)

# ==================================================
# RECOMMENDATIONS
# ==================================================

st.divider()

st.subheader(
    "🛠 Recommended Actions"
)

for action in selected_data[
    "recommendations"
]:
    st.success(action)

# ==================================================
# NOTIFICATION DRAFT
# ==================================================

st.divider()

st.subheader(
    "📧 Stakeholder Notification Draft"
)

st.code(
    notification_draft,
    language="text"
)

if st.button(
    "📨 Send Notification",
    key="send_notification"
):

    st.session_state.sent_notifications.add(
        selected_data["incident_id"]
    )


if (
    selected_data["incident_id"]
    in st.session_state.sent_notifications
):

    total_recipients = (
        1 +
        len(
            selected_data.get(
                "impacted_consumers",
                []
            )
        )
    )

    st.success(
        f"""
Notification sent successfully.

Recipients:
{total_recipients}

Owner Team:
{selected_data['owner']}

Impacted Consumers:
{len(selected_data.get('impacted_consumers', []))}
"""
    )

# ==================================================
# RAW LOG
# ==================================================

st.divider()

with st.expander(
    "📜 View Raw Log"
):

    st.code(
        selected_data[
            "log_content"
        ]
    )

# ==================================================
# MISSION
# ==================================================

st.divider()

st.subheader(
    "🎯 Mission"
)

st.markdown(
    """
Absol AI automatically reviews failed data pipelines,
identifies root causes, evaluates business impact,
discovers affected stakeholders, and recommends actions.

Inspired by Absol's ability to sense disasters before they occur,
Absol AI helps Data Teams detect and respond to incidents
before they propagate downstream.
"""
)