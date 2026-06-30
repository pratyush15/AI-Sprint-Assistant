
from app.agents.graph import graph

def run_ai_task(
    task,
    title,
    description,
    question=""
):

    result = graph.invoke(
        {
            "task": task,
            "title": title,
            "description": description,
            "question": question,
            "content": ""
        }
    )

    return {
        "task": task,
        "content": result["content"]
    }