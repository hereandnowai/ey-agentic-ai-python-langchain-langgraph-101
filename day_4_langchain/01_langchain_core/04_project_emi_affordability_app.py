import os
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import gradio as gr

load_dotenv()
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")
model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)

@tool
def calculate_emi(principal: float, annual_rate: float, years: int) -> dict:
    """Calculate the monthly EMI and total payable for a loan.
    
    Args:
        principal (float): The principal loan amount in rupees.
        annual_rate (float): The annual interest rate in percentage (e.g. 8.4%).
        years (int): The loan tenure in years.
    """
    r = annual_rate / 100 / 12  # monthly interest rate
    n = years * 12  # total number of monthly payments
    emi = principal / n if r == 0 else principal * r * (1 + r) ** n / ((1 + r) ** n - 1) # the standard EMI formula
    return {"emi": round(emi, 2)}

@tool
def check_affordability(monthly_income: float, emi: float) -> dict:
    """Check if the EMI is affordable based on the user's monthly income.
    
    Args:
        monthly_income (float): The user's monthly income in rupees.
        emi (float): The calculated EMI in rupees.
    """
    ratio = emi / monthly_income if monthly_income else 1.0
    return {"emi_to_income": round(ratio, 2), "affordable": ratio <= 0.5}

agent = create_agent(
    model,
    tools=[calculate_emi, check_affordability],
    system_prompt=("""You are Meridian Bank's assistant.
                    Use emi calculation tool for replayment maths
                    and affordability check tool to check if the emi is
                    affordable based on the user's monthly income.
                    Amount are in rupees (1 lakh = ₹100000.00).
                    Give factual guidance only - never regulatory or legal advice.""")
                    )

def respond(message, history):
    messages = history + [{"role": "user", "content": message}]
    result = agent.invoke({"messages": messages})
    return result["messages"][-1].content

demo = gr.ChatInterface(
    respond,
    title="Meridian Bank EMI Affordability Assistant",
    description="Ask about EMI calculations and affordability checks for loans.",
    examples=[
        ["What's the EMI on a 50 lakh loan at 8.4% over 25 years?"],
        ["I earn 1.5 lakh per month - Can I afford a 30 lakh loan at 9% over 20 years?"],
])

if __name__ == "__main__":
    demo.launch()