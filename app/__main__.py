from .profiles.profile_generator import Factory
from .vector.profile_vetorizer import buscar_similaridade

def main():
    # se por algumn motive nao tiver o profile .json na raiz do projeto rode isso:
    # Factory.generate_profile_as_file()

    minha_query = "boa tarde vi o anuncio do imovel, gostaria sabe se ta valendo ainda quero visitar"
    resultado_busca = buscar_similaridade(minha_query)
    print("Query pra pesquisa : " ,minha_query)
    for res in resultado_busca:
        print(res)
    

if __name__ == "__main__":
    main()
