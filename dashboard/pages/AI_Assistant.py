import streamlit as st

from api_client import (
    get_tickets,
    run_ai
)

from utils import page_header

from components.ai_actions import (
    action_buttons
)

from components.ai_output import (
    show_output
)


page_header(
    "🤖 AI Assistant",
    "AI-powered Jira Assistant"
)


# ----------------------------
# Session State
# ----------------------------

if "selected_ticket" not in st.session_state:
    st.session_state.selected_ticket = None

if "ai_result" not in st.session_state:
    st.session_state.ai_result = ""

if "chat_question" not in st.session_state:
    st.session_state.chat_question = ""

if "chat_mode" not in st.session_state:
    st.session_state.chat_mode = False


# ----------------------------
# Load Tickets
# ----------------------------

tickets = get_tickets()


# ----------------------------
# Layout
# ----------------------------

left_col, right_col = st.columns(
    [1, 2]
)


# ============================
# LEFT PANEL
# ============================

with left_col:
    st.subheader("Tickets")

    ticket_titles = [
        f"#{ticket['id']} - {ticket['title']}"
        for ticket in tickets
    ]

    selected = st.selectbox(
        "Select Ticket",
        ticket_titles
    )

    selected_ticket = tickets[
        ticket_titles.index(selected)
    ]

    st.session_state.selected_ticket = selected_ticket


# ============================
# RIGHT PANEL
# ============================

with right_col:
    ticket = st.session_state.selected_ticket
    st.subheader(ticket["title"])
    st.write(ticket["description"])
    st.divider()

    st.subheader("AI Actions")
    task = action_buttons()

    if task == "ticket_chat":
        st.session_state.chat_mode = True

    elif task:
        st.session_state.chat_mode = False

        with st.spinner("Thinking..."):

            result = run_ai(
                task,
                ticket["title"],
                ticket["description"]
            )

            st.session_state.ai_result = result

    if st.session_state.chat_mode:
        st.divider()
        st.subheader("💬 Chat with Ticket")

        question = st.text_input(
            "Ask a question",
            placeholder="What are the risks? What APIs are needed? Is this sprint ready?"
        )

        if st.button(
            "Ask AI",
            use_container_width=True
        ):

            if not question.strip():
                st.warning(
                    "Please enter a question."
                )

            else:
                with st.spinner("Thinking..."):
                    result = run_ai(
                        "ticket_chat",
                        ticket["title"],
                        ticket["description"],
                        question
                    )

                    st.session_state.ai_result = result

    st.divider()
    show_output(
        st.session_state.ai_result
    )