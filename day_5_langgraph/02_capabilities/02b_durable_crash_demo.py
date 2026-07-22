from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig

DEBITS = {"count": 0}
NETWORK = {"down": True}

class Payment(TypedDict):
    log: Annotated[list, add]
    status: str

def debit_payer(state):
    DEBITS["count"] += 1
    return {"log": ["debited 500 from Simran"], "status": "processing"}

def credit_payee(state):
    if NETWORK["down"]:
        NETWORK["down"] = False
        raise RuntimeError("Bank Network timed out")
    return {"log": ["credited 500 to Virat"], "status": "success"}

b = StateGraph(Payment)
b.add_node("debit_payer", debit_payer)
b.add_node("credit_payee", credit_payee)
b.add_edge(START, "debit_payer")
b.add_edge("debit_payer", "credit_payee")
b.add_edge("credit_payee", END)
graph = b.compile(checkpointer=InMemorySaver())

cfg: RunnableConfig = {"configurable": {"thread_id": "txn-9001"}}

# 1. User taps pay button, transaction initiated
try:
    graph.invoke({"log": [], "status": "initiated"}, cfg, durability="sync")
except RuntimeError as e:
    print("BACKEND CRASHED:", e)

# 2. What the user sees after the crash (money gone, screen frozen)
snap = graph.get_state(cfg).values
print("saved log        : ", snap["log"])
print("user sees status : ", snap["status"], " <-- money gone, but shows PROCESSING")
print("time debited     : ", DEBITS["count"], "time")

# 3. The System Resumes (auto-retry) and completes the payment
graph.invoke(None, cfg)
snap = graph.get_state(cfg).values
print("after resume log : ", snap["log"])
print("user sees status : ", snap["status"], " <-- money credited, shows SUCCESS")
print("times debited    : ", DEBITS["count"], "time <-- debited only once, no double charge")


