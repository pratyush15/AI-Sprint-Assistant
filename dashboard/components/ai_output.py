
import streamlit as st


def show_output(result):
    st.subheader("AI Response")

    if not result:
        st.info("Select a ticket and click an AI action.")
        return

    st.markdown(f"### {result['task'].replace('_', ' ').title()}")
    st.markdown(result["content"])