
import streamlit as st


def show_search_results(results):
    st.subheader("Similar Tickets")
    if not results:
        st.info(
            "No similar tickets found."
        )

        return

    for index, ticket in enumerate(
        results,
        start=1
    ):

        with st.container(border=True):
            st.markdown(
                f"### Result {index}"
            )

            similarity = ticket.get(
                "similarity",
                0
            )

            st.metric(
                "Similarity",
                f"{similarity}%"
            )

            st.write(
                ticket["ticket"]
            )