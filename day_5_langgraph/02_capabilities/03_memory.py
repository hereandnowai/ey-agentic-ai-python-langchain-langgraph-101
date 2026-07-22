import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore
from langchain_core.runnables import RunnableConfig

load_dotenv()
model = init_chat_model(
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

STORE = InMemoryStore()
STORE.put(("customer-1",), "profile", {"name": "Travis", "segment": "premium"})

def chat(state):
    item = STORE.get(("customer-1",), "profile")
    profile = item.value if item else {"name": "there", "segment": "standard"}
    system = {
        "role": "system",
        "content": f"Help {profile['name']}, a {profile['segment']} customer, One short line."
    }
    return {"messages": [model.invoke([system] + state["messages"])]}

b = StateGraph(MessagesState)
b.add_node("chat", chat)
b.add_edge(START, "chat")
b.add_edge("chat", END)
graph = b.compile(checkpointer=InMemorySaver())

today: RunnableConfig = {"configurable": {"thread_id": "chat-today"}}
week: RunnableConfig = {"configurable": {"thread_id": "chat-next-week"}}
reply_today = graph.invoke({"messages": [HumanMessage("Hello")]}, today)
reply_week = graph.invoke({"messages": [HumanMessage("Hello")]}, week)
print("today:", reply_today["messages"][-1].content)
print("next week:", reply_week["messages"][-1].content)