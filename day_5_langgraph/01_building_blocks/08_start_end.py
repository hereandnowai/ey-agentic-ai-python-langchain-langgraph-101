from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class S(TypedDict):
    msg: str

def process(state):
    return {"msg": "processed"}

b = StateGraph(S)
b.add_node("process", process)
b.add_edge(START, "process")
b.add_edge("process", END)
graph = b.compile()

print(graph.invoke({"msg": "initial message"}))
print("START node:", repr(START), "| END node:", repr(END))