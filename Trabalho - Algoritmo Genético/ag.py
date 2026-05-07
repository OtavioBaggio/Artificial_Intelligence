import random
import time

from cromossomo import Cromossomo
from util import Util

class AG:

    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        """
        Preenche a lista 'populacao' com cromossomos gerados aleatoriamente.
        Cada cromossomo recebe uma rota aleatória gerada pela Util.gerar_rota().
        """

        for i in range(tamanho_populacao):
            populacao.append(Cromossomo(Util.gerar_rota(len(estado_final)), estado_final))

    @staticmethod
    def exibir(populacao):
        """
        Mostra todos os cromossomos da população
        """
        for i in populacao:
            print(i)
            #time.sleep(0.05)

    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        """
        Seleciona os melhores cromossomos da população atual via torneio.
        
        Como funciona o torneio:
            1. Sorteia 3 cromossomos aleatórios da população
            2. Ordena os 3 (o de menor aptidão vence)
            3. O vencedor vai para a nova_populacao
        
        Elitismo: o melhor cromossomo da população (populacao[0], já ordenada)
        é sempre copiado direto para a nova_populacao sem disputar torneio,
        garantindo que a melhor solução nunca se perde.
 
        qtd_selecionados: quantos vão ser selecionados, proporcional à taxa_selecao.
        Ex: população de 30 com taxa 30% → 9 selecionados
        """

        # OBS.: a populacao nao pode ser pequena e nem a taxa de selecao ser muito alta
        torneio = []

        # calcular quantos devem ser selecionados a partir do tamanho da populacao com a taxa_selecao
        # populacao.size()	->	100
        # qtd_selecionados	-> 	taxa_selecao
        qtd_selecionados = taxa_selecao * len(populacao) / 100
        cromossomo = populacao[0]

        nova_populacao.append( cromossomo ) # elitismo


        i = 1
        while (i <= qtd_selecionados):
            c1 = populacao[ random.randrange( len(populacao) ) ]

            while(True):
                c2 = populacao[ random.randrange( len(populacao) ) ]
                if c2 != c1:
                    break
            
            while(True):
                c3 = populacao[ random.randrange( len(populacao) ) ]
                if c3 != c2 != c1:
                    break
            
            torneio.append(c1)
            torneio.append(c2)
            torneio.append(c3)
            torneio.sort()  # o primeiro é o mais apto

            selecionado = torneio[0]

            nova_populacao.append(selecionado)  # sem verificar unicidade — evita loop infinito
            i += 1
    

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final):
        """
        Gera filhos cruzando pares de cromossomos (crossover de ponto médio).
 
        Como funciona o crossover:
            - Filho 1: primeira metade do pai + segunda metade da mãe
            - Filho 2: primeira metade da mãe + segunda metade do pai
            Ex: pai=[1,2,3,4,5,6,7,8,9], mãe=[9,8,7,6,5,4,3,2,1]
                filho1=[1,2,3,4, 5,4,3,2,1]
                filho2=[9,8,7,6, 5,6,7,8,9]
 
        qtd_reproduzidos: quantos filhos gerar, proporcional à taxa_reproducao.
        No final, poda a nova_populacao para não ultrapassar o tamanho original.
        """

        sPai = sMae = sFilho1 = sFilho2 = []

        #calcular quantos devem ser reproduzidos a partir do tamanho da populacao com a taxa_reproducao
        #populacao.size()	->	100
        #qtdReproduzido	-> 	taxa_reproducao
        qtd_reproduzidos = taxa_reproducao * len(populacao) / 100

        #sFilho1 = Alexone - primeiraMetadeDoPai + segundaMetadeDaMae
        #sFilho2 = Simandre - primeiraMetadeDaMae + segundaMetadeDoPai
        i = 0
        while (i < qtd_reproduzidos):            
            pai = populacao[ random.randrange( len(populacao) ) ]
                
            # Garante que a mãe seja diferente do pai:
            while (True):            
                mae = populacao[ random.randrange( len(populacao) ) ]
                if mae != pai:
                    break               

            sPai = pai.valor
            sMae = mae.valor
            
            sFilho1 = sPai[0 : int(len(sPai)/2)] + sMae[int(len(sMae) / 2) : len(sMae)]
            sFilho2 = sMae[0 : int(len(sMae)/2)] + sPai[int(len(sPai) / 2) : len(sPai)]

            nova_populacao.append(Cromossomo(sFilho1, estado_final)) #estado_final é passado para calcular aptidao do filho
            nova_populacao.append(Cromossomo(sFilho2, estado_final)) #estado_final é passado para calcular aptidao do filho
            i = i + 2
                 
        #podar a nova_populacao, retirando os excedentes do final
        while (len(nova_populacao) > len(populacao)):
            nova_populacao.pop()

         

    @staticmethod
    def mutar(populacao, estado_final):
        """
        Aplica mutação aleatória em alguns cromossomos da população.
        
        Como funciona:
            1. Sorteia uma quantidade aleatória de mutantes (até 20% da população)
            2. Para cada mutante: escolhe uma posição aleatória e substitui
               o valor por uma cidade sorteada aleatoriamente
        
        A mutação serve para introduzir diversidade genética e evitar que
        o algoritmo fique preso em soluções locais (mínimos locais).
        """

        qtd_mutantes = random.randrange(int(len(populacao) / 5))

        while qtd_mutantes > 0:

            posicao_mutante = random.randrange(len(populacao))

            mutante = populacao[posicao_mutante]

            print("vai mutar", mutante)

            #mudando
            valor_mutado = mutante.valor.copy()   # cria uma cópia por segurança, pra não alterar na lista original

            indice = random.randrange(len(valor_mutado))

            cidade_sorteada = Util.cidades[random.randrange(Util.tamanho)]

            # Do prof, com strings: 
         #  valor_mutado = valor_mutado.replace(caracter_mutante, caracter_sorteado) 
            valor_mutado[indice] = cidade_sorteada  # Minha com listas, substitui uma cidade aleatória

            mutante = Cromossomo(valor_mutado, estado_final)

            populacao[posicao_mutante] = mutante
            qtd_mutantes -= 1


