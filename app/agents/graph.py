from langgraph.graph import (
    StateGraph,
    END
)

from app.agents.nodes import (
    AIState,
    context_analyzer_node,
    clarifier_node,
    task_executor_node,
    reviewer_node,
    route_after_analysis,
)

builder = StateGraph(AIState)

builder.add_node("context_analyzer", context_analyzer_node)
builder.add_node("clarifier", clarifier_node)
builder.add_node("task_executor", task_executor_node)
builder.add_node("reviewer", reviewer_node)

builder.set_entry_point("context_analyzer")

# Agent 1 hands off to one of two different agents depending on its own
# assessment of the ticket — this is the actual "multi-agent" branch.
builder.add_conditional_edges(
    "context_analyzer",
    route_after_analysis,
    {
        "clarifier": "clarifier",
        "task_executor": "task_executor",
    },
)

builder.add_edge("clarifier", END)

# Task Executor's draft always passes through the Reviewer agent before
# being returned — a generator + critic handoff.
builder.add_edge("task_executor", "reviewer")
builder.add_edge("reviewer", END)

graph = builder.compile()
