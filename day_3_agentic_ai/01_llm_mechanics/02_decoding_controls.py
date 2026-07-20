import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

MODEL = "meta-llama/llama-3.1-8b-instruct"  # The model to use for the API call

PROMPT = "Give a name for a new savings account product. Replay with just the name, no other text."

def generate(temperature: float, max_tokens: int = 20, stop=None):
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=temperature, # 0 = deterministic, 1 = more random / more varied answers
        top_p=1.0,               # nucleus sampling, 1.0 = no filtering
        max_tokens=max_tokens,   # hard cap on completion length, can be used to limit cost
        stop=stop
    )
    return (resp.choices[0].message.content or "").strip()

print("=== temperature 0.0 (run 3x - expect near-identical) ===")
for _ in range(3):
    print(" ", generate(0.0))

print("\n=== temperature 1.0 (run 3x - expect some variation) ===")
for _ in range(3):
    print(" ", generate(1.0))

print("\n=== max_tokens=2 (truncates) ===")
print(" ", generate(temperature=0.7, max_tokens=5))