import streamlit as st

from utils import page_header

from api_client import (
    search_similar_tickets
)

from components.search_result import (
    show_search_results
)

page_header(
    "🔍 Similar Ticket Search",
    "Search related Jira tickets using ChromaDB"
)

query = st.text_input(
    "Describe your issue"
)

if st.button(
    "Search",
    use_container_width=True
):

    if query.strip():
        with st.spinner(
            "Searching..."
        ):

            results = search_similar_tickets(
                query
            )

            show_search_results(
                results
            )

    else:
        st.warning(
            "Please enter a search query."
        ) 