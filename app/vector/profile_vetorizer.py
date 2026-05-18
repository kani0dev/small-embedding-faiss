from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
from types import SimpleNamespace

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

corpus = []
profiles_corpus = []
with open('profiles.json' , 'r') as file :
    profiles_corpus = (json.load(file,object_hook=lambda to_dic: SimpleNamespace(**to_dic)))


for profile in profiles_corpus:
    corpus.append({
         'name' : profile.name ,
         'message' : profile.message 
        })

only_message = []
for item in corpus:
    only_message.append(item['message'])

emdding_corpuse = embedder.encode(only_message)

query = ["boa tarde vi o anuncio do imovel, gostaria sabe se ta valendo ainda quero visitar"]

vactor_query = embedder.encode(query)
l2 = cosine_similarity(vactor_query,emdding_corpuse)

similarity = l2[0]
similarity_ordem_decrecente = np.argsort(similarity)[::-1]

print("queri : ",query)
for i in similarity_ordem_decrecente :
        if similarity[i] > 0.1:
            print(f"{similarity[i]:.2f} | {only_message[i]}")