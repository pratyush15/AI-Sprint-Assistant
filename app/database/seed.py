from app.database.db import SessionLocal
from app.database.models import Ticket


def seed_database():
    db = SessionLocal()

    # Prevent duplicate seeding
    if db.query(Ticket).count() > 0:
        db.close()
        return

    tickets = [
        Ticket(
            title="Login page crashes",
            description="Application crashes when invalid credentials are entered repeatedly.",
            priority="High",
            status="To Do",
            story_points=5,
            sprint="Sprint 1",
            assignee="Alice"
        ),
        Ticket(
            title="Forgot Password Feature",
            description="Allow users to reset their password via email.",
            priority="Medium",
            status="In Progress",
            story_points=8,
            sprint="Sprint 1",
            assignee="Bob"
        ),
        Ticket(
            title="Dashboard UI Improvements",
            description="Improve alignment and responsiveness of dashboard widgets.",
            priority="Low",
            status="To Do",
            story_points=3,
            sprint="Sprint 2",
            assignee="Charlie"
        ),
        Ticket(
            title="Optimize Database Queries",
            description="Reduce response time of dashboard APIs.",
            priority="High",
            status="Done",
            story_points=8,
            sprint="Sprint 2",
            assignee="David"
        ),
        Ticket(
            title="Profile Page",
            description="Users should be able to update their profile information.",
            priority="Medium",
            status="In Progress",
            story_points=5,
            sprint="Sprint 2",
            assignee="Emma"
        ),
        Ticket(
            title="Dark Mode",
            description="Provide dark mode support across application.",
            priority="Low",
            status="To Do",
            story_points=3,
            sprint="Sprint 3",
            assignee="Frank"
        ),
        Ticket(
            title="Notification Service",
            description="Notify users when ticket status changes.",
            priority="Medium",
            status="To Do",
            story_points=8,
            sprint="Sprint 3",
            assignee="Grace"
        ),
        Ticket(
            title="Search Tickets",
            description="Implement keyword search for tickets.",
            priority="Medium",
            status="Done",
            story_points=5,
            sprint="Sprint 3",
            assignee="Harry"
        ),
        Ticket(
            title="Export Reports",
            description="Allow sprint reports to be exported as PDF.",
            priority="High",
            status="To Do",
            story_points=8,
            sprint="Sprint 4",
            assignee="Ivy"
        ),
        Ticket(
            title="API Authentication",
            description="Secure backend APIs using JWT.",
            priority="Highest",
            status="In Progress",
            story_points=13,
            sprint="Sprint 4",
            assignee="John"
        ),
    ]

    db.add_all(tickets)
    db.commit()
    db.close()