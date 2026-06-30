import streamlit as st


def show_metrics(tickets):
    total = len(tickets)
    completed = len(
        [
            t for t in tickets
            if t["status"] == "Done"
        ]
    )

    in_progress = len(
        [
            t for t in tickets
            if t["status"] == "In Progress"
        ]
    )

    todo = len(
        [
            t for t in tickets
            if t["status"] == "To Do"
        ]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Tickets",
        total
    )

    c2.metric(
        "Completed",
        completed
    )

    c3.metric(
        "In Progress",
        in_progress
    )

    c4.metric(
        "To Do",
        todo
    )