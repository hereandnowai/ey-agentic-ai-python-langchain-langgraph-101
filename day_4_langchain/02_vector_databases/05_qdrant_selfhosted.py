import os
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from qdrant_client import QdrantClient
from qdrant_client import models
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()
EMBEDDING_MODEL = os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small")
embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL,
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")

docs = [
    Document(page_content="Home loans require a minimum CIBIL score of 700.",
             metadata={"id": "hl-001", "category": "home_loan"}),
    Document(page_content="Home loan rates start at 8.4 percentage for scores of 750+",
             metadata={"id": "hl-002", "category": "home_loan"}),
    Document(page_content="Savings accounts earn 3% interest, per annum.",
            metadata={"id": "sa-001", "category": "savings_account"}),
    Document(page_content="Report a lost or stolen card immediately via the app.",
            metadata={"id": "cc-001", "category": "credit_card"}),
]

try:
    store = QdrantVectorStore.from_documents(
        docs,
        embedding=embeddings,
        url=QDRANT_URL,
        collection_name="meridian_demo",
    )
except Exception as error:
    print("could not reach a qdrant. Please run 'docker run -p 6333:6333 qdrant/qdrant'")
    print("Details: ", error)
    raise SystemExit(1)

# --- Plain search ---
print("\n--- plain search: 'Credit score to buy a house' ---")
for d in store.similarity_search("credit score to buy a house", k=2):
    print(f" [{d.metadata['category']}] {d.page_content}")

# --- Metadata filter search ---
print("\n--- metadata filter search: (category = home loan) ---")
qdrant_filter = models.Filter(
    must=[models.FieldCondition(key="metadata.category",
                                match=models.MatchValue(value="home_loan"))])

# With scores (lower distance = closer)
print("\n--- filtered search (category = home loan) ---")
for d in store.similarity_search("interest rate", k=2):
    print(f" [{d.metadata['id']}] {d.page_content}")
