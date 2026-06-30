import streamlit as st
from utils import page_header
from api_client import (
    get_sprint_summary
)

page_header(
    "📄 Sprint Summary",
    "AI-generated Sprint Analysis"
)

st.write(
    """
Generate an AI summary of the current sprint.

The AI analyzes all available tickets and provides:

- Sprint Health
- Progress
- Risks
- Blockers
- Recommendations
"""
)

if st.button(
    "Generate Sprint Summary",
    use_container_width=True
):

    with st.spinner(
        "Analyzing Sprint..."
    ):

        summary = get_sprint_summary()

        st.success(
            "Summary Generated"
        )

        st.markdown(summary)