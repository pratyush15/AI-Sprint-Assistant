import streamlit as st
import pandas as pd


def status_chart(tickets):
    df = pd.DataFrame(tickets)
    counts = df["status"].value_counts()
    st.subheader(
        "Ticket Status"
    )

    st.bar_chart(counts)


def story_point_chart(tickets):
    df = pd.DataFrame(tickets)
    grouped = (
        df.groupby("story_points")
        .size()
    )

    st.subheader(
        "Story Points"
    )

    st.bar_chart(grouped)
    
    
def priority_chart(tickets):
    df = pd.DataFrame(tickets)

    counts = (
        df["priority"]
        .value_counts()
    )

    st.subheader(
        "Priority Distribution"
    )

    st.bar_chart(counts)