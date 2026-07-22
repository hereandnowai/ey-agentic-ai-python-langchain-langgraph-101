import time
from typing import TypedDict, NotRequired
from langgraph.graph import StateGraph, START, END
from langgraph.types import CachePolicy
from langgraph.cache.memory import InMemoryCache

EXECUTIONS = {"count": 0}

class S(TypedDict):
    x: int
    y: NotRequired[int]

def slow_credit_check(state):
    EXECUTIONS["count"] += 1
    time.sleep(2)
    return {"y": state["x"] * 2}

b = StateGraph(S)
b.add_node("slow_credit_check", slow_credit_check, cache_policy=CachePolicy(ttl=120))
b.add_edge(START, "slow_credit_check")
b.add_edge("slow_credit_check", END)
graph = b.compile(cache=InMemoryCache())

graph.invoke({"x": 5})
graph.invoke({"x": 6})
print("times the slow node actually ran:", EXECUTIONS["count"], "(cached, so 1 not 2)")