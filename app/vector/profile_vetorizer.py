import json
from types import SimpleNamespace
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Inicialização e Processamento do Corpus (Feito apenas uma vez)
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

corpus = []
with open("profiles.json", "r") as file:
    profiles_corpus = json.load(
        file, object_hook=lambda to_dic: SimpleNamespace(**to_dic)
    )

for profile in profiles_corpus:
    corpus.append({"name": profile.name, "message": profile.message})

only_message = [item["message"] for item in corpus]
embedding_corpus = embedder.encode(only_message)


# 2. A Função de Busca
def buscar_similaridade(query: str) -> dict:
    """Recebe uma string de consulta e retorna um dicionário com o índice

    do corpus e a mensagem correspondente, ordenados por relevância.
    """
    # Garante que a query esteja em formato de lista para o embedder
    vector_query = embedder.encode([query])

    # Calcula a similaridade
    l2 = cosine_similarity(vector_query, embedding_corpus)
    similarity = l2[0]

    # Ordena os índices do maior para o menor
    similarity_ordem_decrecente = np.argsort(similarity)[::-1]

    # Cria o dicionário de retorno filtrando pelo limiar (threshold) de 0.1
    resultado = []
    for i in similarity_ordem_decrecente:
        if similarity[i] > 0.1:
            # Usa o índice 'i' como chave e a mensagem correspondente como valor
            resultado.append(f'{similarity[i]:.2f} -> {only_message[i]}')

    return resultado