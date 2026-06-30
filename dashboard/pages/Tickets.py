
import streamlit as st

from api_client import (
    get_tickets,
    create_ticket,
    update_ticket,
    delete_ticket
)

from utils import (
    page_header,
    success_message,
    error_message
)

from components.ticket_card import (
    show_ticket
)

page_header(
    "📋 Tickets",
    "Manage project tickets"
)

view_tab, create_tab, update_tab = st.tabs(
    [
        "View Tickets",
        "Create Ticket", 
        "Update Ticket"
    ]
)

# ------------------------
# View Tickets
# ------------------------

with view_tab:
    try:
        tickets = get_tickets()
        for ticket in tickets:
            show_ticket(ticket)

        st.divider()
        st.subheader("Delete Ticket")
        ticket_id = st.number_input(
            "Ticket ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Ticket"):
            delete_ticket(ticket_id)
            success_message(
                "Ticket deleted successfully."
            )

            st.rerun()

    except Exception as e:
        error_message(str(e))


# ------------------------
# Create Ticket
# ------------------------

with create_tab:
    title = st.text_input("Title")
    description = st.text_area("Description")
    priority = st.selectbox(
        "Priority",
        [
            "Low",
            "Medium",
            "High",
            "Highest"
        ]
    )

    status = st.selectbox(
        "Status",
        [
            "To Do",
            "In Progress",
            "Done"
        ]
    )

    story_points = st.number_input(
        "Story Points",
        min_value=0,
        value=0
    )

    sprint = st.text_input("Sprint")
    assignee = st.text_input("Assignee")

    if st.button("Create"):
        create_ticket(
            {
                "title": title,
                "description": description,
                "priority": priority,
                "status": status,
                "story_points": story_points,
                "sprint": sprint,
                "assignee": assignee
            }
        )

        success_message(
            "Ticket created successfully."
        )

        st.rerun()  
        
# ------------------------
# Update Ticket
# ------------------------

with update_tab:
    tickets = get_tickets()

    if not tickets:
        st.info(
            "No tickets available."
        )

    else:
        ticket_options = {
            f"#{t['id']} - {t['title']}": t
            for t in tickets
        }

        selected = st.selectbox(
            "Select Ticket",
            list(ticket_options.keys())
        )

        ticket = ticket_options[selected]

        title = st.text_input(
            "Title",
            value=ticket["title"]
        )

        description = st.text_area(
            "Description",
            value=ticket["description"]
        )

        priority = st.selectbox(
            "Priority",
            [
                "Low",
                "Medium",
                "High",
                "Highest"
            ],
            index=[
                "Low",
                "Medium",
                "High",
                "Highest"
            ].index(ticket["priority"])
        )

        status = st.selectbox(
            "Status",
            [
                "To Do",
                "In Progress",
                "Done"
            ],
            index=[
                "To Do",
                "In Progress",
                "Done"
            ].index(ticket["status"])
        )

        story_points = st.number_input(
            "Story Points",
            min_value=0,
            value=ticket["story_points"] or 0
        )

        sprint = st.text_input(
            "Sprint",
            value=ticket["sprint"] or ""
        )

        assignee = st.text_input(
            "Assignee",
            value=ticket["assignee"] or ""
        )

        if st.button(
            "Update Ticket"
        ):

            update_ticket(
                ticket["id"],
                {
                    "title": title,
                    "description": description,
                    "priority": priority,
                    "status": status,
                    "story_points": story_points,
                    "sprint": sprint,
                    "assignee": assignee
                }
            )

            success_message(
                "Ticket updated successfully."
            )

            st.rerun()