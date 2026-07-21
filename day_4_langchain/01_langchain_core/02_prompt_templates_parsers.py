import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from typing import cast
from dotenv import load_dotenv

load_dotenv()
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")
model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)

# 1. prompt template with {placeholder}
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Meridian Bank's assistant. Answer in one sentence."),
    ("user", "Explain '{term}' to a {audience}")
])

# 2. compose a chain with the pipe operator
chain = prompt | model | StrOutputParser()
print(chain.invoke({"term": "EMI", "audience": "first-time borrower"}))

# 3. structured output parsing with Pydantic
class LoanEnquiry(BaseModel):
    intent: str
    product: str
    amount: float | None = Field(default=None, description="rupees; null if unstated")

structured_model = model.with_structured_output(LoanEnquiry)
result = cast(LoanEnquiry, structured_model.invoke(
    "I'd like to apply for a home loan of about 50 lakhs."))
print("\nstructure:", result)
print("product:", result.product, "| amount:", result.amount)

extracted_chain = ChatPromptTemplate.from_messages([
    ("system", "extract the inquiry amounts in rupees (1 lakh = ₹100000.00). Null if unstated."),
    ("user", "{message}"),
]) | structured_model
print("\nchained: ", extracted_chain.invoke({"message": "Enquiring about a 30 lakh home loan."}))