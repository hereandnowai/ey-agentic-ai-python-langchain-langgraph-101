import os
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")

model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)

response = model.invoke([
    SystemMessage("You are a concise banking assistant"),
    HumanMessage("Answer in one sentence, what is a floating interest rate?")
])

print("type :", type(response).__name__)
print("content :", response.content)
print("tokens :", response.usage_metadata)

print("\nstreaming: ", end="", flush=True)
for chunk in model.stream([HumanMessage("List two types of bank account briefly.")]):
    print(chunk.content, end="", flush=True)
print()



# langgraph - multi-agent - blog writing and publishing agent
# agent 1 - manager (opus)
# agent 2 - research + plan (opus)
# agent 3 - writing (gpt)
# agent 4 - editing (sonnet / gpt)
# agent 5 - publishing (sonnet)
# agent 6 - gemini (react, angular, nextjs) - antigravity

# OpenAI
# system message
# user message
# assistant message

# in LangChain
# SystemMessage
# HumanMessage
# AIMessage