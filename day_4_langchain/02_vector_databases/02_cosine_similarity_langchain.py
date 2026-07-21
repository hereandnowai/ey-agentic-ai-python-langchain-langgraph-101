import os
import math
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()
EMBED_MODEL = os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small")
embeddings = OpenAIEmbeddings(
    model=EMBED_MODEL,
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)

def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute the cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0

passages = [
    "Meridian home loans require a minimum credit score of 700",
    "savings accounts earn 3% interest, per annum"
    "Report a lost or stole stolen card immediately via the app"
]
query = "what credit score do I need to borrow a house?"

passage_vecs = embeddings.embed_documents(passages)
query_vec = embeddings.embed_query(query)

scored = [(cosine_similarity(query_vec, pv), p) for pv, p in zip(passage_vecs, passages)]
scored.sort(reverse=True)

print(f"query: {query}\n")
for score, passage in scored:
    print(f" {score:.4f} {passage}")

print(f"\nbest match: {scored[0][1]}")