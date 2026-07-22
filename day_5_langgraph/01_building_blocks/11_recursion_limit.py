from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.errors import GraphRecursionError

class S(TypedDict):
    count: int

def tick(state):
    return

def loop_back(state):
    return "tick"

b = StateGraph(S)
b.add_node("tick", tick)
b.add_edge(START, "tick")
b.add_conditional_edges("tick", loop_back, ["tick"])
graph = b.compile()

try:
    graph.invoke({"count": 0}, {"recursion_limit": 5})
except GraphRecursionError:
    print("Stopped by recursion limit=5 - the seatbelt worked, no infinite loop!")