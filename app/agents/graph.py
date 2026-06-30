
from langgraph.graph import (
    StateGraph,
    END
)

from app.agents.nodes import (
    AIState,
    ai_node
)

builder = StateGraph(AIState)

builder.add_node(
    "ai_node",
    ai_node
)

builder.set_entry_point(
    "ai_node"
)

builder.add_edge(
    "ai_node",
    END
)

graph = builder.compile()