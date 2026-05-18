from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

corpus = [
    "tenho interesse em carros vermelhos",
    "gostaria de dar uma olhada nesse carro",
    "eu amo carros",
    "gostaria de comprar essa casa em barueri esta disponivel ainda",
    "esse gato ainda esta para adoção eu adoro gatos eles sao muito fofos",
    "nao estou feliz com esse resultado estou nervoso",
    "eu me chamo leticia",
    "eu me chamo jorge"
]

corpus_embedding = embedder.encode(corpus)
query = ["eu gosto muito de carros"]
query_vector = embedder.encode(query)

similaridade = cosine_similarity(query_vector, corpus_embedding)

# similaridade tem shape (1, 8) — 1 query, 8 frases do corpus
scores = similaridade[0]  # pega o array da primeira (e única) query

# ordena do mais similar pro menos
indices_ordenados = np.argsort(scores)[::-1]

for i in indices_ordenados:
    print(f"{scores[i]:.4f} | {corpus[i]}")