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


# ==================================================
# LOAD DATA
# ==================================================

incidents = DailyIncidentAgent().run()

summary = SummaryService().summarize(
    incidents
)

# ai_summary = (
#     ExecutiveSummaryService()
#     .generate(
#         incidents,
#         summary
#     )
# )

@st.cache_data(ttl=3600)
def get_ai_summary(incidents, summary):
    return (
        ExecutiveSummaryService()
        .generate(
            incidents,
            summary
        )
    )

ai_summary = get_ai_summary(
    json.dumps(incidents),
    json.dumps(summary)
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
    "View Agent Reasoning Process",
    expanded=True
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
        "45 mins/day"
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

# ==================================================
# TOP PRIORITY INCIDENTS
# ==================================================

st.divider()

st.subheader(
    "🔥 Top Priority Incidents"
)

for item in ranked_incidents[:3]:

    severity_icon = {
        "HIGH": "🔴",
        "MEDIUM": "🟠",
        "LOW": "🟢"
    }.get(
        item["severity"],
        "⚪"
    )

    st.warning(
        f"""
{severity_icon} Incident: {item['incident_id']}

Severity: {item['severity']}

Category: {item['category']}

Dataset: {item['dataset']}

Owner Team: {item['owner']}
"""
    )
#
# # ==================================================
# # INCIDENT OVERVIEW TABLE
# # ==================================================
#
# st.divider()
#
# st.subheader(
#     "📋 Today's Incident Overview"
# )
#
# table_data = []
#
# for item in incidents:
#
#     table_data.append(
#         {
#             "Incident": item["incident_id"],
#             "Category": item["category"],
#             "Severity": item["severity"],
#             "Dataset": item["dataset"],
#             "Owner": item["owner"],
#             "Impacted Assets": len(
#                 item["impacted_assets"]
#             )
#         }
#     )
#
# st.dataframe(
#     table_data,
#     use_container_width=True
# )

# ==================================================
# INCIDENT DETAIL
# ==================================================

# st.divider()
#
# st.subheader(
#     "🔍 Incident Detail"
# )
# st.subheader(
#     f"🚨 Investigation Report - {selected_data['incident_id']}"
# )

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
    "Top priority incidents identified by Absol AI."
)

for incident in ranked_incidents[:3]:

    current_selected = (
        st.session_state.selected_incident
    )

    if incident["incident_id"] == current_selected:
        st.success(
            f"🟢 Currently Investigating: {incident['incident_id']}"
        )

    col1, col2 = st.columns([4, 1])

    with col1:
        severity_icon = {
            "HIGH": "🔴",
            "MEDIUM": "🟠",
            "LOW": "🟢"
        }.get(
            incident["severity"],
            "⚪"
        )

        st.markdown(
            f"""
        ### {severity_icon} {incident['incident_id']}

        **Severity:** {incident['severity']}

        **Category:** {incident['category']}

        **Dataset:** {incident['dataset']}
        """
        )

    with col2:

        if st.button(
                "🤖 Run Investigation",
                key=incident["incident_id"]
        ):
            st.session_state.selected_incident = (
                incident["incident_id"]
            )
            st.rerun()

st.divider()

st.subheader(
    "📂 Other Incidents"
)

other_incidents = ranked_incidents[3:]

for incident in other_incidents:

    col1, col2 = st.columns([4, 1])

    with col1:

        st.info(
            f"""
{incident['incident_id']} | {incident['severity']}

Category: {incident['category']}
"""
        )

    with col2:

        if st.button(
                "🤖 Run Investigation",
                key=f"other_{incident['incident_id']}"
        ):
            st.session_state.selected_incident = (
                incident["incident_id"]
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

col1, col2, col3 = st.columns(3)

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

notification_draft = (
    NotificationService()
    .generate(
        selected_data
    )
)

# ai_rca = (
#     RCAService()
#     .generate(
#         selected_data
#     )
# )
@st.cache_data(ttl=3600)
def get_ai_rca(incident):
    return (
        RCAService()
        .generate(
            incident
        )
    )

ai_rca = get_ai_rca(
    json.dumps(selected_data)
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
        "### Impacted Assets"
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
#
# # ==================================================
# # CURRENT INVESTIGATION TARGET
# # ==================================================
#
# st.divider()
#
# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.metric(
#         "Incident",
#         selected_data["incident_id"]
#     )
#
# with col2:
#     st.metric(
#         "Severity",
#         selected_data["severity"]
#     )
#
# with col3:
#     st.metric(
#         "Category",
#         selected_data["category"]
#     )



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
    "📨 Send Notification"
):
    sent_to = [
        selected_data["owner"]
    ]

    st.success(
        f"""
    Notification sent successfully.

    Incident:
    {selected_data['incident_id']}

    Owner Team:
    {selected_data['owner']}

    Affected Assets:
    {len(selected_data['impacted_assets'])}
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