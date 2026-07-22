from dataclasses import dataclass
from typing import TypedDict, NotRequired
from langgraph.graph import StateGraph, START, END
from langgraph.runtime import Runtime

@dataclass
class Ctx:
    fee_rate: float

class S(TypedDict):
    amount: float
    fee: NotRequired[float]

def charge(state, runtime: Runtime[Ctx]):
    return {"fee": state["amount"] * runtime.context.fee_rate}

b = StateGraph(S, context_schema=Ctx)
b.add_node("charge", charge)
b.add_edge(START, "charge")
b.add_edge("charge", END)
graph = b.compile()

print(graph.invoke({"amount": 100000}, context=Ctx(fee_rate=0.005)))
print(graph.invoke({"amount": 100000}, context=Ctx(fee_rate=0.010)))
