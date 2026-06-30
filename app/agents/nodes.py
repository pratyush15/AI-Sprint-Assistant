
from typing import TypedDict

from app.services.ai_service import ask_llm
from app.agents import prompts


class AIState(TypedDict):
    task: str
    title: str
    description: str
    question: str
    content: str


PROMPTS = {
    "story_points": prompts.STORY_POINT_PROMPT,
    "priority": prompts.PRIORITY_PROMPT,
    "subtasks": prompts.SUBTASK_PROMPT,
    "acceptance": prompts.ACCEPTANCE_PROMPT,
    "testcases": prompts.TESTCASE_PROMPT,
    "ticket_quality": prompts.TICKET_QUALITY_PROMPT, 
    "rewrite_ticket": prompts.REWRITE_TICKET_PROMPT,
    "ticket_chat": prompts.TICKET_CHAT_PROMPT,
    
}

def ai_node(state: AIState):

    if state["task"] == "ticket_chat":

        prompt = PROMPTS[
            state["task"]
        ].format(
            title=state["title"],
            description=state["description"],
            question=state["question"]
        )

    else:

        prompt = PROMPTS[
            state["task"]
        ].format(
            title=state["title"],
            description=state["description"]
        )

    result = ask_llm(prompt)

    return {
        "content": result
    }