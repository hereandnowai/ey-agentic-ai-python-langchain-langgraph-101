import os
from typing import cast
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.graph import StateGraph, START, END, MessagesState

load_dotenv()
model = init_chat_model(
    os.environ.get("MODEL", "google/gemini-3.1-flash-lite"),
    model_provider="openrouter",
    temperature=0,
)

def chat(state):
    return {"messages": [model.invoke(state["messages"])]}

b = StateGraph(MessagesState)
b.add_node("chat", chat)
b.add_edge(START, "chat")
b.add_edge("chat", END)
graph = b.compile()

question: MessagesState = {"messages": [HumanMessage("Write a funny story on home loan!")]}
print("AI (streaming): ", end="", flush=True)
for token, meta in graph.stream(question, stream_mode="messages"):
    print(cast(BaseMessage, token).content, end="", flush=True)
