
import os
import requests

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL")


# -------------------------
# Ticket APIs
# -------------------------

def get_tickets():
    response = requests.get(
        f"{BASE_URL}/tickets/"
    )

    response.raise_for_status()
    return response.json()


def create_ticket(ticket):
    response = requests.post(
        f"{BASE_URL}/tickets/",
        json=ticket
    )

    response.raise_for_status()
    return response.json()


def update_ticket(
    ticket_id,
    ticket
):

    response = requests.put(
        f"{BASE_URL}/tickets/{ticket_id}",
        json=ticket
    )

    response.raise_for_status()
    return response.json()


def delete_ticket(ticket_id):
    response = requests.delete(
        f"{BASE_URL}/tickets/{ticket_id}"
    )

    response.raise_for_status()
    return response.json()


def run_ai(
    task,
    title,
    description,
    question=""
):

    payload = {
        "task": task,
        "title": title,
        "description": description,
        "question": question
    }

    response = requests.post(
        f"{BASE_URL}/ai/run",
        json=payload
    )

    response.raise_for_status()
    return response.json()


def get_sprint_metrics():
    tickets = get_tickets()
    return tickets


def search_similar_tickets(query):
    payload = {
        "query": query
    }

    response = requests.post(
        f"{BASE_URL}/vector/search",
        json=payload
    )

    response.raise_for_status()
    return response.json()["results"]


def get_sprint_summary():
    response = requests.get(
        f"{BASE_URL}/ai/sprint-summary"
    )

    response.raise_for_status()
    return response.json()["summary"]   


def get_sprint_readiness():
    response = requests.get(
        f"{BASE_URL}/ai/sprint-readiness"
    )

    response.raise_for_status()
    return response.json()["readiness"]


def get_sprint_risk():
    response = requests.get(
        f"{BASE_URL}/ai/sprint-risk"
    )

    response.raise_for_status()
    return response.json()["risk"] 


def download_sprint_report():
    response = requests.get(
        f"{BASE_URL}/ai/sprint-report"
    )

    response.raise_for_status()
    return response.content


def get_sprint_capacity():
    response = requests.get(
        f"{BASE_URL}/ai/sprint-capacity"
    )

    response.raise_for_status()
    return response.json()["capacity"]


def get_workload():
    response = requests.get(
        f"{BASE_URL}/ai/workload"
    )

    response.raise_for_status()
    return response.json()