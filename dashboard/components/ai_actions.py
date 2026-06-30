
import streamlit as st

AI_TASKS = {
    "Estimate Story Points": "story_points",
    "Prioritize Ticket": "priority",
    "Generate Acceptance Criteria": "acceptance",
    "Generate Test Cases": "testcases",
    "Generate Subtasks": "subtasks",
    "Analyze Ticket Quality": "ticket_quality",
    "Rewrite Ticket": "rewrite_ticket",
    "Chat With Ticket": "ticket_chat",
}


def action_buttons():
    clicked_task = None
    st.subheader("AI Actions")

    for label, task in AI_TASKS.items():
        if st.button(
            label,
            use_container_width=True
        ):
            clicked_task = task

    return clicked_task