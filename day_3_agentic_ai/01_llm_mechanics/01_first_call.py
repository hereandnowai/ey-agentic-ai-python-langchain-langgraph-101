import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # reads the .env file and loads the environment variables

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

# MODEL = "openai/gpt-4o-mini"  # The model to use for the API call
MODEL = "meta-llama/llama-3.1-8b-instruct"  # The model to use for the API call

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a concise banking assistant built by Muthu Bank?"},
        {"role": "user", "content": "Who are you? & who built you?"}
    ]
)

print("Bot: ", response.choices[0].message.content)

usage = response.usage
if usage is not None:
    print("promt_tokens: ", usage.prompt_tokens)
    print("completion_tokens: ", usage.completion_tokens)
    print("total_tokens: ", usage.total_tokens)
else:
    print("Usage : Not available for this model.")

