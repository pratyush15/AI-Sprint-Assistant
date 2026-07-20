from typing import TypedDict

from app.services.ai_service import ask_llm
from app.agents import prompts


class AIState(TypedDict):
    task: str
    title: str
    description: str
    question: str

    # populated by context_analyzer_node
    context_notes: str
    needs_clarification: bool

    # populated by task_executor_node
    draft_content: str

    # final output, set by clarifier_node or reviewer_node
    content: str


TASK_PROMPTS = {
    "story_points": prompts.STORY_POINT_PROMPT,
    "priority": prompts.PRIORITY_PROMPT,
    "subtasks": prompts.SUBTASK_PROMPT,
    "acceptance": prompts.ACCEPTANCE_PROMPT,
    "testcases": prompts.TESTCASE_PROMPT,
    "ticket_quality": prompts.TICKET_QUALITY_PROMPT,
    "rewrite_ticket": prompts.REWRITE_TICKET_PROMPT,
    "ticket_chat": prompts.TICKET_CHAT_PROMPT,
}


MIN_DESCRIPTION_WORDS = 4


# ---------------------------------------------------------------------------
# Agent 1 — Context Analyzer
# Reads the raw ticket and produces context notes for the Task Executor.
# ---------------------------------------------------------------------------
def context_analyzer_node(state: AIState):
    prompt = prompts.CONTEXT_ANALYSIS_PROMPT.format(
        title=state["title"],
        description=state["description"],
    )

    result = ask_llm(prompt)
    is_chat = state["task"] == "ticket_chat"
    description_word_count = len(state["description"].split())

    needs_clarification = (
        not is_chat and description_word_count < MIN_DESCRIPTION_WORDS
    )

    return {
        "context_notes": result,
        "needs_clarification": needs_clarification,
    }


def route_after_analysis(state: AIState):
    """Conditional edge: decide which agent runs next."""
    if state["needs_clarification"]:
        return "clarifier"
    return "task_executor"


# ---------------------------------------------------------------------------
# Agent 2 (branch) — Clarifier
# Runs instead of the task executor when the ticket is too vague to guess at.
# ---------------------------------------------------------------------------
def clarifier_node(state: AIState):
    prompt = prompts.CLARIFYING_QUESTIONS_PROMPT.format(
        title=state["title"],
        description=state["description"],
        context_notes=state["context_notes"],
    )

    result = ask_llm(prompt)

    return {
        "content": result,
    }


# ---------------------------------------------------------------------------
# Agent 3 — Task Executor
# Performs the actual requested action, using Agent 1's notes as extra context.
# ---------------------------------------------------------------------------
def task_executor_node(state: AIState):
    template = TASK_PROMPTS[state["task"]]

    if state["task"] == "ticket_chat":
        base_prompt = template.format(
            title=state["title"],
            description=state["description"],
            question=state["question"],
        )
    else:
        base_prompt = template.format(
            title=state["title"],
            description=state["description"],
        )

    enriched_prompt = (
        f"{base_prompt}\n\n"
        f"Additional context from the ticket analysis:\n{state['context_notes']}"
    )

    result = ask_llm(enriched_prompt)

    return {
        "draft_content": result,
    }


# ---------------------------------------------------------------------------
# Agent 4 — Reviewer
# Critiques the executor's draft against the task's own formatting rules
# and returns a corrected final version.
# ---------------------------------------------------------------------------
def reviewer_node(state: AIState):
    prompt = prompts.REVIEW_PROMPT.format(
        task=state["task"],
        draft=state["draft_content"],
    )

    result = ask_llm(prompt)

    return {
        "content": result,
    }
