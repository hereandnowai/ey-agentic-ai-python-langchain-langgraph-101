import os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pydantic import SecretStr
import gradio as gr

load_dotenv()
emdeddings = OpenAIEmbeddings(
    model=os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small"),
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)

def word_map(text):
    words = [w.strip() for w in text.split(",") if w.strip()]
    vectors = np.array(emdeddings.embed_documents(words))
    xy = PCA(n_components=2).fit_transform(vectors)
    fig, ax = plt.subplots()
    for word, point in zip(words, xy):
        ax.scatter(point[0], point[1], color="purple")
        ax.annotate(word, point)
    return fig

demo = gr.Interface(word_map,
                    gr.Textbox(label="Words (comma separated)", value="home loan, credit score, savings account, interest rate, mortgage, python, java, machine learning, artificial intelligence, data science"),
                    gr.Plot(), title="Word Map - close dots mean similar meaning")

if __name__ == "__main__":
    demo.launch()