from langgraph.graph import StateGraph, START, END
from state import State
from graph.router import router

from agents.summary_agent import summarize
from agents.qa_agent import give_answers

graph = StateGraph(State)

# Nodes
graph.add_node("summary", summarize)
graph.add_node("qa", give_answers)

# Router
graph.add_conditional_edges(
    START,
    router,
    {
        "summary":"summary",
        "qa":"qa"   
    }
)

# End connections
graph.add_edge("summary", END)
graph.add_edge("qa", END)

workflow = graph.compile()