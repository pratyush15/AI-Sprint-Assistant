import streamlit as st

from components.badges import (
    priority_badge,
    status_badge
)


def show_ticket(ticket):
    with st.container(border=True):
        col1, col2 = st.columns([5, 2])

        with col1:
            st.subheader(
                f"#{ticket['id']} - {ticket['title']}"
            )

            st.write(ticket["description"])
            st.caption(
                f"👤 {ticket['assignee']} | 🚀 {ticket['sprint']}"
            )

        with col2:
            st.write(
                priority_badge(ticket["priority"])
            )

            st.write(
                status_badge(ticket["status"])
            )

            st.write(
                f"⭐ {ticket['story_points']} SP"
            )