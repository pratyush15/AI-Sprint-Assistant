import streamlit as st
from utils import page_header

st.set_page_config(
    page_title="AI Sprint Assistant",
    page_icon="🤖",
    layout="wide"
)

page_header(
    "🤖 AI Sprint Assistant",
    "Local AI-powered Jira Dashboard"
)

st.markdown("---")

st.markdown(
    """
Welcome to the AI Sprint Assistant.

### Features

- 📋 Manage Tickets
- 🤖 Estimate Story Points
- ⚡ Prioritize Tickets
- ✅ Generate Acceptance Criteria
- 🧪 Generate Test Cases
- 📄 Generate Subtasks
- 🔍 Search Similar Tickets
- 📊 Sprint Summary

Use the left sidebar to navigate.
"""
)