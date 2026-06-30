from io import BytesIO

from reportlab.platypus import ( # type: ignore
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import ( # type: ignore
    getSampleStyleSheet
)

from sqlalchemy.orm import Session
from app.database.models import Ticket
from app.services.ai_service import ask_llm
from app.agents.prompts import (
    SPRINT_SUMMARY_PROMPT, 
    SPRINT_READINESS_PROMPT, 
    SPRINT_RISK_PROMPT, 
    SPRINT_CAPACITY_PROMPT
)


def generate_sprint_summary(db: Session):
    tickets = db.query(Ticket).all()
    sprint_text = ""
    for ticket in tickets:
        sprint_text += f"""
Title: {ticket.title}
Status: {ticket.status}
Priority: {ticket.priority}
Story Points: {ticket.story_points}

Description:
{ticket.description}
--------------------
"""
    prompt = SPRINT_SUMMARY_PROMPT.format(
        tickets=sprint_text
    )

    return ask_llm(prompt)


def generate_sprint_readiness(db: Session):
    tickets = db.query(Ticket).all()
    sprint_text = ""
    for ticket in tickets:
        sprint_text += f"""
Title: {ticket.title}
Status: {ticket.status}
Priority: {ticket.priority}
Story Points: {ticket.story_points}
Assignee: {ticket.assignee}
Description:
{ticket.description}

--------------------
"""

    prompt = SPRINT_READINESS_PROMPT.format(
        tickets=sprint_text
    )

    return ask_llm(prompt)   


def generate_sprint_risk(db: Session):
    tickets = db.query(Ticket).all()
    sprint_text = ""
    for ticket in tickets:
        sprint_text += f"""
Title: {ticket.title}
Status: {ticket.status}
Priority: {ticket.priority}
Story Points: {ticket.story_points}
Assignee: {ticket.assignee}
Description:
{ticket.description}

--------------------
"""

    prompt = SPRINT_RISK_PROMPT.format(
        tickets=sprint_text
    )

    return ask_llm(prompt)


def generate_sprint_report(db: Session):
    summary = generate_sprint_summary(db)
    readiness = generate_sprint_readiness(db)
    risk = generate_sprint_risk(db)
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = []

    content.append(
        Paragraph(
            "AI Sprint Assistant Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Sprint Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Sprint Readiness",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            readiness,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Sprint Risk Analysis",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            risk,
            styles["BodyText"]
        )
    )

    doc.build(content)
    buffer.seek(0)

    return buffer


def generate_sprint_capacity(db: Session):
    tickets = db.query(Ticket).all()
    total_points = sum(
        ticket.story_points or 0
        for ticket in tickets
    )
    assignees = set()
    for ticket in tickets:
        if ticket.assignee:
            assignees.add(
                ticket.assignee
            )
            
    team_size = max(
        len(assignees),
        1
    )

    prompt = SPRINT_CAPACITY_PROMPT.format(
        total_points=total_points,
        team_size=team_size
    )

    return ask_llm(prompt)  


def get_workload_analysis(db: Session):
    tickets = db.query(Ticket).all()
    workload = {}
    for ticket in tickets:
        
        assignee = (
            ticket.assignee
            if ticket.assignee
            else "Unassigned"
        )

        workload.setdefault(
            assignee,
            0
        )

        workload[assignee] += (
            ticket.story_points or 0
        )

    return workload