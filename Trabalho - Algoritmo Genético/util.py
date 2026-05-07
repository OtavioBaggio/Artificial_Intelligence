import random

class Util:
    """
    Fornece as cidades e gera as rotas aleatórias
    """

    cidades = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tamanho = len(cidades)

    @staticmethod
    def gerar_rota(n):
        rota = []

        # Do professor:
        #for i in range(n):
        #    rota += Util.palavras[random.randrange(Util.tamanho)]

        for i in range(n):
            rota.append(Util.cidades[random.randrange(Util.tamanho)])
        
        return rota