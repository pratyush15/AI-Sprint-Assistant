import streamlit as st


PRIORITY_COLORS = {
    "Low": "🟢",
    "Medium": "🟡",
    "High": "🟠",
    "Highest": "🔴",
}


STATUS_COLORS = {
    "To Do": "⚪",
    "In Progress": "🟡",
    "Done": "🟢",
}


def priority_badge(priority: str):
    color = PRIORITY_COLORS.get(priority, "⚪")
    
    return f"{color} {priority}"


def status_badge(status: str):
    color = STATUS_COLORS.get(status, "⚪")

    return f"{color} {status}"